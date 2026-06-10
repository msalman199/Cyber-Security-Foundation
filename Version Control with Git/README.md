# 🚀 Version Control with Git

![Git](https://img.shields.io/badge/Git-Version%20Control-orange?style=for-the-badge\&logo=git)
![Linux](https://img.shields.io/badge/Linux-Command%20Line-blue?style=for-the-badge\&logo=linux)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Foundation-red?style=for-the-badge\&logo=hackaday)

---

# 📚 Lab Overview

Version control is one of the most important skills for software developers, DevOps engineers, and cybersecurity professionals. Git allows users to track file changes, collaborate efficiently, maintain audit trails, and recover previous versions of projects.

This lab introduces the essential Git workflow including repository creation, commits, branching, merging, cloning, tagging, and repository maintenance.

---

# 🎯 Objectives

By the end of this lab, you will be able to:

* Understand Git fundamentals and version control concepts
* Initialize and manage Git repositories
* Stage and commit changes
* Create and manage branches
* Merge code changes
* Clone repositories
* Work with tags and history
* Apply Git best practices

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

* Basic Linux command-line knowledge
* Familiarity with file navigation
* Experience using nano or vim
* Understanding of basic software development concepts

---

# 🖥️ Lab Environment

Al Nafi provides a Linux-based cloud machine with Git pre-installed.

Verify installation:

```bash
git --version
```

Expected output:

```bash
git version 2.x.x
```

---

# 🛠️ Task 1: Git Installation and Configuration

## Configure Git User Information

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Verify:

```bash
git config --list
```

---

# 📁 Task 2: Initialize Repository

## Create Project Directory

```bash
mkdir my-first-repo
cd my-first-repo
git init
```

Output:

```bash
Initialized empty Git repository
```

Check status:

```bash
git status
```

---

# 📄 Create Initial Files

## README.md

```bash
echo "# My First Git Project" > README.md
echo "This is a sample project to learn Git basics." >> README.md
```

## hello.py

```python
#!/usr/bin/env python3
"""
A simple hello world program
"""

def main():
    print("Hello, Git World!")
    print("This is my first versioned program.")

if __name__ == "__main__":
    main()
```

Check status:

```bash
git status
```

---

# 💾 Task 3: Stage and Commit Changes

## Stage Files

```bash
git add README.md
git add hello.py
```

Or:

```bash
git add .
```

Verify:

```bash
git status
```

## First Commit

```bash
git commit -m "Initial commit: Add README and hello world program"
```

View history:

```bash
git log
```

Compact view:

```bash
git log --oneline
```

---

# 🔄 Task 4: Modify and Commit New Changes

## Update hello.py

Append:

```python
def greet_user(name):
    """Greet a specific user"""
    print(f"Hello, {name}! Welcome to Git!")

# Add a new greeting
greet_user("Student")
```

## Create Configuration File

```bash
cat > config.txt << EOF
# Configuration file for my project
version=1.0
author=Student
description=Learning Git basics
EOF
```

Check changes:

```bash
git status
git diff hello.py
```

Commit:

```bash
git add hello.py config.txt
git commit -m "Add user greeting function and configuration file"
```

View history:

```bash
git log --oneline
```

---

# 🌿 Task 5: Working with Branches

## Create Feature Branch

```bash
git checkout -b feature-improvements
```

Verify:

```bash
git branch
```

---

## Add New Feature

Append to hello.py:

```python
def display_info():
    """Display project information"""
    print("=" * 30)
    print("Project: My First Git Project")
    print("Version: 1.0")
    print("Learning: Git version control")
    print("=" * 30)

# Display project info
display_info()
```

Commit:

```bash
git add hello.py
git commit -m "Add project information display function"
```

---

# 🔀 Task 6: Merge Branches

Switch back:

```bash
git checkout main
```

Merge feature branch:

```bash
git merge feature-improvements
```

Verify:

```bash
cat hello.py
git log --oneline
```

Delete merged branch:

```bash
git branch -d feature-improvements
```

---

# 📥 Task 7: Clone Repositories

## Create Bare Repository

```bash
cd ..
git clone --bare my-first-repo my-first-repo.git
```

## Clone Repository

```bash
git clone my-first-repo.git cloned-repo
cd cloned-repo
```

Verify:

```bash
ls -la
cat README.md
cat hello.py
git log --oneline
```

---

## Modify README

```bash
echo "## Installation Instructions" >> README.md
echo "1. Clone this repository" >> README.md
echo "2. Run: python3 hello.py" >> README.md
```

Commit:

```bash
git add README.md
git commit -m "Add installation instructions to README"
```

Push:

```bash
git push origin main
```

---

# ⚡ Task 8: Advanced Git Operations

## View Commit Details

```bash
git show
```

## File History

```bash
git log --follow README.md
```

## Create Tag

```bash
git tag -a v1.0 -m "First stable version"
```

View tags:

```bash
git tag
```

## Repository Statistics

```bash
git log --stat
```

---

# ⏪ Task 9: Working with Previous Versions

View commits:

```bash
git log --oneline
```

Checkout previous commit:

```bash
git checkout <commit-hash>
```

Return:

```bash
git checkout main
```

---

## Create Documentation Branch

```bash
git checkout -b documentation-update
```

Create file:

```bash
echo "# Documentation" > DOCS.md
echo "This project demonstrates basic Git operations." >> DOCS.md
```

Commit:

```bash
git add DOCS.md
git commit -m "Add documentation file"
```

Switch branches:

```bash
git checkout main
git checkout documentation-update
```

---

# 🧹 Task 10: Repository Maintenance

## Repository Size

```bash
git count-objects -v
```

## Create .gitignore

```gitignore
# Python cache
__pycache__/
*.pyc
*.pyo

# Logs
*.log

# Temporary files
*.tmp
*~

# IDE Files
.vscode/
.idea/
```

Test:

```bash
echo "temporary data" > temp.tmp
echo "print('test')" > test.pyc
git status
```

Commit:

```bash
git add .gitignore
git commit -m "Add .gitignore file"
```

---

# 🚨 Troubleshooting

## Merge Conflicts

```bash
git add resolved-file
git commit -m "Resolve merge conflict"
```

---

## Unstage Files

```bash
git reset HEAD filename
```

---

## Undo Last Commit

Keep changes:

```bash
git reset --soft HEAD~1
```

---

## Check Staged Changes

```bash
git diff --staged
```

---

# ✅ Verification

## Repository Status

```bash
cd ~/my-first-repo

git status
git log --oneline --graph --all
```

## Branch Verification

```bash
git branch -a
```

## Run Application

```bash
python3 hello.py
```

## View Tracked Files

```bash
git ls-files
```

---

# 📊 Git Workflow Summary

```text
Working Directory
        │
        ▼
   git add
        │
        ▼
 Staging Area
        │
        ▼
 git commit
        │
        ▼
 Repository History
```

---

# 🔐 Why Git Matters for Cybersecurity

Git is heavily used in cybersecurity because it provides:

### Audit Trails

Every change is recorded permanently.

### Incident Response

Track modifications to security tools and scripts.

### Compliance

Maintain documented change history.

### Team Collaboration

Multiple analysts can work simultaneously.

### Backup & Recovery

Distributed repositories ensure redundancy.

### Security Tool Development

Used to manage:

* Security automation scripts
* SIEM configurations
* Detection rules
* Threat intelligence feeds
* Infrastructure as Code

---

# 🌟 Key Skills Learned

✔ Git installation and configuration

✔ Repository initialization

✔ Staging and committing changes

✔ Viewing commit history

✔ Creating and managing branches

✔ Merging code safely

✔ Cloning repositories

✔ Working with tags

✔ Using .gitignore

✔ Repository maintenance

✔ Version recovery techniques

✔ Cybersecurity-focused Git workflows

---

# 🎓 Lab Conclusion

Congratulations! You have successfully completed **Lab 8: Version Control with Git**.

You now understand:

* Core Git workflows
* Version tracking
* Branching strategies
* Repository cloning
* Collaboration techniques
* Security-focused change management

These skills are essential for Software Development, DevOps, Cloud Engineering, and Cybersecurity careers.

---

## 🚀 Next Steps

Continue learning:

* GitHub
* GitLab
* Remote repositories
* Pull Requests
* Rebasing
* Cherry-Picking
* GitHub Actions
* CI/CD Pipelines
* Infrastructure as Code

Mastering Git is one of the most valuable skills for modern technology professionals and cybersecurity practitioners.
