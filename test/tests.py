import unittest

from ConfigJson import *

with_repetitions_no_diff_types = configjson()
no_repetitions_diff_types = configjson()
repetitions_diff_types = configjson()
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

wrnr = repetitions_diff_types(
    z=2,
    a=3,
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
        self.assertEqual(cfg['z'], cfg.get()['z'])

        start_length = len(cfg)
        self.assertEqual(cfg['z'], cfg.pop('z'))
        self.assertEqual(start_length - 1, len(cfg))

    def test_dict_len(self):
        self.assertEqual(len(cfg.get()), len(cfg))
        self.assertEqual(len(cfg.get()), len(g))
        self.assertEqual(len(cfg.get()), len(~cfg))
        self.assertEqual(len(g), len(~cfg))
        self.assertEqual(len(g), len(cfg))
        self.assertEqual(len(cfg), len(~cfg))

    def test_Errors(self):
        self.assertRaises(RepetitionsError, with_repetitions_no_diff_types.sorted_by_values)
        self.assertRaises(RepetitionsError, with_repetitions_no_diff_types.sorted_by_values)
        self.assertRaises(NotSameTypeError, no_repetitions_diff_types.sorted_by_values)

    def test_contains(self):
        self.assertTrue('z' in cfg)
        self.assertFalse('avas' in cfg)


if __name__ == '__main__':
    unittest.main()
