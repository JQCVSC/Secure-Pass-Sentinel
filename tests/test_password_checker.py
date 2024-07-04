import unittest
from app.main import check_password_strength

class TestPasswordChecker(unittest.TestCase):
    def test_weak_password(self):
        result = check_password_strength("weak")
        self.assertEqual(result['strength'], "Very Weak")

    def test_strong_password(self):
        result = check_password_strength("StrongP@ssw0rd")
        self.assertEqual(result['strength'], "Very Strong")

if __name__ == '__main__':
    unittest.main()