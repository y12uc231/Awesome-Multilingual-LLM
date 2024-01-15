# Awesome-Multilingual-LLM

The repository is designed to support the growing interest within the community in developing large language models (LLMs) that cater not only to English speakers but also to speakers of the other 6,500+ languages worldwide. Its purpose is to aid researchers in discovering pertinent literature in this field. The repository will encompass a comprehensive collection of core training and evaluation datasets, multilingual-capable LLMs, and associated scholarly articles.

![](dp2.png)

### Table of Contents
1. [In-Context Learning and Prompting Strategies](#section1)
2. [Performance and Capabilities in Specific Languages](#section2)
3. [Challenges and Limitations in Multilingual LLMs](#section3)
4. [Multilingual LLMs in Programming and Code](#section4)
5. [Comparative Studies and Benchmarks](#section5)
6. [Datasets And Benchmarks](#section6)
7. [Translation and Language Understanding](#section7)
8. [Instruction Tuning](#section8)
9. [Safety](#section9)
10. [Miscellaneous Studies and Surveys](#section10)


### **In-Context Learning and Prompting Strategies** <a name="section1"></a>
- [2024] [Boosting Many-to-Many Multilingual Translation Performance with Large Language Models via Prompt Strategies and Cross-Lingual Consistency Regularization (XConST)](https://arxiv.org/abs/2401.05861) by Pengzhi Gao et al.
- [2023] [All Languages Matter: On the Multilingual Safety of Large Language Models](https://dx.doi.org/10.48550/arXiv.2310.00905): Develops a multilingual safety benchmark for LLMs, demonstrating the need for safety alignment in non-English languages.
- [2023] [Multilingual Code Co-evolution using Large Language Models](https://dx.doi.org/10.1145/3611643.3616350): Discusses the co-evolution of code in multiple languages using LLMs.
- [2023] [Prompting Large Language Models with Speech Recognition Abilities](https://dx.doi.org/10.48550/arXiv.2307.11795): Presents a method to enhance LLMs with multilingual speech recognition capabilities using a small audio encoder.
- [2023] [M3Exam: A Multilingual, Multimodal, Multilevel Benchmark for Large Language Models](https://dx.doi.org/10.48550/arXiv.2306.05179): Introduces a comprehensive benchmark for evaluating the performance of LLMs across diverse languages.
- [2023] [BigTranslate: Augmenting LLMs with Multilingual Translation Capability over 100 Languages](https://arxiv.org/abs/2305.18098): Presents BigTranslate, a model augmenting LLMs with extensive multilingual translation capabilities.
- [2023] [Eliciting Translation Ability of LLMs via Multilingual Finetuning with Translation Instructions](https://dx.doi.org/10.48550/arXiv.2305.15083): Analyzes how multilingual LLMs carry out translation instructions for different languages through multilingual finetuning.
- [2023] [BUFFET: Benchmarking LLMs for Few-shot Cross-lingual Transfer](https://dx.doi.org/10.48550/arXiv.2305.14857): Introduces BUFFET, a benchmark for evaluating multilingual LLMs in few-shot cross-lingual transfer across various tasks and languages.
- [2023] [ChatGPT Beyond English: Comprehensive Evaluation in Multilingual Learning](https://dx.doi.org/10.48550/arXiv.2304.05613): Evaluates the performance of ChatGPT in multilingual learning across 7 different tasks and 37 languages.
- [2023] [Multilingual Machine Translation with LLMs: Empirical Results and Analysis](https://dx.doi.org/10.48550/arXiv.2304.04675): Investigates the use of LLMs for multilingual machine translation, evaluating popular models including ChatGPT and GPT-4.
- [2023] [Implications of LLMs for Dental Medicine](https://dx.doi.org/10.1111/jerd.13046): Discusses the potential benefits and risks of using LLMs like ChatGPT for dental medicine, with a focus on multilingual communication.
- [2023] [Massively Multilingual Shallow Fusion with LLMs](https://dx.doi.org/10.1109/ICASSP49357.2023.10094796): Explores using a single multilingual language model to improve automatic speech recognition in multiple languages.
- [2022] [Bootstrapping Multilingual Semantic Parsers using Large Language Models](https://dx.doi.org/10.48550/arXiv.2210.07313): Examines the effectiveness of LLMs in translating English datasets into multiple languages for multilingual semantic parsing. 

###  **Performance and Capabilities in Specific Languages** <a name="section2"></a>
- [Holmström et al.](https://www.aclweb.org/anthology/2023.resourceful-1.13): Explores the performance of English and multilingual LLMs in Swedish.

### **Challenges and Limitations in Multilingual LLMs** <a name="section3"></a>
- [Zhu et al.](https://dx.doi.org/10.48550/arXiv.2304.04675): Investigates the advantages and challenges in multilingual machine translation using LLMs.

### **Multilingual LLMs in Programming and Code** <a name="section4"></a>
- [Joshi et al.](https://dx.doi.org/10.48550/arXiv.2208.11640): Introduces RING, a multilingual repair engine powered by a language model trained on code.

### **Comparative Studies and Benchmarks** <a name="section5"></a>
- [Ahuja et al.](https://dx.doi.org/10.48550/arXiv.2211.05100): Discusses the development and evaluation of BLOOM, a 176B-parameter open-access multilingual language model.
- [Lai et al.](https://dx.doi.org/10.48550/arXiv.2304.05613): Evaluates ChatGPT and other LLMs on multilingual NLP tasks.

### **Datasets And Benchmarks** <a name="section6"></a>

- [2023] [CulturaX: A Large, Multilingual Dataset for Training Large Language Models](https://dx.doi.org/10.48550/arXiv.2309.09400): Introduces CulturaX, a large, multilingual dataset for training LLMs in 167 languages, emphasizing quality with careful data cleaning and deduplication.
- [Ladhak et al.](https://dx.doi.org/10.18653/v1/2020.findings-emnlp.360) - Introduces WikiLingua, a benchmark dataset for cross-lingual abstractive summarization in 18 languages from WikiHow (2020).
- [Gupta and Srikumar](https://dx.doi.org/10.18653/v1/2021.acl-short.86) - Presents X-Fact, a multilingual dataset for factual verification in 25 languages labeled for veracity by expert fact-checkers (2021).
- [Nguyen et al.](https://dx.doi.org/10.48550/arXiv.2309.09400) - Proposes CulturaX, with 6.3 trillion tokens in 167 languages, for training multilingual LLMs (2023).
- [Barrière et al.](https://www.aclweb.org/anthology/2022.politicalnlp-1.3) - Introduces a dataset of online debates in English for multilingual stance classification related to the European Green Deal (2022).
- [Wang et al.](https://dx.doi.org/10.48550/arXiv.2308.13387) - Proposes a dataset for evaluating safeguards in LLMs and trains classifiers achieving results similar to GPT-4 (2023).
- [Laperriere et al.](https://www.aclweb.org/anthology/2022.lrec-1.171) - Updates the French MEDIA SLU dataset for spoken language understanding, integrated into the SpeechBrain toolkit (2022).
- [Hu et al.](https://dx.doi.org/10.1162/tacl_a_00609) - Introduces the Multi3WOZ dataset for training and evaluating multilingual and cross-lingual task-oriented dialog systems (2023).
- [2023](https://dx.doi.org/10.48550/arXiv.2303.12528) - Presents MEGA, benchmarking generative LLMs across 70 languages and comparing them to non-autoregressive models (2023).
- [2023](https://dx.doi.org/10.48550/arXiv.2309.07462) - Investigates Large Language Model-based evaluators for multilingual evaluation, highlighting bias and calibration needs (2023).
- [2023](https://dx.doi.org/10.48550/arXiv.2305.13194) - Proposes the SEAHORSE dataset for evaluating multilingual, multifaceted summarization systems (2023).
- [2023](https://dx.doi.org/10.18653/v1/2023.semeval-1.87) - Proposes MINT, a multilingual textual intimacy dataset with tweets in 10 languages (2023).
- [2023](https://dx.doi.org/10.48550/arXiv.2304.05613) - Evaluates ChatGPT on 37 languages across 7 tasks, revealing a performance gap compared to previous models (2023).
- [2023](https://dx.doi.org/10.48550/arXiv.2308.09954) - Proposes Eva-KELLM, a benchmark for evaluating knowledge editing in LLMs with a focus on cross-lingual knowledge transfer (2023).
- [2023](https://dx.doi.org/10.1007/s10579-023-09696-7) - Discusses the ComMA dataset, a multilingual dataset annotated with tags for different types of aggression and bias in four languages (2023).
- [2023](https://arxiv.org/abs/2201.03857) - Introduces the GINCO training dataset for automatic genre identification of web documents.
- [2022](https://dx.doi.org/10.48550/arXiv.2208.11640) - Introduces RING, a multilingual repair engine powered by a large language model trained on code for program repair in multiple languages (2022).
- [2022](https://dx.doi.org/10.48550/arXiv.2211.05955) - Introduces MEE, a Multilingual Event Extraction dataset with over 50K event mentions in 8 languages (2022).
- [Bang et al.](https://arxiv.org/abs/2302.04023) - Presents a framework for evaluating interactive LLMs using a newly designed multimodal dataset.
- [2022] [BigScience: Social Construction of a Multilingual Large Language Model](https://dx.doi.org/10.48550/arXiv.2212.04960): Discusses BigScience, a collaborative project that created a multilingual dataset and trained BLOOM, a multilingual LLM.
- [Zhu et al.](https://dx.doi.org/10.1609/aaai.v36i10.21434) - Proposes the CoST dataset with parallel data from 7 programming languages for code snippet translation (2022).


###  **Translation and Language Understanding** <a name="section7"></a>
- [Guerreiro et al.](https://dx.doi.org/10.1162/tacl_a_00615): Provides insights into the presence of hallucinations in multilingual translation models.
- [Li et al.](https://dx.doi.org/10.48550/arXiv.2305.15083): Discusses the translation abilities of large language models in multilingual contexts.

###  **Instruction Tuning** <a name="section8"></a>

###  **Safety** <a name="section9"></a>
- [2023] [Stereotypes in Multilingual Large Language Models and Cross-Linguistic Leakage](https://dx.doi.org/10.48550/arXiv.2312.07141): Investigates the presence of stereotypes in multilingual LLMs and their cross-linguistic leakage, with an analysis of different languages' susceptibility.
- [2023] [Multilingual Jailbreak Challenges in Large Language Models](https://dx.doi.org/10.48550/arXiv.2310.06474): Explores multilingual jailbreak challenges in LLMs, addressing both unintentional and intentional risks, and proposes a safety fine-tuning framework.

### **Miscellaneous Studies and Surveys** <a name="section10"></a>
- [Pahune et al.](https://dx.doi.org/10.22214/ijraset.2023.54677): Emphasizes recent developments and efforts made for various kinds of LLMs, including multilingual language models.
