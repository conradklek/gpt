"""
Tool for converting PDF files to text.
"""
import PyPDF2


def pdf_to_text(pdf_path):
    """
    Converts a PDF file to text.

    Parameters:
    - pdf_path: The local path to the PDF file.

    Returns:
    A string containing the text extracted from the PDF.
    """
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


tools = [
    {
        "type": "function",
        "function": {
            "name": "pdf_to_text",
            "description": "Converts a PDF file to text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "pdf_path": {
                        "type": "string",
                        "description": "The local path to the PDF file."
                    }
                },
                "required": ["pdf_path"]
            }
        }
    }
]

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(pdf_to_text(sys.argv[1]))
    else:
        print("No PDF path provided. Please run the script with a PDF path as an argument.")
