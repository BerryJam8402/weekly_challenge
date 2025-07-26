# VOWEL SKEWER AUTHENTICATOR
# TODO 1: Skewers must begin and end with a consonant.
# TODO 2: Skewers must alternate between consonants and vowels.
# TODO 3: There must be an even spacing between each letter on the skewer, so that there is a consistent flavour
#  throughout.
# TODO 4: Create a function which returns whether a given vowel skewer is authentic.
# TODO 5: Strings without any actual skewer "-" or letters should return False.
-----------------------------------------------------------------------------------------------------------------
skewer1 = "B--A--N--A--N--A--S"
skewer2 = "A--X--E"
skewer3 = "C-L-A-P"
skewer4 = "M--A---T-E-S"


def is_authentic_skewer(letters):
    vowels = ["A", "E", "I", "O", "U"]
    letters2 = ""
    pattern = []
    check = []
    value = 0
    skewer_count = 0
    # Modifies skewer in function for validating parameters
    for char in letters:
        if char == "-":
            skewer_count += 1
        else:
            letters2 += char
    # Consistency check
    if skewer_count % 2 != 0:
        return False
    # Pattern scheme
    for char in letters2:
        if char in vowels:
            pattern.append(0)
        else:
            pattern.append(1)
    # Checks for consonants at start and end of skewer
    if pattern[-1] and pattern[0] == 0:
        return False
    # Checks for alternating vowel / consonant sequence
    for _ in letters2:
        if value % 2 == 0:
            check.append(1)
        else:
            check.append(0)
        value += 1
    if check != pattern:
        return False
    else:
        return True


print(is_authentic_skewer(skewer1))
print(is_authentic_skewer(skewer2))
print(is_authentic_skewer(skewer3))
print(is_authentic_skewer(skewer4))
