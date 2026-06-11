# 🔐 Cryptography with Python 

<div align="center">

# 🛡️ Python Cryptography & Data Protection 

### Hash • Encrypt • Verify • Secure

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Cryptography](https://img.shields.io/badge/Cryptography-AES%20%7C%20SHA256-red?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge\&logo=linux)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Blue?style=for-the-badge)
![Encryption](https://img.shields.io/badge/Encryption-AES%20256-success?style=for-the-badge)
![Hashing](https://img.shields.io/badge/Hashing-SHA256-yellow?style=for-the-badge)

</div>

---

# 📖 Overview

This hands-on cybersecurity lab introduces practical cryptography using Python.

Students will implement:

* 🔑 AES Encryption
* 🔍 SHA256 Hashing
* 📁 File Integrity Verification
* 🔐 Secure Vault Storage
* 📊 Security Auditing Tools
* ⚙️ Security Automation Scripts

The lab focuses on real-world cybersecurity operations where confidentiality, integrity, and automation are essential.

---

# 🎯 Objectives

By the end of this lab, students will be able to:

✅ Implement SHA256 hashing for integrity verification

✅ Use AES encryption to secure sensitive data

✅ Create Python cryptographic tools

✅ Apply cryptography in cybersecurity workflows

✅ Automate encryption and hashing operations

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

* Python programming fundamentals
* Variables and functions
* File handling knowledge
* Linux command line familiarity
* Basic cybersecurity concepts
* Experience with nano or vim

---

# ☁️ Lab Environment

Al Nafi Cloud Machines provide:

* Python 3.x
* Cryptography libraries
* Linux environment
* Nano/Vim editors
* Pre-configured dependencies

---

# 🛠️ Technologies Used

| Technology           | Purpose                         |
| -------------------- | ------------------------------- |
| Python 3             | Programming Language            |
| SHA256               | File Integrity Verification     |
| AES                  | Data Encryption                 |
| Cryptography Library | Secure Encryption Functions     |
| JSON                 | Metadata Storage                |
| Linux                | Execution Environment           |
| PBKDF2               | Password-Based Key Derivation   |
| Fernet               | Simplified Symmetric Encryption |

---

# 🚀 Task 1: SHA256 File Hashing

## 📂 Create Lab Directory

```bash
mkdir ~/crypto_lab && cd ~/crypto_lab
```

---

## 📄 Create Test File

```bash
echo "Original content for testing" > testfile.txt
```

---

## 🧮 Create Hash Calculator

```bash
nano hash_calculator.py
```

### Features

* SHA256 Hash Calculation
* Chunk-Based Reading
* Error Handling
* Command-Line Arguments
* Integrity Verification

---

## ▶️ Execute Hash Calculator

```bash
python3 hash_calculator.py testfile.txt
```

Expected Output:

```text
SHA256 Hash:
d2b2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Length: 64 characters
```

---

# 🔒 File Integrity Checker

## Create Integrity Checker

```bash
nano integrity_checker.py
```

### Features

* JSON Hash Database
* File Registration
* Integrity Verification
* Timestamp Tracking
* Modification Detection

---

## Add File to Database

```bash
python3 integrity_checker.py add testfile.txt
```

---

## Verify File

```bash
python3 integrity_checker.py verify testfile.txt
```

---

## Modify File

```bash
echo "Modified" >> testfile.txt
```

---

## Verify Again

```bash
python3 integrity_checker.py verify testfile.txt
```

Expected:

```text
WARNING: File Modified!
```

---

# 🚀 Task 2: AES Encryption

## Install Cryptography Package

```bash
pip3 install cryptography
```

---

# 🔐 Text Encryption Tool

## Create Encryptor

```bash
nano text_encryptor.py
```

---

### Features

* Generate Encryption Keys
* Save/Load Keys
* Encrypt Text
* Decrypt Text
* Fernet-Based Encryption

---

## Execute

```bash
python3 text_encryptor.py
```

Expected Workflow:

```text
Enter text:
Hello World

Encrypted:
gAAAAAB...

Decrypted:
Hello World
```

---

# 📁 AES File Encryption

## Create File Encryptor

```bash
nano file_encryptor.py
```

---

### Security Features

* AES Encryption
* CBC Mode
* PBKDF2 Key Derivation
* Random Salt Generation
* Random IV Generation
* PKCS7 Padding

---

## Create Secret File

```bash
echo "Confidential data" > secret.txt
```

---

## Encrypt File

```bash
python3 file_encryptor.py encrypt secret.txt secret.enc
```

---

## Decrypt File

```bash
python3 file_encryptor.py decrypt secret.enc recovered.txt
```

---

## Verify Recovery

```bash
cat recovered.txt
```

Expected:

```text
Confidential data
```

---

# 🚀 Task 3: Automated Security Tools

# 🔐 Secure Vault Manager

## Create Vault Tool

```bash
nano vault_manager.py
```

---

### Features

* AES Encryption
* SHA256 Verification
* Metadata Tracking
* Secure Storage
* File Recovery
* Integrity Validation

---

## Store File

```bash
echo "Report 1" > report1.txt

python3 vault_manager.py store report1.txt
```

---

## List Vault Contents

```bash
python3 vault_manager.py list
```

---

## Retrieve File

```bash
python3 vault_manager.py retrieve report1.txt recovered_report.txt
```

---

## Remove File

```bash
python3 vault_manager.py remove report1.txt
```

---

# 🔍 Security Audit Tool

## Create Auditor

```bash
nano security_audit.py
```

---

### Capabilities

* Directory Scanning
* SHA256 Hashing
* Duplicate Detection
* Permission Analysis
* JSON Reporting
* Security Warnings

---

## Run Audit

```bash
python3 security_audit.py ~/crypto_lab
```

---

Expected Report:

```json
{
  "timestamp": "2025-01-01T12:00:00",
  "directory": "/home/user/crypto_lab",
  "files_scanned": 10,
  "warnings": []
}
```

---

# 📊 Expected Outcomes

Upon completion, you will have:

✅ SHA256 Hash Calculator

✅ File Integrity Monitoring Tool

✅ AES Text Encryptor

✅ AES File Encryptor

✅ Secure Vault Manager

✅ Security Audit Scanner

✅ Practical Cryptography Experience

---

# 🔬 Cryptography Concepts Learned

## SHA256 Hashing

Purpose:

* Integrity Verification
* Fingerprinting
* Tamper Detection

Characteristics:

* One-Way Function
* Fixed 256-bit Output
* Collision Resistant

---

## AES Encryption

Purpose:

* Data Confidentiality
* Secure Storage
* Secure Transmission

Characteristics:

* Symmetric Encryption
* Fast Performance
* Industry Standard

---

## PBKDF2

Purpose:

* Password-Based Key Derivation

Benefits:

* Salt Protection
* Brute Force Resistance
* Secure Key Generation

---

# 🛠️ Troubleshooting

## Module Import Error

```bash
pip3 install --user cryptography
```

Verify:

```bash
python3 -c "import cryptography; print('OK')"
```

---

## Permission Errors

```bash
chmod 644 filename
```

Check:

```bash
ls -la
```

---

## JSON Errors

Remove corrupted database:

```bash
rm integrity.json
```

---

## Decryption Failure

Verify:

* Correct Password
* Correct Salt
* Correct IV
* Uncorrupted File

---

## Hash Mismatch

Check:

* File Modification
* Disk Space
* Complete File Write
* File System Health

---

# 🏆 Skills Gained

### 🔒 Cryptography

Practical implementation of hashing and encryption.

### 🛡️ Cybersecurity

Integrity verification and secure storage.

### ⚙️ Automation

Automated security operations using Python.

### 📁 Secure File Management

Protection of sensitive files and data.

### 🔍 Security Auditing

Scanning and analyzing directories for risks.

---

# 🌍 Real-World Applications

## Enterprise Security

Protect confidential business information.

## Secure Backups

Encrypt sensitive backups before storage.

## Incident Response

Verify integrity of forensic evidence.

## Compliance

Support security and regulatory requirements.

## DevSecOps

Integrate encryption into CI/CD pipelines.

---

# 📈 Future Enhancements

* RSA Public-Key Encryption
* Digital Signatures
* Secure Password Vault
* Multi-Factor Authentication
* Secure File Sharing
* HMAC Authentication
* SHA512 Integration
* Secure APIs

---

# 🎓 Conclusion

This Cryptography with Python lab introduced practical cybersecurity techniques used in real-world environments.

You successfully explored:

* SHA256 Hashing
* AES Encryption
* File Integrity Monitoring
* Secure Vault Management
* Security Automation
* Directory Auditing

These skills form a strong foundation for cybersecurity, secure software development, cloud security, DevSecOps, and incident response.

---

<div align="center">

# 🔐 Encrypt Data • Verify Integrity • Build Secure Systems

### ⭐ Star this repository if you found this lab useful!

</div>
