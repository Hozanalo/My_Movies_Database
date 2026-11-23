import random
from datetime import datetime


def main():
    # Dictionary to store the movies and the rating
    movies = {
        "The Shawshank Redemption": {
            "rating": 9.5,
            "year": 1994
        },
        "Pulp Fiction": {
            "rating": 8.8,
            "year": 1994
        },
        "The Room": {
            "rating": 3.6,
            "year": 2003
        },
        "The Godfather": {
            "rating": 9.2,
            "year": 1972
        },
        "The Godfather: Part II": {
            "rating": 9.0,
            "year": 1974
        },
        "The Dark Knight": {
            "rating": 9.0,
            "year": 2008
        },
        "12 Angry Men": {
            "rating": 8.9,
            "year": 1957
        },
        "Everything Everywhere All At Once": {
            "rating": 8.9,
            "year": 2022
        },
        "Forrest Gump": {
            "rating": 8.8,
            "year": 1994
        },
        "Star Wars: Episode V": {
            "rating": 8.7,
            "year": 1980
        },
        "q": {
            "rating": 8.1,
            "year": 1977
        }
    }

    # Handle user input handling for options 0-8.
    # Display an error message for invalid choices and allow users to select another option
    while True:
        run_menu()
        user_choice = input("Enter choice (0-8): ")

        if user_choice == "0":
            print("Bye!")
            break

        elif user_choice == "1":
            list_all_movies(movies)

        elif user_choice == "2":
            add_new_movie(movies)

        elif user_choice == "3":
            delete_movie(movies)

        elif user_choice == "4":
            update_movie_rate(movies)

        elif user_choice == "5":
            movies_stats(movies)

        elif user_choice == "6":
            random_movie(movies)

        elif user_choice == "7":
            search_movies(movies)

        elif user_choice == "8":
            movies_sorted(movies)

        else:
            print("Invalid choice. Try again.")


# Display the main menu for the user
def run_menu():
    print("********** My Movies Database **********")
    print("""
Menu:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating

    """)


# movie rating input validation
def get_valid_rating():
    while True:
        user_input = input("Enter movie rating (1-10): ")

        try:
            rating = float(user_input)

            if 1 <= rating <= 10 and round(rating, 2) == rating:
                return rating

            print("Invalid rating! Enter a number from 1 to 10 with at most 2 decimal places.")

        except ValueError:
            print("Invalid input! Enter a valid number.")



# movie year input validation
def get_valid_year():
    current_year = datetime.now().year

    while True:
        user_input = input("Enter movie release year: ").strip()

        try:
            year = int(user_input)

            if 1888 <= year <= current_year + 5:
                return year

            print(f"Enter a year between 1888 and {current_year + 5}.")

        except ValueError:
            print("Invalid input! Enter a valid year.")



# Display all available Movies
def list_all_movies(movies):
    if len(movies) == 0:
        print("There are no movies to display")
    else:
        total_movies = len(movies)
        print(f"\n------- {total_movies} movies in total -------")

        for title, data in movies.items():
            rating = data["rating"]
            year = data["year"]
            print(f"- {title}: {rating} - {year}")

    input("\nPress Enter to go back to the main menu...")


# Add new movie to Movies list. Validate and check user input
def add_new_movie(movies):
    while True:
        new_movie_name = input("Enter new movie name: ").strip()

        if not new_movie_name:
            print("Movie name cannot be empty! Try again.")
            continue

        if new_movie_name in movies:
            print("Movie already exists! Try again.")
            continue

        break

    new_movie_rating = get_valid_rating()
    new_movie_year = get_valid_year()

    movies[new_movie_name] = {
        "rating": new_movie_rating,
        "year": new_movie_year
    }

    print(f"Movie {new_movie_name} with rating: {new_movie_rating} and year: {new_movie_year} successfully added")

    input("\nPress Enter to go back to the main menu...")


# Delete movie.
def delete_movie(movies):

    ask_user_delete = input("Enter movie name to delete: ").strip()

    if ask_user_delete in movies:
        del movies[ask_user_delete]
        print(f"{ask_user_delete} successfully deleted")

    else:
        print(f"{ask_user_delete} doesn't exist!")

    input("\nPress Enter to go back to the main menu...")


# update the rating of an existing movie.
def update_movie_rate(movies):
    ask_user_update_name = input("Enter movie name: ").strip()

    if ask_user_update_name not in movies:
        print(f"Movie {ask_user_update_name} doesn't exist!")
    else:
        new_movie_rating = get_valid_rating()

        movies[ask_user_update_name]["rating"] = new_movie_rating

        print(f"Movie {ask_user_update_name} successfully updated")

    input("\nPress Enter to go back to the main menu...")



def movies_stats(movies):
    if len(movies) == 0:
        print("There are no movies in the list to display their stats")
    else:
        ratings = [movie["rating"] for movie in movies.values()]

        highest_rating = max(ratings)
        lowest_rating = min(ratings)
        rating_average = sum(ratings) / len(ratings)

        values = sorted(ratings)
        n = len(values)
        rating_median = (values[(n-1)//2] + values[n//2]) / 2

        print(f"- Average rating: {rating_average:.2f}")
        print(f"- Median rating: {rating_median}")

        # Display all movies with the highest rating
        print("- Best movies:")
        for title, data in movies.items():
            if data["rating"] == highest_rating:
                print(f"  {title}, {data['rating']}")

        # Display all movies with the lowest rating
        print("- Worst movies:")
        for title, data in movies.items():
            if data["rating"] == lowest_rating:
                print(f"  {title}, {data['rating']}")

    input("\nPress Enter to go back to the main menu...")

# Random movie.
def random_movie(movies):
    if len(movies) == 0:
        print("There are no movies to choose from")
    else:
        movie = random.choice(list(movies.keys()))
        print(f"Random movie: {movie}, {movies[movie]['rating']} ({movies[movie]['year']})")

    input("\nPress Enter to go back to the main menu...")


# Search movies.
def search_movies(movies):
    ask_user_search_movies = input("Enter part of movie name: ").strip().lower()

    if not ask_user_search_movies:
        print("Search cannot be empty!")
        input("\nPress Enter to go back to the main menu...")
        return

    if len(movies) == 0:
        print("There are no movies to choose from")
    else:
        found = False
        for title, data in movies.items():
            if ask_user_search_movies in title.lower():
                print(f"{title}, {data['rating']} ({data['year']})")
                found = True

        if not found:
            print("No matching movies found!")

    input("\nPress Enter to go back to the main menu...")


#Movies sorted by rating.
def movies_sorted(movies):
    if len(movies) == 0:
        print("There are no movies in the list to show!")
    else:
        sorted_movies = sorted(
            movies.items(),
            key = lambda item: item[1]["rating"],
            reverse = True
        )

        for title, data in sorted_movies:
            print(f"{title}, {data['rating']}")

    input("\nPress Enter to go back to the main menu...")


if __name__ == "__main__":
    main()
