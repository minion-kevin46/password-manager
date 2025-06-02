![Screenshot](screenshot.png)
# 🔐 Vaultify — Smart Password Manager

**Vaultify** is a simple and secure web-based password manager built with Flask and Python.  
It provides local encryption and easy access to your saved credentials — all in your browser.

---

## 🚀 Features

- AES-based password encryption
- Add, view, and delete credentials (site, login, password)
- Clean user interface with HTML/CSS
- Local file-based data storage (no online server needed)
- Easy to run locally

---

## 📂 Project Structure

password_manager_web/
├── app.py # Main Flask application
├── key.key # Encryption key (auto-generated)
├── templates/
│ └── index.html # Frontend page
├── static/
└── style.css # CSS styles

---

## ▶️ How to Run

1. Install required packages:

```bash
pip install flask cryptography
