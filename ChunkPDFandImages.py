from docling.document_converter import DocumentConverter
import fitz  # PyMuPDF
import io
from PIL import Image
import os

# Đường dẫn file PDF nguồn
name = "your_file_name"
source = name+".pdf"
converter = DocumentConverter()
result = converter.convert(source)

# Xuất văn bản thành Markdown
markdown_text = result.document.export_to_markdown()

# Mở tệp PDF để trích xuất ảnh
pdf_document = fitz.open(source)

# Khởi tạo thứ tự ảnh
image_counter = 1

# Tạo thư mục để lưu ảnh nếu chưa tồn tại
image_dir = "extracted_images"
os.makedirs(image_dir, exist_ok=True)

# Lặp qua các trang trong tài liệu
for page_index in range(len(pdf_document)):
    # Lấy trang hiện tại
    page = pdf_document.load_page(page_index)
    
    # Lấy tất cả các ảnh trên trang
    image_list = page.get_images(full=True)
    
    # Lặp qua các ảnh và lưu chúng vào tệp
    for img_index, img in enumerate(image_list):
        # Lấy chi tiết ảnh
        xref = img[0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]

        # Mở ảnh dưới dạng đối tượng PIL
        image = Image.open(io.BytesIO(image_bytes))

        # Định dạng tên tệp ảnh
        image_filename = f"image_{image_counter}.png"
        image_path = os.path.join(image_dir, image_filename)
        image.save(image_path)
        print(f"Saved: {image_filename}")

        # Thay thế mã đặc biệt bằng tên ảnh trong văn bản
        markdown_text = markdown_text.replace("<!-- image -->", image_filename, 1)
        image_counter += 1

pdf_document.close()

# Lưu văn bản và liên kết ảnh vào file
with open(name+".txt", "w", encoding='utf-8') as f:
    f.write("\n\nMarkdown Conversion:\n")
    f.write(markdown_text)

print(markdown_text)
