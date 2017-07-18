__author__ = 'Irina'

#####################
#                   #
#   Introduction    #
#                   #
#####################

"""
This GUI searches a directory for file paths corresponding to the input gene name and opens the files in excel."""

#################
#               #
#   Libraries   #
#               #
#################

import os
import sys
import subprocess
from Tkinter import *
import tkMessageBox
import argparse
from PIL import ImageTk, Image



#########################
#                       #
#   Auxillary Function  #
#                       #
#########################

mapped_genes = {}
gui=Tk()
search_box= Entry(gui, bd=5)
text=Text(gui)

#############
#           #
#   Core    #
#           #
#############
def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--indir',help='strings data about use',required=True)
    parser.add_argument('-s','--suffix',help='file ending',required=True)

    args = parser.parse_args()
    indir = args.indir
    suffix= args.suffix

    return indir, suffix

#directory = '/Users/Irina/Desktop/sample'
def find_csv_filepaths(indir='.', suffix='_GuideScan_batch_output.csv'):
    files_needed = []  # list of file paths returned by this function
    # http://www.tutorialspoint.com/python/os_walk.htm
    for root, dirs, files in os.walk(indir):
        # need to look at the files found from walk()
        for filename in files:
            if filename.endswith(suffix):
                # need to include the path to a file, not just the file name.
                # http://www.tutorialspoint.com/python/os_walk.htm
                full_path_to_file = os.path.join(root, filename)
                files_needed.append(full_path_to_file)
    return files_needed



def display_file_to_gui(filepath):
    #print filepath
    if os.name == 'nt':
        filepath = filepath.lstrip('./').replace('/', '\\')
    else:
        os.system("open '" +filepath+"' -a "'/Applications/Microsoft\ Office\ 2011/Microsoft\ Excel.app'" ")

def map_genes_to_file_paths(filepaths, suffix='_GuideScan_batch_output.csv'):
    genes_to_files = {}

    for filepath in filepaths:
        if os.name == 'nt':
            filepath = filepath.replace('\\', '/')
        separated_string = filepath.split('/')
        gene_name = separated_string[-1]
        if gene_name.endswith(suffix) and len(suffix) > 0:
            gene_name = gene_name[:-len(suffix)]
        genes_to_files[gene_name] = filepath
    return genes_to_files

def validate_gene_name(gene_to_file_map):
    gene_name=search_box.get()
    multiple_genes = gene_name.split(',')  #genes have to be entered separated by a comma followed by a space
    for gene in multiple_genes:
        gene=gene.strip()
        print gene
        if gene in gene_to_file_map.keys():
             display_file_to_gui(gene_to_file_map[gene])
        else:
            tkMessageBox.showwarning('File not found',  "Couldn't find file '"
                 + gene + "' in "
                         "working directories.")



def main():
    indir,  suffix = arg_parser()

    find_csv_filepaths(indir, suffix)
if __name__ == '__main__':
    main()



    L1 = Label(gui, text="Gene Name")  # static text on screen
    L1.pack(side=LEFT)  # push it to the left
    L2 = Label(gui, text="Please enter gene name(s) separated by a comma. Example: gene1,gene2,etc.")
    L2.pack(side=TOP)
    search_box.focus_set()  # make the search box focus at program start.
    search_box.pack(side=LEFT)
    # create a button to invoke searching for a file
    B = Button(gui, text="Search",
               command=lambda: validate_gene_name(mapped_genes))
    B.pack(side=LEFT)  # pack it next to the search bar
    # create a frame where our file text will exist
    text_frame = Frame(gui)
    text_frame.pack(side=RIGHT, fill=BOTH)  # pack it to the right of the screen

    scrollbar = Scrollbar(text_frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=text.yview)
    gui.configure(background= 'aquamarine')
    img=ImageTk.PhotoImage(Image.open("/Users/Irina/Downloads/dna.gif"))
    panel = Label(gui, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")

    gui.mainloop()  # starts the main GUI window.

