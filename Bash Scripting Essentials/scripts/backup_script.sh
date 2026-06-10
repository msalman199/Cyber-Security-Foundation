#!/bin/bash

# Backup Script - Lab 4
# This script creates a backup of specified directories

# Define variables
SOURCE_DIR="$HOME/test_data"
BACKUP_DIR="$HOME/backups"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="backup_$DATE"

# Create backup directory if it doesn't exist
if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
    echo "Created backup directory: $BACKUP_DIR"
fi

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory $SOURCE_DIR does not exist!"
    exit 1
fi

# Create the backup
echo "Starting backup process..."
echo "Source: $SOURCE_DIR"
echo "Destination: $BACKUP_DIR/$BACKUP_NAME"

# Copy files to backup location
cp -r "$SOURCE_DIR" "$BACKUP_DIR/$BACKUP_NAME"

# Check if backup was successful
if [ $? -eq 0 ]; then
    echo "Backup completed successfully!"
    echo "Backup saved as: $BACKUP_DIR/$BACKUP_NAME"
    
    # Display backup size
    BACKUP_SIZE=$(du -sh "$BACKUP_DIR/$BACKUP_NAME" | cut -f1)
    echo "Backup size: $BACKUP_SIZE"
else
    echo "Backup failed!"
    exit 1
fi
