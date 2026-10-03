from extract import extrair_linhas_urbs
from transform import transformar_linhas
from load import carregar_linhas_postgres

def run_pipeline():
    print("Iniciando pipeline de dados da URBS...")

    # Extract
    print("Extraindo dados...")
    dados_brutos = extrair_linhas_urbs()

    if dados_brutos:
        # Transform
        print("Limpando dados...")
        df_limpo = transformar_linhas(dados_brutos)

        if df_limpo is not None and not df_limpo.empty:
            # Load
            print("Carregando dados no banco de dados...")
            carregar_linhas_postgres(df_limpo)
        else:
            print("Pipeline interrompido: Falha na etapa de transformação.")
    else:
        print("Pipeline interrompido. Falha na etapa de extração.")
    print("Pipeline finalizado.")
if __name__ == "__main__":
    run_pipeline()