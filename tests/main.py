import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
from pyfb import Pyfb, OAuthException, PyfbException

#Your APP ID. It Needs to register your application on facebook
#http://developers.facebook.com/
FACEBOOK_APP_ID = '178358228892649'

class pyfbTests(unittest.TestCase):

    def test_exceptions(self):
        #instance client
        facebook = Pyfb(FACEBOOK_APP_ID)

        #Test new auth exception
        self.assertRaises(OAuthException, facebook.get_myself)
        #Test old and generic exception
        self.assertRaises(PyfbException, facebook.get_myself)

if __name__ == "__main__":

    unittest.main()
