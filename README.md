# Customer Support Assistant using GPT, RAG and Zapier

This AI-powered assistant helps customer support teams efficiently respond to repetitive customer inquiries using GPT, RAG (Retrieval-Augmented Generation), and Zapier automation.

---

## Overview

This assistant:
- Classifies incoming customer emails or form submissions.
- Uses internal documentation to generate accurate, context-aware responses.
- Saves Q&A pairs to a database for later analysis and FAQ enhancement.

While the RAG system is lightly used here due to short sample documents, in real-world applications—where internal content is often large and complex—RAG becomes essential to structure information and allow GPT to provide relevant answers.

---

## Project Status

> **Work in progress**

This project is under active development and will evolve to include:
- More advanced analytics from the database (recurring issues, gaps in content).
- Dynamic content updates based on customer needs.

---

## Features

- [x] Upload internal documentation.
- [x] Customer submits a request (via email or form).
- [x] Zapier captures the message and triggers the backend.
- [x] The system:
  - Classifies the request (e.g., shipping, pricing, technical).
  - Searches internal docs using RAG (LlamaIndex).
  - Generates a contextual response with GPT.
- [x] Saves the original question and AI-generated answer to a CSV database.

---

## Work In Progress

- **Quarterly analysis**:
  - Detect frequently asked questions.
  - Identify missing answers in the internal documentation.
- **Content improvement**:
  - Use database insights to enhance documentation over time.
- **Escalation logic**:
  - Route complex questions to human agents when no relevant info is found.

---

## Tech Stack

| Tool        | Purpose                              |
|-------------|--------------------------------------|
| **Flask**   | API backend                          |
| **OpenAI GPT** | Text classification & response generation |
| **LlamaIndex** | RAG system for document retrieval |
| **Zapier**  | Automation and webhook integration   |
| **Python**  | Core programming language            |
| `pandas`    | CSV/database handling                |
| `dotenv`    | API key and config management        |

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/hajaruk-git/customer-support-RAG-Zapier.git
   cd customer-support-RAG-Zapier
   ```

2. Create a .env file with your OpenAI API key:
   ```bash
   echo "OPENAI_API_KEY=your_key_here" > .env # for Mac/Linux
    ```

3. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # for Mac/Linux
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Deploy the app on Render as a web service, and expose the /webhook route publicly.

6. In Zapier, set up your automation:
    - Trigger: New email in Gmail (if customer support email is only dedicated to customers' requests)
    - Action: Webhook (POST to your Render URL)
    - (Optional) Action: Create Gmail draft reply with GPT's response

---

## Dummy Content

This repo includes a simple content.txt file with dummy content for testing. This should be replaced with your internal documentation - such as FAQs, product guides, or support procedures.