from src.database.connection import obter_conexao

class UsuarioModel:
    @staticmethod
    def criar_usuario(nome, email, senha):
        conn = obter_conexao()
        if not conn: return False
        
        cursor = conn.cursor()
        try:
            query = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s);"
            cursor.execute(query, (nome, email, senha))
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro no banco: {e}")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def listar_usuarios():
        conn = obter_conexao()
        if not conn: return []
        
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email FROM usuario;")
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return usuarios