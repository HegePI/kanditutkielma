from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import DataStructs
import numpy as np

melatonin_smiles = 'CC(=O)NCCC1=CNC2=C1C=C(C=C2)OC'

melatonin_mol = Chem.MolFromSmiles(melatonin_smiles)

melatonin_fp = AllChem.GetMorganFingerprintAsBitVect(
    melatonin_mol,
    2,
    nBits=1024
)

array = np.zeros((0,), dtype=np.int8)

DataStructs.ConvertToNumpyArray(melatonin_fp, array)

print(array.shape, array.nonzero())
