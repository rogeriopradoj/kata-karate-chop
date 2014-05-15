import unittest
from chop import Chop

class ChopTest(unittest.TestCase):

    def test_chop(self):
      self.assertEquals(-1, Chop.chop(3, []))
      self.assertEquals(-1, Chop.chop(3, [1]))
      self.assertEquals(0,  Chop.chop(1, [1]))
      #
      self.assertEquals(0,  Chop.chop(1, [1, 3, 5]))
      self.assertEquals(1,  Chop.chop(3, [1, 3, 5]))
      self.assertEquals(2,  Chop.chop(5, [1, 3, 5]))
      self.assertEquals(-1, Chop.chop(0, [1, 3, 5]))
      self.assertEquals(-1, Chop.chop(2, [1, 3, 5]))
      self.assertEquals(-1, Chop.chop(4, [1, 3, 5]))
      self.assertEquals(-1, Chop.chop(6, [1, 3, 5]))
      #
      self.assertEquals(0,  Chop.chop(1, [1, 3, 5, 7]))
      self.assertEquals(1,  Chop.chop(3, [1, 3, 5, 7]))
      self.assertEquals(2,  Chop.chop(5, [1, 3, 5, 7]))
      self.assertEquals(3,  Chop.chop(7, [1, 3, 5, 7]))
      self.assertEquals(-1, Chop.chop(0, [1, 3, 5, 7]))
      self.assertEquals(-1, Chop.chop(2, [1, 3, 5, 7]))
      self.assertEquals(-1, Chop.chop(4, [1, 3, 5, 7]))
      self.assertEquals(-1, Chop.chop(6, [1, 3, 5, 7]))
      self.assertEquals(-1, Chop.chop(8, [1, 3, 5, 7]))

if __name__ == "__main__":
    unittest.main()