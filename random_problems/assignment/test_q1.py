import unittest
import q1
from unittest import TestCase

class TestQ3(TestCase):
    def setUp(self) -> None:
        self.s = q1.Solution()

    def test_can_create_1(self):           
        self.assertEqual(self.s.mostActive("chats.txt"),"John")
                
if __name__ == '__main__':
    unittest.main()
