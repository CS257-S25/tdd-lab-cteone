import sys
from io import StringIO

import unittest

from production import main


class TestReverseCommandLine(unittest.TestCase):
    def test_reverse_command_line(self):
        sys.argv = ["production.py", "this is a test"]
        sys.stdout = StringIO()
        main()
        printed = sys.stdout.getvalue()
        self.assertEqual(printed, "siht si a tset\n")

    def test_reverse_command_line_no_args(self):
        sys.argv = ["production.py"]
        sys.stdout = StringIO()
        main()
        printed = sys.stdout.getvalue()
        self.assertEqual(printed, "Specify phrase\n")


if __name__ == "__main__":
    unittest.main()
