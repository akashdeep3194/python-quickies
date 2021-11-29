import unittest
import q3
from unittest import TestCase
class TestQ3(TestCase):
    def setUp(self) -> None:
        self.s = q3.Solution()


    def test_can_create_1(self):    

        A = ['back' , 'end', 'front', 'tree']
        input_str = 'backend'
        
        self.assertEqual(self.s.solve(A,input_str),True)

    def test_can_create_2(self):
        
        A = ['back' , 'end', 'front', 'tree']
        input_str = 'frontend'
        self.assertEqual(self.s.solve(A,input_str),True)

    def test_can_create_3(self):
        
        A = ['back' , 'end', 'front', 'tree']
        input_str = 'backyend'
        self.assertEqual(self.s.solve(A,input_str),False)

    def test_can_create_4(self):
        
        A = ['back' , 'end', 'front', 'tree','backy']
        input_str = 'backyend'
        self.assertEqual(self.s.solve(A,input_str),True)

    def test_can_create_5(self):
        
        A = ['back' , 'end', 'front', 'tree']
        input_str = 'frontyard'
        self.assertEqual(self.s.solve(A,input_str),False)

if __name__ == '__main__':
    unittest.main()
