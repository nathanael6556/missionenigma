import os
from selector import MissionEnigmaSelector


base_path = os.getcwd()
subtitles_path = os.path.join(base_path, "subtitles")

selected_postfix = "-selected"
subtitles_selected_path = subtitles_path + selected_postfix
filenames = os.listdir(subtitles_path)

selector = MissionEnigmaSelector()

for filename in filenames:
    path = os.path.join(subtitles_path, filename)
    with open(path, 'r') as f:
        text = f.read()
    filename_only = os.path.splitext(filename)
    selected_path = os.path.join(subtitles_selected_path, filename_only[0]+selected_postfix+filename_only[1])
    result = "\n\n".join(selector.select(text))
    with open(selected_path, 'w') as f:
        f.write(result)
    