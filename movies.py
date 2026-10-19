
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
            print(f"user choice 2 is: {user_choice}")

        elif user_choice == "3":
            print(f"user choice 3 is: {user_choice}")

        elif user_choice == "4":
            print(f"user choice 4 is: {user_choice}")

        elif user_choice == "5":
            print(f"user choice 5 is: {user_choice}")

        elif user_choice == "6":
            print(f"user choice 6 is: {user_choice}")

        elif user_choice == "7":
            print(f"user choice 7 is: {user_choice}")

        elif user_choice == "8":
            print(f"user choice 8 is: {user_choice}")

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
def list_all_movies(movies):
    print("All available Movies:")
    for movie in movies:
        print(movie)

    input("\nPress Enter to go back to the main menu...")



if __name__ == "__main__":
    main()
