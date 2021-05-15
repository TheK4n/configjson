
import unittest
from ConfigJson import *

with_repetitions_no_diff_types = configjson()
no_repetitions_diff_types = configjson()
cfg = configjson()

wr = with_repetitions_no_diff_types(
        z=2,
        a=1,
        pin=3,
        hash=3,
        xuy=16).get()

nr = no_repetitions_diff_types(
        z=2,
        a=1,
        pin=3,
        hash='asdasda',
        xuy=16).get()

g = cfg(
        z=2,
        a=1,
        pin=3,
        hash=112,
        xuy=16).get()


class TestStringMethods(unittest.TestCase):

    def test_return_types(self):
        self.assertIsInstance(cfg.get(), dict)
        self.assertIsInstance(~cfg, dict)
        self.assertIsInstance(cfg, configjson)

    def test_equal(self):
        self.assertEqual(g, cfg.get())
        self.assertNotEqual(g, ~cfg)

    def test_dict_len(self):
        self.assertEqual(len(cfg.get()), len(cfg))
        self.assertEqual(len(cfg.get()), len(g))
        self.assertEqual(len(cfg.get()), len(~cfg))
        self.assertEqual(len(g), len(~cfg))
        self.assertEqual(len(g), len(cfg))
        self.assertEqual(len(cfg), len(~cfg))

    def test_Errors(self):
        self.assertRaises(RepetitionsError, with_repetitions_no_diff_types.sorted_by_values)


if __name__ == '__main__':
    unittest.main()
