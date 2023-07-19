import shlex
from subprocess import PIPE, Popen


cmd1 = shlex.split("grep -oP '\d+(?=% packet loss)'")
for x in range(1, 256):
    cmd = "ping  -c 1  192.168.1.{}".format(x).split()
    p1 = Popen(cmd, stdout=PIPE, stderr=PIPE)
    lines = p1.communicate()[0].splitlines()
    output = (lines[-2]).rsplit(None,5)
    output = output[-5].rstrip()
    if output == "100%":
        print("{} percent packet loss from unreachable ip {}".format(output, cmd[-1]))
    else:
        print("{} percent packet loss from REACHABLE ip {}".format(output, cmd[-1]))