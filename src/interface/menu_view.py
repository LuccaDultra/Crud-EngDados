from src.logica.usuario_logica import SistemaController

class MenuView:
    def __init__(self):
        self.controller = SistemaController()

    def exibir_menu_principal(self):
        while True:
            print("\n=== SISTEMA ACADÊMICO (CRUD) ===")
            print("1. Cadastrar Usuário")
            print("2. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Nome: ")
                email = input("Email: ")
                senha = input("Senha: ")
                resultado = self.controller.cadastrar_novo_usuario(nome, email, senha)
                print(resultado)
            elif opcao == "2":
                print("Saindo...")
                break