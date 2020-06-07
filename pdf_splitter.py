import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter


def split_into_two(fpath, numPages):
    try:
        pdf_reader = PdfFileReader(open(fpath, mode='rb'))
    except FileNotFoundError:
        print("No such file. Check the path.")
        sys.exit()
    fname = os.path.splitext(os.path.basename(fpath))[0]

    try:
        assert numPages < pdf_reader.numPages
        pdf1_writer = PdfFileWriter()
        pdf2_writer = PdfFileWriter()

        for page in range(numPages):
            pdf1_writer.addPage(pdf_reader.getPage(page))
        for page in range(numPages, pdf_reader.getNumPages()):
            pdf2_writer.addPage(pdf_reader.getPage(page))

        with open("PDFS/"+fname+"_part1.pdf", 'wb') as file1:
            pdf1_writer.write(file1)
        with open("PDFS/"+fname+"_part2.pdf", 'wb') as file2:
            pdf2_writer.write(file2)

    except AssertionError:
        print("The pdf file has less pages than you want to split!")
        sys.exit()


if __name__ == "__main__":
    try:
        pdf_to_split = sys.argv[1]
        num_of_pages = int(sys.argv[2])
        split_into_two(pdf_to_split, num_of_pages)
        print("Done.")
    except IndexError:
        print('Please run the script with two arguments: [pdf name] [number of pages to split]')


