import unittest
import ps4
import numpy as np

class Test_Unit4(unittest.TestCase):

    def test_generate_models(self):
        """
        unit test for ps4.generate_models() function
        """
        xVals = [x for x in range(10)]
        yVals = [(y * 2) + 1 for y in xVals]
        degree = [1, 2, 3]
        models = ps4.generate_models(xVals, yVals, degree)
        self.assertEqual((round(models[0][0], 3), (round(models[0][1], 3))), (2.0, 1.0))

    def test_r_squared(self):
        """
        unit test for ps4.r_squared() function
        """
        y = [y for y in range(10)]
        estimated = y.copy()
        self.assertEqual(ps4.r_squared(y, estimated), 1.0)

if __name__ == '__main__':
    unittest.main()
