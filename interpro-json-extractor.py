#!/usr/bin/env python3

import sys, argparse, json

parser = argparse.ArgumentParser(description="""

DESCRIPTION

    v0.0.0-dirty-20220721
    
    Takes in JSON output of interproscan with some options.

    Outputs individual JSON files for all or targeted genes.
    
    

    Why? / Use case?
    EBI has a really cool viewer for the InterProScan JSON output here:
    https://www.ebi.ac.uk/interpro/result/InterProScan/#table

    Using InterProScan on a protein FASTA file corresponding to all genes in a genome leads to a massive JSON file (e.g. many GB).

    It appears that the web-service does not like those huge files.

    So this is for making smaller files of subsets of the larger one...


    Options:
    1. One JSON output file for given protein name....

    FUTURE:
    2. One JSON output file per listed protein sequence.
    3. One JSON output file that includes all listed protein sequences.

    None of this is implemented yet.


    Caveats:
    This is a quick-and-dirty "dumb" script.
    
    It expects that the first 3 lines of the input JSON will be something like:
    {
     "interproscan-version": "5.56-89.0",
    "results": [ {


    
    
    """, formatter_class= argparse.RawTextHelpFormatter)

parser.add_argument('-i', "--inputjson",
                   type= str, default="-",
                   help='''Input JSON file.''')


parser.add_argument('--name', '-p',
                   type= str, default=False,
                    help='''Target protein name to extract. ''')
                   #help='''Comma-separated input list of protein names to extract. ''')

##parser.add_argument('--namesfile', '-n',
##                   type= str, default=False,
##                   help='''File with protein names to extract. One name per line.''')

##parser.add_argument('-a', '--all', action='store_true', default=False,
##                    help='''Not recommended. Extract all entries into their own JSON files. Not compatible with -p, -n, or -1. ''')
##
##parser.add_argument('-1', '--single_json_output', action='store_true', default=False,
##                    help='''Combine all ectracted protein entries into single JSON output.''')

args = parser.parse_args()



#assert not (args.names and args.all)
#assert not (args.namesfile and args.all)
#assert not (args.single_json_output and args.all)

##############################################################################
''' EXECUTE '''
##############################################################################



tail = ['} ]\n', '}']
with open(args.inputjson) as f:
    header = []
    for i in range(3):
        header.append(f.readline())
    newentry = []
    found = False
    while not found:
        newline = f.readline()
        if newline == "},{\n" or newline == "}\n" or newline == "}" or newline == "} ]\n":
            for e in newentry:
                if args.name in e:
                    found = True
                    break
            if found:
                break
            newentry = []
        else:
            newentry.append(newline)


if found:
    print(''.join(header + newentry + tail))









