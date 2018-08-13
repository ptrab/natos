#!/usr/bin/env python
"""
Oxidation states “naturally”: A Natural Bond Orbital method
for determining transition metal oxidation states

Albert J.Webster, Chelsea M.Mueller, Neil P.Foegen,
Patrick H.-L.Sit, Erin D. Speetzen, Drew W.Cunningham,
Jason S. D’Acchiolia

Polyhedron,  Volume 114, 16 August 2016, Pages 128-132

https://doi.org/10.1016/j.poly.2015.11.018


Reimplementation of their perl+octave combination to read the
NAO density matrix section to get the alpha and beta occupations.
"""

import sys
import re
import numpy as np
from numpy import linalg as LA


def getContent(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines


def getIndices(lines):
    densitystart = []
    densityend = []
    index = []

    for n in np.arange(len(lines)):
        line = lines[n]
        if "NAO density matrix:" in line:
            densitystart.append(n)
        if "NATURAL BOND ORBITAL ANALYSIS, alpha spin orbitals:" in line:
            densityend.append(n)
        if "NATURAL BOND ORBITAL ANALYSIS, beta spin orbitals:" in line:
            densityend.append(n)
        if re.search("Val\(\ [0-9]d\)", line):
            sline = line.split()
            index.append(sline[0])

        index = index[:5]

    return densitystart, densityend, index


def getOccupancies(blockstart, blockend, indices, lines):
    n = int(blockstart) + 1
    m = int(blockend)
    templist = []

    for j in np.arange(n, m):
        line = lines[j]
        if "NAO" in line:
            nao = line.split()
            nao = nao[1:]
            for k in np.arange(len(nao)):
                for index in indices:
                    if nao[k] == index:
                        for row in indices:
                            ii = j + int(row) + 1
                            array = lines[ii].split(")")
                            array2 = array[1].split()
                            templist.append(float(array2[k]))

    mat = np.array(templist).reshape(5, 5)
    occupancies = LA.eigvals(mat)

    return occupancies


if __name__ == "__main__":
    LINES = getContent(sys.argv[1])
    START, END, INDICES = getIndices(LINES)
    ALPHA = getOccupancies(START[0], END[0], INDICES, LINES)
    BETA = getOccupancies(START[1], END[1], INDICES, LINES)

    print(ALPHA)
    print(BETA)
