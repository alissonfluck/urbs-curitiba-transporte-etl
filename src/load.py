import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def carregar_linhas_postgres(df):
    if df is None or df.empty:
        print("DataFrame vazio. Carga será abortada.")
        return

    db_user = os.getenv("POSTGRES_USER")
    db_pass = os.getenv("POSTGRES_PASSWORD")
    db_name = os.getenv("POSTGRES_DB")

    db_host = "localhost"
    db_port = "5432"

    conexao = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(conexao)

    try: 
        df.to_sql('linhas_urbs', con=engine, if_exists='replace', index=False)
        print("Carga concluída com sucesso no PostgreSQL.")
    except Exception as e:
        print(f"Erro ao carregar dados no PostgreSQL: {e}")