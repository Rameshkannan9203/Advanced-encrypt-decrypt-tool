const API_URL = "http://127.0.0.1:5000";

async function encryptText() {
    const message = document.getElementById("message").value;
    const password = document.getElementById("password").value;

    const response = await fetch(`${API_URL}/api/encrypt`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message, password })
    });

    const data = await response.json();
    document.getElementById("result").innerText = data.encrypted || data.error;
}

async function decryptText() {
    const encrypted = document.getElementById("encrypted").value;
    const password = document.getElementById("password2").value;

    const response = await fetch(`${API_URL}/api/decrypt`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ encrypted, password })
    });

    const data = await response.json();
    document.getElementById("result2").innerText = data.decrypted || data.error;
}
