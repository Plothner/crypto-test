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
