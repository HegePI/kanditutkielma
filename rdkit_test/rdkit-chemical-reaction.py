from rdkit.Chem import Draw
from rdkit.Chem import AllChem

rxn = AllChem.ReactionFromSmarts(
    '[cH:5]1[cH:6][c:7]2[cH:8][n:9][cH:10][cH:11][c:12]2[c:3]([cH:4]1)[C:2](=[O:1])O.[N-:13]=[N+:14]=[N-:15]>C(Cl)Cl.C(=O)(C(=O)Cl)Cl>[cH:5]1[cH:6][c:7]2[cH:8][n:9][cH:10][cH:11][c:12]2[c:3]([cH:4]1)[C:2](=[O:1])[N:13]=[N+:14]=[N-:15]', useSmiles=True)
d2d = Draw.MolDraw2DCairo(800, 300)
d2d.DrawReaction(rxn)
png = d2d.GetDrawingText()
open('reaction1.o.png', 'wb+').write(png)
