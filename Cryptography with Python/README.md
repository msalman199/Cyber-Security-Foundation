# 🔐 Cryptography with Python

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Cryptography](https://img.shields.io/badge/Cryptography-AES%20%7C%20SHA256-green?style=for-the-badge&logo=securityscorecard)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge&logo=ubuntu)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Hands--On-red?style=for-the-badge&logo=hackaday)

</div>

---

# 📖 Overview

This hands-on lab introduces practical cryptography using Python. You will learn how to:

- 🔒 Generate SHA256 hashes
- 🔑 Encrypt and decrypt data using AES
- 🛡️ Verify file integrity
- 📁 Secure files inside an encrypted vault
- 📊 Perform automated security audits
- ⚙️ Build cybersecurity automation tools

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

✅ Implement SHA256 hashing for file integrity verification

✅ Use AES encryption to secure sensitive data

✅ Create Python scripts for cryptographic operations

✅ Apply cryptographic techniques for cybersecurity tasks

✅ Automate encryption and hashing workflows

---

# 📋 Prerequisites

- Basic Python Programming
- Linux Command Line Knowledge
- Basic Cybersecurity Concepts
- File Handling Knowledge
- Text Editor Experience (Nano/Vim)

---

# 🖥️ Lab Environment

Al Nafi Cloud Machine provides:

- Python 3.x
- Cryptography Library
- Linux Environment
- Nano/Vim Editors
- Preconfigured Dependencies

---

# 📂 Create Lab Directory

```bash
mkdir ~/crypto_lab
cd ~/crypto_lab
```

Create test file:

```bash
echo "Original content for testing" > testfile.txt
```

---

# 🔐 Task 1 — SHA256 File Hashing

## 📌 hash_calculator.py

```python
#!/usr/bin/env python3

import hashlib
import sys

def calculate_sha256(filename):
    try:
        sha256 = hashlib.sha256()

        with open(filename, "rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        print(f"[-] File not found: {filename}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 hash_calculator.py <file>")
        sys.exit(1)

    filename = sys.argv[1]

    file_hash = calculate_sha256(filename)

    if file_hash:
        print(f"\nSHA256: {file_hash}")
        print(f"Length: {len(file_hash)}")

if __name__ == "__main__":
    main()
```

### ▶ Test

```bash
python3 hash_calculator.py testfile.txt
```

---

# 🛡️ Task 1.2 — File Integrity Checker

## 📌 integrity_checker.py

```python
#!/usr/bin/env python3

import hashlib
import json
import os
import sys
from datetime import datetime

class IntegrityChecker:

    def __init__(self, db_file="integrity.json"):
        self.db_file = db_file
        self.database = {}
        self.load_database()

    def load_database(self):
        try:
            with open(self.db_file, "r") as f:
                self.database = json.load(f)
        except FileNotFoundError:
            self.database = {}

    def save_database(self):
        with open(self.db_file, "w") as f:
            json.dump(self.database, f, indent=2)

    def calculate_hash(self, filepath):
        sha256 = hashlib.sha256()

        with open(filepath, "rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    def add_file(self, filepath):

        if not os.path.exists(filepath):
            print("File not found.")
            return False

        self.database[filepath] = {
            "hash": self.calculate_hash(filepath),
            "timestamp": datetime.now().isoformat(),
            "size": os.path.getsize(filepath)
        }

        self.save_database()

        print(f"[+] Added {filepath}")
        return True

    def verify_file(self, filepath):

        if filepath not in self.database:
            print("File not in database.")
            return False

        current_hash = self.calculate_hash(filepath)
        stored_hash = self.database[filepath]["hash"]

        if current_hash == stored_hash:
            print("[✓] File Integrity Verified")
            return True
        else:
            print("[!] File Modified")
            return False

    def list_files(self):

        for file, data in self.database.items():
            print(f"\nFile: {file}")
            print(f"Hash: {data['hash']}")
            print(f"Timestamp: {data['timestamp']}")

def main():

    if len(sys.argv) < 2:
        print("Usage: add|verify|list")
        return

    checker = IntegrityChecker()

    command = sys.argv[1]

    if command == "add":
        checker.add_file(sys.argv[2])

    elif command == "verify":
        checker.verify_file(sys.argv[2])

    elif command == "list":
        checker.list_files()

if __name__ == "__main__":
    main()
```

### ▶ Test

```bash
python3 integrity_checker.py add testfile.txt

python3 integrity_checker.py verify testfile.txt

echo "Modified" >> testfile.txt

python3 integrity_checker.py verify testfile.txt
```

---

# 🔑 Task 2 — AES Text Encryption

Install library:

```bash
pip3 install cryptography
```

---

## 📌 text_encryptor.py

```python
#!/usr/bin/env python3

from cryptography.fernet import Fernet

class TextEncryptor:

    def __init__(self):
        self.key = None

    def generate_key(self):
        self.key = Fernet.generate_key()

    def save_key(self, filename="secret.key"):
        with open(filename, "wb") as f:
            f.write(self.key)

    def load_key(self, filename="secret.key"):
        with open(filename, "rb") as f:
            self.key = f.read()

    def encrypt_text(self, plaintext):

        cipher = Fernet(self.key)

        return cipher.encrypt(plaintext.encode())

    def decrypt_text(self, encrypted_text):

        cipher = Fernet(self.key)

        return cipher.decrypt(encrypted_text).decode()

def main():

    encryptor = TextEncryptor()

    encryptor.generate_key()
    encryptor.save_key()

    plaintext = input("Enter text: ")

    encrypted = encryptor.encrypt_text(plaintext)

    print("\nEncrypted:")
    print(encrypted.decode())

    decrypted = encryptor.decrypt_text(encrypted)

    print("\nDecrypted:")
    print(decrypted)

if __name__ == "__main__":
    main()
```

### ▶ Test

```bash
python3 text_encryptor.py
```

---

# 📁 AES File Encryption

## 📌 file_encryptor.py

```python
#!/usr/bin/env python3

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.backends import default_backend

import os
import getpass
import sys

class FileEncryptor:

    def __init__(self):
        self.backend = default_backend()

    def derive_key(self, password, salt):

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=self.backend
        )

        return kdf.derive(password.encode())

    def encrypt_file(self, input_file, output_file, password):

        with open(input_file, "rb") as f:
            data = f.read()

        salt = os.urandom(16)
        iv = os.urandom(16)

        key = self.derive_key(password, salt)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()

        cipher = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend=self.backend
        )

        encryptor = cipher.encryptor()

        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        with open(output_file, "wb") as f:
            f.write(salt + iv + ciphertext)

        print("[+] File Encrypted")

    def decrypt_file(self, input_file, output_file, password):

        with open(input_file, "rb") as f:
            data = f.read()

        salt = data[:16]
        iv = data[16:32]
        ciphertext = data[32:]

        key = self.derive_key(password, salt)

        cipher = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend=self.backend
        )

        decryptor = cipher.decryptor()

        padded = decryptor.update(ciphertext) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()

        plaintext = unpadder.update(padded) + unpadder.finalize()

        with open(output_file, "wb") as f:
            f.write(plaintext)

        print("[+] File Decrypted")

def main():

    if len(sys.argv) != 4:
        print("Usage:")
        print("encrypt input output")
        print("decrypt input output")
        return

    action = sys.argv[1]

    password = getpass.getpass("Password: ")

    enc = FileEncryptor()

    if action == "encrypt":
        enc.encrypt_file(sys.argv[2], sys.argv[3], password)

    elif action == "decrypt":
        enc.decrypt_file(sys.argv[2], sys.argv[3], password)

if __name__ == "__main__":
    main()
```

### ▶ Test

```bash
echo "Confidential data" > secret.txt

python3 file_encryptor.py encrypt secret.txt secret.enc

python3 file_encryptor.py decrypt secret.enc recovered.txt

cat recovered.txt
```

---

# 🏦 Task 3 — Secure Vault Manager

## 📌 vault_manager.py

```python
#!/usr/bin/env python3

import os
import json
import hashlib
from datetime import datetime

class VaultManager:

    def __init__(self, vault_dir="secure_vault"):

        self.vault_dir = vault_dir

        os.makedirs(vault_dir, exist_ok=True)

        self.metadata_file = os.path.join(
            vault_dir,
            "vault_metadata.json"
        )

        if os.path.exists(self.metadata_file):
            with open(self.metadata_file, "r") as f:
                self.metadata = json.load(f)
        else:
            self.metadata = {}

    def calculate_hash(self, filepath):

        sha256 = hashlib.sha256()

        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    def store_file(self, filepath):

        filename = os.path.basename(filepath)

        hash_value = self.calculate_hash(filepath)

        self.metadata[filename] = {
            "hash": hash_value,
            "timestamp": datetime.now().isoformat(),
            "size": os.path.getsize(filepath)
        }

        with open(self.metadata_file, "w") as f:
            json.dump(self.metadata, f, indent=2)

        print(f"[+] Stored {filename}")

    def list_vault(self):

        for file, data in self.metadata.items():

            print(f"\nFile: {file}")
            print(f"Size: {data['size']}")
            print(f"Hash: {data['hash'][:20]}...")
            print(f"Date: {data['timestamp']}")

def main():

    vault = VaultManager()

    vault.list_vault()

if __name__ == "__main__":
    main()
```

---

# 🔍 Security Audit Tool

## 📌 security_audit.py

```python
#!/usr/bin/env python3

import os
import hashlib
import json
import stat
from datetime import datetime

class SecurityAuditor:

    def __init__(self, scan_dir="."):

        self.scan_dir = scan_dir

        self.report = {
            "timestamp": datetime.now().isoformat(),
            "files_scanned": 0,
            "file_hashes": {},
            "warnings": []
        }

    def calculate_hash(self, filepath):

        sha256 = hashlib.sha256()

        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    def scan_directory(self):

        for root, dirs, files in os.walk(self.scan_dir):

            for file in files:

                path = os.path.join(root, file)

                try:
                    hash_value = self.calculate_hash(path)

                    perms = oct(os.stat(path).st_mode)[-3:]

                    self.report["file_hashes"][path] = {
                        "hash": hash_value,
                        "permissions": perms,
                        "size": os.path.getsize(path)
                    }

                    self.report["files_scanned"] += 1

                except:
                    pass

    def generate_report(self, output="audit_report.json"):

        with open(output, "w") as f:
            json.dump(self.report, f, indent=2)

        print(f"[+] Report saved to {output}")

def main():

    auditor = SecurityAuditor()

    auditor.scan_directory()

    auditor.generate_report()

if __name__ == "__main__":
    main()
```

---

# ▶ Run Security Audit

```bash
python3 security_audit.py ~/crypto_lab
```

---

# 📊 Expected Outcomes

After completing this lab you will have:

✅ SHA256 Hash Generator

✅ File Integrity Checker

✅ AES Text Encryptor

✅ AES File Encryptor

✅ Secure Vault Manager

✅ Security Audit Tool

✅ Practical Cryptography Experience

---

# 🛠 Troubleshooting

## Import Error

```bash
pip3 install --user cryptography
```

Verify:

```bash
python3 -c "import cryptography; print('OK')"
```

---

## Permission Issues

```bash
chmod 644 filename
ls -la
```

---

## Corrupted Integrity Database

```bash
rm integrity.json
```

---

## Validate Python Syntax

```bash
python3 -m py_compile *.py
```

---

# 🎓 Conclusion

This lab demonstrated real-world cryptography using Python.

You successfully implemented:

- 🔒 SHA256 Hashing
- 🔑 AES Encryption
- 🛡️ File Integrity Verification
- 📁 Secure File Storage
- 📊 Security Auditing Automation

These techniques form the foundation of modern cybersecurity operations, secure software development, digital forensics, and data protection systems.

---

<div align="center">

### 🚀 Cybersecurity • Cryptography • Python Automation

**Hands-On Security Engineering Lab**

</div>
