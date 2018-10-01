'''
Filters input into swipl
Author Adrian Postolache
'''

import fileinput
print('consult(["parser.pdb","regex.pdb","prologcc.pdb","prprint.pdb","compiler.pdb"]).\n')

string = "test(["

for line in fileinput.input():
	tempstr = ''
	lookingbegin = False
	lookingend = False
	for char in line:
		if char == '\n':
			continue
		if char == '|':
			if lookingend:
				string+="'=|',"
				lookingend = False
			else:
				tempstr = char
				lookingbegin = True
			continue
		elif char == '=':
			if lookingbegin:
				string+="'|=',"
				lookingbegin = False
			else:
				tempstr = char
				lookingend = True
			continue
		elif lookingbegin or lookingend:
			string+="'"+tempstr+"',"
			lookingbegin = False
			lookingend = False


		string+="'"+char+"',"
	string+="'\\n',"
if string !="test([":
	string = string[:-1]	
string+= "]).\n"

print(string)
	
