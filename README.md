# 🖼️ AI Chatbot with Image Understanding  

This project is a beginner implementation and introduction to using various API keys as well as Ollama models for creating your very own chatbot.

## 🚀 Features  
- Text & Image inputs with AI responses  
- Streamlit-based UI  
- Powered by **Meta's LLaMA 3.2 Vision**  

## 📦 Installation  

```bash
git clone https://github.com/RahulPatnaik/AI-Chatbot-event
cd AI-Chatbot-event
pip install -r requirements.txt
```

## 🔧 Dependencies

Install manually if needed:

```bash
pip install streamlit huggingface_hub transformers torch pillow requests fireworks-ai
```

## 🔑 Setup API Key

```bash
export GROQ_API_KEY=<API_TOKEN>
export HF_API_KEY=<API_TOKEN>
```


## Ollama Models
If you wish to run the `localChatbot.py' ensure you have the associated model installed via ollama on your local device.

```bash
ollama pull deepseek-r1:1.5b
```

# ▶️ Run the App

```bash
streamlit run app.py
```





