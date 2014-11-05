import os
import time
from nose.plugins import Plugin


class TestTooSlow(Exception):
    pass


class TooSlow(Plugin):
    """Treat tests that are too slow as errors."""

    name = 'tooslow'
    enabled = True

    max_time = 1.0

    def options(self, parser, env=os.environ):
        super(TooSlow, self).options(parser, env=env)
        parser.add_option('--tooslow-time', type=float,
                default=1.0, metavar="SECONDS",
                help="Consider any tests that take this many seconds "
                    "(or longer) to be errors; default 1.0")

    def configure(self, options, config):
        super(TooSlow, self).configure(options, config)
        self.config = config
        if not self.enabled:
            return
        self.max_time = options.tooslow_time

    def startTest(self, test):
        self.t1 = time.time()

    def stopTest(self, test):
        t2 = time.time()
        elapsed = t2 - self.t1
        if elapsed >= self.max_time:
            raise TestTooSlow("Elapsed time %0.3fs exceeds max of %0.3fs" %
                    (elapsed, self.max_time))
