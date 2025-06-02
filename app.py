from flask import Flask, render_template, request, redirect
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

# Генерация ключа (один раз)
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)

# Загрузка ключа
def load_key():
    return open("key.key", "rb").read()

# Шифрование/дешифрование
def encrypt(data, key):
    return Fernet(key).encrypt(data.encode())

def decrypt(data, key):
    return Fernet(key).decrypt(data).decode()

# Инициализация ключа
if not os.path.exists("key.key"):
    write_key()
key = load_key()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        site = request.form["site"]
        login = request.form["login"]
        password = request.form["password"]
        with open("data.enc", "ab") as f:
            entry = f"{site} | {login} | {password}\n"
            f.write(encrypt(entry, key) + b"\n")
        return redirect("/")

    passwords = []
    if os.path.exists("data.enc"):
        with open("data.enc", "rb") as f:
            for line in f:
                try:
                    decrypted = decrypt(line.strip(), key)
                    passwords.append(decrypted)
                except:
                    passwords.append("Ошибка расшифровки.")

    return render_template("index.html", passwords=passwords)

if __name__ == "__main__":
    app.run(debug=True)
