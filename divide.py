import re
import os


pattern = r"(Scene (?:.+\r?\n+)(?=Scene))"
input_filename = "subtitles.txt"
save_path = "subtitles"

with open(input_filename, 'r') as f:
    text = f.read()

scenes = text.split("Scene")

# The first one is not part of a scene, so it is removed.
scenes = scenes[1:]

for scene in scenes:
    heading = "Scene" + scene.partition('\n')[0]
    ext = '.txt'
    filename = heading + ext
    path = os.path.join(save_path, filename)
    with open(path, 'w') as f:
        f.write(scene)