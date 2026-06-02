def is_valid_trick(trick_name):
    FIRST_WORDS = ["Misty", "Ghost", "Thunder", "Solar", "Sky", "Phantom", "Frozen", "Polar"]
    SECOND_WORDS = ["Twister", "Icequake", "Avalanche", "Vortex", "Snowstorm", "Frostbite", "Blizzard", "Shadow"]
    words = trick_name.split()
    if len(words) != 2 or words[0] not in FIRST_WORDS or words[1] not in SECOND_WORDS:
        return False
    return True

print(is_valid_trick("Polar Vortex"))
print(is_valid_trick("Solar Icequake"))
print(is_valid_trick("Thunder Blizzard"))
print(is_valid_trick("Phantom Frostbite"))
print(is_valid_trick("Ghost Avalanche"))
print(is_valid_trick("Snowstorm Shadow"))
print(is_valid_trick("Solar Sky"))
