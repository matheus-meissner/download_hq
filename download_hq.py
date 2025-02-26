import requests
from PIL import Image
from io import BytesIO

def baixar_imagem(url):
    """Baixa a imagem a partir da URL e retorna um objeto PIL.Image"""
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    
    if response.status_code == 200:
        return Image.open(BytesIO(response.content)).convert("RGB")
    else:
        print(f"Erro ao baixar {url} (Status: {response.status_code})")
        return None

def gerar_pdf(lista_links, nome_pdf="hq.pdf"):
    """
    Baixa todas as imagens a partir de uma lista de URLs e gera um PDF.
    
    :param lista_links: Lista contendo os links diretos para as imagens
    :param nome_pdf: Nome do arquivo PDF final
    """
    imagens = []

    for i, url in enumerate(lista_links, start=1):
        print(f"Baixando página {i}...")
        imagem = baixar_imagem(url)
        
        if imagem:
            imagens.append(imagem)
        else:
            print(f"Erro ao baixar a imagem da página {i}.")

    if not imagens:
        print("Nenhuma imagem foi baixada. Verifique os links.")
        return

    # Salvar como PDF
    imagens[0].save(nome_pdf, save_all=True, append_images=imagens[1:])
    print(f"✅ PDF '{nome_pdf}' gerado com sucesso!")

# 📌 Exemplo de uso (adicione os links reais das imagens)
links_imagens = [
    "https://static.hq-now.com/hqs/hqs/uploads/picture/image/881693/Daredevil_-_Director_s_Cut_001-000b.jpg",
    "https://static.hq-now.com/hqs/hqs/uploads/picture/image/881700/Daredevil_-_Director_s_Cut_001-001.jpg",
    "https://static.hq-now.com/hqs/hqs/uploads/picture/image/881701/Daredevil_-_Director_s_Cut_001-002.jpg",
    "https://static.hq-now.com/hqs/hqs/uploads/picture/image/881702/Daredevil_-_Director_s_Cut_001-003.jpg"
]

gerar_pdf(links_imagens, "demolidor_1.pdf")
