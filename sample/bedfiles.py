import os
import sys
import argparse

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--indir',help='strings data about use',required=True)
    parser.add_argument('-o', '--outdir',help= 'strings data for output',required=True)
    parser.add_argument('-s','--suffix',help='file ending',required=True)

    args = parser.parse_args()
    indir = args.indir
    outdir= args.outdir
    suffix= args.suffix

    return indir, outdir, suffix


outdir = '/Users/Irina/Desktop/textfiles'

def filepaths_bedgraph(indir='.',outdir= '.', suffix='_lines.sam'):
    """

    :param indir: input directory- User provides the filepath for accessing the files
    :param outdir: output directory- User provides the filepath for where the output file will be written to
    :param suffix: suffix- User provides the suffix of the file ending, for example if the file ends in "_lines.sam" the
                    suffix would be "_lines.sam".
    :return:
    """
    for root, dirs, files in os.walk(indir):
        sys.stdout.write('%s\t%s located\n' % (files,dirs))
        for file_name in files:
            sys.stdout.write('%s\n' % file_name)
            if file_name.endswith(suffix):
                write_to_file(os.path.join(root, file_name), outdir, suffix)

def get_file_from_path(path):
    split = path.split('/')
    return split[-1]


def write_to_file(path, outdir, suffix):
    filename = get_file_from_path(path)[:-len(suffix)]
    myfile = '%s/%s.txt' % (outdir, filename)
    with open(myfile, 'w') as outfile:
        outfile.write('track name=mouse description="50shades_of_GRAY" useScore=1\n')
        with open(path, 'r') as input_file:
            for line in input_file:
                clean_line = line.lstrip().rstrip()
                parts = clean_line.split()
                doench = parts[-2].split(':')[-1]
                specificity = parts[-1].split(':')[-1]
                score1=float(specificity)
                score2=float(doench)
                input_score=(score1*.75*1000)+(score2*0.25*1000)
                inputscore=str(input_score)
                b= 23
                if parts[1]== '16':
                    parts[4]= '-'
                    new_parts=int(parts[3])
                    starts=new_parts-b
                    start=str(starts)
                    ends= new_parts
                    end=str(ends)
                else:
                    parts_new=int(parts[3])
                    start=str(parts_new)
                    ends_1=parts_new+23
                    end=str(ends_1)
                    parts[4]= '+'
                #outfile.write('%s\t%s\t%s\t%s\n' % (parts[2], start, end, '%s_%s_%s' % (parts[0],parts[4],'.')))
                outfile.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (parts[2], start, end, '%s_EFF_=_%s_SPEC_=_%s' % (parts[0],doench,specificity),inputscore,parts[4]))
    header_list(myfile)


def header_list(file):
    myfile=open(file)
    ls=[]
    for i in range(0,4):
        ls.append(myfile.readline().strip())
    print ls
    myfile.close()



def main():

    indir, outdir,suffix = arg_parser()

    filepaths_bedgraph(indir,outdir,suffix)
    """
    if len(sys.argv) < 4:
        print 'Usage: python ___ indir outdir suffix'
    else:
        filepaths_bedgraph(sys.argv[1], sys.argv[2], sys.argv[3])
    """

if __name__ == '__main__':
    main()



