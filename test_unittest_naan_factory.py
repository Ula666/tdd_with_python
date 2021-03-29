from naan_factory import NaanFactory

import unittest


class FactoryTest(unittest.TestCase):
    factory = NaanFactory()

    def test_make_dough(self):
        self.assertEqual(self.factory.make_dough("water", "flour"), "dough")

    def test_bake_dough(self):
        self.assertEqual(self.factory.bake_dough("dough"), "naan")
