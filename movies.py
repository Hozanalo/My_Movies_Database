
def main():
    # Dictionary to store the movies and the rating
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7,
        "q": 1
    }


    # Handle user input handling for options 1-8.
    # Display an error message for invalid choices and allow users to select another option
    while True:
        run_menu()
        user_choice = input("Enter choice (1-8): ")

        if user_choice == "1":
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
            pass

        elif user_choice == "7":
            pass

        elif user_choice == "8":
            pass

        else:
            print("Invalid choice. Try again.")


# Display the main menu for the user
def run_menu():
    print("********** My Movies Database **********")
    print("""
Menu:
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating

    """)

# Rating input validation
def get_valid_rating():
    while True:
        user_input = input("Enter movie rating (0-10): ")

        try:
            rating = float(user_input)

            if 1 <= rating <= 10 and round(rating, 2) == rating:
                return rating

            print("Invalid rating! Enter 0-10.")

        except ValueError:
            print("Invalid input! Enter a valid number.")


# Display all available Movies
def list_all_movies(movies):
    if len(movies) == 0:
        print("There are no movies to display")
    else:
        total_movies = len(movies)
        print(f"\n--- {total_movies} movies in total ---")

        for movie, rate in movies.items():
            print(f"- {movie} {rate}")

    input("\nPress Enter to go back to the main menu...")


# Add new movie to Movies list. Validate and check user input
def add_new_movie(movies):
    new_movie_name = input("Enter new movie name: ").strip()

    if not new_movie_name:
        print("Movie name cannot be empty!")
        return

    if new_movie_name in movies:
        print("Movie already exists!")
        return

    new_movie_rating = get_valid_rating()

    movies[new_movie_name] = new_movie_rating
    print(f"Movie {new_movie_name} with rating {new_movie_rating} successfully added")

    input("\nPress Enter to go back to the main menu...")


# Delete movie.
def delete_movie(movies):

    ask_user_delete = input("Enter movie name to delete: ")

    if ask_user_delete in movies:
        del movies[ask_user_delete]
        print(f"{ask_user_delete} successfully deleted")

    else:
        print(f"{ask_user_delete} doesn't exist!")

    input("\nPress Enter to go back to the main menu...")


# update the rating of an existing movie.
def update_movie_rate(movies):
    ask_user_update_name = input("Enter movie name: ")

    if ask_user_update_name not in movies:
        print(f"Movie {ask_user_update_name} doesn't exist!")
    else:
        new_movie_rating = get_valid_rating()

        movies[ask_user_update_name] = new_movie_rating

        print(f"Movie {ask_user_update_name} successfully updated")

    input("\nPress Enter to go back to the main menu...")


# Movies stats.

def movies_stats(movies):
    if len(movies) == 0:
        print("There are no movies in the list to display their stats")
    else:
        movies_best = max(movies, key=movies.get)
        movies_worst = min(movies, key=movies.get)
        rating_average = sum(movies.values()) / len(movies)

        # find median rating
        values = sorted(movies.values())
        n = len(values)
        rating_median = (values[(n-1)//2] + values[n//2]) / 2

        print(f"- Average rating: {rating_average:.2f}")
        print(f"- Median rating: {rating_median}")
        print(f"- Best movie: {movies_best}, {movies[movies_best]}")
        print(f"- Worst movie: {movies_worst}, {movies[movies_worst]}")

    input("\nPress Enter to go back to the main menu...")

# TODO: Random movie.

# TODO: Search movie.

# TODO: Movies sorted by rating.

if __name__ == "__main__":
    main()
