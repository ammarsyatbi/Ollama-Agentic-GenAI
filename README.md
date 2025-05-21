# Ollama-Agentic-GenAI

This project is a pre-built local LLM template using OLLAMA and Crew AI. You can customized the crews, flows and tools to match your needs.

**What is OLLAMA?**

OLLAMA stands for "Open-Learning Localized Large-scale Autoregressive Model". It's an innovative framework that allows us to fine-tune
pre-trained models on smaller, localized datasets. This approach enables us to create tailored language models that understand the nuances
of specific domains or regions.

**What is Crew AI?**

Crew AI is a powerful platform for building and deploying AI-powered applications. Their frameworks provide pre-built components and tools
for developers to integrate AI capabilities into their projects. In this project, we'll be using Crew AI's framework to create our local
LLM template.
  
  
## To Run
Clone this repo and run the following:
```
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## Future Improvement
- Integrate MCP for RAG
- Add authentication in based app