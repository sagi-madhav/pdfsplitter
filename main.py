import PyPDF2

def split_pdf(input_pdf_path, pages_per_split):
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as input_pdf_file:
        reader = PyPDF2.PdfReader(input_pdf_file)
        total_pages = len(reader.pages)

        # Split the PDF into smaller PDFs
        for part_number in range(1, (total_pages // pages_per_split) + 2):
            writer = PyPDF2.PdfWriter()
            start_page = (part_number - 1) * pages_per_split
            
            # Add the pages for the current split
            for page in range(start_page, min(start_page + pages_per_split, total_pages)):
                writer.add_page(reader.pages[page])

            # Create the output PDF filename
            output_pdf_path = f"pdf{part_number}.pdf"
            
            # Write the split PDF to a file
            with open(output_pdf_path, 'wb') as output_pdf_file:
                writer.write(output_pdf_file)

            print(f"Created: {output_pdf_path}")

# Usage
input_pdf = 'crackingcodeinterview.pdf'  # Replace with your PDF file path
split_pdf(input_pdf, 10)  # Splits the PDF into parts of 10 pages each
