# Awesome Multilingual LLM [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![papers](https://img.shields.io/badge/papers-2728-blue) ![updated](https://img.shields.io/badge/updated-Nov%202026-green) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing) [![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

Most large language models (LLMs) are trained mostly on English, but people speak more than 7,000 languages. This repository collects research on **LLMs that work beyond English**: how multilingual models are built, how abilities and safety carry over (or fail to carry over) from one language to another, how to evaluate models across languages and cultures, and how to serve low-resource languages. It covers **models, pretraining data, tokenization, language adaptation, instruction tuning and alignment, cross-lingual transfer, prompting and reasoning, interpretability, translation, speech and vision, benchmarks, culture, fairness and safety**.

![](dp2.png)

- **2,728 papers** across 33 topics. 2,328 of them are from 2024 or later.
- Candidates came from the ACL Anthology (2023-2026 main conferences, Findings, TACL and workshops), ICLR, ICML, NeurIPS and COLM accepted-paper lists, Semantic Scholar searches, and earlier multilingual-LLM collections (see [Related Lists](#related-lists)).
- A paper is listed when its main contribution concerns multilingual, cross-lingual, non-English, low-resource or cross-cultural behavior of LLMs. Preprints and workshop papers also had to pass a citation bar that depends on their age, so the newest months are covered less completely than earlier years. Shared-task system papers and narrow single-language applications are left out.
- Each paper's link points to its ACL Anthology page when it has one, otherwise to arXiv. Every link was checked, and titles and dates come from those sources.
- Each one-line note was written from the paper's abstract and then checked against it a second time.
- The list has one page per topic group (see [Contents](#contents)). To search everything at once, use [`data/papers.yaml`](data/papers.yaml), the source for every page.

## Start Here

If you are new to the area, these papers give the shape of the field.

| Paper | Why read it |
|---|---|
| [Multilingual LLM survey](https://arxiv.org/abs/2404.04925) (2024) | A map of the field, with resources and a taxonomy of methods. |
| [XLM-R](https://aclanthology.org/2020.acl-main.747/) (2019) / [mT5](https://aclanthology.org/2021.naacl-main.41/) (2020) | The pre-LLM multilingual models, and the first clear look at the "curse of multilinguality". |
| [BLOOM](https://arxiv.org/abs/2211.05100) (2022) / [BLOOMZ & mT0](https://aclanthology.org/2023.acl-long.891/) (2023) | An open 176B model trained on 46 natural languages, and evidence that multitask finetuning in English transfers to other languages. |
| [Aya Model](https://aclanthology.org/2024.acl-long.845/) (2024) / [Aya Dataset](https://aclanthology.org/2024.acl-long.620/) (2024) | Instruction tuning in 101 languages with human-written data collected from fluent speakers. |
| [Turning English-centric LLMs into polyglots](https://aclanthology.org/2024.findings-emnlp.766/) (2023) / [A pinch of multilinguality](https://aclanthology.org/2024.findings-acl.136/) (2024) | A small amount of multilingual instruction data goes a long way. |
| [Do Llamas work in English?](https://aclanthology.org/2024.acl-long.820/) (2024) / [Language-specific neurons](https://aclanthology.org/2024.acl-long.309/) (2024) | What happens inside an English-dominated model when it reads and writes other languages. |
| [Tokenizer unfairness](https://arxiv.org/abs/2305.15425) (2023) | The same text can cost many times more tokens in some languages than in others. |
| [MEGA](https://aclanthology.org/2023.emnlp-main.258/) (2023) / [Global-MMLU](https://aclanthology.org/2025.acl-long.919/) (2024) / [INCLUDE](https://arxiv.org/abs/2411.19799) (2024) | Evaluating LLMs across many languages, and why translated English benchmarks are not enough. |
| [MGSM](https://arxiv.org/abs/2210.03057) (2022) / [Crosslingual test-time scaling](https://arxiv.org/abs/2505.05408) (2025) | Reasoning in other languages, from chain-of-thought prompting to today's reasoning models. |
| [ALMA](https://arxiv.org/abs/2309.11674) (2023) / [Tower](https://arxiv.org/abs/2402.17733) (2024) | How general LLMs became strong translators. |
| [Language confusion](https://aclanthology.org/2024.emnlp-main.380/) (2024) | Models often answer in the wrong language, and this measures how often and why. |
| [BLEnD](https://arxiv.org/abs/2406.09948) (2024) / [Culture in LLMs survey](https://aclanthology.org/2024.emnlp-main.882/) (2024) | Language and culture are linked. This is how cultural knowledge in LLMs is measured. |
| [Low-resource languages jailbreak GPT-4](https://arxiv.org/abs/2310.02446) (2023) / [MultiJail](https://arxiv.org/abs/2310.06474) (2023) | Safety training done mostly in English leaves gaps in other languages. |
| [MTOB](https://arxiv.org/abs/2309.16575) (2023) | Learning a language that has almost no web data from a single grammar book. |

## Papers by Year

| Year | Papers |
|---|---|
| before 2023 | 101 |
| 2023 | 299 |
| 2024 | 666 |
| 2025 | 858 |
| 2026 | 804 |

## Contents

- **[Surveys & Foundations](papers/surveys-and-foundations.md)** (130)
  - [Surveys & Position Papers](papers/surveys-and-foundations.md#surveys--position-papers) (79)
  - [Foundational Multilingual Models & Analyses (pre-2023)](papers/surveys-and-foundations.md#foundational-multilingual-models--analyses-pre-2023) (51)
- **[Models](papers/models.md)** (128)
  - [Massively Multilingual LLMs](papers/models.md#massively-multilingual-llms) (35)
  - [Regional & Language-Specific LLMs](papers/models.md#regional--language-specific-llms) (93)
- **[Data & Tokenization](papers/data-and-tokenization.md)** (122)
  - [Pretraining Corpora & Data Curation](papers/data-and-tokenization.md#pretraining-corpora--data-curation) (47)
  - [Tokenization & Vocabulary](papers/data-and-tokenization.md#tokenization--vocabulary) (75)
- **[Training & Adaptation](papers/training-and-adaptation.md)** (230)
  - [Multilingual Pretraining, Data Mixtures & Scaling](papers/training-and-adaptation.md#multilingual-pretraining-data-mixtures--scaling) (23)
  - [Language Adaptation & Continual Pretraining](papers/training-and-adaptation.md#language-adaptation--continual-pretraining) (65)
  - [Multilingual Instruction Tuning](papers/training-and-adaptation.md#multilingual-instruction-tuning) (52)
  - [Multilingual Preference Optimization & Reward Models](papers/training-and-adaptation.md#multilingual-preference-optimization--reward-models) (19)
  - [Cross-lingual Transfer & Alignment Methods](papers/training-and-adaptation.md#cross-lingual-transfer--alignment-methods) (71)
- **[Prompting & Reasoning](papers/prompting-and-reasoning.md)** (141)
  - [Prompting & In-Context Learning](papers/prompting-and-reasoning.md#prompting--in-context-learning) (47)
  - [Multilingual Reasoning](papers/prompting-and-reasoning.md#multilingual-reasoning) (94)
- **[Understanding Multilinguality](papers/understanding-multilinguality.md)** (121)
  - [Interpretability: How LLMs Represent Languages](papers/understanding-multilinguality.md#interpretability-how-llms-represent-languages) (103)
  - [Language Confusion & Output-Language Control](papers/understanding-multilinguality.md#language-confusion--output-language-control) (18)
- **[Tasks & Modalities](papers/tasks-and-modalities.md)** (875)
  - [Machine Translation with LLMs](papers/tasks-and-modalities.md#machine-translation-with-llms) (261)
  - [Translation & Generation Evaluation with LLMs](papers/tasks-and-modalities.md#translation--generation-evaluation-with-llms) (39)
  - [Code-Switching, Dialects & Transliteration](papers/tasks-and-modalities.md#code-switching-dialects--transliteration) (58)
  - [Cross-lingual Knowledge, Factuality & Consistency](papers/tasks-and-modalities.md#cross-lingual-knowledge-factuality--consistency) (77)
  - [Multilingual Retrieval, Embeddings & RAG](papers/tasks-and-modalities.md#multilingual-retrieval-embeddings--rag) (62)
  - [Low-Resource & Endangered Languages](papers/tasks-and-modalities.md#low-resource--endangered-languages) (39)
  - [Multilingual Speech & Audio LLMs](papers/tasks-and-modalities.md#multilingual-speech--audio-llms) (102)
  - [Multilingual & Multicultural Vision-Language Models](papers/tasks-and-modalities.md#multilingual--multicultural-vision-language-models) (144)
  - [Code & Structured Data](papers/tasks-and-modalities.md#code--structured-data) (21)
  - [Domain Applications](papers/tasks-and-modalities.md#domain-applications) (72)
- **[Evaluation](papers/evaluation.md)** (388)
  - [Multilingual Benchmarks: Knowledge, Understanding & Reasoning](papers/evaluation.md#multilingual-benchmarks-knowledge-understanding--reasoning) (73)
  - [Multilingual Benchmarks: Generation, Chat & Instruction Following](papers/evaluation.md#multilingual-benchmarks-generation-chat--instruction-following) (42)
  - [Language-Specific Benchmarks & Evaluations](papers/evaluation.md#language-specific-benchmarks--evaluations) (216)
  - [Evaluation Methodology & LLM-as-a-Judge](papers/evaluation.md#evaluation-methodology--llm-as-a-judge) (57)
- **[Culture, Fairness & Safety](papers/culture-fairness-and-safety.md)** (593)
  - [Cultural Knowledge & Awareness Benchmarks](papers/culture-fairness-and-safety.md#cultural-knowledge--awareness-benchmarks) (128)
  - [Cultural Alignment & Values](papers/culture-fairness-and-safety.md#cultural-alignment--values) (121)
  - [Language Bias, Fairness & Linguistic Equity](papers/culture-fairness-and-safety.md#language-bias-fairness--linguistic-equity) (100)
  - [Multilingual Safety, Jailbreaks & Guardrails](papers/culture-fairness-and-safety.md#multilingual-safety-jailbreaks--guardrails) (244)

## Related Lists

- [LightChen233/Awesome-Multilingual-LLM](https://github.com/LightChen233/Awesome-Multilingual-LLM): companion list to the survey *Multilingual Large Language Model: A Survey of Resources, Taxonomy and Frontiers*.
- [tjunlp-lab/Awesome-Multilingual-LLMs-Papers](https://github.com/tjunlp-lab/Awesome-Multilingual-LLMs-Papers): papers on multilingual LLMs, organized by topic.
- [NaiveNeuron/awesome-multilingual-llm-benchmarks](https://github.com/NaiveNeuron/awesome-multilingual-llm-benchmarks): multilingual and non-English LLM benchmarks.
- [simran-khanuja/awesome-multilingual-nlp](https://github.com/simran-khanuja/awesome-multilingual-nlp): multilingual NLP more broadly.

## Contributing

Pull requests are welcome. To add a paper, add an entry to [`data/papers.yaml`](data/papers.yaml) with `title`, `date` (YYYY-MM), `authors`, `venue` (if published), `section` (one of the keys in [`scripts/build_readme.py`](scripts/build_readme.py)), a link (`acl`, `arxiv` or `url`) and a one-sentence `note`, then run `python scripts/build_readme.py` to regenerate the README and topic pages.

## License

[MIT](LICENSE)
