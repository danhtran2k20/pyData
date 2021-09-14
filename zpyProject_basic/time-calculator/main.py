# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


# print(add_time("11:06 PM", "2:02"))
test = "12:05 AM", "00:05", "Wednesday"
print(f"{test} add: \n{add_time(*test)}")


# Run unit tests automatically
main(module='test_module', exit=False)