from src.database.usuario_db import UsuarioModel

class SistemaController:
    def cadastrar_novo_usuario(self, nome, email, senha):
        if not nome or not email or not senha:
            return "Todos os campos são obrigatórios!"
        
        if "@" not in email:
            return "Email inválido!"
        
        sucesso = UsuarioModel.criar_usuario(nome, email, senha)
        if sucesso:
            return "Usuário cadastrado com sucesso!"
        else:
            return "Erro ao cadastrar usuário (Email possivelmente já existe)."