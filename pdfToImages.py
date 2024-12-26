from pdf2image import convert_from_path
from pdf2image.exceptions import PDFPageCountError

pdf_path = "1934 - Ирисова диагноза. М. Мадаус.pdf"
poppler_path = "C:\\Program Files\\poppler-24.08.0\\Library\\bin"

# Convert PDF to images
try:
    images = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)
    for i, image in enumerate(images):
        image.save(f'book/page_{i + 1}.png', 'PNG')
    print("PDF successfully converted to images.")
except PDFPageCountError as e:
    print("Unable to get page count. Check Poppler installation or the PDF file.")
except Exception as e:
    print("An error occurred:", e)