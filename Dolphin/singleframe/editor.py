from os import system

print("Do you want to edit the audio of the video? y/n ")
skip = input(">>> ")
if skip == "n":
    system("bash ./combine.sh")        

#Start program
try:
    from pedalboard import Chorus, Distortion, Phaser, Gain, Reverb, PitchShift, Pedalboard
    from pedalboard.io import AudioFile
except ImportError:
    print("Hey! pedalboard is not installed! Do you want to install it? y/n")
    while 1:
        answer = input(">>> ")
        if answer == "y":
            system("pip3 install pedalboard")
            break
        
        elif answer == "n":
            print("Well, the program is built from the pedalboard module so enjoy crashing!")
            break
        else:
            print("Wrong input!")
        
try:
    from termcolor import cprint
except ImportError:
    print("Hey termcolor is not installed! Do you want to install it? y/n")
    while 1:
        answer = input(">>> ")
        if answer == "y":
            system("pip3 install termcolor")
            break
        elif answer == "n":
            print("Well this program will not work so enjoy the errors!")
            break
        else:
            print("Wrong input!")
            
try:
    from silver import Silver
except ImportError:
    print("Silver is not installed! Would you like to install it? y/n")
    while 1:
        answer = input(">>> ")
        if answer == "y":
            system("wget https://raw.githubusercontent.com/Ubuntufanboy/Silver/main/silver.py")
            break
        elif answer == "n":
            print("Hey! Silver is a great tool... You might crash without it...")
            break
        else:
            print("Wrong input!")
system("ffmpeg -i input.mp3 audio.wav -hide_banner -loglevel error")
cprint("----- Welcome to Audio editor! -----", "green")
print("")

with AudioFile('audio.wav', 'r') as f:
    audio = f.read(f.frames)
    samplerate = f.samplerate

board = Pedalboard([])

print("")
print("You are going to enter edit mode. Select what effects you would like to add")

while 1:
    chorus = input("Would you like to add the Chorus effect? y/n ")
    if chorus == "y":
        c = Chorus()
        board.append(c)
        print("")
        
        print("Playing demo audio...")
        effected = board(audio, samplerate)
        with AudioFile('demo1.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
        Silver.play("demo1.wav")
        remove = input("Did you change your mind? We can remove it if you wish y/n ")
        if remove == "y":
            board.remove(c)
            effected = board(audio, samplerate)        
            with AudioFile('demo1.wav', 'w', samplerate, effected.shape[0]) as f:
                f.write(effected)
            Silver.stop()
            print("This is what it sounds like now")
            Silver.play("demo1.wav")
            input("Press enter to stop the playback")
            Silver.stop()
        else:
            Silver.stop()
            break
        break
    elif chorus == "n":
        break
    else:
        continue

while 1:
    distortion = input("Would you like to add the Distortion effect? y/n ")
    if distortion == "y":
        d = Distortion()
        board.append(d)
        print("")
        print("Playing demo audio...")
        effected = board(audio, samplerate)
        with AudioFile('demo2.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
        Silver.play("demo2.wav")
        remove = input("Did you change your mind? We can remove it if you wish y/n ")
        if remove == "y":
            board.remove(d)
            Silver.stop()
            effected = board(audio, samplerate)
            with AudioFile('demo2.wav', 'w', samplerate, effected.shape[0]) as f:
                f.write(effected)
            print("This is what it sounds like now")
            Silver.play("demo2.wav")
            input("Press enter to stop the playback")
            Silver.stop()
        else:
            Silver.stop()
            break
        break
    elif distortion == "n":
        break
    else:
        continue

while 1:
    phaser = input("Would you like to add the Phaser effect? y/n ")
    if phaser == "y":
        p = Phaser()
        board.append(p)
        print("")
        print("Playing demo audio...")
        effected = board(audio, samplerate)
        with AudioFile('demo3.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
        Silver.play("demo3.wav")
        remove = input("Did you change your mind? We can remove it if you wish y/n ")
        if remove == "y":
            board.remove(p)
            Silver.stop()
            effected = board(audio, samplerate)
            with AudioFile('demo3.wav', 'w', samplerate, effected.shape[0]) as f:
                f.write(effected)
            print("This is what it sounds like now")
            Silver.play("demo3.wav")
            input("Press enter to stop the playback")
            Silver.stop()
        else:
            Silver.stop()
            break
        break
    elif phaser == "n":
        break
    else:
        continue

while 1:
    gain = input("Would you like to add the Gain effect? y/n ")
    if gain == "y":
        amount = int(input("How much gain would you like? Less than 40 db please (Your ears will hurt)"))
        gaindb = amount
        g = Gain(gaindb)
        board.append(g)
        
        print("Playing demo audio...")
        effected = board(audio, samplerate)
        with AudioFile('demo4.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
        Silver.play("demo4.wav")
        remove = input("Did you change your mind? We can remove it if you wish y/n ")
        if remove == "y":
            board.remove(g)
            Silver.stop()
            effected = board(audio, samplerate)
            with AudioFile('demo4.wav', 'w', samplerate, effected.shape[0]) as f:
                f.write(effected)
            print("This is what it sounds like now")
            Silver.play("demo4.wav")
            input("Press enter to stop the playback")
            Silver.stop()
        else:
            Silver.stop()
            break
        break
    elif gain == "n":
        break
    else:
        continue

while 1:
    reverb = input("Would you like to add the reverb effect? y/n ")
    if reverb == "y":
        re = Reverb(room_size=0.25)
        board.append(re)
        
        print("Playing demo audio...")
        effected = board(audio, samplerate)
        with AudioFile('demo5.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
        Silver.play("demo5.wav")
        remove = input("Did you change your mind? We can remove it if you wish y/n ")
        if remove == "y":
            board.remove(re)
            Silver.stop()
            effected = board(audio, samplerate)
            with AudioFile('demo5.wav', 'w', samplerate, effected.shape[0]) as f:
                f.write(effected)
            print("This is what it sounds like now")
            Silver.play("demo5.wav")
            input("Press enter to stop the playback")
            Silver.stop()
        else:
            Silver.stop()
            break
        break
    elif reverb == "n":
        break
    else:
        continue
while 1:
    pitch = input("Would you like to add the Pitch Shift effect? y/n ")
    if pitch == "y":
        semis = int(input("How many semitones would you like to shift the audio by"))
        pi = PitchShift(semis)
        board.append(pi)
        print("Playing demo audio...")
        effected = board(audio, samplerate)
        with AudioFile('demo6.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
        Silver.play("demo6.wav")
        remove = input("Did you change your mind? We can remove it if you wish y/n ")
        if remove == "y":
            board.remove(pi)
            Silver.stop()
            effected = board(audio, samplerate)
            with AudioFile('demo6.wav', 'w', samplerate, effected.shape[0]) as f:
                f.write(effected)
            print("This is what it sounds like now")
            Silver.play("demo6.wav")
            input("Press enter to stop the playback")
            Silver.stop()
        else:
            Silver.stop()
            break
        break
    elif pitch == "n":
        break
    else:
        continue
print("")
print("")
print("Exporting audio...")
system("ffmpeg -i demo6.wav output.mp3 -hide_banner -loglevel error")
print("removing old demo files...")
system("rm demo1.wav")
system("rm demo2.wav")
system("rm demo3.wav")
system("rm demo4.wav")
system("rm demo5.wav")
system("rm demo 6.wav")
while 1:
    print("Would you like to Upload the video to YouTube?")
    answer = input(">>> ")
    print("exiting...")
    if answer == "y":
        system("bash ./combine.sh")
        break
    elif answer == "n":
        system("bash ./combine2.sh")
        break
    else:
        print("Wrong input")
