#!/usr/bin/env python3
# The program is meant to test the registration_isvp.py file

# The unittest package is used to performed the test on the different methods.
import unittest
import time
import registration_isvp as reg_isvp

class TestRegistration(unittest.TestCase):

    new_registration = reg_isvp.Registration()
    ca_registration = reg_isvp.RegistrationCA()
    ra_registration = reg_isvp.RegistrationRA()

    def test_1_registration_voter_keys_generation(self):
        """
        Test the private and public key generation for the voter
        """
        result = TestRegistration.new_registration.genetate_keys()
        self.assertTrue(result) 

    def test_2_registration_export_voter_keys(self):
        """
        Test the voter's key export method
        """
        result = TestRegistration.new_registration.export_keys_to_security_token()
        self.assertTrue(result) 

    def test_3_registration_generate_export_voter_csr(self):
        """
        Test the csr generation and export method
        """
        result = TestRegistration.ra_registration.export_voter_csr()
        self.assertTrue(result) 

    def test_4_registration_send_to_ca(self):
        """
        Test sending the CSR from RA to CA
        """
        result = TestRegistration.ra_registration.send_data_to_ca()
        time.sleep(1)
        self.assertTrue(result)

    def test_5_registration_recieve_data_from_ra(self):
        """
        Test recieving the CSR in CA
        """
        result = TestRegistration.ca_registration.recieve_data_from_ra()
        time.sleep(1)
        self.assertTrue(result)
    
    def test_6_registration_send_data_to_ra(self):
        """
        Test sending the certificate from CA to RA
        """
        result = TestRegistration.ca_registration.send_data_to_ra()
        time.sleep(1)
        self.assertTrue(result)
    
    def test_7_registration_recieve_data_from_ca(self):
        """
        Test recieving the CSR in RA
        """
        result = TestRegistration.ra_registration.recieve_data_from_ca()
        time.sleep(1)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()