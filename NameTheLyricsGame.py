import random

# Dictionary of songs with their lyrics (word to guess is marked with BLANK)
lyrics_database = {
    "Bohemian Rhapsody": {
        "lyric": "Is this the real life? Is this just BLANK?",
        "answer": "fantasy"
    },
    "Sweet Dreams": {
        "lyric": "Sweet dreams are made of BLANK",
        "answer": "this"
    },
    "Hey Jude": {
        "lyric": "Hey Jude, don't make it BLANK",
        "answer": "bad"
    },
    "Imagine": {
        "lyric": "Imagine there's no BLANK",
        "answer": "heaven"
    }
}

def play_game():
    print("Welcome to Name the Lyrics!")
    print("Try to guess the missing word in these famous song lyrics.")
    print("----------------------------------------")
    
    # Select random song
    song_title = random.choice(list(lyrics_database.keys()))
    song_data = lyrics_database[song_title]
    attempts = 0
    
    while True:
        attempts += 1
        print(f"\nSong: {song_title}")
        print(f"Lyric: {song_data['lyric']}")
        
        guess = input("What's the missing word? ").lower().strip()
        
        if guess == song_data['answer']:
            print(f"\nCongratulations! You got it in {attempts} attempts!")
            print(f"The complete lyric is: {song_data['lyric'].replace('BLANK', song_data['answer'])}")
            break
        else:
            print("Sorry, that's not correct. Try again!")
            if attempts == 3:
                print(f"Hint: The word starts with '{song_data['answer'][0]}'")

if __name__ == "__main__":
    while True:
        play_game()
        if input("\nWant to play again? (yes/no): ").lower().strip() != 'yes':
            print("Thanks for playing!")
            break