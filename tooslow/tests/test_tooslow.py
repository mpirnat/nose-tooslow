import os
import unittest
from nose.plugins import PluginTester
from nose.tools import raises

from tooslow import TooSlow


class TooSlowTest(PluginTester):

    activate = '--with-tooslow'
    plugins = [TooSlow()]
    suitepath = os.path.join(os.path.dirname(__file__), 'examples')

    def makeSuite(self):
        pass


class TestWhenRunningTests(TooSlowTest, unittest.TestCase):

    def _first_line(self, output):
        return str(output).split('\n')[0]

    def test_one_test_too_slow(self):
        assert self._first_line(self.output).count('E') == 1

    def test_one_test_not_too_slow(self):
        assert self._first_line(self.output).count('.') == 1
