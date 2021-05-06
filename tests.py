import unittest
import json
import flatten

class testFlatten(unittest.TestCase):
    def test_isValidKey_string(self):
       # self.assertEqual(flatten.isValidKey("a."), False)
        self.assertEqual(flatten.isValidKey("a"), True)
        self.assertTrue(flatten.isValidKey("a,'"))
        self.assertFalse(flatten.isValidKey("3."))
        self.assertFalse(flatten.isValidKey("."))
    
    def test_isValidKey_empty(self):
        self.assertEqual(flatten.isValidKey(""), False)
        self.assertFalse(flatten.isValidKey(None))

    def test_isValidString_minimum_json(self):
        self.assertTrue(flatten.isValidString("{}"))

    def test_isValidString_empty(self):
        self.assertFalse(flatten.isValidString(("")))
        self.assertFalse(flatten.isValidString(None))
    
    def test_isValidString_correct(self):
        self.assertTrue(flatten.isValidString("""{"Role": true}"""))
    
    def test_isValidString_random(self):
        self.assertFalse(flatten.isValidString("""{"Role": true}sdk9"""))

    def test_isValidJson_empty(self):
       self.assertFalse(flatten.isValidJson(None))
       
    
# if ran as a script
if __name__ == '__main__':
    unittest.main()
