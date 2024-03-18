def binary_search_guess():
    low = 1
    high = 1000
    tries = 0
    max_tries = 10

    while low <= high and tries < max_tries:
        mid = (low + high) // 2
        print(f"My guess is {mid}. Is it too high (H), too low (L), or correct (C)?")
        feedback = input().upper()
        tries += 1

        if feedback == "C":
            print(f"Yay! I guessed it in {tries} tries!")
            return
        elif feedback == "H":
            high = mid - 1
        elif feedback == "L":
            low = mid + 1
        else:
            print("Invalid input. Please enter H, L, or C.")
            tries -= 1  # Don't count invalid attempts

    print("Oops! I ran out of tries or something went wrong.")

binary_search_guess()
