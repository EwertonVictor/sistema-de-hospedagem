from database_connection import MySQLDatabase
from models.hospede import Hospede
import os

class SistemaHospedagem:
    
    def __init__(self):
        self.db = MySQLDatabase()
        self.hospede = None
    
    def iniciar(self):
        conn = self.db.get_connection()
        if conn and conn.is_connected():
            self.hospede = Hospede(self.db)
            self.menu_principal()
    
    def limpar_tela(self):
        os.system("cls")

    def menu_principal(self):
        try:
            while True:
                print("""
====== MENU PRINCIPAL ======
                      """)
                print("1. Gerenciar Hóspedes")
                print("2. Gerenciar Quartos")
                print("3. Gerenciar Reservas")
                print("4. Gerenciar Pagamentos")
                print("0. Sair")

                opcao = float(input("\nEscolha uma opção: "))
                self.limpar_tela()
                if opcao == 1:
                    self.menu_hospedes()
                elif opcao == 0:
                    print("Saindo do sistema...")
                    break
                else:
                    print("""Opção inválida! Tente novamente.""")
        except Exception as e:
            print(f"\nOps! Parece que temos um problema: {e}")
        except KeyboardInterrupt as e:
            print(f"Sistema encerrado inesperadamente: {e}")

    def menu_hospedes(self):
        print("""
====== MENU HOSPEDES ======
                """)
        while True:
            print("1. Cadastrar Hóspede")
            print("2. Listar Hóspedes")
            print("0. Voltar")

            opcao = float(input("\nEscolha uma opção: "))
            self.limpar_tela()

            if opcao == 1:
                nome = input("Nome: ")
                email = input("Email: ")
                telefone = input("Telefone: ")
                self.hospede.cadastrar(nome, email, telefone)
            elif opcao == 2:
                self.hospede.listar()
            elif opcao == 0:
                break
            else:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    sistema = SistemaHospedagem()
    sistema.iniciar()