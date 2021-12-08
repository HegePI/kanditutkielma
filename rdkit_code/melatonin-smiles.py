from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem

melatonin_smiles = 'CC(=O)NCCC1=CNC2=C1C=C(C=C2)OC'

m = Chem.MolFromSmiles(melatonin_smiles)

img = Draw.MolsToImage(
    mols=[m], legends=[melatonin_smiles], subImgSize=(300, 300))

img.save("melatonin-smiles.png")
