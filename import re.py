import os
import fitz  # PyMuPDF

def convert_pdf_to_jpg(input_folder, output_folder):
    # Certifique-se de que a pasta de saída existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lista todos os arquivos na pasta de entrada
    files = os.listdir(input_folder)

    # Filtra apenas os arquivos PDF
    pdf_files = [file for file in files if file.endswith(".pdf")]

    for pdf_file in pdf_files:
        # Construa os caminhos completos para o arquivo de entrada e saída
        input_path = os.path.join(input_folder, pdf_file)
        output_path_base = os.path.join(output_folder, os.path.splitext(pdf_file)[0])

        # Abre o arquivo PDF
        pdf_document = fitz.open(input_path)

        # Converte cada página do PDF para uma imagem JPEG
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            image = page.get_pixmap()
            
            # Salva a imagem como JPEG
            output_path = f"{output_path_base}_page{page_number + 1}.jpg"
            image.save(output_path, "JPEG")

            print(f"Conversão concluída: {pdf_file}, Página {page_number + 1} -> {os.path.basename(output_path)}")

        # Fecha o documento PDF
        pdf_document.close()

# Substitua 'caminho/para/pasta/pdf' e 'caminho/para/pasta/jpg' pelos caminhos reais em seu sistema
input_folder = 'C:/Users/betro/Documents/COBRAPE/pdf'
output_folder = 'C:/Users/betro/Documents/COBRAPE/jpg'

convert_pdf_to_jpg(input_folder, output_folder)
