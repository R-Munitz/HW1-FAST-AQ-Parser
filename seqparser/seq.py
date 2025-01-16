# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:  
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
   
    #read in sequence as array of letters
    seq = list(seq)
    for base in seq:
        #map base to complement ( A:U)
        seq[base] = TRANSCRIPTION_MAPPING[base]
    if reverse:
        seq = seq[::-1]
    return str(seq)



def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    #transcribe and reverse
    return transcribe(seq, reverse=True)

    