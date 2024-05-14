import unittest
import sys


class Test_run(unittest.TestCase):
    def test_simple_test(self):
        """Simple test to test nothing"""
        pass


if __name__ == "__main__":
    # check if running in interactive mode or not
    if sys.flags.interactive:
        # Directly run the test if running interactively.
        unittest.main()
    else:
        # Creates a testsuite and run it for non interactive
        suite = unittest.TestLoader().loadTestsFromTestCase(Test_run)
        unittest.TextTestRunner().run(suite)
