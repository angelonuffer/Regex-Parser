import unittest
from should_dsl import should
from parser import Parser


class TestParser(unittest.TestCase):

    def it_register_methods(self):
        parser = Parser()
        foo = lambda: "foo"
        parser.register(r"foo", foo)
        parser.patterns |should| equal_to(["foo"])
        parser.actions |should| equal_to([foo])
        parser.get("foo") |should| equal_to(foo)

    def it_calls_methods_following_its_patterns(self):
        parser = Parser()
        parser.register(r"a", lambda: "foo")
        return_list = parser.search("abc")
        return_list |should| equal_to(["foo"])
        parser.register(r"b", lambda: "bar")
        return_list = parser.search("abca")
        return_list |should| equal_to(["foo", "bar", "foo"])

    def it_passes_regex_groups_by_args(self):
        parser = Parser()
        example = lambda foo: "foo=%s" % foo
        parser.register(r"^(?P<foo>.*)$", example)
        return_list = parser.search("bar\nbaar")
        return_list |should |equal_to(["foo=bar", "foo=baar"])
        parser.methods.clear()
        example2 = lambda key, value: "%s = %s" % (key, value)
        parser.register(r"^(?P<key>[^=]*)=(?P<value>.*)$", example2)
        return_list = parser.search("a=1\nb=2")
        return_list |should |equal_to(["a = 1", "b = 2"])
