#!/usr/bin/env python3
"""
Folder Cleanup Script - Lab 3 Task 2
This script automates the cleanup of temporary and old files
"""

import os
import glob
import shutil
from datetime import datetime

def cleanup_by_extension(directory, extensions_to_remove):
    """
    Function to remove files with specific extensions
    """
    removed_files = []
    
    for extension in extensions_to_remove:
        pattern = os.path.join(directory, f"*.{extension}")
        files_to_remove = glob.glob(pattern)
        
        for file_path in files_to_remove:
            try:
                os.remove(file_path)
                removed_files.append(file_path)
                print(f"Removed: {os.path.basename(file_path)}")
            except Exception as e:
                print(f"Error removing {file_path}: {e}")
    
    return removed_files

def cleanup_empty_directories(directory):
    """
    Function to remove empty directories
    """
    removed_dirs = []
    
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                if not os.listdir(dir_path):  # Check if directory is empty
                    os.rmdir(dir_path)
                    removed_dirs.append(dir_path)
                    print(f"Removed empty directory: {dir_name}")
            except Exception as e:
                print(f"Error removing directory {dir_path}: {e}")
    
    return removed_dirs

def list_files_before_cleanup(directory):
    """
    Function to list all files before cleanup
    """
    print("Files before cleanup:")
    print("-" * 30)
    
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")

def main():
    """
    Main function to execute folder cleanup operations
    """
    cleanup_directory = "../temp_files"
    
    # Extensions to remove (temporary files)
    extensions_to_clean = ['tmp', 'log', 'cache', 'bak']
    
    print("=== FOLDER CLEANUP AUTOMATION ===")
    print(f"Target directory: {cleanup_directory}")
    print()
    
    # List files before cleanup
    if os.path.exists(cleanup_directory):
        list_files_before_cleanup(cleanup_directory)
        print()
        
        # Perform cleanup
        print("Starting cleanup process...")
        print("-" * 30)
        
        removed_files = cleanup_by_extension(cleanup_directory, extensions_to_clean)
        removed_dirs = cleanup_empty_directories(cleanup_directory)
        
        print("-" * 30)
        print(f"Cleanup completed!")
        print(f"Files removed: {len(removed_files)}")
        print(f"Directories removed: {len(removed_dirs)}")
        
        # List remaining files
        print()
        print("Remaining files:")
        print("-" * 30)
        list_files_before_cleanup(cleanup_directory)
        
    else:
        print(f"Directory {cleanup_directory} does not exist!")

if __name__ == "__main__":
    main()
