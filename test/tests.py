import unittest
from source.ConfigJson import *


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        """Setup tests"""
        self.with_repetitions_no_diff_types = ConfigJson()
        self.no_repetitions_diff_types = ConfigJson()
        self.repetitions_diff_types = ConfigJson()
        self.cfg = ConfigJson()

        self.wr = self.with_repetitions_no_diff_types(
            z=2,
            a=1,
            pin=3,
            hash=3,
            xuy=16).get()

        self.nr = self.no_repetitions_diff_types(
            z=2,
            a=1,
            pin=3,
            hash='asdasda',
            xuy=16).get()

        self.wrnr = self.repetitions_diff_types(
            z=2,
            a=3,
            pin=3,
            hash='asdasda',
            xuy=16).get()

        self.g = self.cfg(
            z=2,
            a=1,
            pin=3,
            hash=112,
            xuy=16).get()

    def tearDown(self):
        """Closing"""
        del self.g
        del self.wrnr
        del self.nr
        del self.wr

        del self.cfg
        del self.repetitions_diff_types
        del self.no_repetitions_diff_types
        del self.with_repetitions_no_diff_types


    def test_return_types(self):
        self.assertIsInstance(self.cfg.get(), dict)
        self.assertIsInstance(~self.cfg, dict)
        self.assertIsInstance(self.cfg, ConfigJson)

    def test_equal(self):
        self.assertEqual(self.g, self.cfg.get())
        self.assertNotEqual(self.g, ~self.cfg)
        self.assertEqual(self.cfg['z'], self.cfg.get()['z'])

        start_length = len(self.cfg)
        self.assertEqual(self.cfg['z'], self.cfg.pop('z'))
        self.assertEqual(start_length - 1, len(self.cfg))

    def test_dict_len(self):
        self.assertEqual(len(self.cfg.get()), len(self.cfg))
        self.assertEqual(len(self.cfg.get()), len(self.g))
        self.assertEqual(len(self.cfg.get()), len(~self.cfg))
        self.assertEqual(len(self.g), len(~self.cfg))
        self.assertEqual(len(self.g), len(self.cfg))
        self.assertEqual(len(self.cfg), len(~self.cfg))

    def test_Errors(self):
        self.assertRaises(RepetitionsError, self.with_repetitions_no_diff_types.sorted_by_values)
        self.assertRaises(RepetitionsError, self.with_repetitions_no_diff_types.sorted_by_values)
        self.assertRaises(NotSameTypeError, self.no_repetitions_diff_types.sorted_by_values)

    def test_contains(self):
        self.assertTrue('z' in self.cfg)
        self.assertFalse('avas' in self.cfg)


if __name__ == '__main__':
    unittest.main()
