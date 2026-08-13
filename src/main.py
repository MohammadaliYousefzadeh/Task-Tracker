import sys

from src.command import handle_command

def main():
    arguments = sys.argv[1:]

    if not arguments:
        print("No command provided.")
        return

    command = arguments[0]
    command_arguments = arguments[1:]

    handle_command(command, command_arguments)


if __name__ == "__main__":
    main()