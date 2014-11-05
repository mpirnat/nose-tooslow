nose-tooslow
============

Plugin for the Nose test framework that treats tests that take too long to
execute as errors.

The maximum allowable time defaults to 1.0 seconds or may be configured as
desired.

Install
-------

From PyPI:

    pip install nose-tooslow

From source:

    pip install git+git://github.com/mpirnat/nose-tooslow#egg=nose-tooslow

Usage
-----

Treat any tests longer than the default of 1.0 seconds as errors:

    nosetests --with-tooslow

Treat any tests longer than 0.5 seconds as errors:

    nosetests --with-tooslow --tooslow-time 0.5


Example
-------

    $ nosetests --with-tooslow

    ...E...
    ======================================================================
    ERROR: test_a_test_that_is_too_slow
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    ...
    File
    "/Users/mike/.virtualenvs/envs/nose-tooslow/lib/python2.7/site-packages/nose/plugins/manager.py",
    line 362, in stopTest
        return self.plugin.stopTest(test.test)
    File "/Users/mike/code/nose-tooslow/tooslow/tooslow.py", line 40, in stopTest
        (elapsed, self.max_time))
    TestTooSlow: Elapsed time 2.536s exceeds max of 1.000s

