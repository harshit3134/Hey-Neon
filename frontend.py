import streamlit as st
import pvporcupine
from pvrecorder import PvRecorder
import speech_recognition as sr
from LLM import get_action

def detect_wake_word():
    keywords = ["Hey Neon"]
    access_key = "BqbXL8sPoEvB5xbIjW1jO5MaxKso/TnyVYdYNPE0bsIDflfYZ4ivGw=="
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=['C:/Users/harsh/Desktop/College/Python/Voice-assistant/Hey-Neon_en_windows_v3_0_0.ppn']
    )
    recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    r = sr.Recognizer()

    st.title("Hey Neon Voice Assistant")
    st.write("Click on the microphone icon to start a conversation , Say Hey Neon to wake up the assistant and see what wonders it can do for you😀")

    # Microphone icon
    if st.button("🎙️"):
        try:
            recorder.start()

            while True:
                keyword_index = porcupine.process(recorder.read())
                if keyword_index >= 0:
                    st.write("Wake word detected: Hey Neon")
                    with sr.Microphone() as source:
                        st.write("Listening for command...")
                        audio = r.listen(source)
                    try:
                        command = r.recognize_google(audio)

                        st.text_area("User:", command, height=100)
                        st.write("Hey Neon is processing your command...")

                        # Perform action based on the command
                        get_action(command)

                    except sr.UnknownValueError:
                        st.error("Sorry, I could not understand what you said.")
                    except sr.RequestError as e:
                        st.error(f"Could not request results from Speech Recognition service; {e}")
                    # Continue listening for the next command
                    st.write("Listening for the next command...")
        finally:
            porcupine.delete()
            recorder.delete()

if __name__ == "__main__":
    detect_wake_word()
