# ⚡ Windows PowerShell Fundamentals 

<div align="center">

![PowerShell](https://img.shields.io/badge/PowerShell-7+-5391FE?style=for-the-badge\&logo=powershell\&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-Administration-0078D6?style=for-the-badge\&logo=windows\&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Compatible-FCC624?style=for-the-badge\&logo=linux\&logoColor=black)
![Automation](https://img.shields.io/badge/Automation-Scripting-success?style=for-the-badge)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Foundation-red?style=for-the-badge)

</div>

---

# 📖 Overview

This lab introduces the fundamentals of **Windows PowerShell Core** running on Linux environments. PowerShell is one of the most powerful automation and administration tools used by system administrators, DevOps engineers, cloud engineers, and cybersecurity professionals.

Through hands-on exercises, you'll learn how to manage files, automate tasks, create scripts, and gather system information using PowerShell.

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

✅ Execute basic PowerShell commands

✅ Manage files and directories using cmdlets

✅ Understand PowerShell syntax and command structure

✅ Write PowerShell scripts with variables, loops, and conditions

✅ Automate common administrative tasks

✅ Navigate and work efficiently in PowerShell environments

---

# 📋 Prerequisites

Before starting this lab, you should have:

* Basic command-line knowledge
* Understanding of files and directories
* Basic programming concepts
* Access to a Linux machine with PowerShell Core installed

---

# 🖥️ Lab Environment

Al Nafi provides a ready-to-use Linux cloud environment containing:

* PowerShell Core
* Ubuntu Linux
* Terminal Access
* Administrative Tools
* Preconfigured Environment

No installation required.

---

# 🚀 Task 1: Verify PowerShell Installation and Access

---

## 🔹 Subtask 1.1: Launch PowerShell Core

Start PowerShell:

```powershell
pwsh
```

Expected Prompt:

```text
PS /home/student>
```

Verify PowerShell Version:

```powershell
$PSVersionTable
```

---

## 🔹 Subtask 1.2: Understand PowerShell Basics

Display PowerShell Help:

```powershell
Get-Help
```

Get Help for a Specific Command:

```powershell
Get-Help Get-ChildItem
```

List All Available Commands:

```powershell
Get-Command
```

---

# 📁 Task 2: File and Directory Operations

---

## 🔹 Subtask 2.1: List Files and Directories

### Basic Listing

```powershell
Get-ChildItem
```

Alias:

```powershell
ls
```

Detailed Listing:

```powershell
Get-ChildItem -Force
```

### Advanced Listing

Directories Only:

```powershell
Get-ChildItem -Directory
```

Files Only:

```powershell
Get-ChildItem -File
```

Recursive Listing:

```powershell
Get-ChildItem -Recurse
```

Filter by Extension:

```powershell
Get-ChildItem *.txt
```

Hidden Files:

```powershell
Get-ChildItem -Hidden
```

---

## 🔹 Subtask 2.2: Create Files and Directories

### Create Directories

Create Lab Directory:

```powershell
New-Item -ItemType Directory -Name "PowerShellLab"
```

Create Multiple Directories:

```powershell
New-Item -ItemType Directory -Name "TestDir1","TestDir2","TestDir3"
```

Nested Directory Structure:

```powershell
New-Item -ItemType Directory -Path "PowerShellLab/SubDir1/SubDir2" -Force
```

### Create Files

Empty File:

```powershell
New-Item -ItemType File -Name "sample.txt"
```

File with Content:

```powershell
New-Item -ItemType File -Name "greeting.txt" -Value "Hello, PowerShell World!"
```

Multiple Files:

```powershell
New-Item -ItemType File -Name "file1.txt","file2.txt","file3.txt"
```

---

## 🔹 Subtask 2.3: Copy Files and Directories

Navigate:

```powershell
Set-Location PowerShellLab
```

Create Sample File:

```powershell
New-Item -ItemType File -Name "original.txt" -Value "This is the original file content."
```

Copy File:

```powershell
Copy-Item "original.txt" "copy1.txt"
```

Copy to Directory:

```powershell
Copy-Item "original.txt" "SubDir1/original_backup.txt"
```

Copy Multiple Files:

```powershell
Copy-Item *.txt "SubDir1/"
```

Copy Entire Directory:

```powershell
Copy-Item "SubDir1" "SubDir1_Backup" -Recurse
```

Copy with Confirmation:

```powershell
Copy-Item "original.txt" "copy2.txt" -Confirm
```

---

## 🔹 Subtask 2.4: Move Files and Directories

Create Test Files:

```powershell
New-Item -ItemType File -Name "temp1.txt","temp2.txt" -Value "Temporary content"
```

Move File:

```powershell
Move-Item "temp1.txt" "SubDir1/"
```

Move and Rename:

```powershell
Move-Item "temp2.txt" "SubDir1/renamed_temp.txt"
```

Move Multiple Files:

```powershell
New-Item -ItemType File -Name "move1.txt","move2.txt","move3.txt"
Move-Item move*.txt "SubDir2/"
```

Move Directory:

```powershell
Move-Item "TestDir1" "PowerShellLab/"
```

---

# 📜 Task 3: PowerShell Scripting Fundamentals

---

## 🔹 Subtask 3.1: Variables and Basic Scripting

### Variables

```powershell
$name = "PowerShell Student"
$age = 25
$isLearning = $true

Write-Host "Name: $name"
Write-Host "Age: $age"
Write-Host "Learning PowerShell: $isLearning"
```

### Arrays

```powershell
$fruits = @("Apple","Banana","Orange","Grape")

Write-Host "First fruit: $($fruits[0])"
Write-Host "All fruits: $fruits"
```

---

## 🔹 Subtask 3.2: Conditional Statements

### If-Else

```powershell
$number = 15

if ($number -gt 10) {
    Write-Host "$number is greater than 10"
}
else {
    Write-Host "$number is not greater than 10"
}
```

### ElseIf Example

```powershell
$score = 85

if ($score -ge 90) {
    Write-Host "Grade: A"
}
elseif ($score -ge 80) {
    Write-Host "Grade: B"
}
elseif ($score -ge 70) {
    Write-Host "Grade: C"
}
else {
    Write-Host "Grade: F"
}
```

### Switch Statement

```powershell
$day = "Monday"

switch ($day) {
    "Monday" { Write-Host "Start of the work week!" }
    "Friday" { Write-Host "TGIF!" }
    "Saturday" { Write-Host "Weekend time!" }
    "Sunday" { Write-Host "Rest day!" }
    default { Write-Host "Regular day" }
}
```

---

## 🔹 Subtask 3.3: Loops and Iteration

### For Loop

```powershell
for ($i = 1; $i -le 5; $i++) {
    Write-Host "Count: $i"
}
```

Create Files with Loop:

```powershell
for ($i = 1; $i -le 3; $i++) {
    New-Item -ItemType File -Name "loop_file_$i.txt" -Value "File number $i"
}
```

### ForEach Loop

```powershell
$colors = @("Red","Green","Blue","Yellow")

foreach ($color in $colors) {
    Write-Host "Processing color: $color"
}
```

Process Files:

```powershell
$files = Get-ChildItem *.txt

foreach ($file in $files) {
    Write-Host "$($file.Name) - $($file.Length) bytes"
}
```

### While Loop

```powershell
$counter = 1

while ($counter -le 5) {
    Write-Host "While Loop: $counter"
    $counter++
}
```

---

# 🤖 Script 1: File Management Automation

```powershell
Write-Host "=== File Management Automation ===" -ForegroundColor Green

$projectName = "MyProject"

$directories = @(
"src",
"docs",
"tests",
"config"
)

New-Item -ItemType Directory -Name $projectName -Force

Set-Location $projectName

foreach ($dir in $directories) {
    New-Item -ItemType Directory -Name $dir -Force
}

Write-Host "Project Structure Created Successfully!" -ForegroundColor Green
```

---

# 🖥️ Script 2: System Information Gathering

```powershell
Write-Host "=== System Information Report ===" -ForegroundColor Magenta

$PSVersionTable.PSVersion

Get-Location

$items = Get-ChildItem

$fileCount = ($items | Where-Object { -not $_.PSIsContainer }).Count

$dirCount = ($items | Where-Object { $_.PSIsContainer }).Count

Write-Host "Files: $fileCount"

Write-Host "Directories: $dirCount"
```

---

# 📂 Script 3: Interactive File Organizer

```powershell
Write-Host "=== Interactive File Organizer ===" -ForegroundColor Blue

$extensions = Get-ChildItem -File |
ForEach-Object { $_.Extension } |
Sort-Object -Unique

foreach ($ext in $extensions) {

    if ($ext -ne "") {

        $folderName = $ext.TrimStart('.') + "_files"

        New-Item -ItemType Directory -Name $folderName -Force

        Write-Host "Created Folder: $folderName"
    }
}
```

---

# 🧪 Task 4: Practical Exercises

---

## Exercise 1: Directory Navigation

```powershell
Set-Location ~

New-Item -ItemType Directory -Path "Practice/Level1/Level2" -Force

New-Item -ItemType File -Path "Practice/root_file.txt"

New-Item -ItemType File -Path "Practice/Level1/level1_file.txt"

New-Item -ItemType File -Path "Practice/Level1/Level2/level2_file.txt"

Get-ChildItem Practice -Recurse
```

---

## Exercise 2: Bulk File Operations

```powershell
Set-Location Practice

for ($i = 1; $i -le 10; $i++) {

    New-Item -ItemType File -Name "test_$i.txt"

}
```

Copy Files:

```powershell
Copy-Item test_*.txt Level1/
```

Move Even Files:

```powershell
Move-Item test_*[02468].txt Level1/Level2/
```

---

# ✅ Validation Script

```powershell
Write-Host "=== Lab Validation Script ==="

if (Test-Path "PowerShellLab") {

    Write-Host "✓ PowerShellLab Exists"

}

if (Test-Path "Practice") {

    Write-Host "✓ Practice Directory Exists"

}

$fileCount = (Get-ChildItem -File).Count

Write-Host "Files Found: $fileCount"
```

---

# 🛠️ Troubleshooting

## PowerShell Not Installed

```bash
sudo apt update
sudo apt install -y powershell
```

---

## Permission Denied

```powershell
Get-Location

Set-Location ~
```

---

## Script Execution Policy

```powershell
Get-ExecutionPolicy

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Path Not Found

```powershell
Test-Path "your/path"

Resolve-Path "relative/path"
```

---

# 📚 Essential Cmdlets Reference

| Cmdlet        | Purpose              |
| ------------- | -------------------- |
| Get-ChildItem | List Files           |
| New-Item      | Create Files/Folders |
| Copy-Item     | Copy Files           |
| Move-Item     | Move Files           |
| Set-Location  | Change Directory     |
| Test-Path     | Verify Paths         |

---

# 💡 PowerShell Syntax Rules

### Cmdlet Structure

```powershell
Verb-Noun
```

Examples:

```powershell
Get-ChildItem
New-Item
Copy-Item
Move-Item
```

### Variables

```powershell
$name = "Student"
```

### Comments

```powershell
# This is a comment
```

### String Interpolation

```powershell
Write-Host "Hello $name"
```

---

# 🔐 Why PowerShell Matters for Cybersecurity

PowerShell is heavily used in:

✅ Security Automation

✅ Threat Hunting

✅ Incident Response

✅ Log Analysis

✅ Compliance Reporting

✅ System Administration

✅ Digital Forensics

---

# 🏆 Skills Gained

After completing this lab, you can:

* Navigate PowerShell environments
* Manage files and directories
* Write automation scripts
* Use variables and loops
* Create conditional logic
* Build administrative tools
* Automate repetitive tasks

---

# 🎓 Conclusion

Congratulations! You have successfully completed the **Windows PowerShell Fundamentals Lab**.

You now possess foundational PowerShell skills that are widely used in:

* Cybersecurity Operations
* System Administration
* Cloud Engineering
* DevOps
* Automation
* Digital Forensics

These skills provide a strong foundation for advanced PowerShell scripting, security automation, threat hunting, and enterprise system management.

### 🚀 Next Steps

* Learn PowerShell Functions
* Explore PowerShell Modules
* Practice PowerShell Remoting
* Automate Security Tasks
* Build Incident Response Scripts
* Integrate PowerShell with SIEM Platforms

**Happy Scripting & Happy Automating! ⚡🔥**
