#  Copyright (c) 2020. CJ Associates
from subprocess import run, PIPE, CalledProcessError
import shlex
import glob

cmd = 'netstat -anj'
files = glob.glob('*.txt')

# choice 1
# run(cmd, shell=True)
# print('-' * 60)

# choice 2
cmd_words = shlex.split(cmd)
try:
    proc = run(cmd_words, stdout=PIPE, stderr=PIPE)
except CalledProcessError as err:
    print(err, err.returncode)
else:
    lines = proc.stdout.decode().splitlines()
    for line in lines:
        if "ESTAB" in line:
            print(line)
    print(proc.returncode)
    error_lines = proc.stderr.decode()
    print(error_lines)
