import PyPDF2
import sys

inputs = sys.argv[2:]


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(sys.argv[1])


pdf_merger(inputs)
