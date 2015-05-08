import math

def eqn2(l1,l2):
 match = 0
 score = 0
 for item in l1:
  if item in l2 :
    match = match + 1
 if len(l1) != 0 and len(l2) != 0 :
  score = (2*match)/(len(l1)+len(l2)+0.0)
 return score
