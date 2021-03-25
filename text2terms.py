# coding:utf-8
import glob
import os
import shutil
from io import StringIO
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from numpy import dot
from numpy.linalg import norm

def text2terms() :
    fileList = glob.glob("docs/*")
    os.makedirs('docs2')
    for fullFile in fileList:
        file = open(fullFile, 'rt')
        i = 1
        while i <= 134 :
        # while True:
            contents = file.readline()
            if not contents: break
            print(contents)
            inputtext = open("input.txt",'w')
            inputtext.write(contents)
            inputtext.close()
            os.system("index2018.exe input.txt %d.txt" %i)
            makefilename = "%d.txt"%i
            src = "./"
            dir = "./docs2/"
            shutil.move(src+makefilename , dir+makefilename)
            i = i+1
text2terms()

def terms2oneLine():
    os.makedirs('docs3')
    fileList = glob.glob("docs2/*")
    print(fileList)
    for fullFile in fileList:
        textfile = open(fullFile, 'r')
        text = ""
        while True:
            try:
                line = textfile.readline()
            except UnicodeDecodeError:
                continue
            print(text)
            if not line: break
            text += line
        likeFile = StringIO(text)
        fileLines = likeFile.readlines()
        word = []
        for line in fileLines:
            word += line.split()
        newfile = open(os.path.basename(fullFile), 'w')
        newfile.write(str(word))
        newfile.close()
        makefilename = os.path.basename(fullFile)
        src = "./"
        dir = "./docs3/"
        shutil.move(src + makefilename, dir + makefilename)

terms2oneLine()

#
def files2array():
    fileList = glob.glob("docs3/*")
    corpus=[]
    for fullFile in fileList:
        file = open(fullFile, "r")
        line = file.readline()
        corpus.append(line)
    return corpus

corpus = files2array()
print(corpus)
# #
def buildDocTermMatrix():
    Tf = TfidfVectorizer()
    document_term_matrix = Tf.fit_transform(corpus).toarray()
    print(document_term_matrix)
    # print(vector.vocabulary_)
    return document_term_matrix

document_term_matrix = buildDocTermMatrix()



def cos_sim(A, B):
    return dot(A, B) / (norm(A) * norm(B))

def buildSimilarityMatrix():
    similarity_matrix = [[0 for col in range(len(document_term_matrix))] for row in range(len(document_term_matrix))]
    for i in range(len(document_term_matrix)):
        for j in range(len(document_term_matrix)):
            similarity_matrix[i][j] = round(cos_sim(document_term_matrix[i],document_term_matrix[j]),5)

    print("##########cosine similarity########")
    for i in range(len(document_term_matrix)):
        print(similarity_matrix[i])

    return similarity_matrix

similarity_matrix = buildSimilarityMatrix()
print("(",len(similarity_matrix),len(similarity_matrix[0]),")")

# def putSimMatrix() :
#     str = '(' + repr(len(similarity_matrix)) +' '+ repr(len(similarity_matrix[0])) + ')'
#     for i in range(len(similarity_matrix)):
#         str += "\n"
#         for j in range(len(similarity_matrix)):
#             str += repr(similarity_matrix[i][j])+' '
#     newfile = open("sim-matrix.txt", 'w')
#     newfile.write(str)
#     newfile.close()
# putSimMatrix()
#
# def printDocPairs(n):
#     print("유사도가 가장 높은 상위%s개"%n)
#     k=0
#     while k<n:
#         breaker = False
#         maxi = max(map(max, similarity_matrix))
#         for i in range(len(similarity_matrix)):
#             for j in range(len(similarity_matrix)):
#                 if(maxi == similarity_matrix[i][j]):
#                     a = i
#                     b = j
#                     breaker = True
#                     break
#             if breaker == True:
#                 break
#         print("문서번호",a+1,b+1,"유사도값:",maxi)
#         similarity_matrix[a][b] = -1
#         k+=1
#
# printDocPairs(1400)