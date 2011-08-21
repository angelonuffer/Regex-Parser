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

    @property
    def patterns_without_groups(self):
        return map(lambda pattern: re.sub(r"\(\?P<[^>]+>([^)]+)\)", r"\1", pattern), self.patterns)

    @property
    def methods_without_groups(self):
        return zip(self.patterns_without_groups, self.actions)

    def get(self, pattern):
        return self.methods.get(pattern)

    def _match_iter(self, scan):
        match = scan.search()
        while match:
            yield match
            match = scan.search()

    def search(self, text):
        result = []
        scanner = re.Scanner(self.methods_without_groups, flags=re.MULTILINE)
        scan = scanner.scanner.scanner(text)
        for match in self._match_iter(scan):
            pattern = self.patterns[match.lastindex-1]
            action = self.actions[match.lastindex-1]
            result.append(action(**re.search(pattern, match.group()).groupdict()))
        return result
