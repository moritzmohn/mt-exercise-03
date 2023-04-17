#! /bin/bash

scripts=$(dirname "$0")
base=$scripts/..

data=$base/data

mkdir -p $data

tools=$base/tools

# link default training data for easier access

mkdir -p $data/wikitext-2

for corpus in train valid test; do
    absolute_path=$(realpath $tools/pytorch-examples/word_language_model/data/wikitext-2/$corpus.txt)
    ln -snf $absolute_path $data/wikitext-2/$corpus.txt
done

# download a different interesting data set!

mkdir -p $data/doyle

mkdir -p $data/doyle/raw

wget https://www.gutenberg.org/files/1661/1661-0.txt
mv 1661-0.txt $data/doyle/raw/adventures.txt

# preprocess slightly

cat $data/doyle/raw/adventures.txt | python $base/scripts/preprocess_raw.py > $data/doyle/raw/adventures.cleaned.txt

# tokenize, fix vocabulary upper bound

cat $data/doyle/raw/adventures.cleaned.txt | python $base/scripts/preprocess.py --vocab-size 5000 --tokenize --lang "en" --sent-tokenize > \
    $data/doyle/raw/adventures.preprocessed.txt

# split into train, valid and test

head -n 420 $data/doyle/raw/adventures.preprocessed.txt | tail -n 400 > $data/doyle/valid.txt
head -n 840 $data/doyle/raw/adventures.preprocessed.txt | tail -n 400 > $data/doyle/test.txt
tail -n 3500 $data/doyle/raw/adventures.preprocessed.txt | head -n 3000 > $data/doyle/train.txt
