import unittest
from demical_class import changePrecision
from decimal import *


class TestDemicalClass(unittest.TestCase):
    def test_with_demical_outside_the_context_manager(self):
        x = Decimal('1.123132132') + Decimal('2.23232')
        with changePrecision(2):
            pass
        self.assertEqual(float(x), 3.355452132)

    def test_with_demical_in_context_manaager(self):
        with changePrecision(2):
            x = Decimal('1.123132132') + Decimal('2.23232')
        self.assertEqual(float(x), 3.4)

    def test_with_two_demicals(self):
        y = Decimal('1.123132132') + Decimal('2.23232')
        with changePrecision(2):
            x = Decimal('1.123132132') + Decimal('2.23232')
        self.assertEqual(float(x), 3.4)
        self.assertEqual(float(y), 3.355452132)

    def test_try_raise_error(self):
        exc = None
        try:
            with self.assertRaises(TypeError):
                with changePrecision(2):
                    print(Decimal('2.44444444'))
        except Exception as error:
            exc = error

        self.assertIsNotNone(exc)


if __name__ == '__main__':
    unittest.main()
