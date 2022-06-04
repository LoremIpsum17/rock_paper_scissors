is_running = True

while is_running:

    import random
    print("Let\'s play a game called Rock, Paper, Scissors!")
    R = "rock"
    P = "paper"
    S = "scissor"

    choice_list = [R, P, S]

    player_input = input(
        "Pick a choice?\n['R', 'P', 'S'] : ")
    if player_input == "R":
        cpu_choice = random.choice(choice_list)
        print("Player(", R, ")", ":", "CPU(", cpu_choice, ")")

        if cpu_choice == R:
            print("It's a tie")
            continue

        elif cpu_choice == P:
            print("Cpu Wins")

        elif cpu_choice == S:
            print("You Win")

    elif player_input == "S":
        cpu_choice = random.choice(choice_list)
        print("Player(", S, ")", ":", "CPU(", cpu_choice, ")")

        if cpu_choice == S:
            print("It's a tie")
            continue

        elif cpu_choice == P:
            print("You Win")

        elif cpu_choice == R:
            print("Cpu Wins")

    elif player_input == "P":
        cpu_choice = random.choice(choice_list)
        print("Player(", P, ")", ":", "CPU(", cpu_choice, ")")

        if cpu_choice == P:
            print("It's a tie")
            continue

        elif cpu_choice == S:
            print("Cpu Wins")

        elif cpu_choice == R:
            print("You Win")

    else:
        print("Invalid Entry. Try again")
        continue

    continue_choice = input("Would you like to play again? [Y,N] :")
    if continue_choice == "Y":
        pass
    if continue_choice == "N":
        is_running = False

        print("Thank you for playing.")
