"""Functions of the ``flake8_snippets`` to extend the flake8 functionality."""
import pep8
import re
import sys

from . import __version__


class Flake8Snippets(object):
    name = 'flake8_snippets'
    version = __version__

    def __init__(self, tree=None, filename=None, lines=None):
        self.filename = filename
        if filename is None:
            self.filename = 'stdin'
            self.lines = lines or []
        elif filename == '-':
            self.filename = 'stdin'
            self.lines = pep8.stdin_get_value().splitlines(True)
        elif lines is None:
            try:
                self.lines = pep8.readlines(filename)
            except IOError:
                (exc_type, exc) = sys.exc_info()[:2]
                self._io_error = '{}: {}'.format(exc_type.__name__, exc)
                self.lines = []
        else:
            self.lines = lines

    @classmethod
    def add_options(cls, parser):
        parser.add_option('--snippets', default='', metavar='patterns',
                          help="Comma separated code snippets to find")
        parser.config_options.append('snippets')

    @classmethod
    def parse_options(cls, options):
        if options.snippets:
            cls.snippets = options.snippets.split(',')
        else:
            cls.snippets = options.snippets

    def run(self):
        if self.snippets:
            regex = re.compile(r'{}'.format(u'|'.join(self.snippets)))
            for index, line in enumerate(self.lines):
                if pep8.noqa(line):
                    return
                match = regex.search(line)
                if match:
                    text = 'S100 Snippet found: "{}".'.format(match.group())
                    yield index + 1, match.start(), text, type(self)
