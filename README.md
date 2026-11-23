# My Movies Database

A Python command-line app for managing a personal movie collection. Movie titles, ratings, and release years are stored in a JSON file so changes are available the next time you run the app.

## Features

- List, add, update, and delete movies
- Search movies by title
- Sort movies by rating
- View rating statistics
- Pick a random movie
- Validate movie ratings and release years

## Requirements

- Python 3

## Getting Started

Make sure `data.json` exists in the project folder and contains valid JSON. To start with an empty collection, its contents can be:

```json
{}
```

Run the app from the project folder:

```bash
python movies.py
```

Choose an option from the menu. Select `0` to exit.

## Project Files

- `movies.py` — menu, prompts, and movie features
- `movie_storage.py` — reads and saves movie data
- `data.json` — movie collection
