from selector import MissionEnigmaSelector


INPUT_FILENAME = "subtitles.txt"
OUTPUT_FILENAME = "subtitles-selected.txt"
encoding = "utf-8"


selector = MissionEnigmaSelector()
with open(INPUT_FILENAME, 'r', encoding=encoding) as f:
    text = f.read()

selected_text = selector.select(text)
output_text = '\n\n'.join(selected_text)

with open(OUTPUT_FILENAME, 'w', encoding=encoding) as f:
    f.write(output_text)