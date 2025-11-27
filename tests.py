import unittest
from app import app

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_multiply_invalid_input(self):
        r = self.app.get('/multiply?a=abc&b=3')
        self.assertEqual(r.status_code, 400)

    def test_multiply_success(self):
        r = self.app.get('/multiply?a=4&b=5')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'20.0')

    def test_multiply_decimal(self):
        r = self.app.get('/multiply?a=2.5&b=4')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'10.0')

if __name__ == '__main__':
    unittest.main()