def LayMe(bet_amount, parlay_list):
    """Calculates and prints parlay odds, bet amount, and potential earnings.

    Args:
        bet_amount (int): The amount of money being bet.
        parlay_list (list): A list of floats representing the odds of each leg
                            in the parlay. Positive odds are entered directly,
                            while negative odds are entered as their absolute 
                            value (e.g., -150 would be entered as 150).
    """
    lay = 1

    for num in parlay_list:
        if num > 0:
            lay *= (num / 100) + 1
        else:
            lay *= (100 / abs(num)) + 1

    print("Here are your odds:", round(lay, 3))
    print("Bet Amount:", bet_amount)
    final = (lay * bet_amount) - bet_amount
    print("And here is your lay calculated Earnings only:", round(final, 2),
          "Best of luck!!! From, Julian")


def main():
    name = input("Welcome to Julian's Parlay Calculator! Enter your name: ")
    print("Hello, " + name + "!")

    # Taking user input as an integer
    age = int(input("Enter your age: "))
    print("You are", age, "years old.")

    bet_amount = int(input("Enter Bet Amount: "))
    if bet_amount > 25:
        print("Being a Degenerate I see... Love it")

    parlay_list = []

    if age >= 21:  # Check if age is 21 or older
        user_input = ""
        while user_input.lower() != "stop":
            user_input = input("Enter odds (+120, -300, etc.) or 'stop' to stop: You must press ener after each number  ")
            if user_input.lower() != "stop":
                parlay_list.append(float(user_input))
            print("Your slip so far:", parlay_list)
        print("Finished inputting.")
    else:
        print("You must be 21 or older to proceed. ")
        return

    # Call the function after getting user input
    LayMe(bet_amount, parlay_list)


if __name__ == "__main__":
    main()