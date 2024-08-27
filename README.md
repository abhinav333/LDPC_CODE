# Simulation of Low Density Parity Check (LDPC) error correction code.
LDPC is a robust technique for channel coding. Repository consists of python modules to generate and test it's performance using density evolution and EXIT chart analysis.<br />
File description:<br />
**chk_c.py** - calculation of log likelihood ratios of bit/check nodes <br />
**cir_mat.py** - creates random circulant generator matrix <br />
**cons.py** - Adjust bit/check node polynomial co-efficients<br />
**exch.py** - Threshold analysis<br />
**exit.py** - EXIT chart analysis<br />
**hamming.py** - Test sample hamming code<br />
**hard_hash.py** - Iterative algorithm and BER calculation using hard decoding<br />
**hashing.py** - Soft decoding algorithm <br />
**matgen.py** - Database of associated bit/check nodes with matrix entries<br />
**ini_llr.py** - Channel noise log likelihood ratio<br />
**nrm.py** - Newton-Ralphson method to obtain possible root of nth order polynomial<br />






