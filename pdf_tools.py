## Rotate PDF

# from PyPDF2 import PdfReader, PdfWriter
#
# in_file = PdfReader("D:/Scan.pdf")
# out_file = PdfWriter()
#
# with open("D:/Scan_out.pdf", "wb") as out:
#     page = in_file.getPage(0)
#     page.rotateClockwise(270)
#     out_file.addPage(page)
#     out_file.write(out)


## Convert PDF to image
## Must on Linux
## for Windows, download poppler https://blog.alivate.com.au/poppler-windows/
from pdf2image import convert_from_path
import os

pages = convert_from_path('D:/a.pdf', dpi=200, poppler_path='C:/poppler-0.68.0_x86/poppler-0.68.0/bin')

for i, page in enumerate(pages):
    page.save(f'D:/out_{i}.jpg', 'JPEG')
