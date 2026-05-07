mini-bookmark V2

A CLI tool to save and manage web URLs, developed as part of a university assignment at Samsun Üniversitesi.

Student Information

Name: Hüdanur Şener

Student ID: 251478066

Overview

mini-bookmark is a lightweight command-line interface tool that allows users to store, list, search, and delete web bookmarks. All data is persisted in a plain text file (links.dat) located within a hidden .minibookmark/ directory.

V1 vs V2: What's New?

The project has evolved from V1 to V2 with the following key improvements:

Command Completion: In V1, list and delete were placeholders. In V2, they are fully functional.

URL Validation: V2 introduces a safety check ensuring all added URLs start with 'http' or 'https'.

Formatted Output: The list command now presents data in a clean, professional table format.

Enhanced Error Handling: Improved feedback for missing arguments, invalid IDs, and uninitialized states.

V2 Task List

List Command: Implemented full listing of bookmarks with a formatted header and aligned columns.

Delete Command: Added functionality to remove a specific bookmark entry using its ID number.

Validation Logic: Integrated a prefix check for URLs to prevent malformed data entry.

Installation \& Usage

1\. Initialize the Project

python minibookmark.py init

2\. Add a Bookmark

python minibookmark.py add "Google" "https://google.com"

3\. List All Bookmarks

python minibookmark.py list

4\. Search Bookmarks

python minibookmark.py search "keyword"

5\. Delete a Bookmark

python minibookmark.py delete <id>

Data Format

Data is stored in .minibookmark/links.dat using the following structure:

id|title|url|date

License

Educational purpose only.



