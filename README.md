<div align="center">

# 🏗️ BOQ Intelligence System

### 🤖 AI-Powered Construction Document Understanding using Fine-Tuned LLMs

<p align="center">
Fine-tuned <b>Qwen2.5-4B</b> using <b>QLoRA</b> for intelligent Bill of Quantities (BOQ) extraction, revision comparison, and construction document reasoning.
</p>

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Model](https://img.shields.io/badge/LLM-Qwen2.5--4B-success)
![Fine-Tuning](https://img.shields.io/badge/Fine--Tuning-QLoRA-orange)
![Domain](https://img.shields.io/badge/Domain-Construction-red)
![Google Colab](https://img.shields.io/badge/Google-Colab-F9AB00?logo=googlecolab)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

</div>

---

# 📖 Overview

Construction **Bill of Quantities (BOQ)** documents are often lengthy, inconsistent, and difficult to analyze automatically due to engineering abbreviations, OCR errors, and varying document formats.

This project presents an **AI-powered BOQ Intelligence System** that fine-tunes **Qwen2.5-4B** using **QLoRA** to understand construction documents and perform intelligent reasoning across multiple BOQ-related tasks.

Unlike traditional rule-based systems, the model learns domain-specific terminology and generates structured, explainable outputs from noisy real-world construction data.

> ⚠️ **Model weights are NOT included** due to size.
>
> ⚠️ **Remove hardcoded API keys** before making the repository public.

---

# ✨ Key Features

🏗️ Structured BOQ Field Extraction

📑 BOQ Revision Comparison

🔍 Hybrid Extraction + Comparison Pipeline

📄 OCR Noise Handling

🧠 Domain-Adaptive Fine-Tuning

⚡ QLoRA Fine-Tuning

📊 Construction-Specific Reasoning

📈 Real-World Engineering Dataset

---

# 🚀 Use Cases

## 📌 1. BOQ Information Extraction

Automatically extracts structured fields from raw BOQ descriptions.

Example:

```
AAC block 200mm CM 1:5 external wall
```

↓

```json
{
  "material": "AAC block",
  "thickness": "200mm",
  "mortar_ratio": "CM 1:5",
  "location": "external wall"
}
```

---

## 📌 2. BOQ Revision Comparison

Compares two BOQ versions and identifies changes.

Supported categories:

- ✅ Added
- ✏️ Modified
- ❌ Removed
- 🔄 Unchanged

Ideal for:

- Tender evaluation
- Contract variation
- Revision auditing

---

## 📌 3. Hybrid Analysis

Combines both tasks into one pipeline.

```
BOQ Document
      │
      ▼
Information Extraction
      │
      ▼
Revision Comparison
      │
      ▼
AI Summary Report
```

---

## 📌 4. OCR-Based Document Cleaning

Handles real-world engineering documents containing:

- OCR noise
- Missing units
- Engineering abbreviations
- Shorthand notation
- Mixed measurement systems

---

# 🏗️ System Architecture

```text
                 Raw BOQ Documents
                        │
                        ▼
             OCR / PDF Processing
                        │
                        ▼
          Text Cleaning & Preprocessing
                        │
                        ▼
         Fine-Tuned Qwen2.5-4B (QLoRA)
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
 Field Extraction   BOQ Comparison   Hybrid Analysis
        │               │               │
        └───────────────┼───────────────┘
                        ▼
             Structured JSON Output
```

---

# 📚 Dataset

The fine-tuning dataset contains **1,500 manually annotated construction samples** covering three different tasks.

| Task | Samples |
|--------|---------|
| 🏗️ Extraction | 750 |
| 📑 Comparison | 600 |
| 🔀 Hybrid | 150 |

---

## Domain Coverage

✔ RCC Structures

✔ Masonry

✔ Flooring

✔ Painting

✔ Waterproofing

✔ MEP

✔ Curtain Walls

✔ ACP Cladding

✔ Insulation

---

## Edge Cases

The dataset intentionally includes challenging scenarios such as:

- OCR corruption
- Engineering abbreviations
- Missing attributes
- Mixed units
- Semantic synonyms
- Incomplete BOQs

---

# 📝 Training Format

All examples follow **ChatML Instruction Tuning**.

Example:

```
TASK: EXTRACTION

Input:

AAC block 200mm CM 1:5 external wall
```

↓

```json
{
  "material":"AAC block",
  "thickness":"200mm",
  "mortar_ratio":"CM 1:5",
  "location":"external wall"
}
```

---

# 🤖 Model

| Property | Details |
|----------|---------|
| Base Model | Qwen2.5-4B-Instruct |
| Fine-Tuning | QLoRA |
| Precision | FP16 |
| Quantization | 4-bit NF4 |
| Framework | HuggingFace Transformers |
| PEFT | Yes |

---

## QLoRA Configuration

| Parameter | Value |
|-----------|-------|
| Rank | 16 |
| Alpha | 32 |
| Dropout | 0.05 |
| Target Modules | q_proj, k_proj, v_proj, o_proj |

---

# ⚙️ Training Configuration

| Setting | Value |
|---------|--------|
| Optimizer | AdamW |
| Precision | FP16 |
| Quantization | 4-bit |
| Training Style | ChatML |
| GPU | Google Colab |
| Duration | ~1 hr 45 min |

---

# 📈 Performance

The model improved significantly during iterative fine-tuning.

| Training Phase | Accuracy |
|---------------|----------|
| 🔴 Phase 1 | 49% |
| 🟡 Phase 2 | 76% |
| 🟢 Phase 3 | **86%** |

---

# 🧪 Evaluation

The model was evaluated on:

✅ Unseen BOQ Documents

✅ OCR-Noisy Inputs

✅ Multi-Change Revisions

✅ Cross-Domain Construction Samples

✅ Mixed Engineering Categories

---

# 📊 Sample Outputs

## Extraction

**Input**

```
AAC block 200mm CM 1:5 external wall
```

**Output**

```json
{
 "material":"AAC block",
 "thickness":"200mm",
 "mortar_ratio":"CM 1:5",
 "location":"external wall"
}
```

---

## Comparison

```
BOQ1
AAC block 200mm

BOQ2
AAC block 150mm
```

↓

```
Modified

• Thickness changed
200mm → 150mm
```

---

# 🧠 LLM vs Fine-Tuned SLM

This repository also benchmarks:

| Gemini LLM | Fine-Tuned Qwen SLM |
|------------|---------------------|
| Prompt Engineering | Domain Fine-Tuning |
| General Knowledge | Construction Knowledge |
| Variable Outputs | Consistent Outputs |
| Higher Latency | Faster Inference |

The comparison evaluates:

- Accuracy
- Consistency
- Latency
- JSON Quality
- Domain Understanding

---

# 📂 Repository Structure

```text
BOQ-Intelligence-System/

├── Fine Tuning/
│   ├── Documentation/
│   ├── Finetuning Code/
│   ├── Evaluation/
│   ├── Testing/
│   └── Demo/
│
├── LLM vs SLM (Finetuned)/
│   ├── Documentation/
│   ├── Evaluation Results/
│   └── LLM Extraction/
│
├── Interaction Using LLM/
│   ├── PDF_processing.ipynb
│   └── boq_extraction_dataset.csv
│
└── README.md
```

---

# 💻 Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Development |
| 🤗 Transformers | Model Training |
| ⚡ PEFT | QLoRA |
| 🔥 PyTorch | Deep Learning |
| 📊 Pandas | Data Processing |
| ☁️ Google Colab | GPU Training |
| ✨ Gemini API | Benchmarking |
| 📄 OCR | PDF Processing |

---

# 📦 Installation

```bash
pip install transformers datasets peft accelerate bitsandbytes trl torch pandas google-generativeai
```

A CUDA-enabled GPU is recommended.

---

# 🚀 Future Improvements

- 🌐 Web Application
- 📄 PDF Upload Interface
- 📊 Interactive Dashboard
- 🏗️ Multi-language BOQ Support
- ☁️ Hugging Face Deployment
- 📚 RAG Integration
- 📑 Contract Clause Understanding
- 🏢 Enterprise Construction Assistant

---

# 👨‍💻 Author

**Aditya Jayant Ahirrao**

GitHub: *https://github.com/Aditya728-ace*

LinkedIn: *https://www.linkedin.com/in/aditya-ahirrao-733b6026b/*

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star!

Made with ❤️ using **Qwen2.5, QLoRA, Hugging Face & Google Colab**

</div>
