
Import unittest
From calculator import prime.py

Class Testprime (unittest.testcase):
Def test_input_Is_prime_string(self):
With iself.assertraises(typeerror):
prime(“string”)
Def works_correctly(self)
self.asssertequals({2,3,5}, {is PRIME})


