from fastapi import FastAPI, HTTPException
import csv
import random

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

@app.get("/")
async def get_random_verse():
    # If the list is empty (e.g., file was missing or empty), return an error
    if not bible_verses:
        raise HTTPException(status_code=404, detail="No verses available.")
    
    # Return a random verse as JSON
    return random.choice(bible_verses)