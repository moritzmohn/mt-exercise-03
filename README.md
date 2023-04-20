# MT Exercise 3: Pytorch RNN Language Models

This repo shows how to train neural language models using [Pytorch example code](https://github.com/pytorch/examples/tree/master/word_language_model). Thanks to Emma van den Bold, the original author of these scripts. 

# Requirements

- This only works on a Unix-like system, with bash.
- Python 3 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

# Steps

Clone this repository in the desired place:

    git clone https://github.com/moritz-steiner/mt-exercise-03
    cd mt-exercise-03

Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Download and install required software:

    ./scripts/install_packages.sh

Download and preprocess data:

    ./scripts/download_data.sh

Train a model:

    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved.

Generate (sample) some text from a trained model with:

    ./scripts/generate.sh

# Changed files part 1

- I changed the download_data script to download the adventures of Sherlock Holmes instead of the Tales and also adapted the splitting of the data a bit (leaving out 500 last lines to make sure that all training data is part of the book)
- The train script has just the minor change that the file path for the data is changed, the hyperparameters are still the same, also I renamed it to train_original.
- In the generate script also only the file path of the data was changed.

# Changed files part 2

- I adapted the train script everytime before I ran it to train a model with a certain dropout. More precisely I adapted always the name of the model (e.g. model02.pt for dropout 0.2), set the dropout e.g. to 0.2 and set the log_file flag e.g. to results/dropout02.log where the log files should be saved.
- In the main.py file I added a log_file flag to the command line arguments which takes the path where the log file should be saved. I wrote to this file the train/val/test perplexity only if a path was given / the flag was given. I saved the log files in the results folder.
- I added a table_creator.py file in the results folder which creates the tables and plots. It takes as input the log files. Example call (from the results folder): python3 table_creator.py --log_file0 dropout0.log --log_file02 dropout02.log --log_file04 dropout04.log --logfile06 dropout06.log --logfile08 dropout08.log
- All the tables and plots are also saved in the results folder.
- To output the samples with models model08.pt and model04.pt I adapted the script generate.sh.
- I also added a copy of main.py to the results folder.

