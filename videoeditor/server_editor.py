import moviepy as mpy
clips = []
timeline = []
audioline = []
try:
    f = open("conf.dolphin", "r")
    content = f.readlines()
except:
    print("Error: Please check that you have a conf.dolphin file!")
finally:
    f.close()

count = 0
for dolphin in content:
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

count *= 2
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

dolphin = content[count]
listed = dolphin.split()
filename = listed[2]
exported.write_videofile(filename)
count += 1

listed = content[count].split()
if listed[2] == "y":
    from os import system
    system(f"mpv {filename}")

