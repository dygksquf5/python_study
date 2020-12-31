# This is Virtual Assistant mini project.

      1.  pip3 install SpeechRecognition
      2.  pip3 install pyttsx3
      3.  brew install portaudio
      4.  pip install pyaudio 
      5.  pip3 install pywhatkit
      6.  pip install wikipedia


# you can use this project as a personal virtual assistant as Alexa from Google or Siri from Apple. 

It based on a Voice recognition which already trained by SpeechRecognition.
Through this project, you can find videos on Youtube. 
Moreover you can search something that you want to know on Google or Wikipedia. 
I set the command as 'bixby' in order to call your Assistant.
Thus, if you not call 'bixby', your computer will not any action at all.

                    with sr.Microphone() as source:
                        print(" listening ... ")
                        voice = listener.listen(source)
                        command = listener.recognize_google(voice)
                        command = command.lower()
                        if 'bixby' in command: 
                            command = command.replace('bixby', '')
                            print(command)


# If you command like ' hey bixby, play Matt maltese ', after then Bixby says 'playing Matt maltese', then you can hear the beautiful voice of Matt maltese on Youtube. 

                      if 'play' in command:
                          song = command.replace('play', '')
                          talk('playing ' + song)
                          pywhatkit.playonyt(song)
                          
                          
 <img width="350" alt="Screenshot 2020-12-31 at 12 29 11 PM" src="https://user-images.githubusercontent.com/66229916/103393125-7d8ae700-4b64-11eb-8c14-a473e53a4d92.png">

