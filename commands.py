def select(input_filename, output_filename, encoding):
    from selector import MissionEnigmaSelector

    selector = MissionEnigmaSelector()
    with open(input_filename, 'r', encoding=encoding) as f:
        text = f.read()

    selected_text = selector.select(text)
    output_text = '\n\n'.join(selected_text)

    with open(output_filename, 'w', encoding=encoding) as f:
        f.write(output_text)


def split(input_filename, output_filename, encoding):
    from splitter import NLTKSplitter

    splitter = NLTKSplitter()
    with open(input_filename, 'r', encoding=encoding) as f:
        text = f.read()

    lines = text.split('\n\n')
    for line in lines:
        splitted_line = splitter.split(line)
    splitted_lines = ['\n\n'.join(splitter.split(line)) for line in lines]
    output_text = '\n\n'.join(splitted_lines)

    with open(output_filename, 'w', encoding=encoding) as f:
        f.write(output_text)


def create(input_filename, output_filename, encoding):
    from subtitle_creator import SubtitleCreator
    from settings import DURATION_PER_WORD

    creator = SubtitleCreator(DURATION_PER_WORD)
    creator.create_from_file(input_filename, output_filename, encoding)


commands_dictionary = {
    'select': select,
    'split': split,
    'create': create
}