import unittest
# Import the functions from your main script
from contacts_manager import validate_phone, validate_email

class TestContactValidation(unittest.TestCase):

    # --- Test Phone Validation ---
    def test_valid_phones(self):
        self.assertTrue(validate_phone("1234567890")[0])
        self.assertTrue(validate_phone("+1 123-456-7890")[0])
        self.assertTrue(validate_phone("123.456.7890")[0])

    def test_invalid_phones(self):
        self.assertFalse(validate_phone("12345")[0]) # Too short
        self.assertFalse(validate_phone("1234567890123456")[0]) # Too long
        self.assertFalse(validate_phone("abc-def-ghij")[0]) # No digits

    # --- Test Email Validation ---
    def test_valid_emails(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertTrue(validate_email("user.name+label@domain.co.uk"))

    def test_invalid_emails(self):
        self.assertFalse(validate_email("plainaddress"))
        self.assertFalse(validate_email("@missinguser.com"))
        self.assertFalse(validate_email("user@missingtld."))

if __name__ == '__main__':
    unittest.main()