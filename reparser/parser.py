import re


class Parser(object):

    def __init__(self):
        self.methods = {}

    def register(self, pattern, method):
        self.methods[pattern] = method

    @property
    def patterns(self):
        return self.methods.keys()

    @property
    def actions(self):
        return self.methods.values()

    def get(self, pattern):
        return self.methods.get(pattern)

    def _match_iter(self, scan):
        match = scan.search()
        while match:
            yield match
            match = scan.search()

    def search(self, text):
        result = []
        scanner = re.Scanner(self.methods.items(), flags=re.MULTILINE)
        scan = scanner.scanner.scanner(text)
        for match in self._match_iter(scan):
            pattern = scanner.lexicon[match.lastindex-1][0]
            action = scanner.lexicon[match.lastindex-1][1]
            result.append(action(**re.search(pattern, match.group()).groupdict()))
        return result
