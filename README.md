# 🌱 RythuGuru AI – Intelligent Agricultural Voice Assistant

**Making agricultural knowledge accessible to every farmer through voice-based AI.**

RythuGuru AI is an AI-powered agricultural assistant designed to help farmers access useful farming information through natural voice conversations in their own language.

The project aims to reduce the digital gap in agriculture by allowing farmers to ask questions and receive understandable agricultural guidance without depending on complex mobile applications.

---

## 🚜 Problem Statement

Farmers often face difficulties accessing reliable information about:

- Crop cultivation and management
- Soil health and fertility
- Pest and disease management
- Weather conditions
- Agricultural market prices
- Government agricultural schemes

Many farmers find it difficult to navigate mobile applications or search for information online.

**RythuGuru AI aims to solve this problem through a simple telephone-based AI assistant.**

## 💡 Our Solution

RythuGuru AI is designed around two interaction modes:

### 1. Quick Agricultural Services
Farmers can select predefined services through an interactive voice menu (IVR), such as weather updates, mandi prices, crop guidance, and government schemes.

### 2. Conversational AI Assistant
Farmers can ask agricultural questions naturally in Telugu and receive AI-generated voice responses based on relevant agricultural knowledge.

*Telephone and IVR integration are planned features.*

---

## ✨ Developed Features

- 🎙️ **Telugu Voice Input:** Captures farmer questions using Python and SoundDevice.
- 📝 **Speech Recognition:** Converts spoken Telugu into text using Groq Whisper.
- ⚡ **FastAPI Backend:** Processes farmer queries through REST API endpoints.
- 🔍 **RAG-Based Retrieval:** Retrieves relevant agricultural information using BM25 and ChromaDB.
- 📚 **Agricultural Knowledge Base:** Uses ICAR Kharif Agro-Advisories for Farmers 2025 as an initial knowledge source.
- 🤖 **AI-Powered Responses:** Uses Groq LLM to generate responses to agricultural questions.
- 🔊 **Telugu Voice Output:** Converts AI-generated text into speech using Edge TTS.
- 🎧 **Audio Playback:** Plays generated voice responses using Pygame.

## 🧠 RAG – Retrieval-Augmented Generation

RythuGuru AI uses Retrieval-Augmented Generation (RAG) to provide answers using agricultural documents.

### How It Works

1. Farmer asks a question in Telugu.
2. Groq Whisper converts the voice into text.
3. BM25 and ChromaDB search the agricultural knowledge base.
4. Relevant information is retrieved from the ICAR document.
5. The retrieved context is passed to the Groq LLM.
6. The AI generates a response.
7. Edge TTS converts the response into Telugu speech.
8. Pygame plays the audio response.

### RAG Architecture

```text
Farmer Voice Input
        |
        v
Groq Whisper
(Speech-to-Text)
        |
        v
FastAPI Backend
        |
        v
Hybrid RAG Retrieval
   /          \
 BM25       ChromaDB
   \          /
    v        v
Relevant Agricultural
      Information
        |
        v
     Groq LLM
        |
        v
   AI Response
        |
        v
     Edge TTS
   (Text-to-Speech)
        |
        v
   Telugu Audio
        |
        v
    Farmer
```

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend | FastAPI |
| AI Language Model | Groq LLM |
| Speech Recognition | Groq Whisper |
| Retrieval System | RAG, BM25 |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| Text-to-Speech | Edge TTS |
| Audio Processing | SoundDevice, SoundFile, Pygame |
| Knowledge Source | ICAR Kharif Agro-Advisories 2025 |

## 📖 Knowledge Base

The initial agricultural knowledge base is developed using:

**ICAR Kharif Agro-Advisories for Farmers 2025**

It provides agricultural information related to:

- Crop cultivation
- Soil health
- Crop management
- Farming practices
- Seasonal agricultural advisories

The knowledge base will be expanded using additional reliable agricultural sources.

---

## 🚀 Planned Features

The following features are planned for future development:

- ☎️ Telephone-based access through a dedicated RythuGuru AI number using Exotel.
- 🗣️ Automated Telugu greeting and interactive IVR menu.
- 🌦️ Five-day weather forecasts and weather-based farming guidance.
- 📊 Live mandi price information.
- 🏛️ Government agricultural schemes and farmer support programs.
- 🌾 Agricultural market knowledge, crop marketing and selling practices.
- 💬 Natural conversational AI through telephone calls.
- 🔄 Real-time bidirectional voice communication.
- 📚 Expanded agricultural knowledge base with reliable sources.

## ⚠️ Current Limitations

- Telugu-language RAG retrieval accuracy requires further improvement.
- Complete voice-to-answer-to-audio integration requires final testing.
- The current knowledge base contains a limited collection of agricultural documents.
- Agricultural market knowledge needs additional reliable sources.
- Live mandi prices and real-time weather information are not yet integrated.
- Incoming telephone calls and real-time audio streaming are under development.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git
- Internet connection
- Groq API key

### 1. Clone the Repository

```bash
git clone https://github.com/hariprasad032006-457/RythuGuru-AI.git
cd RythuGuru-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the required Python packages used by the project:

```bash
pip install fastapi uvicorn python-dotenv groq faster-whisper sounddevice soundfile edge-tts pygame pypdf sentence-transformers chromadb rank-bm25
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder with your own Groq API key. Never upload this file to GitHub.

### 5. Start the FastAPI Server

```bash
uvicorn app:app --host 127.0.0.1 --port 8001 --reload
```

Open the API documentation:

http://127.0.0.1:8001/docs

### 6. Run the Voice Prototype

Open another terminal, activate the virtual environment, and run:

```bash
python voice_test.py
```

Speak a question in Telugu and test the voice interaction.

*Note: The RAG database must be created before running retrieval-based queries. Audio recording also requires a working microphone and speaker.*

---

## 🔮 Future Vision

Our vision is to make agricultural knowledge accessible to farmers regardless of their digital skills.

By combining voice technology, AI, and reliable agricultural knowledge, RythuGuru AI aims to become a simple and useful digital farming companion.

**One Call. One Question. Smarter Farming.**

---

## 👨‍💻 Project

**Project Name:** RythuGuru AI

**Domain:** Artificial Intelligence | Agriculture | Voice-Based AI | RAG

**GitHub Repository:** [RythuGuru-AI](https://github.com/hariprasad032006-457/RythuGuru-AI)

---

### 🌱 RythuGuru AI

*Empowering Farmers Through Intelligent Voice Technology.*
