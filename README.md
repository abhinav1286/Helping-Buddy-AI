# Helping-Buddy-AI
This project, titled "HelpingBuddy," is a voice-based assistant designed to assist users by transcribing their spoken questions, generating responses using OpenAI's GPT-3.5 model, and then vocalizing the responses back to the user. 
This project, titled "HelpingBuddy," is a voice-based assistant designed to assist users by transcribing their spoken questions, generating responses using OpenAI's GPT-3.5 model, and then vocalizing the responses back to the user. The project utilizes various libraries such as pyttsx3, speech_recognition, streamlit, and gtts.

Key Components:

User Interface: The interface is built using Streamlit, providing a simple user interface where users can select their preferred language and interact with the assistant.

Voice Input: Users initiate interaction by saying "hello," which triggers the assistant to start listening for the user's question.

Speech Recognition: The assistant utilizes the speech_recognition library to transcribe the user's spoken question into text format.

OpenAI GPT-3.5 Model: The transcribed text is then passed to OpenAI's GPT-3.5 model for generating responses. The model generates responses based on the input question, providing helpful assistance to the user.

Voice Output: The generated response is converted into speech using Google Text-to-Speech (gTTS) and played back to the user.

Multi-language Support: The assistant supports multiple languages, including English, Spanish, German, Russian, Portuguese, and Italian.

Overall, this project provides a convenient and user-friendly voice-based assistant capable of understanding and responding to user queries in real-time, enhancing the user's experience through natural language interaction.
