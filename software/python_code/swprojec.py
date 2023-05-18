import pygame
import numpy as np
import os

# Function to play audio files randomly from a given playlist
def play_random_playlist(playlist_directory):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Get a list of audio files in the playlist directory
    playlist = os.listdir(playlist_directory)

    # Shuffle the playlist using numpy
    np.random.shuffle(playlist)

    # Iterate over the shuffled playlist
    for i, audio_file in enumerate(playlist):
        # Get the file path of the audio file
        file_path = os.path.join(playlist_directory, audio_file)

        # Load and play the audio file
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Print the name of the song
        print(f"Now playing: {audio_file}")

        # Wait until the audio playback is finished
        while pygame.mixer.music.get_busy():
            continue

        # Check for user input
        while True:
            user_input = input("Press 'n' to play the next song,or 'q' to quit: ")
            if user_input.lower() == 'n':
                break  # Proceed to the next song
           # elif user_input.lower() == 's':
           #     pygame.mixer.music.stop()
                break  # Skip to the next song
         #   elif user_input.lower() == 'r':
          #      pygame.mixer.music.rewind()  # Repeat the current song
            elif user_input.lower() == 'q':
                pygame.mixer.music.stop()
                return  # Exit the playlist

    # After the playlist ends
    while True:
        user_input = input("Press 'r' to repeat the playlist or 'q' to quit: ")
        if user_input.lower() == 'r':
            # Call the function to play the audio playlist randomly again
            play_random_playlist(playlist_directory)
        elif user_input.lower() == 'q':
            return  # Exit the program

# Specify the directory containing your audio playlist
playlist_directory = "/home/suraj/softwareproject"

# Call the function to play the audio playlist randomly
play_random_playlist(playlist_directory)

