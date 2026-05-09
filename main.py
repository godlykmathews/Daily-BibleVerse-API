from fastapi import FastAPI, HTTPException
import csv
import random
from datetime import date

app = FastAPI()

# List to store the verses in memory
bible_verses = []

# Load the CSV file when the app initializes
try:
    with open("Bible.csv", mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Check if the required fields exist in the current row
            if "verse" in row and "reference" in row:
                bible_verses.append({
                    "verse": row["verse"],
                    "reference": row["reference"]
                })
except FileNotFoundError:
    print("Warning: Bible.csv not found. Ensure the file is in the same directory.")


def ensure_verses_available():
    if not bible_verses:
        raise HTTPException(status_code=404, detail="No verses available.")


@app.get("/")
async def get_random_verse():
    ensure_verses_available()

    # Return a random verse as JSON
    return random.choice(bible_verses)


@app.get("/daily")
async def get_daily_verse():
    ensure_verses_available()

    today = date.today()
    verse = bible_verses[today.toordinal() % len(bible_verses)]

    return {
        "date": today.isoformat(),
        "verse": verse["verse"],
        "reference": verse["reference"],
    }
