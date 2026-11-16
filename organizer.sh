#!/bin/bash


ARCHIVE_DIR="archive"
ORIGINAL_FILE="grades.csv"
LOG_FILE="organizer.log"
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
ARCHIVED_NAME="grades_${TIMESTAMP}.csv"


echo "Starting archiving process..."


if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "Directory '$ARCHIVE_DIR' created."
fi


if [ -f "$ORIGINAL_FILE" ]; then
    mv "$ORIGINAL_FILE" "$ARCHIVE_DIR/$ARCHIVED_NAME"
    echo "File archived as: $ARCHIVE_DIR/$ARCHIVED_NAME"
    
    touch "$ORIGINAL_FILE"
    echo "New empty file '$ORIGINAL_FILE' created."
    
    echo "$TIMESTAMP | $ORIGINAL_FILE | $ARCHIVED_NAME" >> "$LOG_FILE"
    echo "Action logged in '$LOG_FILE'."
else
    echo "Error: File '$ORIGINAL_FILE' does not exist. Nothing to archive."
fi
