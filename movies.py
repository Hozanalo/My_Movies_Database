
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
        "Star Wars: Episode V": 8.7
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
            pass

        elif user_choice == "5":
            pass

        elif user_choice == "6":
            pass

        elif user_choice == "7":
            pass

        elif user_choice == "8":
            pass

        else:
            print("Invalid choice. Try again.")
        continue



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


# Display all available Movies
# TODO add total movie count on the top of the list "<Movies Count here> movies in total"
# TODO add movie rating to the right side of each movie
def list_all_movies(movies):

    if len(movies) == 0:
        print("There are no movies to display")
    else:
        print("All available Movies:")
        for movie in movies:
            print(movie)

    input("\nPress Enter to go back to the main menu...")


# Add new movie to Movies list. Validate and check user input
def add_new_movie(movies):
    new_movie_name = input("Enter new movie name: ")

    while True:
        new_movie_rating = input("Enter new movie rating (0-10): ")

        try:
            new_movie_rating = float(new_movie_rating)

            if 0 <= new_movie_rating <= 10 and new_movie_rating * 10 % 1 == 0:
                break
            else:
                print("Invalid rating! Enter a number between 0 and 10 with max 1 decimal place.")

        except ValueError:
            print("Invalid input! Enter a valid number.")

    movies.update({new_movie_name: new_movie_rating})
    print(f"Movie {new_movie_name} with rating {new_movie_rating} successfully added")

    input("\nPress Enter to go back to the main menu...")

    return movies


# Delete movie.
def delete_movie(movies):

    ask_user_delete = input("Enter movie name to delete: ")

    if ask_user_delete in movies:
        del movies[ask_user_delete]
        print(f"{ask_user_delete} successfully deleted")

    else:
        print(f"{ask_user_delete} doesn't exist!")

    input("\nPress Enter to go back to the main menu...")



# TODO: Update movie.

# TODO: Stats.

# TODO: Random movie.

# TODO: Search movie.

# TODO: Movies sorted by rating.

if __name__ == "__main__":
    main()
