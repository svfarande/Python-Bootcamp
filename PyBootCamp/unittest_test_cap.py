import unittest
import unittest_cap


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = unittest_cap.MyFunc(text)
        self.assertEqual('Python', result)  # self.assertEqual(<expected>, <actual>)

    def test_multi_word(self):
        text = 'many python words'
        result = unittest_cap.MyFunc(text)
        self.assertEqual('Many Python Words', result)   # self.assertEqual(<expected>, <actual>)


if __name__ == '__main__':
    unittest.main()
