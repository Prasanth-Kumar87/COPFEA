# COPFEA
_COrrelated Pharmacophore FEatures Analysis (COPFEA) – Identifies correlative pharmacophore features of small molecules from the trajectories of molecular dynamic simulations_

The COPFEA approach analyzes the time-lagged correlation of pharmacophore features present in the small molecules extracted at regular intervals from the dynamic simulation trajectories. It is useful for designing small molecule binders against different conformational states. The approach was validated on 15 protein-ligand systems and showed efficiency in 3 leading simulation packages as Desmond, Gromacs and YASARA.

**Input:**
1) PDB coordinates of small molecules extracted from the stabilized conformations in the simulation trajectory (e.g., 051.pdb to 100.pdb).
2) The starting / initial PDB coordinate of the small molecule used for simulations (e.g., 001.pdb).
3) A text file containing the atom names corresponding to the encoded pharmacophore features (e.g., N4, O9).

**System requirements:**

1) Python 3 (any stable version) with Matplotlib
2) Windows or Linux OS.

_Tested on Python 3.8.1 with Matplotlib 3.3.2 dependency in Ubuntu 18 and Python3 IDE 3.10 Windows 10 (64-bit) OS._

**Execution:**

Keep the complete set of PDB coordinates, pharmacophore.txt, and the COPFEA.py script in a single directory.

**Example:**

The adenosine deaminase complexed with FR221647 (1ndw) was simulated for 100 ns using Desmond Dynamics package and extracted the ligand coordinates corresponding to stabilized conformations from 50 ns till 100 ns. The example set contains the PDB coordinates and associated files for testing purposes. 
![image](https://user-images.githubusercontent.com/57387735/155455164-05d95fc0-5fe4-4c50-ad6f-6b84a5ec235d.png)

The encircled atom positions were specified as pharmacophore features in the pharmacophore.txt as N4, O9, N10, O15, C27. Navigate to the folder containing the PDB files, pharmacophore.txt and COPFEA.py in the example folder and execute the following command in the Linux terminal or Python3 IDE in Windows.

`python3 COPFEA.py`

**Results:**

The COPFEA script returns the count of features given in the pharmacophore.txt and the list of features. The script selects 001.pdb (default) as the reference set and flattens the 3D coordinates to compute the cross-correlation matrix and further requests the user to provide a single input (here N4) of feature from the list of features specified in the pharmacophore.txt.

![image](https://user-images.githubusercontent.com/57387735/155457464-548b037d-460f-43a7-ac29-799017ea80b1.png)

The results will be stored graphically in PNG format in the current directory (Computed Correlated Features.png).

![Computed Correlated Features](https://user-images.githubusercontent.com/57387735/155457769-2cb0179a-532b-4c86-ac4b-6f5757593b1f.png)

The input feature N4 constituted positive correlations with N10, O15 and O9 features. The feature N4 negatively correlated with the C27 feature implying that C27 fluctuated largely in the motions during the simulations thereby restricting its usage in dynamic pharmacophore analysis. N4, N10, O15 and O9 features are preferable for such analysis.

**Developer and Primary contact:**

Prasanth Kumar (prasanthbioinformatics[at]gmail.com).

**Publication:**

Kumar SP, Rawal RM, Pandya HA (2022). COrrelated Pharmacophore FEatures Analysis (COPFEA): An approach to identify correlative pharmacophore features of small molecules from simulation trajectories. In Preparation.











