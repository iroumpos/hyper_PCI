# Hyper_PCI
This repository contains the implementation of 3 variations (strict,loose and additive)
of HyperPCI, a metric for hypergraphs.\
For constructing the hypergraphs the HyperNetX Python library was used.\
The following link contains information of this library and installation information.\
[https://pnnl.github.io/HyperNetX/install.html](https://pnnl.github.io/HyperNetX/install.html)\
\
\
This repository contains the datasets that are used for this project and 2 .py files.\
The **wrapper.py** file takes as an argument the dataset which is in a specific form and returns 
the graph in a list which is going to be the argument for a HyperNetX class.\
The **hyper_pci.py** file contains the 3 variations and the results of their execution are
passed in a .txt file.\
\
**Datasets**\
The datasets that are used for this project where taken from the following link
[https://www.cs.cornell.edu/~arb/data/](datasets) and the choise was made in the premise
that they will cover a big variety regarding their size, the number of hyperedges and their cardinality.

