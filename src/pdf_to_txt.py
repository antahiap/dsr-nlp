import PyPDF2

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]  #pdf_reader.getPage(page_num)
            text += page.extract_text()

    return text

if __name__ == "__main__":
    
    ver = 'r13'
    vol = 'i'

    pdf_path = f"data/ls-dyna_manual_volume_{vol}_{ver}.pdf"
    extracted_text = pdf_to_text(pdf_path)
    
    with open(f"data/lsdyna_{vol}_{ver}.txt", "w", encoding="utf-8") as output_file:
        output_file.write(extracted_text)

    print("Text extracted and saved to output.txt")
