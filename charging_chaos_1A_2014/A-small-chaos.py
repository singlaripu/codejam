#! /usr/bin/env python
import math


#################################################################################################

def parseInputData(problem, s_input, s_id):
	finput = open(problem + '-' + s_input + '-' + s_id + '.in','r')
	nCase = int(finput.readline().strip())
	inputList = finput.readlines()	
	finput.close()
	return nCase, inputList

#################################################################################################

def writeOutput(result, problem, s_input, s_id):
	foutput = open(problem + '-' + s_input + '-' + s_id + '.out','w')
	foutput.writelines(result)
	foutput.close()
	
#################################################################################################

def StrToNumList(s):
	s = s.strip()
	return [int(x) for x in s.split()]

#################################################################################################

def solve_chaos(elt):

	global sol
	sol = 11

	def check_now(O, D):
		return set(O) == set(D)

	def flip(outlets, p):
		return [''.join([o[:p], '0' if o[p]=='1' else '1', o[p+1:]]) for o in outlets]

	def brute_force(n, l, O, D, i, f):
		global sol
		if check_now(O, D):
			sol = min(f, sol)
		for j in range(i, l, 1):
			brute_force(n, l, flip(O, j), D, j+1, f+1)

	n, l = [int(x) for x in elt[0].strip().split()]
	outlets = elt[1].strip().split()
	devices = elt[2].strip().split()
	brute_force(n, l, outlets, devices, 0, 0)

	if sol < 11:
		return sol
	else:
		return "NOT POSSIBLE"

###################################################################################################
					
problem = 'A'
s_input = 'small'
s_id = 'chaos'

nCase, inputList = parseInputData(problem, s_input, s_id)
result = []
sol = 11

for i in range(nCase):
	result.append("Case #%d: %s\n" %(i+1, solve_chaos(inputList[3*i :  3*i + 3])))
	
writeOutput(result, problem, s_input, s_id)



		




		

