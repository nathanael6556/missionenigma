import os
from splitter import NLTKSplitter


base_path = os.getcwd()
subtitles_selected_path = os.path.join(base_path, "subtitles-selected")

splitted_postfix = "-splitted"
subtitles_splitted_path = "subtitles" + splitted_postfix
filenames = os.listdir(subtitles_selected_path)

splitter = NLTKSplitter()

for filename in filenames:
    path = os.path.join(subtitles_selected_path, filename)
    with open(path, 'r') as f:
        text = f.read()
    filename_only, ext = os.path.splitext(filename)
    filename_only = filename_only.partition('-')[0]
    splitted_path = os.path.join(subtitles_splitted_path, filename_only+splitted_postfix+ext)
    result = "\n\n".join(splitter.split(text))
    with open(splitted_path, 'w') as f:
        f.write(result)
    