
import pypdf
'''
This imports the pypdf library — a Python tool specifically built for working with PDF files. 
It lets you read, extract, and manipulate PDF content.
'''



with open('Plain_Text.pdf', 'rb') as file:
    reader = pypdf.PdfReader(file)
    for page in reader.pages:
        print(page.extract_text())
