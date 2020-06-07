import PyPDF2
import sys


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    count = 0
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
        count += 1
    merger.write("PDFS/super.pdf")
    merger.addBookmark("Paweł", 1)
    print(f"\nDone. {count} files merged.")


def main():
    inputs = sys.argv[1:]
    pdf_combiner(inputs)


if __name__ == '__main__':
    main()