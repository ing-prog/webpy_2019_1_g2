from main import Calculus
import unittest

#pip install unittest --user

class TestCalculus(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculus(2,3).add(),5)
        self.assertEqual(Calculus(0,0).add(),0)
        self.assertEqual(Calculus(-1,-3).add(),-4)

    def test_sub(self):
        self.assertEqual(Calculus(2,3).sub(),-1)
        self.assertEqual(Calculus(-1,-7).sub(),6)

    def test_mult(self):
        self.assertEqual(Calculus(2,3).mult(),6)
        self.assertEqual(Calculus(0,-7).mult(),0)


    def test_div(self):
        self.assertEqual(Calculus(2,1).div(),2)
        self.assertEqual(Calculus(15,-5).div(),-3)






if __name__ == "__main__":
    unittest.main()



#2 1 
#3 4

#[2 1] [ 3 4] [ 2 3] [ 1 4]

#TransPose 2 3
#          1 4