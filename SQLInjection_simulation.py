import sqlite3
import tkinter as tk
from tkinter import messagebox

# Verilənlər bazasını yaradırıq
connection = sqlite3.connect(":memory:")  # Yaddaşda müvəqqəti verilənlər bazası
cursor = connection.cursor()

# Users cədvəlini yaradırıq
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
# Nümunə məlumatlar əlavə edirik
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('user', 'user123')")
connection.commit()


def insecure_login(username, password):
    # SQL Injection-a açıq kod
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result


def on_login_button_click():
    username = entry_username.get()  # İstifadəçi adı alınır
    password = entry_password.get()  # Şifrə alınır

    user = insecure_login(username, password)

    if user:
        messagebox.showinfo("Giriş icazəsi verildi", f"obaa Xoş gəlibsizzz, {user[1]}!")
        root.quit()  # Pəncərəni bağlayır
    else:
        messagebox.showerror("Giriş rədd edildi", "İstifadəçi adı və ya şifrə yanlışdır.")


# Tkinter pəncərəsini yaradırıq
root = tk.Tk()
root.title("Giriş Ekranı")  # Pəncərə başlığını təyin edirik
root.geometry("300x200")  # Pəncərə ölçülərini təyin edirik

# İstifadəçi adı üçün etiket və giriş qutusu
label_username = tk.Label(root, text="İstifadəçi adı:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Şifrə üçün etiket və giriş qutusu
label_password = tk.Label(root, text="Şifrə:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="")  # Şifrənin gizli göstərilməsi üçün show="*"
entry_password.pack(pady=5)

# Giriş düyməsi
login_button = tk.Button(root, text="Giriş", command=on_login_button_click)
login_button.pack(pady=10)

# Pəncərəni göstəririk
root.mainloop()

# Bağlantını bağlayırıq
connection.close()