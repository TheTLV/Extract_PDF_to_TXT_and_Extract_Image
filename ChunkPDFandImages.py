import pypdfium2 as pdfium
import csv
from PIL import Image
from io import BytesIO
from pytesseract import image_to_string

def convert_pdf_to_images(file_path, scale=300/72):
    pdf_file = pdfium.PdfDocument(file_path)  
    page_indices = list(range(len(pdf_file)))  # Lấy danh sách số trang
    
    renderer = pdf_file.render(
        pdfium.PdfBitmap.to_pil,
        page_indices=page_indices, 
        scale=scale,
    )
    
    list_final_images = []
    
    for i, image in zip(page_indices, renderer):
        image_byte_array = BytesIO()
        image.save(image_byte_array, format='JPEG', optimize=True)
        image_byte_array = image_byte_array.getvalue()
        list_final_images.append({i: image_byte_array})  # Lưu số trang và ảnh dạng bytes
    
    return list_final_images

def extract_text_with_pytesseract(list_dict_final_images):
    image_list = [list(data.values())[0] for data in list_dict_final_images]
    image_content = []
    
    for index, image_bytes in enumerate(image_list):
        image = Image.open(BytesIO(image_bytes))
        raw_text = image_to_string(image, lang='vie')
        image_content.append((index + 1, raw_text.strip()))  # Lưu số trang và nội dung
    
    return image_content

def save_text_to_txt(text_data, output_file="output.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        for page, text in text_data:
            f.write(f"Page {page}:\n{text}\n\n")
    print(f"Đã lưu văn bản vào {output_file}")

def save_text_to_csv(text_data, output_file="output.csv"):
    with open(output_file, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Page", "Text"])
        writer.writerows(text_data)
    print(f"Đã lưu văn bản vào {output_file}")

# Chạy chương trình
pdf_path = "Quy_trình.pdf"  # Đổi thành đường dẫn file PDF của bạn
images = convert_pdf_to_images(pdf_path)
text_data = extract_text_with_pytesseract(images)

# Lưu ra file TXT và CSV
save_text_to_txt(text_data, "chunked.txt")
save_text_to_csv(text_data, "chunked.csv")
