import os

print(os.getenv('LOGNAME'))

print(os.getenv('WOMBAT'))
print(os.getenv('WOMBAT', "WHAAA??"))

print(os.path.expandvars("My name is $LOGNAME"))


