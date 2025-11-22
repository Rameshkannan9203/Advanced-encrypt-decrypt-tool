# 🔐 Advanced Encryption & Decryption Tool  
A powerful Python + JavaScript based application that provides **AES-256 encryption and decryption** using the **Fernet** algorithm.  
This tool allows users to securely encrypt sensitive text and decrypt it using a password-based key.

---

## 🚀 Features
-✔️ AES-256 level encryption (Fernet – cryptography library)  
- ✔️ Password-based key generation (SHA-256 + Base64)  
- ✔️ Modern frontend built using **HTML + CSS + JavaScript**  
- ✔️ Secure backend API using **Flask**  
- ✔️ Clean UI for easy encryption & decryption  
- ✔️ CORS enabled for frontend-backend communication  

---

## 🗂️ Project Structure

advanced-encryption-tool/
│
├── backend.py
│
└── frontend/
├── index.html
├── style.css
└── frontend.js

yaml
Copy code

---

## 🛠️ Backend Setup (Python)

### 1️⃣ Install required libraries
```bash
pip install flask flask-cors cryptography
2️⃣ Run the backend
bash
Copy code
python backend.py
You will see:

nginx
Copy code
Running on http://127.0.0.1:5000
🖥️ Frontend Setup
Go to the frontend folder

Open index.html in your browser

Right-click → Open with Chrome/Edge

Frontend uses JavaScript to communicate with the backend API.

🔧 API Endpoints
1. Encrypt Text
bash
Copy code
POST /api/encrypt
Request JSON:
json
Copy code
{
  "message": "hello world",
  "password": "12345"
}
Response:
json
Copy code
{
  "encrypted": "gAAAAABl..."
}
2. Decrypt Text
bash
Copy code
POST /api/decrypt
Request JSON:
json
Copy code
{
  "encrypted": "gAAAAABl...",
  "password": "12345"
}
Response:
json
Copy code
{
  "decrypted": "hello world"
}
🔒 Security Details
Password is converted to a 256-bit key using SHA-256

Key is encoded into a Fernet-compatible format

AES encryption ensures:

confidentiality

integrity

tamper protection

🎨 Frontend UI
The tool provides two sections:

🔐 Encryption Section
Enter text

Enter password

Click Encrypt

🔓 Decryption Section
Paste encrypted text

Enter password

Click Decrypt

📸 Screenshot (Add your own)
You can upload your project screenshot and insert here:

scss
Copy code
![App Screenshot](screenshot.png)
🧑‍💻 Technologies Used
Python

Flask Framework

Flask-CORS

Cryptography (Fernet / AES)

HTML5

CSS3

JavaScript

📌 Future Enhancements
🔑 File encryption support

📁 Download encrypted files

📱 Mobile version (PWA)

💻 Convert to Desktop app (EXE using PyInstaller)

❤️ Author
Made with 🔒 security + ❤️ love
by Ramesh Kannan (Your Name)

