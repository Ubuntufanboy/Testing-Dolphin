import moviepy.editor as mpy
import os
clips = []
timeline = []
audioline = []

os.chdir("..")
pwd = os.getcwd()
ls = os.listdir(pwd)
print(ls)
content = open("conf.dolphin", "r")

file_content = []

for line in content:
    file_content.append(line)

os.chdir("videoeditor")
# print("Error: Please check that you have a conf.dolphin file!")

count = 0
for dolphin in file_content:
    listed = dolphin.split()
    if listed[0] == "video_editor.py":
        if listed[2] == "exit":
            count += 1
            print("exit was inputed")
            break
        else:
            print("appending...")
            clips.append(listed[2])
            count += 1

print(clips)

for clip in clips:
    if str(clip).endswith(".mp4"):
        timeline.append(mpy.VideoFileClip(clip))
    elif str(clip).endswith(".mp3") or str(clip).endswith(".wav"):
        audioline.append(mpy.AudioFileClip(clip))
    else:
        print("Unsupported file type! You will encounter errors or bugs! ")
        exit()

exported = mpy.concatenate_videoclips(timeline, method="compose")
exported.audio = mpy.concatenate_audioclips(audioline)

# This get's the next line we need
for line in file_content:
    copy = line.split()
    if copy[2].endswith(".mp4"):
        filename = copy[2]

print(filename)
exported.write_videofile(filename, fps=30, threads=1, codec="libx264")
count += 1

num = 0
for line in file_content:
    print(num)
    if num == count:
        listed = line
    num += 1

listed = listed.split()
if listed[2] == "y":
    from os import system
    system(f"mpv {filename}")

