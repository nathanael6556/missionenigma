from subtitle_creator import SubtitleCreator
from settings import DURATION_PER_WORD


INPUT_FILENAME = "subtitles-splitted.txt"
OUTPUT_FILENAME = "subtitles.srt"
encoding = "utf-8"


creator = SubtitleCreator(DURATION_PER_WORD)
creator.create_from_file(INPUT_FILENAME, OUTPUT_FILENAME, encoding)
