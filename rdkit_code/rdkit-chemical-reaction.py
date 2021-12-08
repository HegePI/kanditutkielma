from rdkit.Chem import Draw
from rdkit.Chem import AllChem

rxn = AllChem.ReactionFromSmarts('C(=O)O.OCC>>C(=O)OCC.O', useSmiles=True)
d2d = Draw.ReactionToImage(rxn)

d2d.save("reaction.png")
