#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from seq import original as ori
from seq import correspond as cor 
from seq import specific as spe
import pprint


dna_seq = [ 'DG5','DA','DG','DT','DC','DA','DA','DC','DG','DT',
			'DC','DT','DG','DG','DA','DT','DC','DC','DT','DG',
			'DT','DT','DT','DT',
			'DC','DA','DG','DG','DA','DT','DC','DC','DA','DG',
			'DA','DC','DG','DT','DT','DG','DA','DC','DT','DC3']

original_file = open("./dna.pdb", "r")
original_lines = original_file.readlines()
original_file.close()

result_pdb = open("./result.pdb", "a+")

line = 1
lines_num = 0
residues_num = 1

for nucleotide in dna_seq:
	line += lines_num
	lines_num = len(ori.original_seq[nucleotide])

	correspond_coordinate = {}
	for row in range(line, lines_num+line):
		#print(row)
		original_line = original_lines[row].strip().split()
		#print(original_line)
		coordinate_list = []
		coordinate_list.append(original_line[4])
		coordinate_list.append(original_line[5])
		coordinate_list.append(original_line[6])
		coordinate_list.append(original_line[2])

		correspond_coordinate[cor.correspond_seq[nucleotide][row-line]] = coordinate_list
		pprint.pprint(correspond_coordinate)

	for row in range(line, lines_num+line):
		result_pdb.write("ATOM   {0:>4} {1:>4}  {2} A   {3}   {4:>8}{5:>8}{6:>8}  1.00  0.00           {7}\n".format(
			row, 
			spe.specific_seq[nucleotide][row-line],
			nucleotide[:2], 
			residues_num,
			correspond_coordinate[spe.specific_seq[nucleotide][row-line]][0],
			correspond_coordinate[spe.specific_seq[nucleotide][row-line]][1],
			correspond_coordinate[spe.specific_seq[nucleotide][row-line]][2],
			correspond_coordinate[spe.specific_seq[nucleotide][row-line]][3],))

	residues_num += 1

result_pdb.write("END")
result_pdb.close()