import sys
from commands import commands_dictionary


if __name__ == "__main__":
    try:
        command_name = sys.argv[1]
        command = commands_dictionary[command_name]
        command(*sys.argv[2:])
    except:
        print("Arguments invalid!")