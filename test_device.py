from device import *

data = {'Смартфон': -34, 'Компьютер': 52, 'Планшет': 67, 'ТВ': 12}

# table(data)

import unittest


class Test_device(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_test_arr(self):
        self.assertEqual(type(test_arr(data)), tuple)

    def test_percent_1(self):
        self.assertEqual(type(percent([13, 256, 2])), list)

    def test_percent_2(self):
        for i in percent([12, 256, 2]):
            with self.subTest(i=i):
                self.assertGreaterEqual(100, i)


if __name__ == '__main__':
    unittest.main()

# python -m unittest -v test_device - для запуска из cmd/powershell
