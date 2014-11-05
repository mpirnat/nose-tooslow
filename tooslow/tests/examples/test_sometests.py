import time


class TestWhenTooSlow(object):

    def test_marks_test_failed(self):
        time.sleep(2)


class TestWhenNotTooSlow(object):

    def test_marks_test_passed(self):
        time.sleep(0.5)
