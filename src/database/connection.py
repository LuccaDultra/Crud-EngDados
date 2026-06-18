import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def obter_conexao():
    try:
        
        conexao = psycopg.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        return conexao
    except Exception as e:
        print(f"Erro ao conectar ao banco na AWS: {e}")
        return None