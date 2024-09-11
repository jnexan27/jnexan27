import os
import subprocess
import sqlite3
from cryptography.fernet import Fernet

# Vulnerabilidad 1: Uso inseguro de las variables de entorno
SECRET_KEY = os.getenv('SECRET_KEY')  # No validamos si SECRET_KEY está presente

# Vulnerabilidad 2: Inyección de comandos
def run_command(command):
    return subprocess.check_output(command, shell=True)

# Vulnerabilidad 3: Inyección de SQL
def execute_query(query):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    cursor.execute(query)  # Ejecución directa de consulta SQL sin validación
    connection.commit()
    connection.close()

# Vulnerabilidad 4: Uso inseguro de datos cifrados
def decrypt_data(encrypted_data):
    cipher_suite = Fernet(SECRET_KEY)
    return cipher_suite.decrypt(encrypted_data)  # Uso de una clave secreta sin validación

# Ejemplo de uso de funciones vulnerables
if __name__ == '__main__':
    # Inyección de comandos
    result = run_command('ls -la')
    print(result)

    # Inyección de SQL
    execute_query('INSERT INTO users (username, password) VALUES ("admin", "password123")')

    # Datos cifrados
    encrypted_data = b'gAAAAABlZB1P5LbZT6V9H4hpKr5FVdTHlg7tFJ5Et7E_PkpGd1g9B1Jw0Od8V-3ROsOfbJ8xkROXrT5f'
    decrypted_data = decrypt_data(encrypted_data)
    print(decrypted_data)
