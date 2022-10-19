from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name ("Carson", "McBride") == "McBride; Carson"
    assert make_full_name("Leilani", "Ka'anapali") == "Ka'anapali; Leilani"
    #assert make_full_name("", "") == "; "

def test_extract_family_name ():
    assert extract_family_name ("McBride; Carson") == "McBride"
    #assert extract_family_name("; ") == ""

def test_extract_given_name():
    assert extract_given_name ("McBride; Carson") == "Carson"
    #assert extract_given_name("; ") == ""



pytest.main(["-v", "--tb=line", "-rN", __file__])