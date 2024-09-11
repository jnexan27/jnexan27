import os

# Vulnerabilidad: Inyección de comando
def run_command(command):
    os.system(command)

# Vulnerabilidad: Uso de datos de entrada sin sanitizar
def unsafe_input():
    user_input = input("Enter something: ")
    run_command(user_input)

# Vulnerabilidad: Información sensible expuesta
def expose_secret():
    secret_key = "my_secret_key_123"
    print(f"Secret Key: {secret_key}")

if __name__ == "__main__":
    unsafe_input()
    expose_secret()