import nltk as n
string = '''
At Waterloo we were fortunate in catching a train for Leatherhead, where we hired a trap at the station inn and drove for four or five miles through the lovely Surrey lanes. 
It was a perfect day, with a bright sun and a few fleecy clouds in the heavens. 
The trees and wayside hedges were just throwing out their first green shoots, and the air was full of the pleasant smell of the moist earth. To me at least there was a strange contrast between the sweet promise of the spring and this sinister quest upon which we were engaged. 
My companion sat in the front of the trap, his arms folded, his hat pulled down over his eyes, and his chin sunk upon his breast, buried in the deepest thought. 
Suddenly, however, he started, tapped me on the shoulder, and pointed over the meadows.
'''

string=string.lower()
print string

word_t=n.tokenize.word_tokenize(string)
sent_t=n.tokenize.sent_tokenize(string)

print word_t

print sent_t

from nltk.corpus import RegexpTokenizer as rToken

token= rToken(r'\w+')
tokens = token.tokenize(string)

print tokens

tokens = [tok.lower() for tok in tokens]

from nltk.corpus import stopwords
stop = stopwords.words('english')

tokens = [token for token in tokens if token not in stop]
print tokens

tokens = [n.SnowballStemmer(language='english').stem(token) for token in tokens]

print tokens

for ngram in n.ngrams(tokens,2):
    print ngram

f=n.FreqDist(n.ngrams(tokens,2))
print f.most_common(10)

raw_text = open("C:\Users\Phanindhar\Downloads\\shakespeare-macbeth.txt",'r').read()
tokens1 = n.tokenize.word_tokenize(raw_text)
print len(tokens1)

from nltk.corpus import RegexpTokenizer as rToken
tokens2 =rToken(r'\w+').tokenize(raw_text)
print len(tokens2)
f=n.FreqDist(n.ngrams(tokens2,1))
print len(f)
print len(set(tokens2))

wordLen = map(len , tokens)
print sum(wordLen)/len(wordLen)

#unigram model

text = open("C:\Users\Phanindhar\Downloads\\shakespeare-macbeth.txt",'r').read()
tokens = n.RegexpTokenizer(r'\w+').tokenize(text.lower())
f1=n.FreqDist(n.ngrams(tokens,1))
sum= float(sum(f1.values()))

for keys in f1:
    f1[keys]/=sum
print f1.most_common(10)