import unittest
import Parser

class UnitTest(unittest.TestCase):
    # This makes sure the unit tests are functioning properly
    def test(i):
        assert 1 == 1
    # Tests if raw commands can be sent to subprocess without issue
    def test_cmdRun(i):
        assert Parser.RunCommand("")

if __name__ == '__main__':
    unittest.main()
