from sklearn.feature_extraction.text import TfidfVectorizer
from time import time

data = '''Time flies like an arrow
Fruit flies like a banana,
Sam sat on the cat
The cat is white.'''
t0 = time()
dataset = data.split('\n')

# print "done in time :"%(time()-t0)

tFerq = TfidfVectorizer(ngram_range=(1, 3))
tf = tFerq.fit_transform(dataset)
print tf
dense = tf.todense()

dense.shape
print len(dense[0].tolist()[0])
feature_names = tFerq.get_feature_names()

print len(feature_names), feature_names

article = dense[0].tolist()[0]
print article
phrases_scrore = [pair for pair in zip(range(0, len(article)), article) if pair[1] > 0]

print phrases_scrore

top_features = sorted(phrases_scrore, reverse=True)[:4]
top_features1 = [(feature_names[i[0]], i[1]) for i in top_features]
print top_features1

new = 'Time flies like sam'

tf =tFerq.transform([new])

from sklearn.metrics.pairwise import cosine_similarity

alp = map(lambda x: cosine_similarity(tf, x), dense)

print alp

with(open("C:\Users\Phanindhar\Downloads\\ende_cleaned.json","r")) as f:
    corpus = f.readlines()
print len(corpus)
label1= [0]*90
label2= [1]*90
labels = label1+label2
tFerq= TfidfVectorizer(ngram_range=(1,3), max_features=10000, stop_words='english')
tf1=tFerq.fit_transform(corpus)

dense= tf1.todense()