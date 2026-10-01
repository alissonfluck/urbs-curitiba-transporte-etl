import os
import requests
from dotenv import load_dotenv

load_dotenv()

def extrair_linhas_urbs():
    url_base = "https://transporteservico.urbs.curitiba.pr.gov.br/getLinhas.php"
    api_code = os.getenv("URBS_API_CODE")

    if not api_code:
        raise ValueError("Credencial da URBS não encontrada no ambiente.")

    params = {"c": api_code}

    try:
        response = requests.get(url_base, params=params)
        response.raise_for_status()

        dados = response.json()
        print(f"Extração concluída: {len(dados)} linhas retornadas da API.")
        return dados

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição à API da URBS: {e}")
        return None

if __name__ == "__main__":
    dados_linhas = extrair_linhas_urbs()

    if dados_linhas:
        print(dados_linhas[0])