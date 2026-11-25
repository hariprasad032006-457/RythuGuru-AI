
import asyncio
import os
import time

import edge_tts
import pygame
import sounddevice as sd
import soundfile as sf
import requests

from groq import Groq
from dotenv import load_dotenv


# ==========================================
# 1. LOAD API KEY
# ==========================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")

client = Groq(api_key=api_key)


# ==========================================
# 2. TELUGU TEXT TO SPEECH
# ==========================================

async def speak_telugu(text):

    voice = "te-IN-ShrutiNeural"
    audio_file = "kisan_mitra_answer.mp3"

    communicate = edge_tts.Communicate(
        text,
        voice
    )

    print("\nGenerating Telugu audio...")

    await communicate.save(audio_file)

    print("Playing complete Telugu answer...")

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # Wait until the complete audio finishes
    while pygame.mixer.music.get_busy():
        time.sleep(0.2)

    pygame.mixer.music.stop()
    pygame.mixer.quit()

    print("Telugu audio playback completed!")


# ==========================================
# 3. START KISAN MITRA
# ==========================================

print("\n===================================")
print("       🌾 KISAN MITRA 🌾")
print("===================================")

print("\nWelcome, Farmer!")
print("Speak your farming question in Telugu...")


try:

    # ======================================
    # STEP 1: RECORD FARMER'S VOICE
    # ======================================

    print("\n🎤 Listening for 5 seconds...")

    audio = sd.rec(
        int(5 * 16000),
        samplerate=16000,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    sf.write(
        "farmer_voice.wav",
        audio,
        16000
    )

    print("Voice recording completed!")


    # ======================================
    # STEP 2: SPEECH TO TEXT
    # ======================================

    print("\nConverting Telugu voice into text...")

    with open("farmer_voice.wav", "rb") as file:

        transcription = client.audio.transcriptions.create(
            file=("farmer_voice.wav", file.read()),
            model="whisper-large-v3",
            language="te",
            response_format="text"
        )

    question = transcription.strip()

    if not question:
        raise ValueError("No speech detected. Please try again.")

    print("\n👨‍🌾 Farmer's Question:")
    print(question)


    # ======================================
    # STEP 3: GET AI ANSWER
    # ======================================

    print("\n🌱 Kisan Mitra is preparing your answer...")

    response = requests.post(
        "http://127.0.0.1:8001/ask",
        json={
            "question": question
        },
        timeout=60
    )

    response.raise_for_status()

    result = response.json()

    answer = result["answer"]

    if not answer:
        raise ValueError("Kisan Mitra returned an empty answer.")

    print("\n🌾 KISAN MITRA'S ANSWER:")
    print("-----------------------------------")
    print(answer)
    print("-----------------------------------")


    # ======================================
    # STEP 4: SPEAK ANSWER IN TELUGU
    # ======================================

    print("\n🔊 Speaking the answer in Telugu...")

    asyncio.run(speak_telugu(answer))


    # ======================================
    # STEP 5: COMPLETED
    # ======================================

    print("\n===================================")
    print("🌾 KISAN MITRA COMPLETED SUCCESSFULLY!")
    print("===================================")


except requests.exceptions.ConnectionError:

    print("\n❌ Cannot connect to Kisan Mitra server.")
    print("Start your FastAPI server in another terminal.")


except requests.exceptions.Timeout:

    print("\n❌ Server took too long to respond. Please try again.")


except Exception as e:

    print("\n❌ Something went wrong:")
    print(str(e))
