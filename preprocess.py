#!/usr/bin/python3
import sys, getopt
import dataset_builder as dsb
import feature_extraction as fe

def print_help():
    print("\t--fs:\t\tFeature Set. 1 for BoW, 2 word2vec")
    print("\t--ds:\t\t1 Concat, 2 for one question per line")
    print("\t-f:\t\tOnly feature extraction")
    print("\t--sample:\t\t<sample size>")

def main(argv):
    f = False
    fs = ''
    ds = ''
    sample_size = 0
    method = None
    try:
        opts, args = getopt.getopt(argv, "hf", ["sample=", "fs=", "ds="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt == '--ds':
            ds = arg
        elif opt == '--sample':
            sample_size = int(arg)
        elif opt == '--fs':
            fs = arg
        elif opt == '-f':
            f = True

    if ds == '1' and not f:
        dsb.generate_concat(sample_size)
    elif ds == '2' and not f:
        dsb.generate_one_question_per_line(sample_size)

    ds = 1 if ds == '' else ds
    if fs == '1':
        fe.bag_of_words(int(ds))
    elif ds and fs == '2':
        fe.word2vec(int(ds))



if __name__ == "__main__":
   main(sys.argv[1:])
