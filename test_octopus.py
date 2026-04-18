import unittest
from octopus import Octopus

class TestOctopus(unittest.TestCase):
    def test_ink(self):
        o = Octopus("Test")
        self.assertIn("ink", o.ink())

if __name__ == "__main__":
    unittest.main()
