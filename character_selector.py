# imports

import sys
import time

from colorama import Back, Fore, Style, init

from characters import characters

# init function resets colors defined with Colorama in a single line
init(autoreset=True)

# the function typing animation need a parameter to set the delay, with delay default we can set a default delay to all typing animations
delay_default = 0.03


# the function typing_animation make a animation to all print lines in our code
def typing_animation(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# welcome message
message = "Olá, seja bem-vindo ao menu de escolha de personagens \nSerão apresentadas 3 opções de classes para seu personagem."
typing_animation(message, delay_default)


def menu():
    print(Fore.YELLOW + "     MENU     ")
    typing_animation("Escolha sua classe", delay_default)

    def show_details(characters):
        for key, details in characters.items():
            print("*" * 40)
            print(f"Detalhes de {Fore.GREEN}{key}{Style.RESET_ALL}:")
            for atribute, value in details.items():
                typing_animation(f" • {atribute.capitalize()}: {value}", delay_default)

    show_details(characters)
    typing_animation("Escolha uma das classes: ", delay_default)
    options = ["Guerreiro", "Arqueiro", "Mago"]
    options_lower = [option.lower() for option in options]

    while True:
        input_class = input("Digite o nome da classe que deseja selecionar: ").lower()
        if input_class:
            if input_class in options_lower:
                print(
                    "Sua classe selecionada foi ",
                    Fore.YELLOW + input_class.capitalize() + "!",
                )
                break
            else:
                print(Fore.RED + "Por favor, escolha uma das 3 classes")
                print(Fore.GREEN + "Guerreiro - Arqueiro - Mago")

        else:
            print(Fore.RED + "Escolha uma classe.")


menu()

print("fim do codigo")
