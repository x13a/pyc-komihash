import unittest
import komihash

class KomihashTestCase(unittest.TestCase):
    def test_komihash(self):
        self.assertEqual(komihash.komihash(b'test1'), 5270236647356506095)
        self.assertEqual(komihash.komihash(b'test2'), 11456916202224026228)
    
    def test_komirand(self):
        self.assertEqual(komihash.komirand(0, 0), 12297829382473034410)
