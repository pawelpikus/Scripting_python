import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
pdf_name = sys.argv[1]
watermark_name = sys.argv[2]

ipdf = PdfFileReader(open(pdf_name, mode='rb'))
wpdf = PdfFileReader(open(watermark_name, 'rb'))
watermark = wpdf.getPage(0)
for i in range(ipdf.getNumPages()):
    page = ipdf.getPage(i)
    page.mergePage(watermark)
    output.addPage(page)

with open("watermarked.pdf", 'wb') as file:
    output.write(file)







