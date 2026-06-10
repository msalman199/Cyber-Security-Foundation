# 🐧 Linux Command-Line Basics 

<div align="center">

![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge\&logo=ubuntu\&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-Shell-4EAA25?style=for-the-badge\&logo=gnubash\&logoColor=white)
![CLI](https://img.shields.io/badge/CLI-Command_Line-black?style=for-the-badge)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Foundation-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Lab-Completed-success?style=for-the-badge)

</div>

---

# 📚 Overview

Welcome to the **Linux Command-Line Basics Lab**. This lab introduces the Linux terminal and fundamental commands used by Linux administrators, DevOps engineers, and cybersecurity professionals.

By completing this lab, you will learn how to navigate the Linux filesystem, manage files and directories, understand permissions, and perform essential command-line operations.

---

# 🎯 Learning Objectives

By the end of this lab, you will be able to:

✅ Navigate the Linux file system using CLI commands

✅ Understand Linux directory structures and paths

✅ Create, copy, move, and delete files and directories

✅ Manage permissions using `chmod` and `chown`

✅ Use essential Linux commands for cybersecurity tasks

---

# 📋 Prerequisites

Before starting this lab, you should have:

* Basic understanding of operating systems
* Familiarity with files and folders
* No prior Linux experience required
* Access to Al Nafi cloud lab environment

---

# 🖥️ Lab Environment

The lab environment includes:

* Ubuntu Linux Operating System
* Terminal Access
* Pre-installed Tools
* Root and User Accounts

---

# 🗂️ Task 1: Navigate Directories

---

## 🔹 Understanding Linux File System

Linux uses a hierarchical directory structure beginning with the root directory:

```text
/
├── bin
├── boot
├── dev
├── etc
├── home
├── root
├── tmp
├── usr
└── var
```

Think of `/` as the top of the filesystem tree.

---

## 🔹 Subtask 1.1: Find Current Location

Display your current directory:

```bash
pwd
```

### ✅ Expected Output

```text
/home/student
```

### 💡 Explanation

`pwd` = **Print Working Directory**

Shows your current location in the filesystem.

---

## 🔹 Subtask 1.2: List Directory Contents

Basic listing:

```bash
ls
```

Detailed listing:

```bash
ls -l
```

Show hidden files:

```bash
ls -la
```

### 📖 Understanding Output

| Command | Description          |
| ------- | -------------------- |
| ls      | List files           |
| ls -l   | Detailed listing     |
| ls -la  | Include hidden files |

---

## 🔹 Subtask 1.3: Navigate Between Directories

Go to root:

```bash
cd /
```

Verify:

```bash
pwd
```

List root contents:

```bash
ls
```

Go to home:

```bash
cd /home
```

Go to your home directory:

```bash
cd ~
```

Move up one level:

```bash
cd ..
```

Return home:

```bash
cd
```

### 🚀 Navigation Summary

```bash
cd /
cd ~
cd ..
cd directory_name
```

---

# 📁 Task 2: Create, Copy, Move, and Delete Files

---

## 🔹 Subtask 2.1: Create Files and Directories

Navigate home:

```bash
cd ~
```

Create directory:

```bash
mkdir lab_practice
```

Enter directory:

```bash
cd lab_practice
```

Create files:

```bash
touch test_file.txt

touch file1.txt file2.txt file3.txt
```

Create subdirectory:

```bash
mkdir documents
```

Verify:

```bash
ls -la
```

---

## 🔹 Subtask 2.2: Add Content to Files

Write content:

```bash
echo "This is my first Linux file" > test_file.txt
```

Append content:

```bash
echo "This is line 2" >> test_file.txt
```

Display file:

```bash
cat test_file.txt
```

Create multiline file:

```bash
cat > file1.txt << EOF
Welcome to Linux
This is a cybersecurity lab
Learning command line is important
EOF
```

### 💡 Notes

```text
>   Overwrite file
>>  Append to file
cat Display file contents
```

---

## 🔹 Subtask 2.3: Copy Files

Copy file:

```bash
cp test_file.txt test_file_backup.txt
```

Copy into directory:

```bash
cp file1.txt documents/
```

Copy multiple files:

```bash
cp file2.txt file3.txt documents/
```

Copy and rename:

```bash
cp test_file.txt documents/renamed_file.txt
```

Verify:

```bash
ls -la

ls -la documents/
```

---

## 🔹 Subtask 2.4: Move and Rename Files

Create backup folder:

```bash
mkdir backup_folder
```

Move file:

```bash
mv test_file_backup.txt backup_folder/
```

Rename file:

```bash
mv file2.txt important_file.txt
```

Move and rename:

```bash
mv file3.txt backup_folder/archived_file.txt
```

Move directory:

```bash
mkdir temp_dir

mv temp_dir backup_folder/
```

Verify:

```bash
ls -la

ls -la backup_folder/
```

---

## 🔹 Subtask 2.5: Delete Files and Directories

Delete file:

```bash
rm important_file.txt
```

Create temporary files:

```bash
touch delete_me1.txt delete_me2.txt delete_me3.txt
```

Delete multiple files:

```bash
rm delete_me1.txt delete_me2.txt delete_me3.txt
```

Delete empty directory:

```bash
mkdir empty_dir

rmdir empty_dir
```

Delete directory recursively:

```bash
rm -r backup_folder
```

### ⚠️ Safety Warning

Never run:

```bash
rm -rf /
```

Always verify targets before deleting.

---

# 🔐 Task 3: Manage Users and Permissions

---

## 🔹 Subtask 3.1: Understanding Permissions

Create file:

```bash
touch permission_test.txt
```

View permissions:

```bash
ls -l permission_test.txt
```

Example:

```text
-rw-r--r-- 1 student student 0 Jan 1 permission_test.txt
```

### 📖 Permission Breakdown

```text
-rw-r--r--
││ │ │
││ │ └── Others
││ └──── Group
│└────── Owner
└──────── File Type
```

Permission Values:

```text
r = Read (4)
w = Write (2)
x = Execute (1)
```

---

## 🔹 Subtask 3.2: Change Permissions Using chmod

Create script:

```bash
echo "#!/bin/bash" > my_script.sh

echo "echo 'Hello from my script!'" >> my_script.sh
```

Check permissions:

```bash
ls -l my_script.sh
```

Run script:

```bash
./my_script.sh
```

Expected:

```text
Permission denied
```

Add execute permission:

```bash
chmod u+x my_script.sh
```

Run again:

```bash
./my_script.sh
```

### Common chmod Examples

```bash
chmod go-w my_script.sh

chmod a+r my_script.sh

chmod 755 my_script.sh

chmod 444 permission_test.txt
```

Verify:

```bash
ls -l my_script.sh permission_test.txt
```

---

## 🔹 Subtask 3.3: Numeric Permissions

| Value | Meaning |
| ----- | ------- |
| 7     | rwx     |
| 6     | rw-     |
| 5     | r-x     |
| 4     | r--     |
| 3     | -wx     |
| 2     | -w-     |
| 1     | --x     |
| 0     | ---     |

Examples:

```bash
touch demo1.txt demo2.txt demo3.txt

chmod 644 demo1.txt

chmod 755 demo2.txt

chmod 600 demo3.txt
```

Verify:

```bash
ls -l demo*.txt
```

---

## 🔹 Subtask 3.4: Change Ownership Using chown

Check ownership:

```bash
ls -l my_script.sh
```

View user:

```bash
whoami
```

View groups:

```bash
groups
```

Change owner:

```bash
sudo chown root:root my_script.sh
```

Restore ownership:

```bash
sudo chown $USER:$USER my_script.sh
```

Common syntax:

```bash
chown user file

chown user:group file

chown :group file
```

---

## 🔹 Subtask 3.5: Directory Permissions

Create structure:

```bash
mkdir test_permissions

cd test_permissions

mkdir secret_folder

touch secret_folder/secret_file.txt

echo "Top secret information" > secret_folder/secret_file.txt
```

Restrict access:

```bash
chmod 700 secret_folder
```

Verify:

```bash
ls -ld secret_folder
```

Test:

```bash
ls secret_folder/
```

Remove permissions:

```bash
chmod 000 secret_folder
```

Attempt access:

```bash
ls secret_folder/
```

Restore:

```bash
chmod 755 secret_folder
```

---

# ✅ Verification Tasks

## Navigation Verification

```bash
cd /

pwd

cd ~

pwd

mkdir verification_test

cd verification_test

pwd
```

---

## File Management Verification

```bash
mkdir -p project/{src,docs,tests}

touch project/README.md

touch project/src/main.py

touch project/docs/manual.txt

touch project/tests/test_main.py
```

Verify:

```bash
ls -la project/

ls -la project/src/

ls -la project/docs/

ls -la project/tests/
```

---

## Permission Verification

Create script:

```bash
echo "#!/bin/bash" > final_test.sh

echo "echo 'Congratulations! You have mastered Linux basics!'" >> final_test.sh
```

Make executable:

```bash
chmod 755 final_test.sh
```

Verify:

```bash
ls -l final_test.sh
```

Run:

```bash
./final_test.sh
```

Expected:

```text
Congratulations! You have mastered Linux basics!
```

---

# 🛠️ Troubleshooting

## Permission Denied

```bash
ls -l filename

chmod +x filename
```

---

## Cannot Remove Directory

Empty:

```bash
rmdir directory_name
```

Non-empty:

```bash
rm -r directory_name
```

---

## Lost in Filesystem

```bash
pwd

cd ~
```

---

## Command Not Found

Check command:

```bash
which command_name
```

Verify spelling and syntax.

---

# 📖 Quick Command Reference

## Navigation

```bash
pwd
cd
cd ~
cd ..
ls
ls -la
```

## File Management

```bash
touch
mkdir
cp
mv
rm
rmdir
```

## Permissions

```bash
chmod
chown
ls -l
```

---

# 🏆 What You Learned

✅ Linux File System Navigation

✅ File and Directory Management

✅ Linux Permission System

✅ Ownership Management

✅ Command-Line Productivity

✅ Cybersecurity Foundation Skills

---

# 🔒 Why Linux Matters in Cybersecurity

Linux is the foundation of modern cybersecurity because:

* Most servers run Linux
* Security tools are Linux-based
* Incident response relies on CLI skills
* Log analysis is command-line focused
* Automation depends on scripting and permissions

---

# 🎓 Conclusion

Congratulations! You have completed the **Linux Command-Line Basics Lab**.

You now understand:

* Linux filesystem navigation
* File and directory operations
* Permission management
* Ownership control
* Essential cybersecurity command-line skills

These skills form the foundation for advanced Linux administration, penetration testing, incident response, and security engineering.

### 🚀 Next Steps

* Learn text processing (`grep`, `awk`, `sed`)
* Explore process management
* Learn Bash scripting
* Study Linux networking commands
* Begin cybersecurity-specific Linux tools

**Happy Learning & Happy Hacking (Ethically)! 🐧🚀**
