
import openai
import pyttsx3
import speech_recognition as sr
import os
from gtts import gTTS
import streamlit as st


api_key = "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"
openai.api_key = api_key

engine = pyttsx3.init()

language_details = {
    "en": {"name": "English"},
    "es": {"name": "Spanish"},
    "de": {"name": "German"},
    "ru": {"name": "Russian"},
    "pt": {"name": "Portuguese"},
    "it": {"name": "Italian"},
}
def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            print("Skipping unknown error")

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response["choices"][0]["message"]["content"]

def speak_text_with_gtts(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")

def main():
    st.title("Welcome to HelpingBuddy")

    selected_language = st.sidebar.selectbox("Select Language", ["en", "es", "de", "ru", "pt","it"])
   
    language_name = language_details[selected_language]["name"]
    st.sidebar.markdown(f"\n*Name:* {language_name}")

   

    while True:
        st.write("Say 'hello' to start recording your question...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "hello":
                    
                    filename = "input.wav"
                    st.write("Say your question...")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(
                            source, phrase_time_limit=None, timeout=None
                        )
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    text = transcribe_audio_to_text(filename)
                    if text:
                        st.write(f"User: {text}")

                        response = generate_response(text)
                        st.write(f"Alex: {response}")

                        speak_text_with_gtts(response, lang=selected_language)
            except Exception as e:
                st.write(f"Error occurred: {e}")

if __name__ == "__main__":
    main()

     