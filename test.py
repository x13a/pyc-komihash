import unittest
import komihash

class KomihashTestCase(unittest.TestCase):
    def test_komihash(self):
        self.assertEqual(komihash.hash64(b'test1'), 5270236647356506095)
        self.assertEqual(komihash.hash64(b'test2'), 11456916202224026228)
    
    def test_komirand(self):
        rng = komihash.Rand(0, 0)
        self.assertEqual(rng.rand(), 12297829382473034410)
        self.assertEqual(rng.rand(), 18446744073709551614)
        self.assertEqual(rng.rand(), 5270498306774157584)
        self.assertEqual(rng.rand(), 13469051228422846976)
