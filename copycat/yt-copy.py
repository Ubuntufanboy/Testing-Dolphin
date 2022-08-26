from os import system
link = input("Enter the yt-link >>> ")
system(f"yt-dlp {link} -o video")
print("Do you want to upload the video to youtube? (y/n)")
answer = input(">>> ")
if answer == "y":
    system("python3 upload_wizard.py")
else:
    print("Exiting...")
    exit()
