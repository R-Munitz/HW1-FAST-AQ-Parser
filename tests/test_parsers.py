# write tests for parsers
#add these packages to .toml?
from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    
    fasta_parser = FastaParser("data/test.fa")
    #test that the file is being read in properly
    assert fasta_parser.filename == "data/test.fa"
    #test that the first line matches the expected output
    with open(fasta_parser.filename, "r") as file:
        first_record = next(fasta_parser.get_record(file))
        assert first_record[0] == "seq0"

  

    #test that value error is raised for blank file
    fasta_parser = FastaParser("tests/blank.fa")
    with pytest.raises(ValueError):
        for record in fasta_parser: #trigger iteration of empty file
            pass

    #test that value error is raised for corrupted file
    fasta_parser = FastaParser("tests/bad.fa")
    with pytest.raises(ValueError):
        for record in fasta_parser: #trigger iteration of corrupted file
            pass
        
    pass


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    
    fasta_parser = FastaParser("data/test.fa")
    #test that the file is being read in properly
    assert fasta_parser.filename == "data/test.fa"
    #test that the first item is not None
    with open(fasta_parser.filename, "r") as file:
        first_record = next(fasta_parser.get_record(file))
        assert first_record[0] != "None"

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
   
    fastq_parser = FastqParser("data/test.fq")
    #test that the file is being read in properly
    assert fastq_parser.filename == "data/test.fq"
    #test that the first item matches the expected output
    with open(fastq_parser.filename, "r") as file:
        first_record = next(fastq_parser.get_record(file))
        assert first_record[0] == "seq0"
        #assert fastq_parser.get_record(file)[0] == ('seq0') #double check this is expected output

    '''
    #test that value error is raised for blank file
    fastq_parser = FastqParser("tests/blank.fq")    #create blank file to test
    with pytest.raises(ValueError):
        for record in fastq_parser:  #trigger iteration of empty file 
            pass
            
    #test that value error is raised for corrupted file 
    fastq_parser = FastqParser("tests/bad.fq")  #create corrupted file to test
    with pytest.raises(ValueError):
        for record in fastq_parser:  #trigger iteration of corrupted file 
            pass
    '''

    pass

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """

    fastq_parser = FastqParser("data/test.fq")
    #test that the file is being read in properly
    assert fastq_parser.filename == "data/test.fq"

    #test that the first item is not None
    with open(fastq_parser.filename, "r") as file:
        first_record = next(fastq_parser.get_record(file))
        assert first_record[0] != "None"
    
