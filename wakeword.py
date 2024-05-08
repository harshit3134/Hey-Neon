# import pvporcupine
# from pvrecorder import PvRecorder
# keywords = ["Hey Neon"] 
# Access_key = "BqbXL8sPoEvB5xbIjW1jO5MaxKso/TnyVYdYNPE0bsIDflfYZ4ivGw=="
# porcupine = pvporcupine.create(
#   access_key=Access_key,
#   keyword_paths=['C:/Users/harsh/Desktop/College/Python/Voice-assistant/Hey-Neon_en_windows_v3_0_0.ppn']
# )
# recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

# try:
#     recorder.start()

#     while True:
#         keyword_index = porcupine.process(recorder.read())
#         if keyword_index >= 0:
#             print("Detected Hey Neon")
#             break
#         else:
#             print("recording")

# except KeyboardInterrupt:
#     recorder.stop()
# finally:
#     porcupine.delete()
#     recorder.delete()


import streamlit as st
import pvporcupine
from pvrecorder import PvRecorder
import speech_recognition as sr


def detect_wake_word():
    keywords = ["Hey Neon"] 
    access_key = "BqbXL8sPoEvB5xbIjW1jO5MaxKso/TnyVYdYNPE0bsIDflfYZ4ivGw=="
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=['C:/Users/harsh/Desktop/College/Python/Voice-assistant/Hey-Neon_en_windows_v3_0_0.ppn']
    )
    recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    r = sr.Recognizer()

    try:
        recorder.start()

        while True:
            keyword_index = porcupine.process(recorder.read())
            if keyword_index >= 0:
                print("Detected Hey Neon")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = r.listen(source)
                try:
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")
                break
    finally:
        porcupine.delete()
        recorder.delete()


detect_wake_word()
# def main():
#     st.title("Wake Word Detection")
#     if st.button("Start Detection"):
#         result = detect_wake_word()
#         st.write(result)

# if __name__ == "__main__":
#     main()