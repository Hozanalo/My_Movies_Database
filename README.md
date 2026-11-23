# My Movies Database

A Python command-line app for managing a personal movie collection. Each movie has a title, release year, and rating. Changes are saved automatically in a JSON file and remain available after restarting the app.

## Features

- List movies with their ratings and release years
- Add and delete movies
- Update movie ratings
- View average, median, highest, and lowest ratings
- Pick a random movie
- Search by part of a movie title
- Sort movies from highest to lowest rating
- Check user input for valid titles, ratings, and years

## Requirements

- Python 3
- Git, if cloning the repository

No extra Python packages are required.

## Getting Started

**1. Download the project**

Clone the repository:

```bash
git clone https://github.com/Hozanalo/My_Movies_Database.git
```

Or select **Code → Download ZIP** on GitHub and extract the downloaded folder.

**2. Open the project folder in a terminal**

If you cloned the repository:

```bash
cd My_Movies_Database
```

**3. Check the data file**

The project folder must contain `data.json`. The app reads this file at startup and saves movie changes to it.

If the file is missing, create it with these contents:

```json
{}
```

This starts an empty movie collection.

**4. Start the app**

```bash
python movies.py
```

On systems where Python 3 uses the `python3` command:

```bash
python3 movies.py
```

## Using the App

Enter the number of the action you want:

```text
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
```

Follow the prompts to enter movie details. Adding, deleting, and updating movies saves changes automatically.

Search accepts part of a title and ignores capitalization. Deleting or updating a movie requires its exact title.

## Project Structure

```text
My_Movies_Database/
├── movies.py          # Menu, user input, and movie features
├── movie_storage.py   # JSON reading and writing
├── data.json          # Saved movie collection
└── README.md          # Project documentation
```

## Data Format

Movies are stored by title, with a rating and release year:

```json
{
    "The Shawshank Redemption": {
        "rating": 9.5,
        "year": 1994
    },
    "Pulp Fiction": {
        "rating": 8.8,
        "year": 1994
    }
}
```
