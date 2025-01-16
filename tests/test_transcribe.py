# write tests for transcribe functions
import pytest

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    #assert function is working
    assert transcribe("ATCG") == "UAGC"

    assert transcribe("ATCG", reverse=True) == "CGAU"

    #assert value error is raised for invalid input
    with pytest.raises(ValueError, "Invalid input"):
        transcribe("ATCGZ")

    pass


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    #assert function is working
    assert reverse_transcribe("ATCG") == "CGAU"

    #assert value error is raised for invalid input
    with pytest.raises(ValueError, "Invalid input"):
        reverse_transcribe("ATCGZ")


    pass