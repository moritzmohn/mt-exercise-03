#! /bin/bash

scripts=$(dirname "$0")
base=$(realpath $scripts/..)

models=$base/models
data=$base/data
tools=$base/tools
results=$base/results

mkdir -p $models
mkdir -p $results

num_threads=4
device=""

SECONDS=0

#set dropout to 0, 0.2, 0.4, 0.6, 0.8
#set model name to model0.pt, model02.pt, model04.pt, ...

(cd $tools/pytorch-examples/word_language_model &&
    CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python main.py --data $data/doyle \
        --epochs 40 \
        --log-interval 100 \
        --emsize 200 --nhid 200 --dropout 0.8 --tied \
        --save $models/model08.pt \
	--log_file $results/dropout08.log
)

echo "time taken:"
echo "$SECONDS seconds"
