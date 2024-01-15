# Awesome-Multilingual-LLM

The repository is designed to support the growing interest within the community in developing large language models (LLMs) that cater not only to English speakers but also to speakers of the other 6,500+ languages worldwide. Its purpose is to aid researchers in discovering pertinent literature in this field. The repository will encompass a comprehensive collection of core training and evaluation datasets, multilingual-capable LLMs, and associated scholarly articles.


### 1. **In-Context Learning and Prompting Strategies**
- [2024] [Boosting Multilingual Translation with Prompt Strategies and Cross-Lingual Consistency](https://arxiv.org/abs/2401.05861): This paper focuses on enhancing multilingual translation in large language models through prompt strategies and a novel cross-lingual consistency regularization.

- [2023] [Adapt in Contexts: Retrieval-Augmented Domain Adaptation via In-Context Learning](https://dx.doi.org/10.48550/arXiv.2311.11551): Explores unsupervised domain adaptation in multilingual large language models using in-context learning and retrieval-augmented techniques.

- [2023] [Improving Robustness of Large Language Models in In-Context Learning with Natural Language Explanations](https://dx.doi.org/10.48550/arXiv.2311.07556): Investigates the use of natural language explanations to enhance the robustness of large language models in in-context learning.

- [2023] [Instruct Me More: Enhancing Visual In-Context Learning](https://dx.doi.org/10.48550/arXiv.2311.03648): Introduces a method called Instruct Me More to improve the effectiveness of visual in-context learning.

- [2023] [Chain-of-Thought Prompting for Few-Shot Knowledge Base Question Generation](https://dx.doi.org/10.48550/arXiv.2310.08395): Discusses Chain-of-Thought prompting as an in-context learning strategy for reasoning in Knowledge Base Question Generation tasks.

- [2023] [Prompt Engineering in Large Language Models for Automated Software Engineering Tasks](https://dx.doi.org/10.48550/arXiv.2310.10508): Analyzes the effectiveness of different prompting strategies in large language models for automated software engineering tasks.

- [2023] [Large Language Models as Post Hoc Explainers](https://dx.doi.org/10.48550/arXiv.2310.05797): Presents a framework to evaluate the effectiveness of Large Language Models in explaining other predictive models.

- [2023] [Self-Contemplation Prompting Strategy for In-Context Learning](https://dx.doi.org/10.48550/arXiv.2309.14681): Proposes a self-contempl

ation prompting strategy as an alternative to human-generated demonstrations for in-context learning.

- [2023] [Prompting Strategies for Large Language Models in Zero-Shot Clinical Natural Language Processing](https://dx.doi.org/10.48550/arXiv.2309.08008): Evaluates various prompt types for large language models in the clinical domain.

- [2023] [Ambiguity-Aware In-Context Learning with Large Language Models](https://dx.doi.org/10.48550/arXiv.2309.07900): Explores how to select good demonstrations for in-context learning considering the LLM's knowledge about the task.

- [2023] [Backdoor Attacks for In-Context Learning with Language Models](https://dx.doi.org/10.48550/arXiv.2307.14692): Explores developing backdoor attacks in large language models with in-context learning capability.

- [2023] [Enhancing In-Context Learning with Answer Feedback for Multi-Span Question Answering](https://dx.doi.org/10.48550/arXiv.2306.04508): Proposes a novel way of using labeled data to improve in-context learning performance in multi-span question answering.

- [2023] [ExpertPrompting: Instructing Large Language Models to be Distinguished Experts](https://dx.doi.org/10.48550/arXiv.2305.14688): Introduces ExpertPrompting, a prompting strategy that improves the answering quality of large language models.

- [2023] [Prompt Design Strategies for Large Language Models in Text-to-SQL Systems](https://dx.doi.org/10.48550/arXiv.2305.12586): Investigates demonstration selection methods and instruction formats for utilizing large language models in Text-to-SQL systems.

- [2023] [Chain-of-Dictionary Prompting Elicits Translation in Large Language Models](https://dx.doi.org/10.48550/arXiv.

2305.06575): Introduces a method called Chain-of-Dictionary Prompting to enhance multilingual neural machine translation in large language models.

- [2023] [Generating Code Comments with Large Language Models](https://arxiv.org/abs/2304.11384): Investigates the use of large language models to generate code comments fulfilling diverse intents with in-context learning and prompts.

- [2023] [Interpretable Mental Health Analysis with Large Language Models](https://dx.doi.org/10.18653/v1/2023.emnlp-main.370): Evaluates the mental health analysis and emotional reasoning ability of large language models, focusing on different prompting strategies.

- [2023] [Fairness-guided Few-shot Prompting for Large Language Models](https://dx.doi.org/10.48550/arXiv.2303.13217): Explores constructing prompts to improve in-context learning in large language models, introducing a metric to evaluate predictive bias and a search strategy for near-optimal prompts.


### 2. **Performance and Capabilities in Specific Languages**
- [Holmström et al.](https://www.aclweb.org/anthology/2023.resourceful-1.13): Explores the performance of English and multilingual LLMs in Swedish.

### 3. **Challenges and Limitations in Multilingual LLMs**
- [Zhu et al.](https://dx.doi.org/10.48550/arXiv.2304.04675): Investigates the advantages and challenges in multilingual machine translation using LLMs.

### 4. **Multilingual LLMs in Programming and Code**
- [Joshi et al.](https://dx.doi.org/10.48550/arXiv.2208.11640): Introduces RING, a multilingual repair engine powered by a language model trained on code.

### 5. **Comparative Studies and Benchmarks**
- [Ahuja et al.](https://dx.doi.org/10.48550/arXiv.2211.05100): Discusses the development and evaluation of BLOOM, a 176B-parameter open-access multilingual language model.
- [Lai et al.](https://dx.doi.org/10.48550/arXiv.2304.05613): Evaluates ChatGPT and other LLMs on multilingual NLP tasks.

### 6. **Datasets And Benchmarks**

- **Multilingual Multimodal Learning with Machine Translated Text** by Chen Qiu et al. investigates using machine-translated English multimodal data for training multilingual LLMs. They propose a framework called TD-MML and demonstrate its effectiveness in the IGLUE benchmark across 20 languages ([Qiu et al.](https://dx.doi.org/10.48550/arXiv.2210.13134)).

- **The BigScience ROOTS Corpus: A 1.6TB Composite Multilingual Dataset** by Hugo Laurenccon et al. presents the Responsible Open-science Open-collaboration Text Sources (ROOTS) corpus, a 1.6TB dataset spanning 59 languages, used to train the BigScience Large Open-science Open-access Multilingual (BLOOM) language model ([Laurenccon et al.](https://dx.doi.org/10.48550/arXiv.2303.03915)).

- **XLM-T: Multilingual Language Models in Twitter for Sentiment Analysis and Beyond** by Francesco Barbieri et al. introduces a dataset for multilingual LLMs using tweets in over thirty languages, along with sentiment analysis Twitter datasets in eight different languages ([Barbieri et al.](https://arxiv.org/abs/2104.12250)).

- **Generating Extended and Multilingual Summaries with Pre-trained Transformers** by Rémi Calizzano et al. introduces the WikinewsSum dataset for multilingual summarization, including news articles in seven languages tailored for extended summaries ([Calizzano et al.](https://www.aclweb.org/anthology/2022.lrec-1.175)).

- A paper by Po-Yao (Bernie) Huang et al. proposes Multi-HowTo100M, a multilingual instructional video dataset for pre-training models to improve video search in non-English languages ([Huang et al.](https://dx.doi.org/10.18653/V1/2021.NAACL-MAIN.195)).

- **PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification** by Yinfei Yang et al. proposes PAWS-X, consisting of human-translated paraphrase identification pairs in six languages, to evaluate multilingual LLMs ([Yang et al.](https://dx.doi.org/10.18653/v1/D19-1382)).

- **African News Corpus** by David Ifeoluwa Adelani et al. covers 16 African languages, including 8 languages not part of any existing evaluation dataset, demonstrating the effectiveness of leveraging high-quality translation data ([Adelani et al.](https://dx.doi.org/10.48550/arXiv.2205.02022)).

- **REDFM: a Filtered and Multilingual Relation Extraction Dataset** by Pere-Lluís Huguet Cabot et al. introduces SREDFM and REDFM datasets for training and evaluating multilingual relation extraction systems ([Cabot et al.](https://dx.doi.org/10.48550/arXiv.2306.09802)).

-  **GINCO Training Dataset** by Taja Kuzman et al. consists of 1,125 Slovenian web documents for genre identification, showing that Transformer-based models perform well on this task ([Kuzman et al.](https://arxiv.org/abs/2201.03857)).
- [Li et al.](https://dx.doi.org/10.48550/arXiv.2306.04387): Introduces the M$^3$IT dataset for optimizing the alignment of vision-language models with human instructions.
- 

### 7. **Translation and Language Understanding**
- [Guerreiro et al.](https://dx.doi.org/10.1162/tacl_a_00615): Provides insights into the presence of hallucinations in multilingual translation models.
- [Li et al.](https://dx.doi.org/10.48550/arXiv.2305.15083): Discusses the translation abilities of large language models in multilingual contexts.

### 8. **Miscellaneous Studies and Surveys**
- [Pahune et al.](https://dx.doi.org/10.22214/ijraset.2023.54677): Emphasizes recent developments and efforts made for various kinds of LLMs, including multilingual language models.
