import os
from subtitle_creator import SubtitleCreator
from settings import DURATION_PER_WORD


base_path = os.getcwd()
subtitles_splitted_path = os.path.join(base_path, "subtitles-splitted")

SRT_postfix = "-SRT"
subtitles_SRT_path = "subtitles" + SRT_postfix
filenames = os.listdir(subtitles_splitted_path)

subtitle_creator = SubtitleCreator(DURATION_PER_WORD)

for filename in filenames:
    path = os.path.join(subtitles_splitted_path, filename)
    filename_only, ext = os.path.splitext(filename)
    filename_only = filename_only.partition('-')[0]
    ext = '.srt'
    SRT_path = os.path.join(subtitles_SRT_path, filename_only+ext)
    subtitle_creator.create_from_file(path, SRT_path, 'utf-8')
    