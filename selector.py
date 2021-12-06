import re
from settings import SELECT_PATTERN


class RegexSelector:
    def __init__(self, pattern):
        self.compiled_pattern = re.compile(pattern)

    def select(self, text):
        matches = self.compiled_pattern.findall(text)
        result = []
        for match in matches:
            if isinstance(match, tuple|list):
                for elem in match:
                    if elem: result.append(elem)
            else:
                result.append(match)
        return result
        

    def select_from_file(self, path, encoding="ascii"):
        with open(path, 'r') as f:
            text = f.read()
        return self.select(text)


class MissionEnigmaSelector(RegexSelector):
    def __init__(self, *args, **kwargs):
        super().__init__(SELECT_PATTERN, *args, **kwargs)
        self.compiled_pattern = re.compile(SELECT_PATTERN)
