"""Coffee machine start file"""
from machine import Machine
from machine import MachineState

def main():
    """coffeemachine main function"""
    print("\t\tCOFFEEMACHINE\n\n")
    coffeemachine = Machine()
    try:
        while True:
            coffeemachine.print_interface()
            user_input = input("> ")
            coffeemachine.input_method(user_input.lower().strip())
            if coffeemachine.action == MachineState.EXITING:
                break
    except KeyboardInterrupt:
        print("Exiting...")
    print("Goodbye...")

if __name__ == "__main__":
    main()
