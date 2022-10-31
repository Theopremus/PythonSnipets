#Translates a string using a key phrase using a Vigenère cypher. 
import string
#cypher matrix
key = open("key.txt", 'r')
lines = key.read().splitlines(keepends=False)
v_cypher = list(map(list, lines))

#Letters and numbers for later use.
alphaDictionary =  {'A': 0, 'B': 1,'C': 2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11, 'M':12,'N':13,'O':14,'P':15,'Q':16,
'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

def mapFunc(i):
   return alphaDictionary[i]
numbers = list(range(25))

#Get cyphertext and parse into list.
ct = list(input("Enter Cyphertext: ").upper())
#Map to indices
cttemp = map(mapFunc, ct)
ct = cttemp
#Get keyphrase
key = list (input ("Enter Key String: ").upper())
#Map to indices
keytemp = map(mapFunc, key)
key = keytemp
#Decrypt using matrix. 
for (a, b) in zip(key, ct): 
    print (v_cypher[a][b], end = "")