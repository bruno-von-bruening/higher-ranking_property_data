# higher-ranking_property_data
This repository provides the data for the Paper *Benchmarking higher-ranking multipoles and
polarizability tensors for small molecular systems* **(give doi, citation data etc.)**


# Data
## Data Folds

The properties evaluated for basis set convergence at correlated level:
* ```props_correlated_level_basis_set_convergence```

Following datasets are evaluated on the 73 compounds using the produciton level basis (see paper)
* ```props_cc_reference_main_dataset.json```: contains CCSD(T) references
* ```props_correlate_methods_main_dataset.json```: contains  CCSD(T), CCSD, MP, HF
* ```props_all_methods_main_dataset.json```: contains all methods evaluated: CCSD(T), CCSD, MP, HF and all DFAs 
* ```props_dfas_with_smaller_basis.json```: properties of selected DFA evaluated at various basis set.

The properties evaluated for basis set study at DFA level:
* ```errors_full_dataset.json```: Error of CCSD,MP2,HF, and DFAS at main-basis against CCSD(T)/main-basis references
* ```errors_basis_set_convergence_dataset.json```: Error of CCSD(T),CCSD,MP2,HF, and  against the same method paried  with aug-cc-pwCV5Z for multipoles and t-aug-cc-pV5Z for polarizabilities
* ```errors_dfas_with_smaller_basis.json```: Error of selected DFAs evaluated with different basis sets against CCSD(T) references, also includes scaled methods which are marked by suffix ```_scale-cc```

## Data Format
The properties can be found in the ```data/``` directory.
Each is structured like a table with the following fields.
First the columns that index the specific compound and level of theory the properties are evaluated for:
* ```method```: correlated of DFA used for the calculation
* ```basis```: basis set used for the calculation
* ```inchikey```: unique identifier for each compound, search pubchem ```InChI=<inchi>``` to find the compound
* ```molecular_formula```: molecular formula named according to Hait and Head-Gordon's work. See Table X.Y **(fill in when paper finished)** in the main paper
For datasets containing the values for properties these can be found under the following column names (all traceless cartesian):
* ```D```: dipole moment (x,y,z)
* ```Q```: quadrupole moment (xx,xy,yy,xz,yz,zz)
* ```DDP```: dipoles (x,y,z) of the dipole-dipole polarizbality tensor
* ```QQP```: diagonal (xx,xy,yy,xz,yz,zz) of the dipole-dipole polarizability tensor
For datasets containg errors there are 20 columns with 5 the following five indicators for each property (properties denoted as ```D```,```Q```,```DDP```,```QQP``` as above):
* ```rel-prc-aniso```: percentual isotropic error
* ```rel-prc-iso```: percentual isotropic error
* ```mgn-ref-au```: magnitude of reference in atomic units
* ```mgn-try-au```: magnitude of the property in atomic units
* ```mgn-diff-au```: magnitude of the difference tensor (element wise subtraction trial-reference) in atomic units
Note that  ```basis='main_basis'``` refers to d-aug-cc-pVQZ with cW core polarization at Si,P,S elements used as main basis in the corresponding paper.
Errors and magnitudes are define in the paper under subsection 4.1.




# Going through the data
## Install 
You should setup a python environment that contains the necessary packages. These can be found in ```conda_env.yaml``` file which also can be used to create a conda environment directly:
```bash
    conda env create -f conda_env.yaml
```

## Load data
Have a look at the jupyter notebbok ```view_data.ipynb``` on how to load the data and convert to spherical harmonics.

# Example Finite Difference calculations
Find example files for the calculation under example_psi4_input_files. There **wil be** different types of calculations.
Provided are the ```.psi4inp``` files which can be run through ```psi4 <input>.psi4inp```. (we used ```psi4``` in version 1.10)
Furthermore, these files can be auto generated thorugh the provided ```.yaml``` files using the **custom script run_psi4... (link to my github)**

Following calculations are provided (meanding ```<method-name>_<basis-set>_compound```)
* ```B97-3_aug-pcseg-2_H2O/``` 

Later include
* B97-3/main_basis for water
* B97-3/main_basis for SH2
* CCSD(T)/main_basis for water
* CCSD(T)/main_basis for SH2

