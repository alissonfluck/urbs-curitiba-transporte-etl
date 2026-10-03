import pandas as pd

def transformar_linhas(dados_json):
    if not dados_json:
        print("Nenhum dado recebido para transformação.")
        return None

    df = pd.DataFrame(dados_json)
    df.columns = [col.lower() for col in df.columns]
    df = df.drop_duplicates(subset=['cod'])

    print(f"Transformação concluída: {len(df)} registros processados.")
    return df