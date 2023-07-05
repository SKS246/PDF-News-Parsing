from PyPDF2 import PdfReader
import json

pdf_file = open("Form ADT-1-19052019_signed.pdf", 'rb')

reader = PdfReader(pdf_file)
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

data = json.dumps(text)

print(data)