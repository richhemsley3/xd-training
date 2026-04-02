#!/usr/bin/env python3
"""Grade all eval outputs for iteration-3 against assertions."""
import json, re, os, sys

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

# ──────────────────────────────────────────────
# Common assertions for all evals
# ──────────────────────────────────────────────
COMMON_ASSERTIONS = [
    {
        "text": "Uses D3.js from CDN",
        "check": lambda h: "d3" in h.lower() and (
            "cdn" in h.lower() or "jsdelivr" in h.lower() or "unpkg" in h.lower()
            or "cdnjs" in h.lower() or "d3.min.js" in h.lower() or "d3@" in h.lower()
        ),
        "evidence_search": r'(?i)(d3[@\.\w]*(?:cdn|jsdelivr|unpkg|cdnjs)[^\s"\'<>]*|<script[^>]*d3[^>]*>)'
    },
    {
        "text": "Single standalone HTML file",
        "check": lambda h: h.strip().startswith("<!") or h.strip().startswith("<html"),
        "evidence_search": r'^<!DOCTYPE|^<html'
    },
    {
        "text": "Nodes are clickable (click handlers)",
        "check": lambda h: (
            ("onclick" in h.lower() or ".on('click'" in h or '.on("click"' in h
             or ".on(\"click\"" in h or "addEventListener('click'" in h
             or 'addEventListener("click"' in h or ".on('click'" in h)
        ),
        "evidence_search": r'onclick|\.on\([\'"]click[\'"]|addEventListener\([\'"]click[\'"]'
    },
    {
        "text": "Multiple zoom levels (at least 2 distinct views)",
        "check": lambda h: (
            any(w in h.lower() for w in ["level 1", "level1", "level-1", "overview", "zoom", "drill"])
            or re.search(r'level[_\s]?[123]', h.lower()) is not None
            or ("zoomIn" in h or "zoomOut" in h or "zoom(" in h or "d3.zoom" in h
                or "scale" in h.lower())
            or ("phase" in h.lower() and ("detail" in h.lower() or "expand" in h.lower()))
        ),
        "evidence_search": r'(?i)(level[_\s]?[123]|d3\.zoom|zoomIn|zoomOut|scaleExtent|zoom\s*=)'
    },
    {
        "text": "Breadcrumb or back navigation",
        "check": lambda h: any(w in h.lower() for w in [
            "breadcrumb", "back-btn", "back-button", "backbtn", "go back",
            "goback", "nav-back", "previous", "navigatestep", "navigate"
        ]) or re.search(r'back.*level|return.*overview|navigate.*back|←|›', h) is not None,
        "evidence_search": r'(?i)(breadcrumb|back-btn|previous|navigateStep|nav-back|›|←)'
    },
    {
        "text": "Custom styled nodes (not default SVG)",
        "check": lambda h: (
            ("border-radius" in h or "box-shadow" in h or "rounded" in h.lower()
             or "rx=" in h or "rx:" in h or "fill:" in h or "fill=" in h)
            and ("hover" in h.lower() or "transition" in h.lower())
        ),
        "evidence_search": r'(?:border-radius|box-shadow|rx=|rx:)[^;}\n]*'
    },
    {
        "text": "Smooth transitions between states",
        "check": lambda h: "transition" in h.lower() and any(w in h.lower() for w in [
            "duration", "300", "400", "ease", "d3.transition", ".transition(",
            "0.15s", "0.2s", "0.25s", "0.3s", "0.35s", "cubic-bezier"
        ]),
        "evidence_search": r'(?i)(transition[^;}{]*(?:duration|ease|cubic|0\.\d+s))'
    },
    {
        "text": "Dark theme styling (#0F0F0F or similar dark background)",
        "check": lambda h: any(c in h.lower() for c in [
            "#0f0f0f", "#0f1117", "#111", "#1a1a1a", "#161b22", "#0d1117",
            "background: #0", "background:#0", "background: #1", "background:#1"
        ]),
        "evidence_search": r'(?i)(background\s*:\s*#0[0-9a-f]{5}|background\s*:\s*#1[0-9a-f]{5})'
    },
    {
        "text": "Orthogonal connectors (right-angle paths)",
        "check": lambda h: (
            bool(re.search(r'["\']M\s*[\d.]+ [\d.]+ H\s*[\d.]', h))  # SVG H/V commands
            or bool(re.search(r'["\']M\s*[\d.]+,[\d.]+ H[\d.]', h))
            or "H${" in h or "V${" in h  # Template literal H/V commands
            or bool(re.search(r'M\$\{.*\}\s*H\$\{', h))  # Template H commands
            or ("elbow" in h.lower() or "orthogonal" in h.lower())
            or bool(re.search(r'connector.*line|connector-line', h.lower()))
        ),
        "evidence_search": r'(?:H\$\{|V\$\{|H\s*[\d.]+|V\s*[\d.]+|elbow|orthogonal|connector.*line)'
    },
    {
        "text": "Action pills on connectors",
        "check": lambda h: (
            ("pill" in h.lower() and ("connector" in h.lower() or "edge" in h.lower() or "action" in h.lower()))
            or ("action" in h.lower() and ("pill" in h.lower() or "label" in h.lower()))
            or bool(re.search(r'pill[WH_]|pillW|pillH|action.?pill|ACTION_PILL', h))
        ),
        "evidence_search": r'(?i)(pill[WH_]|action.?pill|ACTION_PILL)'
    },
]

# ──────────────────────────────────────────────
# Eval-specific assertions
# ──────────────────────────────────────────────
CHECKOUT_ASSERTIONS = [
    {
        "text": "Decision diamonds for validation steps",
        "check": lambda h: (
            "diamond" in h.lower() or "rotate(45" in h or "transform: rotate" in h
            or "polygon" in h.lower() or bool(re.search(r'decision|diamond', h.lower()))
        ),
        "evidence_search": r'(?i)(diamond|rotate\(45|polygon|decision)'
    },
    {
        "text": "Error paths with distinct red styling",
        "check": lambda h: (
            ("error" in h.lower() or "fail" in h.lower())
            and ("red" in h.lower() or "#ff" in h.lower() or "#e5484d" in h.lower()
                 or "#ef5350" in h.lower() or "#dc" in h.lower() or "#da3633" in h.lower()
                 or "#f28b8b" in h.lower())
        ),
        "evidence_search": r'(?i)(error|fail)[^}]*(?:red|#ff|#e5|#ef|#dc|#da|#f28)'
    },
    {
        "text": "Happy path visually highlighted",
        "check": lambda h: (
            "happy" in h.lower()
            or ("path" in h.lower() and ("highlight" in h.lower() or "thick" in h.lower()
                or "bold" in h.lower() or "stroke-width: 3" in h or "stroke-width:3" in h
                or "stroke-width: 2.5" in h or "stroke-width:2.5" in h))
        ),
        "evidence_search": r'(?i)(happy.?path|highlight.*path|process.?happy|tag.?happy|connector.?happy)'
    },
]

MERMAID_ASSERTIONS = [
    {
        "text": "All 10 Mermaid nodes preserved",
        "check": lambda h: all(w.lower() in h.lower() for w in [
            "Start", "Search Products", "Found results", "Product Detail",
            "No Results", "In Stock", "Add to Cart", "Notify", "Checkout", "Order Confirmed"
        ]),
        "evidence_search": r'(?i)(Start|Search Products|Found results|Product Detail|No Results|In Stock|Add to Cart|Notify|Checkout|Order Confirmed)'
    },
    {
        "text": "Start/end nodes use pill or stadium shapes",
        "check": lambda h: (
            any(w in h.lower() for w in ["pill", "stadium", "rounded", "rx=", "border-radius"])
            and ("start" in h.lower() and ("confirmed" in h.lower() or "end" in h.lower()))
        ),
        "evidence_search": r'(?i)(pill|stadium|rx=.*start|start.*rx=|terminal.*rx=|node-start.*rounded)'
    },
    {
        "text": "Decision nodes use diamond shapes",
        "check": lambda h: (
            ("diamond" in h.lower() or "rotate(45" in h or "polygon" in h.lower())
            and ("found" in h.lower() or "stock" in h.lower() or "decision" in h.lower())
        ),
        "evidence_search": r'(?i)(diamond.*decision|decision.*diamond|polygon.*found|rotate\(45.*decision|decision.*rotate)'
    },
]

# Skill-specific assertions (only checked for with_skill variants)
SKILL_SPECIFIC = [
    {
        "text": "Uses Software DS color tokens",
        "check": lambda h: any(t in h for t in [
            "#013D5B", "#1C1A17", "#E0DCD3", "--sds-", "#0C4A69",
            "#62800B", "#8A7515", "#805AA1", "#B8D944"
        ]),
        "evidence_search": r'(#013D5B|#1C1A17|#E0DCD3|--sds-|#0C4A69|#62800B|#8A7515|#805AA1|#B8D944)'
    },
    {
        "text": "Three distinct zoom levels",
        "check": lambda h: (
            (h.lower().count("level") >= 3
             or ("overview" in h.lower() and "detail" in h.lower()
                 and ("flow" in h.lower() or "screen" in h.lower())))
            and any(w in h.lower() for w in ["sidebar", "modal", "panel", "detail"])
        ),
        "evidence_search": r'(?i)(level\s*[123]|renderLevel[123]|overview.*detail|sidebar|detail.?panel)'
    },
]


def find_evidence(html, pattern):
    """Find first match of evidence pattern in HTML."""
    try:
        match = re.search(pattern, html, re.MULTILINE)
        if match:
            start = max(0, match.start() - 20)
            end = min(len(html), match.end() + 20)
            snippet = html[start:end].replace('\n', ' ').strip()
            if len(snippet) > 120:
                snippet = snippet[:120] + '...'
            return snippet
        return None
    except Exception:
        return None


def grade_file(html_path, assertions):
    """Grade an HTML file against a list of assertions."""
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    results = []
    for a in assertions:
        passed = a["check"](html)
        evidence_pattern = a.get("evidence_search", "")
        if passed and evidence_pattern:
            snippet = find_evidence(html, evidence_pattern)
            evidence = f"Found: ...{snippet}..." if snippet else f"Found in {os.path.basename(html_path)}"
        elif not passed:
            evidence = f"Not found in {os.path.basename(html_path)}"
        else:
            evidence = f"Found in {os.path.basename(html_path)}"

        results.append({
            "text": a["text"],
            "passed": passed,
            "evidence": evidence
        })

    return results


# ──────────────────────────────────────────────
# Eval definitions
# ──────────────────────────────────────────────
evals = [
    {
        "name": "onboarding-flow",
        "eval_id": 0,
        "with_skill": "onboarding-flow/with_skill/outputs/onboarding-flow.html",
        "without_skill": "onboarding-flow/without_skill/outputs/onboarding-flow.html",
        "extra_assertions": [],
    },
    {
        "name": "checkout-flow",
        "eval_id": 1,
        "with_skill": "checkout-flow/with_skill/outputs/checkout-flow.html",
        "without_skill": "checkout-flow/without_skill/outputs/checkout-flow.html",
        "extra_assertions": CHECKOUT_ASSERTIONS,
    },
    {
        "name": "mermaid-conversion",
        "eval_id": 2,
        "with_skill": "mermaid-conversion/with_skill/outputs/product-search-flow.html",
        "without_skill": "mermaid-conversion/without_skill/outputs/flow-diagram.html",
        "extra_assertions": MERMAID_ASSERTIONS,
    },
]

# ──────────────────────────────────────────────
# Run grading
# ──────────────────────────────────────────────
print("=" * 60)
print("Iteration-3 Grading Results")
print("=" * 60)
print()

summary = []

for ev in evals:
    for variant in ["with_skill", "without_skill"]:
        html_path = os.path.join(WORKSPACE, ev[variant])

        if not os.path.exists(html_path):
            print(f"  MISSING: {html_path}")
            continue

        # Build assertion list
        assertions = COMMON_ASSERTIONS + ev["extra_assertions"]
        if variant == "with_skill":
            assertions = assertions + SKILL_SPECIFIC

        results = grade_file(html_path, assertions)

        passed = sum(1 for r in results if r["passed"])
        total = len(results)
        pass_rate = round(passed / total, 2) if total > 0 else 0

        # Build grading output
        grading = {
            "eval_id": ev["eval_id"],
            "eval_name": ev["name"],
            "variant": variant,
            "pass_rate": pass_rate,
            "passed": passed,
            "total": total,
            "expectations": results
        }

        # Save grading.json in the run directory (e.g., onboarding-flow/with_skill/grading.json)
        run_dir = os.path.join(WORKSPACE, ev["name"], variant)
        grading_path = os.path.join(run_dir, "grading.json")
        with open(grading_path, 'w', encoding='utf-8') as f:
            json.dump(grading, f, indent=2)

        summary.append({
            "eval": ev["name"],
            "variant": variant,
            "passed": passed,
            "total": total,
            "pass_rate": pass_rate
        })

        status = "PASS" if passed == total else "PARTIAL"
        print(f"  [{status}] {ev['name']} / {variant}: {passed}/{total} ({pass_rate*100:.0f}%)")
        for r in results:
            mark = "+" if r["passed"] else "-"
            print(f"    [{mark}] {r['text']}")
            if not r["passed"]:
                print(f"        {r['evidence']}")
        print()

# Summary table
print("=" * 60)
print("Summary")
print("=" * 60)
print(f"{'Eval':<22} {'Variant':<16} {'Score':<8} {'Rate':<6}")
print("-" * 52)
for s in summary:
    print(f"{s['eval']:<22} {s['variant']:<16} {s['passed']}/{s['total']:<5} {s['pass_rate']*100:.0f}%")

# Compare with_skill vs without_skill
print()
print("Skill Uplift:")
for ev_name in ["onboarding-flow", "checkout-flow", "mermaid-conversion"]:
    ws = next((s for s in summary if s["eval"] == ev_name and s["variant"] == "with_skill"), None)
    wos = next((s for s in summary if s["eval"] == ev_name and s["variant"] == "without_skill"), None)
    if ws and wos:
        delta = ws["pass_rate"] - wos["pass_rate"]
        sign = "+" if delta >= 0 else ""
        print(f"  {ev_name}: with_skill={ws['pass_rate']*100:.0f}% vs without_skill={wos['pass_rate']*100:.0f}% ({sign}{delta*100:.0f}%)")

print()
print("All grading complete. Results saved to grading.json in each run directory.")
