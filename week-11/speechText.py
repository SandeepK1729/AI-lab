import speech_recognition as sr 

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Something ")
    audio = r.listen(
        source, 
        timeout = 5,
        phrase_time_limit = 10
    )
    print("Done Listening, in processing")

    try:
        text = r.recognize_google(audio)
        print(f"You said : {text}")
    except:
        print("Error while processing")