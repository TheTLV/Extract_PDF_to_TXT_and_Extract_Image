# Document Converter with Docling & PyMuPDF

This script extracts text and images from a PDF file, converts the text into Markdown format using Docling, and saves extracted images.

## Requirements

Make sure you have the following dependencies installed:

```bash
pip install docling PyMuPDF pillow
```

## Usage

1. Place the source PDF file in the same directory as the script and name it in `name = "your_file_name"`.
2. Run the script:

```bash
python pdftotxtandimage.py
```

## How It Works

- **Text Extraction**: Uses `DocumentConverter` from Docling to convert the PDF text into Markdown format.
- **Image Extraction**: Uses PyMuPDF (`fitz`) to extract images from the PDF and saves them as PNG files in the `extracted_images/` directory.
- **Output**:
  - A `.txt` file containing the extracted text in Markdown format.
  - Extracted images saved in the `extracted_images/` folder.

## Output Files

- `name+".txt"`: Contains the extracted text in Markdown format.
- `extracted_images/`: Directory storing extracted images as `image_1.png`, `image_2.png`, etc.

## Notes

- The script replaces `<!-- image -->` placeholders in the Markdown text with the corresponding image filenames.
- Ensure the PDF has selectable text for better conversion results.

## License

This project is licensed under the MIT License.

