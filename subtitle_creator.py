import os
import re
from math import floor
from datetime import timedelta
from utils import number_of_word, td_to_srt_time


class SubtitleCreator:
    def __init__(self, duration_per_word):
        # duration is in seconds.
        self.duration_per_word = duration_per_word
    
    def create_from_file(self, input_filename, output_filename, encoding="ascii"):
        with open(input_filename, 'r', encoding=encoding) as f:
            text = f.read()
        
        self.create(text, output_filename)

    def interpret_input(self, text):
        # Take the input and return list.
        return re.split('\n{2,}', text)
    
    def get_duration(self, line):
        total_duration = number_of_word(line)*self.duration_per_word
        duration_seconds = floor(total_duration)
        duration_milliseconds = floor((total_duration-duration_seconds) * 1e3)
        return timedelta(seconds=duration_seconds, milliseconds=duration_milliseconds)

    def create(self, text, output_path):
        lines = self.interpret_input(text)
        length = len(lines)

        # Initialize starting time and subtitle duration.
        start = timedelta(hours=0)

        # Combining created list into a string in accordance with .srt formatting.
        subtitle_lines = []
        for i, line in enumerate(lines):
            duration = self.get_duration(line)
            end = start + duration
            srtstart = td_to_srt_time(start)
            srtend = td_to_srt_time(end)
            curr_text = f"{i+1}\n{srtstart} --> {srtend}\n{line}\n"
            subtitle_lines.append(curr_text)
            start = end

        # Converting the list into a string with the delimiter '\n'.
        subtitle_string = '\n'.join(subtitle_lines)

        # Writing the string to a new file.
        with open(output_path, 'w') as f:
            f.write(subtitle_string)
