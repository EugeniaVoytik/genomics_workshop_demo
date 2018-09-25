from genomics_demo.rna import RNA
from genomics_demo.dna import DNA
import pytest

def test_bad_sequence_raise_error():
    with pytest.raises(ValueError):
        RNA('AUB')

def test_complimentary_sequence_works():
    assert RNA('GUC').complimentary_sequence == RNA('CAG')
    assert RNA('AUC').complimentary_sequence == RNA('UAG')

def test_reverse_transcription():
    assert RNA('UAGC').dna_sequence == DNA('GCTA')
    assert RNA('UAGC').dna_sequence == 'GCTA'

print('it worked')