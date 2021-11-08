from Bio.PDB import *
import nglview as nv
import ipywidgets

def view_pdb(file):
    pdb_parser = PDBParser()
    structure = pdb_parser.get_structure("PHA-L", file)
    view = nv.show_biopython(structure)

def view_cif(file):
    cif_parser = MMCIFParser()
    structure = cif_parser.get_structure("6EBK", file)
    view = nv.show_biopython(structure)

# view_pdb("data/1fat.pdb")

view_cif("data/5xhs.cif")

mmcif_dict = MMCIFDict.MMCIFDict("data/5xhs.cif")
len(mmcif_dict) # 689

# .get_residues() method in a loop
for model in structure:
    for residue in model.get_residues():
        print(residue)
# .get_residues() method as generator object
residues = structure.get_residues() # returns a generator object
[item for item in residues]
# .unfold_entities - keyword for each level of the SMCRA structure
Selection.unfold_entities(structure, "R") # R is for residues

polypeptide_builder = CaPPBuilder()
counter = 1
for polypeptide in polypeptide_builder.build_peptides(structure):
    seq = polypeptide.get_sequence()
    print(f"Sequence: {counter}, Length: {len(seq)}")
    print(seq)
    counter += 1
