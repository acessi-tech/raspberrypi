# from gtts import gTTS

import pyttsx3

engine = pyttsx3.init()

# import os 
# voices = engine.getProperty("voices")
# for voice in voices:
#     print(voice.id)

# engine.setProperty("rate", 120)s
# Defina a voz para "brazil"
engine.setProperty("voice", "brazil")

dadadosDoArduino = ''

engine.say("369124")
engine.runAndWait()
engine.stop()



# idioma = 'pt-br'

# tts = gTTS('olá 1 2 3444', lang=idioma)
# tts.save('ola.mp3')

# os.system('mog321 ola.mp3')

# from pocketsphinx import LiveSpeech, get_model_path

# model_path = get_model_path()

# fala =LiveSpeech(
#     verbose=False,
#     sampling_rate=16000,
#     buffer_size=2048,
#     no_search=False,
#     full_utt=False,
#     hmm=os.path.join(model_path, 'pt-br'),
#     lm=os.path.join(model_path, ''
# )

