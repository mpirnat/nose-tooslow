import os
import time
from nose.plugins import Plugin


class TestTooSlow(Exception):
    pass


class TooSlow(Plugin):

    name = 'tooslow'
    enabled = True

    max_time = 1

    def options(self, parser, env=os.environ):
        super(TooSlow, self).options(parser, env=env)

    def configure(self, options, config):
        super(TooSlow, self).configure(options, config)
        self.config = config
        if not self.enabled:
            return

    def startTest(self, test):
        self.t1 = time.time()

    def stopTest(self, test):
        t2 = time.time()
        elapsed = t2 - self.t1
        if elapsed >= self.max_time:
            raise TestTooSlow("Elapsed time %ss exceeds max of %ss" %
                    (elapsed, self.max_time))
