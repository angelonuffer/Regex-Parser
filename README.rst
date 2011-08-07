Regex Parser 0.0.1
==================

Provide a tool to create parsers using regex to call methods.


Simple example
--------------

To call a method every times the pattern matches the string::

    >>> from reparser import matches
    >>> @matches(r"^(?P<foo>.*)$")
    >>> def my_method(foo):
    ...     print "Method called with arg: %s" % foo
    >>> search("foo\nbar")
    Method called with arg: foo
    Method called with arg: bar


Installing
----------

Install using latest version::

    $ git clone git@github.com:angelonuffer/Regex-Parser.git
    # python setup.py install

*NOTE: the second command needs be runned with root user
        you can use the sudo application for this
