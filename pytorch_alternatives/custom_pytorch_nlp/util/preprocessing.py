from __future__ import division

# Python Built-Ins:
import os
import re
import subprocess
import shutil
import functools
import operator
from collections import Counter
import tarfile
import zipfile

# External Dependencies:
import numpy as np
import torchtext
from sklearn import preprocessing

def to_categorical(y, num_classes):
    """ 1-hot encodes a tensor """
    return np.eye(num_classes, dtype='float32')[y]

def download_dataset():
    os.makedirs("data", exist_ok=True)
    print("Downloading data...")
    subprocess.call(
        ["aws s3 cp s3://fast-ai-nlp/ag_news_csv.tgz data/ag_news_csv.tgz --no-sign-request"],
        shell=True,
    )
    with tarfile.open("data/ag_news_csv.tgz", 'r:gz') as tar:
        print("Unzipping...")
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar, path="data/")
        tar.close()
    try:
        # Clean up the noise in the folder, don't care too much if it fails:
        shutil.rmtree("data/__MACOSX/")
    except:
        pass
    print("Saved to data/ folder")

def dummy_encode_labels(df,label):
    encoder = preprocessing.LabelEncoder()
    encoded_y=encoder.fit_transform(df[label].values)
    # convert integers to dummy variables (i.e. one hot encoded)
    dummy_y = to_categorical(encoded_y, len(encoder.classes_))
    return dummy_y, encoder.classes_

def tokenize_and_pad_docs(df,columns):
    docs = df[columns].values
    # pad documents to a max length of 10 words
    max_length = 40
    
    t = torchtext.data.Field(
      lower       = True,
      tokenize   = "basic_english",
      fix_length  = max_length
    )
    docs = list(map(t.preprocess, docs))
    padded_docs = t.pad(docs)
    t.build_vocab(padded_docs)
    numericalized_docs = []
    for d in padded_docs:
        temp = []
        for c in d:
            temp.append(t.vocab.stoi[c])
        numericalized_docs.append(temp)
    return np.array(numericalized_docs), t

def get_word_embeddings(t, folder):
    os.makedirs(folder, exist_ok=True)
    if os.path.isfile(f"{folder}/glove.6B.100d.txt"):
        print("Using existing embeddings file")
    else:
        print("Downloading Glove word embeddings...")
        subprocess.call(
            [f"wget -O {folder}/glove.6B.zip http://nlp.stanford.edu/data/glove.6B.zip"],
            shell=True,
        )
        print("Unzipping...")
        with zipfile.ZipFile(f"{folder}/glove.6B.zip", "r") as zip_ref:
            print("Unzipping...")
            zip_ref.extractall(folder)

        try:
            # Remove unnecessary files, don't mind too much if fails:
            for name in ["glove.6B.200d.txt", "glove.6B.50d.txt", "glove.6B.300d.txt", "glove.6B.zip"]:
                os.remove(os.path.join(folder, name))
        except:
            pass

    print("Loading into memory...")
    # load the whole embedding into memory
    embeddings_index = dict()
    with open(f"{folder}/glove.6B.100d.txt", "r") as f:
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype="float32")
            embeddings_index[word] = coefs
    vocab_size = len(embeddings_index)
    print(f"Loaded {vocab_size} word vectors.")

    # create a weight matrix for words in training docs
    embedding_matrix = np.zeros((vocab_size, 100))
    i = 0
    for word in t.vocab.itos:
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector
        i = i+1

    return embedding_matrix
