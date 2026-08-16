#!/usr/bin/env python3

"""
Description: This Python script is for my own note taking system. I can just run the cli tool and then it will automatically init work environment for that day.
Author: Ben
"""

from datetime import date
from pathlib import Path

NOTES_FILE_NAME = "NOTES.md"

note_template_content = """

# {date}

---

## TODAY'S OBJECTIVES

---

## IMPORTANT NOTES

"""

def main():

    # get the day of today
    today = date.today()

    # format the string for today's date
    today_date_string = today.strftime("%d-%m-%Y")
    today_string_for_notes = today.strftime("%A, %B %d %Y").upper()
    month_dir_string = today.strftime("%Y-%B").lower()

    # ensure that today's directory exist
    absolute_day_dir = Path("/Users/benedictestefanhalkin/Developer/lndata/carbon64/md-notes") / month_dir_string / today_date_string

    print(f"Target Directory: {absolute_day_dir}")
        
    # if directory exisdt
    if absolute_day_dir.is_dir():
        # ensure NOTES.md exist and is not empty
        if ensure_notes_exist(absolute_day_dir):
            print("[SKIP] NOTES.md already exists, skipping file creation.")

        else:
            print(f"[FOUND] Target directory exists, creating notes file...")
            create_notes_file(absolute_day_dir, today_string_for_notes)

            print("[SUCCESS] NOTES.md created with template.")
    else:
        print("[CREATING] Day level directory not found, creating...")

        absolute_day_dir.mkdir(parents=True, exist_ok=True)
        print(f"[CREATED] Day level directory created at {absolute_day_dir}")

        create_notes_file(absolute_day_dir, today_string_for_notes)

        print("[SUCCESS] Created NOTES.md under new day-level directory")


def create_notes_file(absolute_day_dir: Path, day_string: str):
        notes_dir = absolute_day_dir / NOTES_FILE_NAME

        with open(notes_dir, "w", encoding="utf-8") as file:
            file.write(note_template_content.format(date=day_string))


def ensure_notes_exist(absolute_day_dir: Path):
    notes_dir = absolute_day_dir / NOTES_FILE_NAME
    if notes_dir.is_file():
        return True
    else:
        return False

# if running the file directly
if __name__ == "__main__":
    main()
