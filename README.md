# Daily Bible Verse API

A small FastAPI project that serves Bible verses/quotes from a CSV file. The API loads verses from `Bible.csv` and returns one verse as JSON, making it easy to power a daily Bible verse widget, app, bot, or website.

The included `clean.py` script helps convert raw verse text from `input.txt` into a clean CSV format that the API can read.

## Features

- FastAPI-based Bible verse API
- Random verse response from `Bible.csv`
- Daily verse endpoint that returns the same verse for one calendar day
- UTF-8 CSV support for Malayalam Bible verses
- Simple text-to-CSV formatter in `clean.py`
- Output format ready for API use: `verse,reference`

## Project Structure

```text
.
├── main.py            # FastAPI app
├── clean.py           # Converts raw input text into formatted CSV
├── input.txt          # Raw Bible verse text input
├── Bible.csv          # CSV data used by the API
├── requirements.txt   # Python dependencies
└── README.md
```

## Requirements

- Python 3.9+
- pip

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run The API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/
```

Example response:

```json
{
  "verse": "യഹോവ എന്റെ ഇടയനാകുന്നു; എനിക്കു മുട്ടുണ്ടാകയില്ല.",
  "reference": "സങ്കീർത്തനങ്ങൾ 23:1"
}
```

## API Endpoint

### `GET /`

Returns a random Bible verse from `Bible.csv`.

Response format:

```json
{
  "verse": "Bible verse text",
  "reference": "Book chapter:verse"
}
```

If no verses are available, the API returns:

```json
{
  "detail": "No verses available."
}
```

### `GET /daily`

Returns one Bible verse for the current day. The verse is selected from the current server date, so every request on the same day returns the same verse.

Open:

```text
http://127.0.0.1:8000/daily
```

Response format:

```json
{
  "date": "2026-05-09",
  "verse": "Bible verse text",
  "reference": "Book chapter:verse"
}
```

Example response:

```json
{
  "date": "2026-05-09",
  "verse": "യഹോവ എന്റെ ഇടയനാകുന്നു; എനിക്കു മുട്ടുണ്ടാകയില്ല.",
  "reference": "സങ്കീർത്തനങ്ങൾ 23:1"
}
```

If no verses are available, the API returns:

```json
{
  "detail": "No verses available."
}
```

## CSV Format

The API expects `Bible.csv` to contain these columns:

```csv
"verse","reference"
"Verse text here","Book 1:1"
```

Example:

```csv
"യഹോവ എന്റെ ഇടയനാകുന്നു; എനിക്കു മുട്ടുണ്ടാകയില്ല.","സങ്കീർത്തനങ്ങൾ 23:1"
```

## Cleaning And Formatting Verse Data

Use `clean.py` to convert raw Bible verse text from `input.txt` into a formatted CSV file.

Run:

```bash
python clean.py
```

Current behavior:

- Reads raw text from `input.txt`
- Detects Bible references such as `മത്തായി 6:33` or `സങ്കീർത്തനങ്ങൾ 37:25`
- Writes formatted CSV output to `perfect_output.csv`
- Uses CSV headers: `verse`, `reference`
- Quotes all CSV fields for safer API parsing

After generating `perfect_output.csv`, rename or copy it to `Bible.csv` if you want the API to use the cleaned output.

## Contributing

Contributions are welcome. Good ways to help:

- Add more Bible verses
- Improve verse/reference parsing in `clean.py`
- Add new API endpoints, such as verse by reference or verse of the day
- Add tests for the API and CSV cleaning script
- Improve documentation or examples
- Add deployment instructions

Suggested workflow:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test the API locally.
5. Open a pull request with a clear description.

Please keep CSV data in this format:

```csv
"verse","reference"
```

## Possible Future Improvements

- Add search by book, chapter, or reference
- Add pagination for all verses
- Add language metadata
- Add automated tests
- Add Docker support
