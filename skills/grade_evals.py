#!/usr/bin/env python3
"""Grade all eval outputs against their assertions and produce grading.json + benchmark.json files."""

from __future__ import annotations

import json
import os
import glob as globmod
import re
import sys

SKILLS_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIGS = [
    {
        "skill": "screen-flow-diagram",
        "iteration": "iteration-2",
        "evals": ["food-delivery-flow", "login-signup-flow", "desktop-settings-flow"],
    },
    {
        "skill": "journey-map",
        "iteration": "iteration-3",
        "evals": ["saas-onboarding", "ecommerce-journey", "structured-data"],
    },
    {
        "skill": "interactive-flow-diagram",
        "iteration": "iteration-5",
        "evals": ["onboarding-flow", "checkout-flow", "mermaid-conversion"],
    },
]


def check_assertion(assertion: dict, output_dir: str) -> dict:
    """Check a single assertion against files in output_dir. Returns {text, passed, evidence}."""
    name = assertion["name"]
    atype = assertion["type"]

    if atype == "file_exists":
        pattern = assertion.get("pattern", "*.html")
        matches = globmod.glob(os.path.join(output_dir, pattern))
        if matches:
            fname = os.path.basename(matches[0])
            return {"text": name, "passed": True, "evidence": f"Found: {fname} exists in outputs directory"}
        return {"text": name, "passed": False, "evidence": f"Missing: no file matching {pattern}"}

    if atype == "contains":
        text = assertion["text"]
        also = assertion.get("also_contains", [])

        # Read all HTML files in the output dir
        html_files = globmod.glob(os.path.join(output_dir, "*.html"))
        if not html_files:
            return {"text": name, "passed": False, "evidence": "No HTML files found in outputs"}

        content = ""
        for f in html_files:
            with open(f, "r", encoding="utf-8", errors="replace") as fh:
                content += fh.read()

        content_lower = content.lower()
        text_lower = text.lower()

        if text_lower not in content_lower:
            return {"text": name, "passed": False, "evidence": f"Missing: '{text}' not found in output"}

        # Check also_contains
        missing = []
        for also_text in also:
            if also_text.lower() not in content_lower:
                missing.append(also_text)

        if missing:
            return {
                "text": name,
                "passed": False,
                "evidence": f"Found '{text}' but missing: {', '.join(missing)}",
            }

        # Find context around the match
        idx = content_lower.find(text_lower)
        snippet = content[max(0, idx - 20) : idx + len(text) + 30].replace("\n", " ").strip()
        return {"text": name, "passed": True, "evidence": f"Found: '{text}' in output"}

    return {"text": name, "passed": False, "evidence": f"Unknown assertion type: {atype}"}


def grade_eval(skill: str, iteration: str, eval_name: str, config: str) -> dict | None:
    """Grade a single eval config (with_skill or without_skill)."""
    ws = os.path.join(SKILLS_DIR, f"{skill}-workspace", iteration, eval_name)
    meta_path = os.path.join(ws, "eval_metadata.json")
    output_dir = os.path.join(ws, config, "outputs")
    grading_path = os.path.join(ws, config, "grading.json")

    if not os.path.exists(meta_path):
        print(f"  SKIP {eval_name}/{config}: no eval_metadata.json")
        return None

    if not os.path.exists(output_dir) or not os.listdir(output_dir):
        print(f"  SKIP {eval_name}/{config}: no outputs")
        return None

    with open(meta_path) as f:
        meta = json.load(f)

    assertions = meta.get("assertions", [])
    if not assertions:
        print(f"  SKIP {eval_name}/{config}: no assertions defined")
        return None

    expectations = []
    for assertion in assertions:
        result = check_assertion(assertion, output_dir)
        expectations.append(result)

    passed = sum(1 for e in expectations if e["passed"])
    total = len(expectations)
    pass_rate = passed / total if total > 0 else 0

    grading = {
        "eval_name": eval_name,
        "configuration": config,
        "expectations": expectations,
        "pass_rate": round(pass_rate, 4),
    }

    with open(grading_path, "w") as f:
        json.dump(grading, f, indent=2)

    print(f"  {eval_name}/{config}: {passed}/{total} ({pass_rate*100:.0f}%)")
    return grading


def build_benchmark(skill: str, iteration: str, eval_names: list[str]) -> dict:
    """Build benchmark.json aggregating results across evals."""
    ws = os.path.join(SKILLS_DIR, f"{skill}-workspace", iteration)

    with_rates = []
    without_rates = []

    for name in eval_names:
        for config, rates in [("with_skill", with_rates), ("without_skill", without_rates)]:
            gpath = os.path.join(ws, name, config, "grading.json")
            if os.path.exists(gpath):
                with open(gpath) as f:
                    data = json.load(f)
                rates.append(data["pass_rate"])

    with_avg = sum(with_rates) / len(with_rates) if with_rates else 0
    without_avg = sum(without_rates) / len(without_rates) if without_rates else 0

    benchmark = {
        "skill": skill,
        "iteration": iteration,
        "with_skill_avg": round(with_avg * 100, 1),
        "without_skill_avg": round(without_avg * 100, 1),
        "delta": round((with_avg - without_avg) * 100, 1),
        "eval_count": len(eval_names),
        "with_rates": [round(r * 100, 1) for r in with_rates],
        "without_rates": [round(r * 100, 1) for r in without_rates],
    }

    bpath = os.path.join(ws, "benchmark.json")
    with open(bpath, "w") as f:
        json.dump(benchmark, f, indent=2)

    print(f"\n  Benchmark: WITH {with_avg*100:.1f}% vs WITHOUT {without_avg*100:.1f}% (delta: {(with_avg-without_avg)*100:+.1f}%)")
    return benchmark


def main():
    print("=" * 60)
    print("Grading all evals")
    print("=" * 60)

    for cfg in CONFIGS:
        skill = cfg["skill"]
        iteration = cfg["iteration"]
        eval_names = cfg["evals"]

        print(f"\n── {skill} ({iteration}) ──")

        for eval_name in eval_names:
            grade_eval(skill, iteration, eval_name, "with_skill")
            grade_eval(skill, iteration, eval_name, "without_skill")

        build_benchmark(skill, iteration, eval_names)

    print("\n" + "=" * 60)
    print("Done!")


if __name__ == "__main__":
    main()
