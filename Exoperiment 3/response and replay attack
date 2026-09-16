import hashlib
import secrets

secret_key = "mysecret"

challenge = secrets.token_hex(8)

print("Server Challenge:", challenge)


response = hashlib.sha256(
    (challenge + secret_key).encode()
).hexdigest()

print("Client Response:", response)


expected_response = hashlib.sha256(
    (challenge + secret_key).encode()
).hexdigest()

if response == expected_response:
    print("Authentication Successful")
else:
    print("Authentication Failed")

print("\nReplay Attack Simulation")

if challenge == challenge:
    print("Replay Attack Detected")
