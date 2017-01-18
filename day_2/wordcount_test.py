import unittest
words="olly olly in come free free"
wordlist=words.split()

def wordfreq(wordlist):
freq=(wordlist.count(w) for w in wordlist)
dictionary=dict(zip(wordlist,freq))
d=""
for i in dictionary :
a=i
b=dictionary[i]
c=a+":"+ str =(dictionary[i])
d=d+c+'\n'
return d
print(wordfreq(wordlist)