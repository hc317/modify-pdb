#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_file = open('./result.pdb')
lines = input_file.readlines()
output_file = open('./hbond.csv', 'a+')
output_file.write('A-T: N1-N3,0.3nm\nG-C: N1-N3,0.3nm\n')
output_file.write('atom,atom-seq,res,res-seq\n')

for line in lines[:-1]:
	line = line.strip().split()
	if line[3] == 'DA' and line[2] == 'N1':
		output_file.write('{0},{1},{2},{3}\n'.format(line[2],line[1],line[3],line[5]))
	elif line[3] == 'DT' and line[2] == 'N3':
		output_file.write('{0},{1},{2},{3}\n'.format(line[2],line[1],line[3],line[5]))
	elif line[3] == 'DG' and line[2] == 'N1':
		output_file.write('{0},{1},{2},{3}\n'.format(line[2],line[1],line[3],line[5]))
	elif line[3] == 'DC' and line[2] == 'N3':
		output_file.write('{0},{1},{2},{3}\n'.format(line[2],line[1],line[3],line[5]))
	else:
		pass

input_file.close()
output_file.close()

output_file = open('./hbond-o.csv', 'a+')
output_file.write('A-T: N1-N3,0.3nm\nG-C: N1-N3,0.3nm\n')
output_file.write('A-T: N6-O4,0.29nm\nG-C: O6-N4; N2-O2,0.29nm; 0.29nm\n')
output_file.write('atom,atom-seq,res,res-seq\n')

for line in lines[:-1]:
	line = line.strip().split()
	if line[3] == 'DA' and line[2] == 'N1':
		output_file.write('{0},{1},{2},{3}\n'.format(line[2],line[1],line[3],line[5]))
	elif line[3] == 'DT' and line[2] == 'N3':
		output_file.write('{0},{1},{2},{3}\n'.format(line[2],line[1],line[3],line[5]))
	elif line[3] == 'DG' and line[2] == 'N1':
		output_file.write('{0},{1},{2},{3}\n'.format(line[2],line[1],line[3],line[5]))
	elif line[3] == 'DC' and line[2] == 'N3':
		output_file.write('{0},{1},{2},{3}\n'.format(line[2],line[1],line[3],line[5]))

	elif line[3] == 'DA' and line[2] == 'N6':
		output_file.write('{0},{1},{2},{3}\n'.format(line[2],line[1],line[3],line[5]))
	elif line[3] == 'DT' and line[2] == 'O4':
		output_file.write('{0},{1},{2},{3}\n'.format(line[2],line[1],line[3],line[5]))
	elif line[3] == 'DG' and line[2] == 'N2':
		output_file.write('{0},{1},{2},{3}\n'.format(line[2],line[1],line[3],line[5]))
	elif line[3] == 'DG' and line[2] == 'O6':
		output_file.write('{0},{1},{2},{3}\n'.format(line[2],line[1],line[3],line[5]))
	elif line[3] == 'DC' and line[2] == 'N4':
		output_file.write('{0},{1},{2},{3}\n'.format(line[2],line[1],line[3],line[5]))
	elif line[3] == 'DC' and line[2] == 'O2':
		output_file.write('{0},{1},{2},{3}\n'.format(line[2],line[1],line[3],line[5]))		
	else:
		pass

output_file.close()