import math

# =============================================================
#  RSA ENCRYPTION — GUIDED IMPLEMENTATION EXERCISE
#  Fill in every section marked with TODO.
#  Run  python test_rsa.py  to check your work.
# =============================================================


# ---------- TASK 1: BASIC FUNCTIONS ----------
# The Greatest Common Divisor (GCD) of two integers is the largest
# number that divides both without a remainder.
# Python's math module already provides this — wrap it.

def gcd(a, b):
    # TODO: return the GCD of a and b using math.gcd
    pass


# A prime number is only divisible by 1 and itself.
# Use trial division up to sqrt(n) — no need to check further.

def is_prime(n):
    # TODO: return True if n is prime, False otherwise
    # Hint: n must be > 1, and no integer i in range(2, sqrt(n)+1)
    #       should divide n evenly.
    pass


# ---------- TASK 2: KEY GENERATION ----------
# RSA key generation follows these steps:
#   1. Compute n = p * q                       (the modulus)
#   2. Compute phi = (p-1) * (q-1)             (Euler's totient)
#   3. Choose e: smallest odd number >= 3 where gcd(e, phi) == 1
#   4. Compute d: the modular inverse of e mod phi
#
# The PUBLIC key  is (e, n).
# The PRIVATE key is (d, n).

def generate_keys(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")

    # TODO: compute n and phi
    n   = None  # replace None
    phi = None  # replace None

    # TODO: find e — start at 3, increment by 2, stop when gcd(e, phi) == 1
    e = 3
    # your loop here

    # TODO: compute d — the modular inverse of e (mod phi)
    # Hint: pow(e, -1, phi) works in Python 3.8+
    d = None  # replace None

    return (e, n), (d, n)


# ---------- TASK 3: ENCRYPTION ----------
# To encrypt a plaintext message with the public key (e, n):
#   - Convert each character to its ASCII code with ord()
#   - Raise it to the power e, modulo n:  c = m^e mod n
#   - Return the list of resulting numbers

def encrypt(message, public_key):
    e, n = public_key
    # TODO: return a list of encrypted values, one per character
    pass


# ---------- TASK 4: DECRYPTION ----------
# To decrypt a ciphertext with the private key (d, n):
#   - For each number c in the ciphertext, compute: m = c^d mod n
#   - Convert m back to a character with chr()
#   - Join all characters into a string and return it

def decrypt(ciphertext, private_key):
    d, n = private_key
    # TODO: return the decrypted plaintext string
    pass


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    p = 11
    q = 17

    public_key, private_key = generate_keys(p, q)
    print("Public key: ", public_key)
    print("Private key:", private_key)

    message = "HELLO"
    print("\nOriginal message:", message)

    encrypted = encrypt(message, public_key)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, private_key)
    print("Decrypted:", decrypted)
