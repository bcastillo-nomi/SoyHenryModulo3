#import pytest
from func import es_primo


# Test cases for valid prime numbers
def test_small_prime_number():
    """Test that small prime numbers are correctly identified"""
    assert es_primo(5) is True


def test_number_two_edge_case():
    """Test that 2 (the smallest prime) is correctly identified as prime"""
    assert es_primo(2) is True


def test_large_prime_number():
    """Test that larger prime numbers are correctly identified"""
    assert es_primo(97) is True


def test_large_prime_efficiency():
    """Test handling of larger prime numbers for performance"""
    assert es_primo(101) is True


def test_identifies_prime_number():
    """Test additional prime number identification"""
    assert es_primo(7) is True
    assert es_primo(11) is True
    assert es_primo(13) is True


def test_known_primes():
    """Test that a list of known small primes are correctly identified"""
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for p in primos:
        assert es_primo(p) is True


# Test cases for non-prime numbers
def test_small_non_prime_number():
    """Test that small composite numbers are correctly identified"""
    assert es_primo(4) is False


def test_even_numbers_greater_than_two():
    """Test that even numbers greater than 2 are correctly identified as non-prime"""
    assert es_primo(8) is False
    assert es_primo(100) is False


def test_composite_numbers_multiple_factors():
    """Test composite numbers with multiple factors"""
    assert es_primo(15) is False  # 15 = 3 × 5
    assert es_primo(21) is False  # 21 = 3 × 7
    assert es_primo(35) is False  # 35 = 5 × 7


def test_identifies_non_prime_number():
    """Test additional non-prime number identification"""
    assert es_primo(9) is False


# Test cases for edge cases (0, 1, negative numbers)
def test_input_zero():
    """Test that 0 is correctly identified as non-prime"""
    assert es_primo(0) is False


def test_input_one():
    """Test that 1 is correctly identified as non-prime"""
    assert es_primo(1) is False


def test_negative_numbers():
    """Test that negative numbers are correctly identified as non-prime"""
    assert es_primo(-7) is False
    assert es_primo(-3) is False
    assert es_primo(-1) is False


# Test cases for input validation - Boolean
def test_rejects_boolean_true():
    """Test that boolean True input returns appropriate error message"""
    assert es_primo(True) == "Error: el parámetro no debe ser booleano"


def test_rejects_boolean_false():
    """Test that boolean False input returns appropriate error message"""
    assert es_primo(False) == "Error: el parámetro no debe ser booleano"


# Test cases for input validation - Float
def test_rejects_float_input():
    """Test that float input returns appropriate error message"""
    assert es_primo(5.5) == "Error: el parámetro no debe ser decimal"


def test_rejects_float_whole_number():
    """Test that float representing whole number returns appropriate error message"""
    assert es_primo(5.0) == "Error: el parámetro no debe ser decimal"


# Test cases for input validation - String
def test_rejects_string_input():
    """Test that string input returns appropriate error message"""
    assert es_primo("5") == "Error: el parámetro no debe ser una cadena"


def test_rejects_empty_string():
    """Test that empty string input returns appropriate error message"""
    assert es_primo("") == "Error: el parámetro no debe ser una cadena"


# Test cases for input validation - Other types
def test_rejects_none_input():
    """Test that None input returns appropriate error message"""
    assert es_primo(None) == "Error: el parámetro debe ser un número entero"


def test_rejects_list_input():
    """Test that list input returns appropriate error message"""
    assert es_primo([5]) == "Error: el parámetro debe ser un número entero"


def test_rejects_dict_input():
    """Test that dictionary input returns appropriate error message"""
    assert es_primo({"num": 5}) == "Error: el parámetro debe ser un número entero"


def test_known_non_primes():
    """Test that a list of known small non-primes are correctly identified"""
    no_primos = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
    for n in no_primos:
        assert es_primo(n) is False