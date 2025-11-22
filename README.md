<h1 align="center">🌙🔐 Advanced Encryption & Decryption Tool (Dark Mode Edition)</h1>
<p align="center">
  <b>A Secure AES-256 Encryption App built using Python + Flask + HTML/CSS/JS with Dark/Light Mode Support</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Mode-Dark%20%26%20Light-blueviolet">
  <img src="https://img.shields.io/badge/Language-Python-blue">
  <img src="https://img.shields.io/badge/Backend-Flask-orange">
  <img src="https://img.shields.io/badge/Encryption-AES--256-purple">
  <img src="https://img.shields.io/badge/Status-Active-success">
</p>

---

## 🌙 Dark Mode Preview  
*(Replace with your actual screenshot)*  
```
![Dark Mode Screenshot](https://your-darkmode-image-link-here)
```

---

## 📸 Light Mode Preview  
```
![Light Mode Screenshot](https://your-lightmode-image-link-here)
```

---

## 📌 Overview  
The **Advanced Encryption & Decryption Tool** is a secure web-based application that performs AES-256 encryption & decryption using a password-derived key.

Now upgraded with:

✨ **Dark Mode + Light Mode Switch**  
✨ **New modern UI design**  
✨ **Smooth transitions (CSS animations)**

---

## 🚀 Features  
- 🔐 AES-256 Encryption (Fernet)  
- 🔑 SHA-256 Password → AES Key  
- 🌙 **Dark Mode + Light Mode Toggle**  
- 🖥️ Modern & Responsive UI  
- ⚡ Flask Backend API  
- 🛡️ Secure Error Handling  
- 📂 Full Project Folder Structure  

---

## 🗂️ Project Structure
```
advanced-encryption-decryption-tool/
│── backend.py
│── README.md
│── /frontend
│     ├── index.html
│     ├── style.css  (dark + light mode)
│     └── frontend.js
```

---

## ⚙️ Installation

### 1️⃣ Install Dependencies
```bash
pip install flask cryptography
```

### 2️⃣ Run Backend
```bash
python backend.py
```

### 3️⃣ Open Frontend
```
frontend/index.html
```

---

## 📡 API Documentation

### 🔸 **Encrypt**
POST → `/encrypt`
```json
{
  "message": "Hello World",
  "password": "mypassword"
}
```

Response:
```json
{
  "encrypted": "gAAAAAB..."
}
```

---

### 🔸 **Decrypt**
POST → `/decrypt`
```json
{
  "encrypted_text": "gAAAAAB...",
  "password": "mypassword"
}
```

Response:
```json
{
  "decrypted": "Hello World"
}
```

---

## 🎨 Dark Mode — How It Works  
- CSS variable system (`:root`)  
- JavaScript toggle button  
- Smooth fade transition  
- Stored theme preference in localStorage  

---

## ⭐ Future Improvements  
- Upload file encryption  
- Auto key generator  
- Mobile version  
- Online hosted version (GitHub Pages)  

---

## 🧑‍💻 Developer  
**Ramesh Kannan**  
Cybersecurity & Networking Enthusiast  

GitHub Profile:  
https://github.com/Rameshkannan9203

---

## 📜 License  
For education & learning.

