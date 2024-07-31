# An-Encryption-and-Decryption-Web-Application

*** Project Description: AES Encryption and Decryption Web Application
Project Overview:
This project is a web application designed to perform encryption and decryption of text data using the Advanced Encryption Standard (AES) algorithm. It showcases a blend of cryptographic techniques and web development skills, demonstrating the capability to build secure and user-friendly applications.

Key Features:

*** AES Encryption and Decryption:

Utilizes the AES algorithm in Cipher Block Chaining (CBC) mode for secure data encryption and decryption.
Supports symmetric key encryption, where the same key is used for both encrypting and decrypting data.

***User-Friendly Interface:

A clean and simple web interface built with HTML, CSS, and JavaScript.
Textareas for inputting plain text and displaying the encrypted or decrypted output.
Buttons to trigger encryption and decryption processes.

***Backend with Flask:

A lightweight Python backend using the Flask framework to handle encryption and decryption requests.
Provides RESTful API endpoints for encrypting and decrypting text data.

***Technologies Used:

Cryptography: AES algorithm from the pycryptodome library.
Backend: Python and Flask for handling HTTP requests and processing encryption/decryption.
Frontend: HTML, CSS, and JavaScript for creating a responsive and interactive user interface.


***How It Works:

Encryption:

The user inputs plain text into the textarea.
Upon clicking the "Encrypt" button, a POST request is sent to the /encrypt endpoint with the plain text.
The backend encrypts the text using AES, returning the initialization vector (IV) and ciphertext.
The encrypted data is displayed on the web interface.

Decryption:

The user inputs the IV and ciphertext into the textarea.
Upon clicking the "Decrypt" button, a POST request is sent to the /decrypt endpoint with the IV and ciphertext.
The backend decrypts the text using AES, returning the original plain text.
The decrypted data is displayed on the web interface.
