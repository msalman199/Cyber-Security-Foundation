#!/bin/bash

# File Management Script - Demonstrating Loops and Conditionals
# Lab 4 - Bash Scripting Essentials

# Create test directory structure
TEST_DIR="$HOME/file_test"
mkdir -p "$TEST_DIR"

# Function to create test files
create_test_files() {
    echo "Creating test files..."
    
    # For loop to create numbered files
    for i in {1..10}; do
        echo "Test file content $i" > "$TEST_DIR/testfile$i.txt"
    done
    
    # Create some files with different extensions
    echo "Log entry 1" > "$TEST_DIR/app.log"
    echo "Log entry 2" > "$TEST_DIR/system.log"
    echo "Configuration data" > "$TEST_DIR/config.conf"
    echo "Backup data" > "$TEST_DIR/backup.bak"
    
    echo "Test files created successfully!"
}

# Function to analyze files
analyze_files() {
    echo "Analyzing files in $TEST_DIR..."
    
    # Initialize counters
    txt_count=0
    log_count=0
    other_count=0
    total_size=0
    
    # While loop to read file list
    find "$TEST_DIR" -type f | while read file; do
        # Get file extension
        extension="${file##*.}"
        file_size=$(stat -c%s "$file")
        
        echo "Processing: $(basename "$file") (Size: $file_size bytes)"
        
        # Conditional statements for file categorization
        case "$extension" in
            "txt")
                echo "  -> Text file detected"
                ;;
            "log")
                echo "  -> Log file detected"
                ;;
            "conf")
                echo "  -> Configuration file detected"
                ;;
            "bak")
                echo "  -> Backup file detected"
                ;;
            *)
                echo "  -> Other file type"
                ;;
        esac
    done
}

# Function to organize files by type
organize_files() {
    echo "Organizing files by type..."
    
    # Create subdirectories
    mkdir -p "$TEST_DIR/txt_files"
    mkdir -p "$TEST_DIR/log_files"
    mkdir -p "$TEST_DIR/config_files"
    mkdir -p "$TEST_DIR/backup_files"
    
    # Move files to appropriate directories
    for file in "$TEST_DIR"/*; do
        # Skip if it's a directory
        if [ -d "$file" ]; then
            continue
        fi
        
        filename=$(basename "$file")
        extension="${filename##*.}"
        
        # Conditional file movement
        if [ "$extension" = "txt" ]; then
            mv "$file" "$TEST_DIR/txt_files/"
            echo "Moved $filename to txt_files/"
        elif [ "$extension" = "log" ]; then
            mv "$file" "$TEST_DIR/log_files/"
            echo "Moved $filename to log_files/"
        elif [ "$extension" = "conf" ]; then
            mv "$file" "$TEST_DIR/config_files/"
            echo "Moved $filename to config_files/"
        elif [ "$extension" = "bak" ]; then
            mv "$file" "$TEST_DIR/backup_files/"
            echo "Moved $filename to backup_files/"
        fi
    done
}

# Function to generate report
generate_report() {
    echo "Generating file organization report..."
    
    # Array of directories to check
    directories=("txt_files" "log_files" "config_files" "backup_files")
    
    for dir in "${directories[@]}"; do
        full_path="$TEST_DIR/$dir"
        if [ -d "$full_path" ]; then
            file_count=$(ls -1 "$full_path" | wc -l)
            echo "$dir: $file_count files"
            
            # List files if any exist
            if [ "$file_count" -gt 0 ]; then
                echo "  Files:"
                ls -1 "$full_path" | while read file; do
                    echo "    - $file"
                done
            fi
        fi
    done
}

# Main execution
echo "File Management Script Starting..."
echo "=================================="

# Menu system using case statement
while true; do
    echo ""
    echo "Choose an option:"
    echo "1) Create test files"
    echo "2) Analyze files"
    echo "3) Organize files"
    echo "4) Generate report"
    echo "5) Clean up test directory"
    echo "6) Exit"
    echo -n "Enter your choice (1-6): "
    
    read choice
    
    case $choice in
        1)
            create_test_files
            ;;
        2)
            analyze_files
            ;;
        3)
            organize_files
            ;;
        4)
            generate_report
            ;;
        5)
            echo "Cleaning up test directory..."
            rm -rf "$TEST_DIR"
            echo "Test directory removed."
            ;;
        6)
            echo "Exiting file manager..."
            break
            ;;
        *)
            echo "Invalid option. Please choose 1-6."
            ;;
    esac
done

echo "File management script completed!"
