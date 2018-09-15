import random

cons = ['p','t','h']
vow = ['a','o']

syll_1 = random.choice(cons)
syll_2 = random.choice(vow)

print(syll_1, syll_2)

for c in cons:
    for v in vow:
        print (c+v)
        
nouns = ['ПИЛЯ', 'АЛИСА']
verbs = ['ДЕЛАЛА', 'УБИВАЛА']
adjectives = ['прекрасная','ужасная']

for A in adjectives:
    for S in nouns:
        for P in verbs:
            for A in adjectives:
                for O in nouns:
                    print (A + ' ' + S + ' ' + P + ' ' + ' ' + O)

def mean(vals):
    if len(vals) > 0:
        return float(sum(vals))/len(vals)
    else:
        print ("CBD")

def main():
    print (mean([1,2,3]))
    



