# Python File Organizer Script

## Description

A Python script designed to automatically organize files within a specified directory by moving them into subfolders based on their file extensions. This project aims to help keep directories tidy and make files easier to locate.

This is a learning project to practice Python programming, focusing on file system operations, loops, conditional logic, and potentially data structures like dictionaries.

## Features (Version 1.0 - Planned)

* Scans a user-defined source directory (initially, a sample test directory).
* Identifies the extension of each file.
* Creates categorized subfolders (e.g., "Images," "Documents," "Archives," "Videos," "Audio," "Others") within the source directory if they don't already exist.
* Moves files into their respective category subfolders.
* Handles a predefined set of common file extensions and their corresponding categories.

## How to Use (Initial Setup for Development)

1.  **Set up a sample directory:** Create a folder (e.g., `files_to_organize` in the project root) and populate it with some dummy files of various types (e.g., `.txt`, `.jpg`, `.png`, `.pdf`, `.zip`, `.mp3`, `.mp4`).
2.  **Configure the script:** (Initially, the source directory path will be hardcoded in the script to point to this sample directory for safe testing).
3.  **Run the script:**
    ```bash
    python file_organizer.py
    ```
4.  Check the sample directory to see if files have been organized into new subfolders.

## Technologies Used

* Python 3
* Standard Python Libraries:
    * `os` (for interacting with the operating system, like listing files, creating directories)
    * `shutil` (for file operations like moving files)

## Future Enhancements (Potential Ideas)

* Allow user to specify the source directory via a command-line argument.
* Read extension-to-category mappings from a configuration file (e.g., JSON or text file) to make it easily customizable.
* Implement a "dry run" mode that shows what changes would be made without actually moving any files.
* Add logging of file operations.
* Option to handle duplicate filenames during moves.
* GUI (Graphical User Interface) - much later!

## Learning Journey

This project is part of an ongoing effort to learn Python and apply programming concepts to practical, everyday problems.

---
