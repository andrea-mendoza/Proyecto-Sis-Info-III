import nltk
import string
import numpy as np
import pandas as pd
import collections
import math
import os
from bs4 import BeautifulSoup
import re
from nltk.stem import WordNetLemmatizer


def clean_markups(comment):
    soup = BeautifulSoup(comment, "html.parser")
    comment = soup.get_text()
    return comment

def clean_special_characters(comment):
    comment = re.sub('\[[^]]*\]', ' ', comment)
    comment = re.sub('[^a-zA-Z]', ' ', comment)
    return comment

def clean_stop_words(comment):
    english_stop_words = set( nltk.corpus.stopwords.words('english') + list(string.punctuation))
    comment = [word for word in comment if not word in english_stop_words]
    return comment

def clean_review(comment):
    comment = clean_markups(comment)
    comment = clean_special_characters(comment)
    return comment

def tokenize(comment):
    comment = comment.split()
    return comment

def get_clean_text(comment):
    comment = clean_review(comment)
    comment = comment.lower()
    comment = tokenize(comment)
    comment = clean_stop_words(comment)

    lem = WordNetLemmatizer()
    comment = [lem.lemmatize(word) for word in comment]
    
    comment = ' '.join(comment)
    corpus = comment
    return corpus