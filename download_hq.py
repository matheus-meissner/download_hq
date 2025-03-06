import requests
from PIL import Image
from io import BytesIO

def baixar_imagem(url, tentativas_extra=None):
    """
    Baixa uma imagem de uma URL e retorna um objeto PIL.Image.
    Se a URL original falhar, tenta variantes do nome da imagem.

    :param url: URL original da imagem
    :param tentativas_extra: Lista de sufixos alternativos a serem testados caso a primeira tentativa falhe
    :return: Objeto PIL.Image ou None se todas as tentativas falharem
    """
    tentativas = [url]  # Lista de URLs a testar

    if tentativas_extra:
        tentativas.extend(tentativas_extra)

    for tentativa in tentativas:
        response = requests.get(tentativa, headers={"User-Agent": "Mozilla/5.0"})

        if response.status_code == 200:
            print(f"✅ Imagem encontrada: {tentativa}")
            return Image.open(BytesIO(response.content)).convert("RGB")
        else:
            print(f"❌ URL inexistente ou erro ao baixar: {tentativa} (Status: {response.status_code})")

    return None  # Retorna None se todas as tentativas falharem

def gerar_links_paginas(base_url, base_id, total_paginas, nome_base):
    """
    Gera a lista de URLs das páginas do quadrinho, ajustando IDs para evitar quebras.

    :param base_url: URL base das imagens
    :param base_id: ID inicial da primeira página
    :param total_paginas: Número total de páginas da HQ
    :param nome_base: Nome base usado nos arquivos das imagens
    :return: Lista de (ID, URLs principais e variações) para cada página
    """
    links = []
    id_atual = base_id  # Mantém o ID base fixo

    for i in range(total_paginas):
        num_pagina = str(i + 1).zfill(3)  # Número da página formatado (001, 002, etc.)
        base_url_pagina = f"{base_url}/{id_atual}/{nome_base}-{num_pagina}.jpg"

        # Possíveis variações para tentar caso a URL original falhe
        variacoes = [
            base_url_pagina.replace(".jpg", "-Recuperado.jpg"),
            base_url_pagina.replace(".jpg", "-Alt.jpg")
        ]

        links.append((id_atual, num_pagina, base_url_pagina, variacoes))

    return links

def gerar_pdf(base_url, capa_id, base_id, total_paginas, nome_base, nome_pdf):
    """
    Baixa todas as capas e páginas de um quadrinho e gera um PDF.

    :param base_url: URL base das imagens
    :param capa_id: ID inicial da capa
    :param base_id: ID inicial da primeira página
    :param total_paginas: Número total de páginas do quadrinho
    :param nome_base: Nome base usado nos arquivos
    :param nome_pdf: Nome do arquivo PDF final
    """
    print("\n📥 Iniciando download das capas...")
    capas = baixar_capas(base_url, capa_id, nome_base)

    print("\n📥 Iniciando download das páginas...")
    lista_links = gerar_links_paginas(base_url, base_id, total_paginas, nome_base)

    imagens = capas
    id_atual = base_id
    numero_pagina = 1

    while numero_pagina <= total_paginas:
        num_pagina_str = str(numero_pagina).zfill(3)
        url = f"{base_url}/{id_atual}/{nome_base}-{num_pagina_str}.jpg"

        # Variações da URL caso a original falhe
        variacoes = [
            url.replace(".jpg", "-Recuperado.jpg"),
            url.replace(".jpg", "-Alt.jpg")
        ]

        print(f"📥 Tentando baixar página {num_pagina_str} (ID: {id_atual})...")
        imagem = baixar_imagem(url, tentativas_extra=variacoes)

        if imagem:
            imagens.append(imagem)
            id_atual += 1  # Aumenta o ID apenas quando uma imagem é encontrada
            numero_pagina += 1  # Aumenta o número da página normalmente
        else:
            print(f"⚠️ Página {num_pagina_str} não encontrada. Tentando próximo número de página mantendo ID...")
            numero_pagina += 1  # Apenas aumenta o número da página, mantendo o ID

    if not imagens:
        print("❌ Nenhuma imagem foi baixada. Verifique os links.")
        return

    imagens[0].save(nome_pdf, save_all=True, append_images=imagens[1:])
    print(f"\n✅ PDF '{nome_pdf}' gerado com sucesso!")

def baixar_capas(base_url, base_id, nome_base):
    """
    Baixa todas as capas disponíveis, garantindo que o ID numérico e o sufixo aumentem juntos.

    :param base_url: URL base das imagens
    :param base_id: ID inicial da primeira capa
    :param nome_base: Nome base dos arquivos das capas
    :return: Lista de imagens das capas baixadas
    """
    capas = []
    sufixos = ["000a", "000b", "000c", "000d", "000e", "000f", "000g", "000h", "000"]

    id_atual = base_id

    for sufixo in sufixos:
        url = f"{base_url}/{id_atual}/{nome_base}-{sufixo}.jpg"
        imagem = baixar_imagem(url)

        if imagem:
            capas.append(imagem)
        else:
            print(f"⚠️ Nenhuma capa encontrada com ID {id_atual} e sufixo {sufixo}, continuando com próximos sufixos...")

    return capas

# 📌 Configuração para qualquer volume
config_hq = {
    "base_url": "https://static.hq-now.com/hqs/hqs/uploads/picture/image",
    "capa_id": 915445,  # ID inicial da capa
    "base_id": 915447,  # ID inicial da primeira página
    "total_paginas": 27,  # Número total de páginas
    "nome_base": "Daredevil_014",
    "nome_pdf": "demolidor_14.pdf"
}

# Gerar o PDF
gerar_pdf(**config_hq)
