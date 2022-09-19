print("----- Welcome to the Music-Video maker! -----")
print("Do you have the songs audio file? (y/n)")
answer = input(">>> ")

while 1:
    if answer == "y":
        print("Great! Do you have a background image? (y/n)")
        answer = input(">>> ")
        if answer == "n":
            print("You need to save an image to this directory then press enter")
            input()
            print("Good! Enter the image's filename (Include the extension)")
            file = input("File path >>> ")
        elif answer == "y":
            print("Good! Just enter the file path (Including the file extension)")
            file = input("File path >>> ")
        else:
            print("Wrong input! ")

    elif answer == "n":
        print("Would you like to the audio yourself or use the singleframe mode to get a video?")
        print("[1] Myself")
        print("[2] Single frame mode")
        
        while 1:
            try:
                mode = int(input("Enter the number >>> "))
                if mode > 2 or mode < 1:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("You need to enter a valid number")
        
        while 1:
            if mode == 1:
                print("Press enter once you have moved the video file into this directory")
                input()
                print("What is the video file name?")
                file = input(">>> ")
                break
            elif mode == "2":
                print("Take this time to find a YouTube link of the song you want the audio of.")
                input("Press enter once you have found a YouTube link")
                print("Now take this time to download an jpg image and name it img.jpg")
                input("Press enter once you have found a JPG image ")
                from os import system
                import os
                org = os.getcwd()
                system("cd ..")
                system("cd singleframe")
                system("python3 yt-download.py")
                system("python3 editor.py")
                # Get video.mp4 into this directory
                print("Loading... This may take a while")
                system(f"cp video.mp4 {org}")
                print("Done!")
                file = "video.mp4"
                break
            else:
                print("Wrong input!")
        print("What is the song name?")
        title = input(">>> ")
        