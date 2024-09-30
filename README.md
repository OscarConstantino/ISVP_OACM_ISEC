# ISVP_OACM_ISEC

Repository for the ISVP implementation and tests

This repository provides some examples on how to implement the ISVP (Internet Secure Voting Protocol) using Python 3 and the packages **cryptography** and **sslib**.

The announcement phase is implemented using elliptic curcves public key encryption and Shamir secret key sharing. The registration phase is implemented using RSA public key encryption.

## Installation

To start using this examples it is necessary to install the packages locally or in the venv that will execute the program. To install them use the next command:

```
 pip3 install cryptography sslib
```

## How to use it

You can run unit testing using the test_announcement.py file to verify the methods avaialble in the announcement_isvp.py file. You can do it by running the next command:

### Announcement phase

```
 python3 -m unittest test_announcement.py
```

### Registration phase

```
 python3 -m unittest test_registration.py
```

You can use the file announcement_isvp.py or registration_isvp.py as a package or run your tests locally. Here is an example on how to run the file directly from the python console:

![Screenshot 2024-09-26 at 11 28 05](https://github.com/user-attachments/assets/6541a4ae-7e0b-4a3b-ac07-e5426805d4f4)

## Methods avaialble

### Announcement
The methods available in the Announcement class:

 - __set_election_data
 - ask_election_data
 - __generate_electoral_authority_keys
 - __share_private_key
 - __recover_private_key
 - __sign_ea_public_key
 - verify_signature_ea_public_key
 - publish_data_bulletin_board
 - announcement_process

### Registration
The methods available in the Registration class:

 - __recover_ca_public_key -> private method to recover the certificate authotity's public key 
 - __recover_ra_public_key -> private method to recover the registration authotity's public key 
 - __generate_voter_keys -> private method to generate the voter's private and public keys
 - genetate_keys -> public method that calls the private method and generate the keys
 - export_keys_to_security_token -> public method that makes two pem files with the created keys 
 - __sign_message -> private method that signs a given message with a private key
 - __cipher_message -> private method to encrypt a given message with a public key 
 - __decipher_mesage ->  private method to unencrypt a given message with a private key 
 - verify_cert -> public method to verify a given signature with a public key

### RegistrationCA
The methods available in the RegistrationCA class:

 - __recover_ca_private_key -> private method to recover the certificate authotity's private key 
 - __generate_voter_certificate -> private method to recover the registration authotity's public key
 - send_data_to_ra -> private method to recover the registration authotity's public key
 - recieve_data_from_ra -> private method to recover the registration authotity's public key

### RegistrationCA
The methods available in the RegistrationCA class

 - __recover_ra_private_key -> private method to recover the registration authotity's private key 
 - send_data_to_ca -> public method to send the csr file to the certification authority
 - recieve_data_from_ca -> public method to recieve the voter's certificate from the certification authority
 - __generate_voter_csr -> private method to generate the voter's csr
 - export_voter_csr -> public method to export the csr to a pem file
