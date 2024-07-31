// static/script.js
document.getElementById('encryptBtn').addEventListener('click', async () => {
    const plaintext = document.getElementById('inputText').value;
    const response = await fetch('/encrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ plaintext })
    });
    const result = await response.json();
    document.getElementById('outputText').value = `IV: ${result.iv}\nCiphertext: ${result.ciphertext}`;
});

document.getElementById('decryptBtn').addEventListener('click', async () => {
    const [ivLine, ciphertextLine] = document.getElementById('inputText').value.split('\n');
    const iv = ivLine.split(': ')[1];
    const ciphertext = ciphertextLine.split(': ')[1];
    const response = await fetch('/decrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ iv, ciphertext })
    });
    const result = await response.json();
    document.getElementById('outputText').value = result.plaintext;
});
