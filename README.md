# ISVP_OACM_ISEC

Repository for the ISVP implementation and tests

This repository provides some examples on how to implement the ISVP (Internet Secure Voting Protocol) using Python 3 and the packages **cryptography** and **sslib**.

## Installation

To start using this examples it is necessary to install the packages locally or in the venv that will execute the program. To install them use the next command:

```
 pip3 install cryptography sslib
```

## How to use it

You can run unit testing using the test_announcement.py file to verify the methods avaialble in the announcement_isvp.py file. You can do it by running the next command:

```
 python3 -m unittest test_announcement.py
```

You can use the file announcement_isvp.py as a package or run your tests locally. Here is an example on how to run the file directly from the python console:

![Screenshot 2024-09-26 at 11 28 05](https://github.com/user-attachments/assets/6541a4ae-7e0b-4a3b-ac07-e5426805d4f4)

## Methods avaialble

The methods available in the Announcement class are:

 - __set_election_data
 - ask_election_data
 - __generate_electoral_authority_keys
 - __share_private_key
 - __recover_private_key
 - __sign_ea_public_key
 - verify_signature_ea_public_key
 - publish_data_bulletin_board
 - announcement_process
