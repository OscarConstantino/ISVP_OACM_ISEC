#!/usr/bin/env python3
# The program is meant to test the announcement_isvp.py file

# The unittest package is used to performed the test on the different methods.
import unittest
import announcement_isvp as an_isvp

class TestAnnouncement(unittest.TestCase):

    def test_1_announcement_keys_generation(self):
        """
        Test the announcement private and public key generation
        """
        result = an_isvp.Announcement._Announcement__generate_electoral_authority_keys(self)
        self.assertTrue(result)
    
    def test_2_announcement_share_private_key(self):
        """
        Test the sharing key process
        """
        result = an_isvp.Announcement._Announcement__share_private_key(self)
        self.assertTrue(result)

    def test_3_announcement_recover_private_key(self):
        """
        Test the recovering key process
        """
        result = an_isvp.Announcement._Announcement__recover_private_key(self)
        self.assertTrue(result)
    
    def test_4_announcement_signing(self):
        """
        Test the signing public key process
        """
        result = an_isvp.Announcement._Announcement__sign_ea_public_key(self)
        self.assertTrue(result)

    def test_5_announcement_signing_verification(self):
        """
        Test the verification public key process
        """
        result = an_isvp.Announcement.verify_signature_ea_public_key(self, an_isvp.Announcement._Announcement__signed_public_key)
        self.assertTrue(result)
    
    def test_6_announcement_publish_bb(self):
        """
        Test the bulletin board export process
        """
        result = an_isvp.Announcement.publish_data_bulletin_board(self)
        self.assertTrue(result)    

if __name__ == '__main__':
    unittest.main()
