#!/usr/bin/env python3
"""Grade all eval outputs against assertions."""
import json, re, os, sys

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

# Common assertions for all evals
COMMON_ASSERTIONS = [
    {"text": "Uses D3.js from CDN", "check": lambda h: "d3" in h.lower() and ("cdn" in h.lower() or "jsdelivr" in h.lower() or "unpkg" in h.lower() or "cdnjs" in h.lower() or "d3.min.js" in h.lower() or "d3@" in h.lower())},
    {"text": "Single standalone HTML file", "check": lambda h: h.strip().startswith("<!") or h.strip().startswith("<html")},
    {"text": "Nodes are clickable (click handlers)", "check": lambda h: "click" in h.lower() and ("onclick" in h.lower() or ".on(" in h or "addEventListener" in h or "click" in h)},
    {"text": "Multiple zoom levels (at least 2 distinct views)", "check": lambda h: any(w in h.lower() for w in ["level 1", "level1", "level-1", "overview", "zoom", "drill"]) or re.search(r'level[_\s]?[123]', h.lower()) is not None or ("phase" in h.lower() and ("detail" in h.lower() or "expand" in h.lower()))},
    {"text": "Breadcrumb or back navigation", "check": lambda h: any(w in h.lower() for w in ["breadcrumb", "back-btn", "back-button", "backbtn", "go back", "goback", "nav-back", "← back", "←", "level 1", "overview"]) or re.search(r'back.*level|return.*overview|navigate.*back', h.lower()) is not None},
    {"text": "Custom styled nodes (not default SVG)", "check": lambda h: ("border-radius" in h or "box-shadow" in h or "rounded" in h.lower() or "rx=" in h or "fill:" in h or "fill=" in h) and ("hover" in h.lower() or "transition" in h.lower())},
    {"text": "Smooth transitions between states", "check": lambda h: "transition" in h.lower() and any(w in h.lower() for w in ["duration", "300", "400", "ease", "d3.transition", ".transition("])},
]

# Eval-specific assertions
CHECKOUT_ASSERTIONS = [
    {"text": "Decision diamonds for validation steps", "check": lambda h: "diamond" in h.lower() or "rotate(45" in h or "transform: rotate" in h or "polygon" in h.lower() or re.search(r'decision|diamond', h.lower()) is not None},
    {"text": "Error paths with distinct red styling", "check": lambda h: ("error" in h.lower() or "fail" in h.lower()) and ("red" in h.lower() or "#ff" in h.lower() or "#e" in h.lower() or "#BF5547" in h or "#dc" in h.lower())},
    {"text": "Happy path visually highlighted", "check": lambda h: "happy" in h.lower() or ("path" in h.lower() and ("highlight" in h.lower() or "thick" in h.lower() or "bold" in h.lower() or "stroke-width: 3" in h or "stroke-width:3" in h))},
]

MERMAID_ASSERTIONS = [
    {"text": "All 10 Mermaid nodes preserved", "check": lambda h: all(w.lower() in h.lower() for w in ["Start", "Search Products", "Found results", "Product Detail", "No Results", "In Stock", "Add to Cart", "Notify", "Checkout", "Order Confirmed"])},
    {"text": "Start/end nodes use pill or stadium shapes", "check": lambda h: any(w in h.lower() for w in ["pill", "stadium", "rounded", "rx=", "border-radius: 50", "border-radius:50", "ellipse", "start", "end"]) and ("start" in h.lower() and ("confirmed" in h.lower() or "end" in h.lower()))},
]

SKILL_SPECIFIC = [
    {"text": "Uses Software DS color tokens", "check": lambda h: any(t in h for t in ["#013D5B", "#1C1A17", "#E0DCD3", "--sds-", "#0C4A69", "#62800B", "#8A7515", "#805AA1"])},
    {"text": "Three distinct zoom levels", "check": lambda h: (h.lower().count("level") >= 3 or ("overview" in h.lower() and "detail" in h.lower() and ("flow" in h.lower() or "screen" in h.lower()))) and any(w in h.lower() for w in ["sidebar", "modal", "panel", "detail"])},
]

def grade_file(html_path, assertions):
    with open(html_path, 'r') as f:
        html = f.read()
    results = []
    for a in assertions:
        passed = a["check"](html)
        results.append({
            "text": a["text"],
            "passed": passed,
            "evidence": f"{'Found' if passed else 'Not found'} in {os.path.basename(html_path)}"
        })
    return results

evals = [
    {
        "name": "onboarding-flow",
        "with_skill": "onboarding-flow/with_skill/outputs/onboarding-flow.html",
        "without_skill": "onboarding-flow/without_skill/outputs/onboarding-flow.html",
        "extra_assertions": [],
    },
    {
        "name": "checkout-flow",
        "with_skill": "checkout-flow/with_skill/outputs/checkout-flow.html",
        "without_skill": "checkout-flow/without_skill/outputs/checkout-flow.html",
        "extra_assertions": CHECKOUT_ASSERTIONS,
    },
    {
        "name": "mermaid-conversion",
        "with_skill": "mermaid-conversion/with_skill/outputs/product-search-flow.html",
        "without_skill": "mermaid-conversion/without_skill/outputs/flow-diagram.html",
        "extra_assertions": MERMAID_ASSERTIONS,
    },
]

for ev in evals:
    for variant in ["with_skill", "without_skill"]:
        html_path = os.path.join(WORKSPACE, ev[variant])
        assertions = COMMON_ASSERTIONS + ev["extra_assertions"]
        if variant == "with_skill":
            assertions = assertions + SKILL_SPECIFIC

        results = grade_file(html_path, assertions)

        passed = sum(1 for r in results if r["passed"])
        total = len(results)

        out_dir = os.path.dirname(os.path.dirname(html_path))
        grading = {
            "eval_name": ev["name"],
            "variant": variant,
            "pass_rate": round(passed / total, 2),
            "passed": passed,
            "total": total,
            "expectations": results
        }

        grading_path = os.path.join(out_dir, "grading.json")
        with open(grading_path, 'w') as f:
            json.dump(grading, f, indent=2)

        status = "✅" if passed == total else "⚠️"
        print(f"{status} {ev['name']} / {variant}: {passed}/{total} passed")
        for r in results:
            mark = "✓" if r["passed"] else "✗"
            print(f"   {mark} {r['text']}")
        print()

print("All grading complete.")
