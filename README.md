# genomics_demo_workshop

This is a demo of a genomic python package

## Installation

```
pip install git+https://github.com/EugeniaVoytik/genomics_workshop_demo
```

## Usage
```python
from genomics_demo import DNA
dna_strand = DNA('AGTTA') #make DNA strand
dna_strand.complimentary_sequence() # output 'TCAAT'
```