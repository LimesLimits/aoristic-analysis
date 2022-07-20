# aoristic analysis
Python script used for estimating probabilities of find numbers per period. Input is a text file with probabilities of dating per find. These probabilities are summed in sequential order from earliest to latest period in order to attribute the simulated finds to one particular period.

INPUT SAMPLE FILE
The first column contains the site number, columns 2 through 8 the probabilities of dating per period, and the last column the total number of finds for this observation.
1 0.00 0.00 0.00 0.40 1.00 1.00 1.00 1.00
1 0.19 0.22 0.25 0.32 0.41 0.48 0.56 2.00
1 0.30 0.30 0.30 0.30 0.30 0.30 0.30 50.00
2 0.00 0.00 0.00 0.00 0.00 0.44 1.00 1.00
2 0.03 0.03 0.04 0.05 0.07 0.08 0.09 1.00
3 0.00 0.00 0.00 0.00 0.00 0.44 1.00 1.00
3 0.00 0.08 0.17 0.35 0.61 0.78 1.00 2.00
3 0.00 0.10 0.22 0.44 0.77 1.00 1.00 1.00
4 0.00 0.00 0.00 0.28 0.71 1.00 1.00 1.00
4 0.00 0.01 0.04 0.08 0.14 0.17 0.22 8.00

