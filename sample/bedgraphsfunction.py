__author__ = 'Irina'


import sys
outdir = '/Users/Irina/Desktop/textfiles'
filename = '/Users/Irina/Desktop/textfiles/ce11_1e4_lines.sam'

def bedgraph_tracks(filename):
        with open('%s/test_3.txt' % (outdir), 'w') as outfile:
            outfile.write('track \ntype=bedGraph \nname="BedGraph Format" \ndescription="BedGraph Format \nvisibility=full color \n')
            with open(filename, 'r') as infile:
                for line in infile:
                    clean_line = line.lstrip().rstrip()
                    parts = clean_line.split()
                    outfile.write('%s\t%s\t%s\t%s\n' % (parts[0], parts[1], parts[2], parts[3]))
                sys.stdout.write('write out written to %s\n' % ('%s/test_3.txt' % (outdir)))






########################################################################
