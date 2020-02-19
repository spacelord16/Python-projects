import os

from pygame import mixer

avaiable_files = []

for root, dir, filename_list in os.walk(os.path.join("D:/", "Songs")):
    for i, file in enumerate(filename_list):
        extension = file.split(".")[::-1][0]
        if extension.lower() == "mp3":
            avaiable_files.append(os.path.join(root, file))

print(avaiable_files)
song_no = int(input("Enter index of song"))

mixer.init()   #Start mixer
mixer.music.load(avaiable_files[song_no])  #Load the song
mixer.music.set_volume(0.7)   #set the volume
mixer.music.play()      #play the music


while True:
    print("Press 'p' to pause and 'r' to resume")
    print("Press 'e' to exit the programme")
    query=input(">>> ")

    if query == 'p':
        mixer.music.pause()  #Pause mixer
    elif query == 'r':
        mixer.music.play() #Resume mixer
    elif query == 'e':
        mixer.music.stop()  #Stop mixer
        break