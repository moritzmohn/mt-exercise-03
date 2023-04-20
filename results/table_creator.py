import matplotlib.pyplot as plt
import argparse
import pandas as pd


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log_file0", type=str, help="file to process", required=True)
    parser.add_argument("--log_file02", type=str, help="file to process", required=True)
    parser.add_argument("--log_file04", type=str, help="file to process", required=True)
    parser.add_argument("--log_file06", type=str, help="file to process", required=True)
    parser.add_argument("--log_file08", type=str, help="file to process", required=True)
    args = parser.parse_args()
    return args


def get_perplexities(input_file):
    perplexities_train = []
    perplexities_val = []
    perplexities_end = []
    file = open(input_file, 'r')
    for index, line in enumerate(file.readlines()):
        if index == 80:
            line_list = line.split()
            perplexities_end.append(line_list[1])
        elif index%2 == 0:
            line_list = line.split()
            perplexities_train.append(line_list[1])
        else:
            line_list = line.split()
            perplexities_val.append(line_list[1])
    file.close()
    perplexities_train = [float(i) for i in perplexities_train]
    perplexities_val = [float(i) for i in perplexities_val]
    perplexities_end = [float(i) for i in perplexities_end]
    return perplexities_train, perplexities_val, perplexities_end
    
    
def get_table(perp1, perp2, perp3, perp4, perp5):
    df = pd.DataFrame({'Dropout 0': perp1, 'Dropout 0.2': perp2, 'Dropout 0.4': perp3, 'Dropout 0.6': perp4, 'Dropout 0.8': perp5})
    return df
    
def get_linechart(table):
    plt.plot(table['Dropout 0'], label='Dropout 0')
    plt.plot(table['Dropout 0.2'], label='Dropout 0.2')
    plt.plot(table['Dropout 0.4'], label='Dropout 0.4')
    plt.plot(table['Dropout 0.6'], label='Dropout 0.6')
    plt.plot(table['Dropout 0.8'], label='Dropout 0.8')
    plt.legend()
    return plt
    
def main():
    args = parse_arguments()
    train0, val0, end0 = get_perplexities(args.log_file0)
    train02, val02, end02 = get_perplexities(args.log_file02)
    train04, val04, end04 = get_perplexities(args.log_file04)
    train06, val06, end06 = get_perplexities(args.log_file06)
    train08, val08, end08 = get_perplexities(args.log_file08)
    train_table = get_table(train0, train02, train04, train06, train08)
    val_table = get_table(val0, val02, val04, val06, val08)
    end_table = get_table(end0, end02, end04, end06, end08)
    train_table.to_csv('train.csv', index = True)
    val_table.to_csv('val.csv', index = True)
    end_table.to_csv('end.csv', index = True)
    plt = get_linechart(train_table)
    plt.savefig('train_plot.png')
    plt.clf()
    val_plot = get_linechart(val_table)
    val_plot.savefig('val_plot.png')
    
    
if __name__ == '__main__':
    main()        
