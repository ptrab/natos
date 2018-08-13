# natos

Python reimplementation of a perl+octave combination to read the NAO density matrix from, e.g., a \*.nbo file section to get the alpha and beta occupations. As described in:

A. J.Webster, C. M.Mueller, N. P.Foegen, P. H.-L.Sit, E. D. Speetzen, D. W.Cunningham, J. S. D’Acchiolia, Oxidation states “naturally”: A Natural Bond Orbital method for determining transition metal oxidation states *Polyhedron* **2016**, *114* (16), 128–132, DOI: https://doi.org/10.1016/j.poly.2015.11.018

## usage
`./natos.py output.log`

## input
Gaussian output or \*.nbo file with `pop=nboread` and `$NBO DMNAO $END`.

### example input
```
#p ub3lyp genecp pop=nboread

[Fe(C5H5)2] from the SI of the paper

0 1
Fe -0.00079 0.00056 0.00036
C 0.28358 2.03707 0.30591
C 0.80847 1.65281 -0.96538
C 1.81955 0.66843 -0.74596
C 1.91932 0.44431 0.66081
C 0.97013 1.29021 1.31093
H -0.51463 2.74668 0.47579
H 0.47585 2.01934 -1.92678
H 2.38703 0.15838 -1.51217
H 2.57709 -0.26361 1.14623
H 0.78244 1.33432 2.37504
C -0.41335 -1.98164 0.46673
C -1.37494 -1.12243 1.08032
C -2.04040 -0.39579 0.04676
H -1.54623 -1.01677 2.14273
C -1.49050 -0.80616 -1.20559
C -0.48509 -1.78630 -0.94602
H 0.27039 -2.64169 0.98269
H -1.76610 -0.42062 -2.17762
H 0.13433 -2.27279 -1.68706
H -2.80476 0.35570 0.18948

C H 0
6-31G(d,p)
****
Fe 0
LANL2DZ
****

Fe 0
LANL2DZ

$NBO DMNAO $END                                                                                                                                                            


```

### example output
```
[0.4675999  0.46759951 0.99291434 0.92890009 0.92898616]
[0.4675999  0.46759951 0.99291434 0.92890009 0.92898616]
```
