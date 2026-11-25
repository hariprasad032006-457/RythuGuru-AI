
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq


# ==========================================
# 1. LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found. Check your .env file."
    )


# ==========================================
# 2. CONNECT TO GROQ AI
# ==========================================

client = Groq(api_key=api_key)


# ==========================================
# 3. CREATE FASTAPI APPLICATION
# ==========================================

app = FastAPI(
    title="Kisan Mitra AI Assistant",
    description="Voice-based AI farming assistant for Indian farmers",
    version="1.0"
)


# ==========================================
# 4. REQUEST MODEL
# ==========================================

class Question(BaseModel):
    question: str


# ==========================================
# 5. HOME ROUTE
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Welcome to Kisan Mitra!",
        "status": "Running successfully",
        "features": [
            "Telugu language support",
            "AI farming assistance",
            "Voice-based interaction"
        ]
    }


# ==========================================
# 6. HEALTH CHECK
# ==========================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "project": "Kisan Mitra"
    }


# ==========================================
# 7. AI FARMING ASSISTANT
# ==========================================

@app.post("/ask")
def ask_kisan_mitra(data: Question):

    try:

        # Check empty question
        if not data.question.strip():
            raise HTTPException(
                status_code=400,
                detail="Please provide a farming question."
            )

        # Send question to Groq AI
        response = client.chat.completions.create(

            model="openai/gpt-oss-120b",

            max_completion_tokens=1500,

            messages=[
                {
                    "role": "system",

                    "content": (
                        "You are Kisan Mitra, a friendly AI farming "
                        "assistant for Indian farmers. "

                        "Always reply in the language used by the farmer. "

                        "If the farmer speaks Telugu, answer in natural, "
                        "simple Telugu. "

                        "Use everyday words that farmers can understand. "

                        "Give practical and easy-to-follow advice. "

                        "Explain the main reason and provide useful "
                        "steps when appropriate. "

                        "Keep answers concise, around 5 to 7 sentences. "

                        "Use short bullet points when helpful. "

                        "Always finish your answer with a complete sentence. "

                        "Never invent agricultural facts, pesticide doses, "
                        "fertilizer quantities, or crop recommendations. "

                        "Do not give region-specific recommendations "
                        "unless the location is known and the information "
                        "supports that recommendation. "

                        "If you are unsure, say so honestly."
                    )
                },

                {
                    "role": "user",
                    "content": data.question
                }
            ]
        )

        # Extract AI answer
        answer = response.choices[0].message.content

        # Check empty response
        if not answer or not answer.strip():

            raise HTTPException(
                status_code=502,
                detail="AI returned an empty answer. Please try again."
            )

        # Return response
        return {
            "question": data.question,
            "answer": answer.strip(),
            "status": "success"
        }


    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"AI response error: {str(e)}"
        )
