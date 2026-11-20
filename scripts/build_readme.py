"""Regenerate README.md and the per-topic pages in papers/ from data/papers.yaml.

Usage: python scripts/build_readme.py
"""
import re
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

# (group title, intro, [(section key, section title), ...]) in README order.
SECTIONS = [
    ("Surveys & Foundations", "Overviews of the field, and the pre-2023 multilingual models and analyses that today's LLMs build on.", [
        ("surveys", "Surveys & Position Papers"),
        ("foundations", "Foundational Multilingual Models & Analyses (pre-2023)"),
    ]),
    ("Models", "Technical reports of multilingual LLMs and of LLMs built for one language or region.", [
        ("models_multilingual", "Massively Multilingual LLMs"),
        ("models_regional", "Regional & Language-Specific LLMs"),
    ]),
    ("Data & Tokenization", "Where multilingual training text comes from, and how it is cut into tokens.", [
        ("pretrain_data", "Pretraining Corpora & Data Curation"),
        ("tokenization", "Tokenization & Vocabulary"),
    ]),
    ("Training & Adaptation", "Pretraining mixtures, adapting English-centric models to new languages, instruction tuning, preference alignment and cross-lingual transfer.", [
        ("pretraining_scaling", "Multilingual Pretraining, Data Mixtures & Scaling"),
        ("adaptation", "Language Adaptation & Continual Pretraining"),
        ("instruction_tuning", "Multilingual Instruction Tuning"),
        ("preference_alignment", "Multilingual Preference Optimization & Reward Models"),
        ("crosslingual_transfer", "Cross-lingual Transfer & Alignment Methods"),
    ]),
    ("Prompting & Reasoning", "Using LLMs across languages at inference time, and reasoning in languages other than English.", [
        ("prompting", "Prompting & In-Context Learning"),
        ("reasoning", "Multilingual Reasoning"),
    ]),
    ("Understanding Multilinguality", "What happens inside a multilingual LLM, and why it sometimes answers in the wrong language.", [
        ("interpretability", "Interpretability: How LLMs Represent Languages"),
        ("language_fidelity", "Language Confusion & Output-Language Control"),
    ]),
    ("Tasks & Modalities", "Translation, code-switching, knowledge, retrieval, low-resource languages, speech, vision, code and domain applications.", [
        ("mt", "Machine Translation with LLMs"),
        ("mt_eval", "Translation & Generation Evaluation with LLMs"),
        ("codeswitching", "Code-Switching, Dialects & Transliteration"),
        ("knowledge", "Cross-lingual Knowledge, Factuality & Consistency"),
        ("retrieval", "Multilingual Retrieval, Embeddings & RAG"),
        ("low_resource", "Low-Resource & Endangered Languages"),
        ("speech", "Multilingual Speech & Audio LLMs"),
        ("vision", "Multilingual & Multicultural Vision-Language Models"),
        ("code", "Code & Structured Data"),
        ("domains", "Domain Applications"),
    ]),
    ("Evaluation", "Benchmarks across many languages, single-language benchmarks, and how to evaluate multilingual models well.", [
        ("bench_general", "Multilingual Benchmarks: Knowledge, Understanding & Reasoning"),
        ("bench_generation", "Multilingual Benchmarks: Generation, Chat & Instruction Following"),
        ("bench_language", "Language-Specific Benchmarks & Evaluations"),
        ("eval_methods", "Evaluation Methodology & LLM-as-a-Judge"),
    ]),
    ("Culture, Fairness & Safety", "Cultural knowledge and values, unequal performance across languages, and safety outside English.", [
        ("culture_eval", "Cultural Knowledge & Awareness Benchmarks"),
        ("culture_align", "Cultural Alignment & Values"),
        ("fairness", "Language Bias, Fairness & Linguistic Equity"),
        ("safety", "Multilingual Safety, Jailbreaks & Guardrails"),
    ]),
]


def anchor(title):
    a = title.strip().lower()
    a = re.sub(r"[^\w\- ]", "", a)
    return a.replace(" ", "-")


def link(p):
    if p.get("acl"):
        return f"https://aclanthology.org/{p['acl']}/"
    if p.get("arxiv"):
        return f"https://arxiv.org/abs/{p['arxiv']}"
    return p["url"]


def md(text):
    return str(text).replace("*", "\\*").replace("|", "\\|")


def entry(p):
    line = f"- `{p['date']}` **[{md(p['title'])}]({link(p)})**"
    meta = " · ".join(x for x in [p.get("authors"), f"*{p['venue']}*" if p.get("venue") else None] if x)
    if meta:
        line += f" — {meta}"
    extra = []
    if p.get("acl") and p.get("arxiv"):
        extra.append(f"[[arXiv](https://arxiv.org/abs/{p['arxiv']})]")
    if p.get("code"):
        extra.append(f"[[code]({p['code']})]")
    if extra:
        line += " · " + " ".join(extra)
    if p.get("note"):
        line += f"<br>{md(p['note'])}"
    return line


def main():
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text())
    known = {k for _, _, subs in SECTIONS for k, _ in subs}
    unknown = {p["section"] for p in papers} - known
    assert not unknown, f"unknown sections: {unknown}"
    by_sec = {}
    for p in papers:
        by_sec.setdefault(p["section"], []).append(p)

    head = (ROOT / "scripts" / "readme_head.md").read_text()
    tail = (ROOT / "scripts" / "readme_tail.md").read_text()
    years = Counter(int(str(p["date"])[:4]) for p in papers)
    recent = sum(v for y, v in years.items() if y >= 2024)
    for k, v in {"{{N_PAPERS_PLAIN}}": str(len(papers)), "{{N_PAPERS}}": f"{len(papers):,}", "{{N_RECENT}}": f"{recent:,}",
                 "{{N_SECTIONS}}": str(len(known))}.items():
        head = head.replace(k, v)

    toc = ["## Contents", ""]
    (ROOT / "papers").mkdir(exist_ok=True)
    for gtitle, intro, subs in SECTIONS:
        slug = anchor(gtitle.replace("&", "and"))
        gcount = sum(len(by_sec.get(k, [])) for k, _ in subs)
        toc.append(f"- **[{gtitle}](papers/{slug}.md)** ({gcount})")
        page = [f"# {gtitle}", "", f"[⬅ Back to the main list](../README.md) · {gcount:,} papers, newest first within each section.", "",
                f"*{intro}*", ""]
        page += [f"- [{t}](#{anchor(t)}) ({len(by_sec.get(k, []))})" for k, t in subs] + [""]
        for key, stitle in subs:
            items = sorted(by_sec.get(key, []), key=lambda p: (str(p["date"]), p["title"]), reverse=True)
            toc.append(f"  - [{stitle}](papers/{slug}.md#{anchor(stitle)}) ({len(items)})")
            page += [f"## {stitle}", ""] + [entry(p) for p in items] + ["", "[⬆ Back to top](#)", ""]
        page += ["[⬅ Back to the main list](../README.md)", ""]
        (ROOT / "papers" / f"{slug}.md").write_text("\n".join(page))

    start = yaml.safe_load((ROOT / "data" / "start_here.yaml").read_text())
    by_title = {p["title"]: p for p in papers}
    rows = ["| Paper | Why read it |", "|---|---|"]
    for s in start:
        cells = []
        for t in s["papers"]:
            assert t in by_title, f"start_here paper not in list: {t}"
            p = by_title[t]
            cells.append(f"[{s.get('labels', {}).get(t, t)}]({link(p)}) ({str(p['date'])[:4]})")
        rows.append(f"| {' / '.join(cells)} | {s['why']} |")
    head = head.replace("{{START_HERE}}", "\n".join(rows))

    year_rows = ["| Year | Papers |", "|---|---|"] + [f"| {y} | {years[y]:,} |" for y in sorted(years) if y >= 2023]
    year_rows.insert(2, f"| before 2023 | {sum(v for y, v in years.items() if y < 2023):,} |")
    head = head.replace("{{YEAR_TABLE}}", "\n".join(year_rows))
    (ROOT / "README.md").write_text("\n".join([head.rstrip(), "", *toc, "", tail.strip(), ""]))
    print(f"README.md + {len(SECTIONS)} pages: {len(papers)} papers")


if __name__ == "__main__":
    main()
