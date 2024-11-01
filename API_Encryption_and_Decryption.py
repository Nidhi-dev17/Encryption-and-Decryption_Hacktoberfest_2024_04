#For API encryption, using HMAC (Hash-based Message Authentication Code) with SHA-256 is a secure method to ensure data integrity.

import hmac
import hashlib
import base64

# Shared secret key (for HMAC)
api_key = b'supersecretkey'

def generate_signature(data):
    """Encrypt the data to create an HMAC signature."""
    signature = hmac.new(api_key, data.encode(), hashlib.sha256).digest()
    encoded_signature = base64.b64encode(signature).decode()
    return encoded_signature

def verify_signature(data, signature):
    """Verify the HMAC signature."""
    expected_signature = generate_signature(data)
    return hmac.compare_digest(expected_signature, signature)

# Usage
data = "Sensitive API Data"
signature = generate_signature(data)
print("Generated Signature:", signature)

is_valid = verify_signature(data, signature)
print("Signature Valid:", is_valid)


#In this method:

#generate_signature creates an HMAC signature for the data.
#verify_signature confirms the data hasn’t been altered by comparing the generated and provided signatures.
#This example uses the standard Python hmac and hashlib libraries.
