import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_name = sys.argv[1]
watermark_name = sys.argv[2]


def open_pdf(file_name):
    try:
        pdf = PdfFileReader(open(file_name, mode='rb'))
        return pdf
    except FileNotFoundError as e:
        print("Check the argument names:", e)
        sys.exit()


def write_pdf(output):
    with open("PDFS/watermarked.pdf", mode='wb') as file:
        output.write(file)
        print("Done.")


def make_watermark(pdf, watermark):
    try:
        input_pdf = open_pdf(pdf)
        wtr_pdf = open_pdf(watermark)
        wtr_page = wtr_pdf.getPage(0)

        output = PdfFileWriter()

        for i in range(input_pdf.getNumPages()):
            page = input_pdf.getPage(i)
            page.mergePage(wtr_page)
            output.addPage(page)
        return output
    except AttributeError:
        print("Check the argv names.")


if __name__ == "__main__":
    out = make_watermark(pdf_name, watermark_name)
    write_pdf(out)
