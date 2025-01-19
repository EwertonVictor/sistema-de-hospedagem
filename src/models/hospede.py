import mysql.connector

class Hospede:
    def __init__(self, db):
        self.db = db
    
    def cadastrar(self, nome, email, telefone):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO hospedes (nome, email, telefone) 
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (nome, email, telefone))
            conn.commit()
            print("Hóspede cadastrado com sucesso!")
        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar hóspede: {e}")
        finally:
            cursor.close()

    def listar(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM hospedes")
            for hospede in cursor.fetchall():
                print(hospede)
        except mysql.connector.Error as e:
            print(f"Erro ao listar hóspedes: {e}")
        finally:
            cursor.close()