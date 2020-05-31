import os
import csv
import re
import string

path=os.path.join('Resources','PyParagraph_raw_data_paragraph_1.txt')  #Change the text file name if necessary.

SentenceList=[]
WordList=[]
LetterList=[]
Letter_Count=0
with open(path,'r') as datafile:
    paragraph=datafile.read()
    Sentences = re.split("(?<=[.!?]) +", paragraph)
    for sentence in Sentences:
        SentenceList.append(sentence)
        Words=sentence.split(" ")
        for word in Words:
            WordList.append(word)
            for letter in word:
                LetterList.append(letter)

for i in range(len(LetterList)):
    if LetterList[i].isalpha():         #Letter_Count will add one only if it is alphabet. So, ",", ".", "-", and "'" will not be counted.
        Letter_Count+=1

Average_Letter_Count=round((Letter_Count/len(WordList)),1)
Average_Sentence_Length=round((len(WordList)/len(SentenceList)),1)
print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {len(WordList)}")
print(f"Approximate Sentence Count: {len(SentenceList)}")
print(f"Average Letter Count: {Average_Letter_Count}")
print(f"Average Sentence Length: {Average_Sentence_Length}")