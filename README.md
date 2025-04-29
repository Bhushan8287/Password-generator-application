# 🔐 Password Generator CLI Tool
A simple yet functional Python command-line utility to generate secure passwords, encrypt them, and store them in a text file with usage tags (e.g., service names). This tool uses symmetric encryption to allow decryption using a `.key` file and supports persistent storage for personal, low-sensitivity password management.

## ⚙️ Features
- Generate random passwords of user-specified length
- Supports uppercase, lowercase, numbers, and special characters
- Save passwords to `.txt` file with purpose/usage info
- Encrypt stored passwords using symmetric encryption (`Fernet`)
- Create and load `.key` files for decryption
- CLI-based interaction for ease of use

## 🛠 Tech Stack
- **Python 3**
- `cryptography` library for encryption/decryption
- Standard Python modules (`os`, `random`, `getpass`, etc.)


## 🚀 Usage
1. Clone the repo:
   ```
   git clone 
   cd password-generator-cli
   ```

2. Run the script:
   ```
   python password_generator.py
   ```

3. Follow on-screen prompts to:
   - Generate a password
   - Save it with context
   - Encrypt/decrypt stored passwords

## 🔐 Note
This project is designed for educational and personal low-sensitivity use. It is **not** intended for secure, production-level password management.
