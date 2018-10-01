'''
Filters the trues out of the prolog output
Author Adrian Postolache
'''

import fileinput

lines = []
count = 0
for line in fileinput.input():
	if count>1:
		lines.append(line)
	count+=1
lines = lines[:-2]

for line in lines:
	print(line.rstrip())

