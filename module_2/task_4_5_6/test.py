import unittest
import client

class TestClient(unittest.TestCase):

	client = client.Client('test', client.SERVER)

	def test_init(self):
		self.assertIsInstance(self.client.name, str, 'Should be string')
		self.assertIsInstance(self.client.id, int, 'Should be int')
		self.assertGreater(self.client.id, 99, 'Should be greater than 99')
		self.assertLess(self.client.id, 1000, 'Should be less than 1000')

	def test_run(self):
		self.client.run()

if __name__=='__main__':
	unittest.main()