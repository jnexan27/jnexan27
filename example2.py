import os
import subprocess

def run_command(user_input):
    # Vulnerabilidad: Uso inseguro de entrada del usuario en la ejecución de comandos
    command = f"echo {user_input}"
    result = subprocess.check_output(command, shell=True)
    return result.decode('utf-8')

if __name__ == '__main__':
    user_input = input("Enter something: ")
    print(run_command(user_input))