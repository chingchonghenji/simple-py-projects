
import pyfiglet
ascii_banner = pyfiglet.figlet_format("THE WHITERAT")
print(ascii_banner)

print("Enter 1 to convert and exit to exit the program.")


while True:
    choice = input("Enter your choice: ")
    while True:
        if choice == "1":
            text = input("Enter text to convert: ")
            if text == "exit":
                break
            else:
                print(pyfiglet.figlet_format(text))

        elif choice == "exit":

            break
        else:
            print("Choice not valid.")
            break
   
    if choice == "exit":
        break
