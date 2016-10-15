# -*- coding: utf-8 -*-

import os

import nltk
from goose import Goose
from stemming.porter2 import stem
import unicodedata
import re


def cleanhtml(raw_html):
  cleanr =re.compile('<.*?>')
  cleantext = re.sub(cleanr,'', raw_html)
  return cleantext


def textCleanser(text):
    #nltk.download()
    from nltk.corpus import stopwords
    from nltk.tokenize import wordpunct_tokenize
    from nltk.stem.porter import PorterStemmer

    porter = PorterStemmer()

    stops = set(stopwords.words('english'))
    stops.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
    #words = [w for w in text.lower().split() if w not in stops]
    text = text.lower()
    # words = [w for w in wordpunct_tokenize(text) if w not in stops]
    # text_stop_cleaned = " ".join(words)

    # raw string bytes to unicode
    text = text.decode('utf-8', 'ignore')
    words = [porter.stem(i.lower()) for i in wordpunct_tokenize(text) if i.lower() not in stops]
    #words = [i.lower() for i in wordpunct_tokenize(text) if i.lower() not in stops]
    text = " ".join(words)

    print(type(text))
    return text


def input_format(text_dir, labels, newDict):
    with open('spam_v2.txt', 'w') as spam_file:
        for subdir, dirs, files in os.walk(text_dir):
            for file in sorted(files):
                if file.endswith('eml'):
                    id = file.split('_')[1].split('.')[0]
                    label = newDict.get(int(id))
                    if label == '0':
                        label = -1
                    else:
                        label = 1
                    with open(text_dir + '/' + file, 'r') as emlFile:
                        content = emlFile.readlines()

                        # clean html body
                        #print file[file.rfind('_')+1:file.rfind('.')]
                        if file[file.rfind('_')+1:file.rfind('.')] in ['html']:
                            print file
                            extractor = Goose()
                            article = extractor.extract(raw_html="".join(content))
                            text = article.cleaned_text
                            #text_html_phase = text.encode('ascii', 'ignore')
                            #text_html_phase = text.encode()
                        else:
                            #text_html_phase = unicodedata.normalize('NFKD', content).encode('ascii', 'ignore')
                            text_html_phase = " ".join(content)
                            #text_html_phase = text_html_phase.encode()
                            #text_html_phase = text_html_phase.encode('ascii', 'ignore')

                        # remove stopwords and do stemming
                        document = textCleanser(text_html_phase)
                        # unicode to string bytes
                        document = document.encode('utf-8', 'ignore')
                        print(type(document))

                        document = cleanhtml(document)
                        # re.sub('[^A-Za-z0-9]+', '', mystring)
                        document = re.sub('[^A-Za-z]+', ' ', document)

                        spam_file.write(file + ' | ' + str(label) + ' | ' + document + "\n")


def input_format_v1(text_dir, labels, newDict):
    with open('spam_v3.txt', 'w') as spam_file:
        for subdir, dirs, files in os.walk(text_dir):
            for file in sorted(files):
                if file.endswith('eml'):
                    id = file.split('_')[1].split('.')[0]
                    label = newDict.get(int(id))
                    if label == '0':
                        label = -1
                    else:
                        label = 1
                    with open(text_dir + '/' + file, 'r') as emlFile:
                        content = emlFile.readlines()

                        text_html_phase = " ".join(content)

                        # remove stopwords and do stemming
                        document = textCleanser(text_html_phase)
                        # unicode to string bytes
                        document = document.encode('utf-8', 'ignore')
                        print(type(document))

                        document = cleanhtml(document)
                        # re.sub('[^A-Za-z0-9]+', '', mystring)
                        document = re.sub('[^A-Za-z]+', ' ', document)

                        spam_file.write(str(label) + ' | ' + document + "\n")


def cleanup_test(text_dir):
    with open('kaggle_test_set_1827.txt', 'w') as spam_file:
        for subdir, dirs, files in os.walk(text_dir):
            for file in sorted(files):
                if file.endswith('eml'):
                    with open(text_dir + '/' + file, 'r') as emlFile:
                        content = emlFile.readlines()

                        text_html_phase = " ".join(content)

                        # remove stopwords and do stemming
                        document = textCleanser(text_html_phase)
                        # unicode to string bytes
                        document = document.encode('utf-8', 'ignore')
                        print(type(document))

                        document = cleanhtml(document)
                        # re.sub('[^A-Za-z0-9]+', '', mystring)
                        document = re.sub('[^A-Za-z]+', ' ', document)

                        spam_file.write('1' + ' | ' + document + "\n")


def labels_to_dict():
    newDict = {}
    with open('/Users/manpreet.singh/Sandbox/codehub/github/machinelearning/BeingDataScientist/vowpal_wabbit/vw_apps/spam/dataset/spam-mail.tr.label', 'r') as f:
        next(f)
        for line in f:
            splitLine = line.rstrip("\n").split(',')
            newDict[int(splitLine[0])] = splitLine[1]
    return newDict


if __name__ == '__main__':
    newDict = labels_to_dict()
    #input_format_v1('/Users/manpreet.singh/Sandbox/codehub/github/machinelearning/BeingDataScientist/vowpal_wabbit/vw_apps/spam/dataset/emails_tr', '/Users/manpreet.singh/Sandbox/codehub/github/machinelearning/BeingDataScientist/vowpal_wabbit/vw_apps/spam/dataset/spam-mail.tr.label', newDict)
    cleanup_test('/Users/manpreet.singh/Sandbox/codehub/github/machinelearning/BeingDataScientist/vowpal_wabbit/vw_apps/spam/dataset/emails_tt')
