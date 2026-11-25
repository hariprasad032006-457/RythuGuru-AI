
import asyncio
import edge_tts

async def main():
    text = "నమస్కారం రైతు సోదరా! మీ కిసాన్ మిత్రకు స్వాగతం."

    voice = "te-IN-ShrutiNeural"

    communicate = edge_tts.Communicate(
        text,
        voice
    )

    await communicate.save("kisan_mitra_voice.mp3")

    print("Telugu voice generated successfully!")

asyncio.run(main())
