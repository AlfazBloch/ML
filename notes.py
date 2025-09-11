import numpy as np

# List of notes in an octave
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

# A4 is the 49th key on piano (starting from 1)
A4_index = 49
A4_freq = 440

# Generate all 88 keys
piano_keys = []

for key_number in range(1, 89):
    # Calculate number of semitones from A4
    n = key_number - A4_index
    freq = A4_freq * 2**(n / 12)
    
    # Find note name and octave
    note_index = (key_number + 8) % 12  # +8 because piano starts at A0, which corresponds to notes[0]
    octave = (key_number + 8) // 12
    
    note_name = notes[note_index] + str(octave)
    
    piano_keys.append((key_number, note_name, round(freq, 2)))

# Print the results
for key in piano_keys:
    print(f"Key {key[0]:2}: {key[1]:3} - {key[2]} Hz")
