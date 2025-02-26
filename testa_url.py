import requests
from PIL import Image
from io import BytesIO

def baixar_imagem(url):
    """Baixa a imagem a partir de uma URL e retorna um objeto PIL.Image"""
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if response.status_code == 200:
        content_type = response.headers.get("Content-Type", "")
        
        if "image" in content_type:  # Verifica se o conteúdo é uma imagem
            try:
                return Image.open(BytesIO(response.content)).convert("RGB")
            except Exception as e:
                print(f"Erro ao processar imagem de {url}: {e}")
                return None
        else:
            print(f"URL {url} retornou um conteúdo inválido: {content_type}")
            return None
    else:
        print(f"Erro ao acessar {url} (Status: {response.status_code})")
        return None
