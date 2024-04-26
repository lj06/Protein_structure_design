# Protein_structure_design
CX4803 Group 8 Project


## Training Data 

### option1: pdb files of E.coli
obtain pdb files of E.coli from alphafold with ```pdb.py``` and ```ecoli.txt```

### option2: pdb files of other species
obtain all pdb files of interested species from Alphafold full dataset downloads: https://alphafold.ebi.ac.uk/download#full-dataset-section

```tar –xvf``` the downloaded tar file.
Rename the folder to ```data```.
```
cd data
rm *.cif.gz
pigz -d *.pdb.gz
cd ..
```
Run ```rename.py``` to rename all the PDB files to Uniprot ID with ```./rename.py```.
Extract all the basename of the PDB files to create a list of Uniprot ID with ```list.py```.
Command line usage for ```list.py```
```
./list.py [OUTPUT_FILE].txt
```

Extract the protein sequence into a CSV file based on the [Uniprot_list].txt with ```sequence.py```.


