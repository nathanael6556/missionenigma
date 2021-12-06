# Mission's Enigma Subtitle Creator
This repository is dedicated for the purpose of automating the creation of subtitle for a short film that goes by the title 'Mission's Enigma'.

# How it works
Selector will select only the dialogs.
Splitter will split the dialogs into lines for better reading.
Subtitle Creator will make the SRT file.

# How to use it
Save your texts as subtitles.txt in the same folder as this file.

Execute "main-select.py".
Revise the texts in the newly created file, "subtitles-selected.txt", to make sure everything is working properly.

Execute "main-split.py".
Revise the texts in the newly created file, "subtitles-splitted.txt", to make sure everything is working properly.

Execute main-create.py.

If everything is done properly, you should now have "subtitles.srt" in the same folder as this file.

# Supported dialogs formats
## 1. Single line
The name followed by colon and the dialogs.
Example: "John: Hello world!"

## 2. Multiline
The dialogs are directly in the next line after the name.
The name is in caps.
There should be an empty line after the dialogs.

Example:<br/>
JOHN<br/>
Hello world!<br/>
Hello again world!<br/>
