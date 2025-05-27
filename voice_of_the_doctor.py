# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1a: Setup Text to Speech–TTS–model with gTTS
# import os
# from dotenv import load_dotenv
# from gtts import gTTS
# import subprocess
# import platform
# import elevenlabs
# from elevenlabs.client import ElevenLabs

# # ✅ Load environment variables
# load_dotenv()
# ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# # 🔹 GTTS version (no API key needed)
# def text_to_speech_with_gtts(input_text, output_filepath):
#     language = "en"
#     audioobj = gTTS(text=input_text, lang=language, slow=False)
#     audioobj.save(output_filepath)
#     try:
#         os_name = platform.system()
#         if os_name == "Darwin":
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":
#             subprocess.run(['aplay', output_filepath])
#     except Exception as e:
#         print(f"Playback error: {e}")

# # 🔹 ElevenLabs TTS version
# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     if not ELEVENLABS_API_KEY:
#         raise ValueError("Missing ELEVENLABS_API_KEY in environment.")
        
#     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio = client.generate(
#         text=input_text,
#         voice="Aria",
#         output_format="mp3_22050_32",
#         model="eleven_turbo_v2"
#     )
#     elevenlabs.save(audio, output_filepath)
    
#     try:
#         os_name = platform.system()
#         if os_name == "Darwin":
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":
#             subprocess.run(['aplay', output_filepath])
#     except Exception as e:
#         print(f"Playback error: {e}")


































    
    
import os
import platform
from elevenlabs.client import ElevenLabs
import elevenlabs

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

    # ✅ Optional: Debug print
    print(f"Audio saved to: {output_filepath}")

    return output_filepath  # ✅ This is the key: return the file path

