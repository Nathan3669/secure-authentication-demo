import pytest
from authentication_service import validate_password, hash_password, verify_password

def test_validate_password_success():
    valid, _ = validate_password("StrongPass1!")
    assert valid

def test_validate_password_fail_short():
    valid, message = validate_password("S1!")
    assert not valid
    assert "at least 8 characters" in message

def test_validate_password_fail_no_upper():
    valid, message = validate_password("weakpass1!")
    assert not valid
    assert "uppercase" in message

def test_password_hash_and_verify():
    password = "MySecure1!"
    hashed = hash_password(password)
    assert verify_password(password, hashed)