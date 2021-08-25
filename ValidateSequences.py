# Author: Shubham Tiwari
# Difficulty: Easy

def isValidSubsequence(array, sequence):
    
	j = 0
	
	if len(array) < len(sequence):
		return False
	
	for i in array:
		if (i == sequence[j]):
			j += 1
		
		if (j == len(sequence)):
			return True

  return False