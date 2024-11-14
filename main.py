from cli import clear_console
from game_logic.welcome import welcome
from modes.attack_mode import run_attack_mode
from modes.classic_mode import run_classic_mode
from modes.defense_mode import run_defense_mode


def selectmode():
    welcome()

    while True:
        print("Select mode:")
        print("a - Attack Mode")
        print("d - Defense Mode")
        print("c - Classic Mode")
        mode = str(input("Enter your choice: "))
        if mode in ["a", "d", "c"]:
            break
        else:
            clear_console()
            print("Invalid Input! Please select a valid mode.")
            print("-" * 30)

    if mode == "a":
        run_attack_mode()
    elif mode == "d":
        run_defense_mode()
    elif mode == "c":
        run_classic_mode()


if __name__ == "__main__":
    selectmode()
