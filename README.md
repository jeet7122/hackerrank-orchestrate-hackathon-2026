# AI Claim Review Agent

An intelligent multimodal AI system that automates insurance claim assessment by analyzing claimant conversations, uploaded evidence images, historical claim data, and evidence requirements.

The system evaluates whether submitted evidence supports a claim, determines if additional peer review is required, identifies potential fraud or risk indicators, and generates structured claim decisions with explainable reasoning.

> Developed for the HackerRank Orchestrate 2026 AI Hackathon.

---

# Features

- Multimodal claim analysis using text and images
- Automated evidence validation
- Intelligent claim decision pipeline
- Risk flag detection
- Severity estimation
- Explainable AI decisions
- Modular architecture for extensibility
- Evaluation framework for comparing prompt strategies
- Batch claim processing

---

# Architecture

```
Claim Request
      │
      ▼
CSV & Image Loaders
      │
      ▼
Evidence Extraction
      │
      ▼
Image Analysis
      │
      ▼
Claim Processing
      │
      ▼
Decision Engine
      │
      ▼
Evidence Evaluation
      │
      ▼
Risk Analysis
      │
      ▼
Structured Output Writer
```

---

# Project Structure

```
code/
│
├── main.py                     # Application entry point
│
├── models/
│   └── model.py                # Shared data models
│
├── loaders/
│   ├── claims_loader.py
│   ├── data_loader.py
│   ├── evidence_requirements_loader.py
│   ├── test_loaders.py
│   └── user_history_loader.py
│
├── prompts/
│   └── image_analysis_prompt.py
│
├── services/
│   ├── claim_image_analysis.py
│   ├── claim_processor.py
│   ├── image_analyzer.py
│   ├── decision_engine.py
│   ├── evidence_evaluator.py
│   └── risk_engine.py
│
├── writers/
│   └── output_writer.py
│
├── utils/
│   ├── normalizer.py
│   └── patterns.py
│
└── evaluation/
    └── main.py
```

---

# Processing Workflow

The application performs the following pipeline for every insurance claim:

1. Load claim metadata
2. Retrieve customer history
3. Read evidence requirements
4. Analyze uploaded images using a Vision Language Model
5. Extract visible damages
6. Compare visual evidence against claimant conversation
7. Detect inconsistencies or fraud indicators
8. Evaluate evidence sufficiency
9. Generate claim decision
10. Export structured results

---

# Output

Each processed claim produces:

- Evidence validation
- Evidence justification
- Risk flags
- Issue type
- Affected object part
- Claim status
- Decision explanation
- Supporting images
- Image validity
- Damage severity

---

# Technologies

- Python
- Large Language Models (LLMs)
- Vision Language Models (VLMs)
- Prompt Engineering
- Structured AI Workflows
- CSV Processing
- Modular Software Architecture

---

# Evaluation

The repository includes an evaluation framework that compares multiple prompting strategies and measures prediction quality against sample datasets.

Evaluation includes:

- Prompt comparison
- Accuracy analysis
- Runtime comparison
- Operational metrics
- Error inspection

---

# Design Principles

- Modular architecture
- Separation of concerns
- Explainable AI outputs
- Extensible service pipeline
- Production-style project organization
- Easily replaceable AI models

---

# Running

```bash
git clone <repo>

cd AI-Claim-Review-Agent

pip install -r requirements.txt

python code/main.py
```

---

# Future Improvements

- Multi-agent orchestration
- Human-in-the-loop review
- Confidence scoring
- OCR integration
- RAG-powered policy validation
- Web dashboard
- Cloud deployment
- API endpoints

---

# Author

**Jeet Thakkar**

Software Engineer | AI Application Developer