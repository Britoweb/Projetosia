import speech_recognition as sr

r = sr.Recognizer()
arquivo = sr.AudioFile("speechrecognition/audio_barulhento.wav")
with arquivo as fonte:
    r.adjust_for_ambient_noise(fonte, duration=0.5)
    audio_barulhento = r.record(arquivo)
 
texto = r.recognize_google(audio_barulhento, language="en-US")
print(texto)