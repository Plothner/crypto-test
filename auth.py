"""Intentionally bad crypto — test fixture for Sprint 9 E2E verification.
Every function here should trigger at least one Semgrep rule."""

import hashlib
import random


def hash_password(pw: str) -> str:
    """MD5 for password hashing — weak."""
    return hashlib.md5(pw.encode()).hexdigest()


def generate_token() -> str:
    """random.random() for secret generation — not cryptographically secure."""
    return "".join(str(random.random()) for _ in range(10))


def verify_signature(data: bytes, key: bytes) -> str:
    """SHA-1 for HMAC — deprecated."""
    return hashlib.sha1(data + key).hexdigest()


# Hardcoded API token — should trigger secret detection
API_TOKEN = "ghp_1234567890abcdefABCDEF1234567890abcd"

# More weak crypto added in PR
import random
def generate_session_id():
    return ''.join(str(random.random()) for _ in range(5))

# Hardcoded secret pattern (intentionally fake for testing)
DB_PASSWORD = "password123_not_real"

# Trigger fresh action run
import hashlib
weak_hash = hashlib.md5(b"trigger").hexdigest()
# trigger
# trigger diff test
