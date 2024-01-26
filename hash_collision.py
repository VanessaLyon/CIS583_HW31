import hashlib
import os
import random

def hash_collision(k):
    # Check if k is a valid integer
    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return b'\x00', b'\x00'
    if k <= 0:
        print("Specify a positive number of bits")
        return b'\x00', b'\x00'

    # Initialize x and y
    x = y = ''
    # Generate a random seed to ensure randomness in string generation
    random.seed(os.urandom(1024))

    while True:
        # Generate two random strings
        x = str(random.random())
        y = str(random.random())

        # Convert strings to bytes
        x_bytes = x.encode()
        y_bytes = y.encode()

        # Compute SHA256 hashes
        hash_x = hashlib.sha256(x_bytes).hexdigest()
        hash_y = hashlib.sha256(y_bytes).hexdigest()

        # Convert hex hashes to binary
        binary_x = bin(int(hash_x, 16))[2:].zfill(256)  # Ensuring 256 bits
        binary_y = bin(int(hash_y, 16))[2:].zfill(256)  # Ensuring 256 bits

        # Check if the last k bits match
        if binary_x[-k:] == binary_y[-k:]:
            break

    return x_bytes, y_bytes

# Example usage
x, y = hash_collision(10)  # Example for k=10
print(f"x: {x}")
print(f"y: {y}")
