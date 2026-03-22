# rsa
# RSA Encryption — Implementation Exercise

Implement a minimal RSA encryption system from scratch in Python.

---

## Setup

```bash
git clone <repo-url>
cd rsa-exercise
```

No external libraries required — only the Python standard library.

---

## Your Task

Open **`rsa_exercise.py`**. Every function contains a `TODO` comment and returns `pass` or `None`.  
Replace those placeholders with working code.

There are **4 tasks** in order:

| Task | Function | What you implement |
|------|----------|--------------------|
| 1a | `gcd(a, b)` | Wrap `math.gcd` |
| 1b | `is_prime(n)` | Trial-division primality test |
| 2  | `generate_keys(p, q)` | RSA key generation (n, phi, e, d) |
| 3  | `encrypt(message, public_key)` | Character-by-character RSA encryption |
| 4  | `decrypt(ciphertext, private_key)` | RSA decryption back to plaintext |

Read the comments inside each function — they explain the required maths step by step.

---

## Testing

```bash
python test_rsa.py
```

You should see output like:

```
test_basic (TestGCD) ... ok
test_one (TestGCD) ... ok
...
----------------------------------------------------------------------
Ran 14 tests in 0.002s

OK
```

All 14 tests must pass for full marks.

---

## Quick sanity check

Once your functions are working, running the main script should produce:

```
Public key:  (3, 187)
Private key: (107, 187)

Original message: HELLO
Encrypted: [72, 23, 55, 55, 104]   ← values may differ with different e
Decrypted: HELLO
```

---

## Background reading

If you are unfamiliar with RSA, these concepts are worth reviewing before you start:

- Modular arithmetic and `a mod n`
- What a prime number is and why it matters for RSA
- Euler's totient function φ(n)
- Modular inverse and why `e × d ≡ 1 (mod φ(n))`

---

## Constraints

- Do **not** import any third-party cryptography library (`pycryptodome`, `cryptography`, etc.).
- Do **not** modify `test_rsa.py`.
- Python 3.8+ is required (`pow(e, -1, phi)` syntax).
