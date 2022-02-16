

from distutils.command.clean import clean
from lib2to3.pgen2 import token
from operator import truediv
from os import remove
import string

COMMENT_STARTS_WITH = '#'


VALID_COMMANDS = set(["P", "D", "U", "N", "S", "E", "W"])

COMMAND_ARGS = {
    "P": {
        "hasArgs": True,
        "args": [int]
    },
    "D": {
        "hasArgs": False
    },
    "U": {
        "hasArgs": False
    },
    "N": {
        "hasArgs": True,
        "args": [int]
    },
    "S": {
        "hasArgs": True,
        "args": [int]
    },
    "E": {
        "hasArgs": True,
        "args": [int]
    },
    "W": {
        "hasArgs": True,
        "args": [int]
    }

}

def splitArgAndComment(line):
    arg, cm = (a:=line.split(COMMENT_STARTS_WITH))[0],"".join(a[1:])
    return arg,cm

class Command:

    def __init__(self, tokens) -> None:
        if len(tokens)==0:
            return None
        self.command=None
        self.comment=None
        self.arguments=None
        if tokens[0] in VALID_COMMANDS:
            self.command = tokens[0]


            args, self.comment = splitArgAndComment(' '.join(tokens[1:]))
            # print(self.comment)
            details = COMMAND_ARGS[self.command]
            if details['hasArgs']:
                # print("Setting", command, arguments)
                self.arguments = args
        else:
            raise InvalidCommandError

    def __repr__(self) -> str:
        return "Command({}, {}, #{})".format(self.command, self.arguments, self.comment)

def readfile(filePath):
    with open(filePath,'r') as f:
        lines = f.readlines()
        lines = [line.strip("\n") for line in lines]
        return lines



class InvalidCommandError(Exception):
    pass
def createCmd(line):
    tokens = line.split(' ')
    
    c=Command(tokens)
    #First token in a command
    # print(tokens,tokens[0])
    #Depending on the cmd, we knew whether to have args or not
    
    return c




if __name__=='__main__':
    lines = readfile('./turtle.txt')
    for line in lines:
        print(createCmd(line))
