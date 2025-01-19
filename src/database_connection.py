import os
import mysql.connector as mysql_connector
from dotenv import load_dotenv

load_dotenv()

class MySQLDatabase:
    def __init__(self):
        self._host = os.getenv("HOST")
        self._username = os.getenv("USERNAME")
        self._password = os.getenv("PASSWORD")
        self._database = os.getenv("DATABASE")
        self._conn = None
        self._connect()
        self.criar_tabela()

    def _connect(self):
        try:
            self._conn = mysql_connector.connect(
                user=self._username,
                password=self._password,
                host=self._host,
                database=self._database
            )
            # print("Conexão estabelecida com sucesso.")
        except mysql_connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            self._conn = None

    def get_connection(self):
        if self._conn is None or not self._conn.is_connected():
            self._connect()
        return self._conn

    def close_connection(self):
        if self._conn and self._conn.is_connected():
            self._conn.close()
            print("Conexão encerrada.")

    def criar_tabela(self):
        try:
            cursor = self._conn.cursor()
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS hospedes (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nome VARCHAR(255) NOT NULL,
                            email VARCHAR(255) NOT NULL,
                            telefone VARCHAR(20) NOT NULL
                           );
                           """)
            self._conn.commit()
            # print("Tabela 'hospedes' verificada/criada com sucesso!")
        except mysql_connector.Error as e:
            print(f"Erro ao criar/verificar a tabela hospedes: {e}")
        finally:
            cursor.close()