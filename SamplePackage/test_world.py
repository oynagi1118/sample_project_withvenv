from unittest import TestCase
from SamplePackage.SampleClass import SampleClass


class TestWorld(TestCase):
    def test_say(self):
        sample = SampleClass()
        assert sample.hello() is True
        # self.fail()

