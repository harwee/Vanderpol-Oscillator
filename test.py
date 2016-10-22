import unittest
from vanderpol import vanderpol_func

class TestVanderpolFunction(unittest.TestCase):

	def testArray(self):
		self.assertEqual(vanderpol_func([1,2],5),[2,-1])


if __name__=='__main__':
	unittest.main()
