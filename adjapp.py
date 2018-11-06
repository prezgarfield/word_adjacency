import nltk
from nltk import tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
import csv


def hello(t):
    print(t)

def removePunct(words):
    stops = [',', '.', "'", 's', ':', '!', '?', '(', ')', ';']
    words_clean = []
    for w in words:
        if w not in stops:
            words_clean.append(w)
    return words_clean

def lowerList(words):
    words = (map(lambda x: x.lower(), words))
    return words

def createNodes(words, nodesfile):
    csv_nodes = open(nodesfile, 'w', newline='')
    csv_writer_nodes = csv.writer(csv_nodes)
    csv_writer_nodes.writerow(['Id', 'tag'])

    for w in words:
        csv_writer_nodes.writerow(w)

def getRawText(file, nodesfile, edgesfile):
    t = open(file)
    raw = t.read()
    words = nltk.word_tokenize(raw)
    words = lowerList(words)
    words = removePunct(words)

    #run bigrams before making changing words to unique list
    bigrams = ngrams(words, 2)
    bigrams_l = list(bigrams)

    nodes = list(set(words))
    createNodes(nltk.pos_tag(nodes), nodesfile)

    csv_edges = open(edgesfile, 'w', newline='')
    csv_writer_edge = csv.writer(csv_edges)
    csv_writer_edge.writerow(['Source', 'Target'])
    i = 0
    for bg in bigrams_l:
        csv_writer_edge.writerow(bg)
    # while i < len(bigrams) - 1:
    #     csv_writer_edge.writerow([words[i], words[i+1]])
    #     i+=1
    return bigrams_l



if __name__ == '__main__':
    hello("Working on it...")
    # print(getRawText('illuminations_para1.txt'))
    print(getRawText('knausgaard_short.txt', 'nodes_kn.csv', 'edges_kn.csv'))

