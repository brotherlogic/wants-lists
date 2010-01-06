import os,random,sys

#Check to see if we have funds
money = float(os.popen('python scripts/money-left.py').readlines()[0])
if money < 0:
    print "Keep saving"

best_score = 0
best_name = ''

for line in os.popen('python scripts/score-list.py').readlines():
    (scorestr,name) = line.strip().split()
    score = float(scorestr)

    if score > best_score:
        best_score = score
        best_name = name

possible = []
for line in open(best_name,'r'):
    elems = line.strip().split('~')
    if len(elems) == 2:
        possible.append(elems[0] + " - " + elems[1])

random.shuffle(possible)
print possible[0],"(" + best_name + ")"
