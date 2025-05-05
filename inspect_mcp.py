import inspect
from mcpcli.__main__ import main

# Print the signature of the main function
print(inspect.signature(main))
print(inspect.getdoc(main))
