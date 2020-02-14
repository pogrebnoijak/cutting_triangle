import unittest
from plan import*

class TestStringMethods(unittest.TestCase):

    def test_valid_direct(self):
        line1 = [0, 0, 4, 4]
        line2 = [0, 4, 4, 0]
        line3 = [1, 1, 4, 1]
        line4 = [-2, -1, 2, 1]
        self.assertFalse(valid_direct(line1, line2))
        self.assertFalse(valid_direct(line1, line3))
        self.assertFalse(valid_direct(line1, line4))
        self.assertTrue(valid_direct(line2, line4))
        self.assertFalse(valid_direct(line3, line4))
        self.assertFalse(valid_direct(line2, line3))

    def test_Iter(self):
        bord1 = [2, 4]; bord2 = [10, 15]
        pr_x = 2
        pr_y = 0
        self.assertTrue(Iter(bord1, bord2, pr_x, pr_y) != -1)
        pr_y = 3
        self.assertTrue(Iter(bord1, bord2, pr_x, pr_y) != -1)
        pr_x = 0
        self.assertTrue(Iter(bord1, bord2, pr_x, pr_y) != -1)
        pr_y = 0
        self.assertFalse(Iter(bord1, bord2, pr_x, pr_y) != -1)

    def test_line_border(self):
        x1 = 0.5; y1 = 0.866025; x2 = 0.7071; y2 = 0.7071; L = 4; x = y = 0
        point = line_border(x1, y1, x2, y2, L, x, y)
        self.assertTrue(point[0] > 5.2770 and point[0] < 5.2771)
        self.assertTrue(point[1] > 5.2770 and point[0] < 5.2771)

if __name__ == '__main__':
    unittest.main()
