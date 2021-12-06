from splitter import NLTKSplitter


INPUT_FILENAME = "subtitles-selected.txt"
OUTPUT_FILENAME = "subtitles-splitted.txt"
encoding = "utf-8"


splitter = NLTKSplitter()
with open(INPUT_FILENAME, 'r', encoding=encoding) as f:
    text = f.read()

lines = text.split('\n\n')
for line in lines:
    splitted_line = splitter.split(line)
splitted_lines = ['\n\n'.join(splitter.split(line)) for line in lines]
output_text = '\n\n'.join(splitted_lines)

with open(OUTPUT_FILENAME, 'w', encoding=encoding) as f:
    f.write(output_text)
