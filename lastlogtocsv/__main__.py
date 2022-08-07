import argparse
import os
import sys
from sys import argv
from traceback import print_exc
from typing import Any, Dict, List, Optional
import csv
import struct
from functools import partial
from typing import Dict
from typing_extensions import Literal, Protocol

LEGACY: Literal["L"] = "L"
ACTUAL: Literal["A"] = "A"
StyleKeyType = Literal["L", "A"]
STYLES: Dict[StyleKeyType, str] = dict((
    (LEGACY, "I8s16s"),
    (ACTUAL, "I32s256s")
))

DEFAULT_STYLE = ACTUAL


class BinaryReadable(Protocol):
    """Represent a bianry reader file."""
    def read(self, size: int) -> bytes:
        ...


class TextWritable(Protocol):
    """Represent a text writer file."""
    def write(self, data: str) -> int:
        ...


def lastlog_to_csv(
    lastlog_in: BinaryReadable,
    csv_out: TextWritable,
    style: StyleKeyType = DEFAULT_STYLE
) -> None:
    """Convert an lastlog input stream to an csv output stream."""
    fmt = STYLES[style]
    structure = struct.Struct(fmt)
    writer = csv.writer(csv_out, lineterminator="\n")
    for block in iter(partial(lastlog_in.read, structure.size), b""):
        if any(block):
            timestamp: int
            line: bytes
            host: bytes
            timestamp, line, host = structure.unpack(block)
            writer.writerow((timestamp,
                             line.rstrip(b"\x00").decode("utf8"),
                             host.rstrip(b"\x00").decode("utf8")))



def clear():
    os.system("cls" if os.name=="nt" else "clear")



def get_banner(my_banner):
     def wrapper():
        clear()
        banner="""
.__                   __  .__                 __                               
|  | _____    _______/  |_|  |   ____   _____/  |_  ____   ____   _________  __
|  | \__  \  /  ___/\   __\  |  /  _ \ / ___\   __\/  _ \_/ ___\ /  ___/\  \/ /
|  |__/ __ \_\___ \  |  | |  |_(  <_> ) /_/  >  | (  <_> )  \___ \___ \  \   / 
|____(____  /____  > |__| |____/\____/\___  /|__|  \____/ \___  >____  >  \_/  
          \/     \/                  /_____/                  \/     \/                              
"""
        print(banner)
        print("")
        my_banner()

     return wrapper



@get_banner
def Check_UserInput():
    WordListUsage=["--help","-help","--h","-h","/help","/h","--usage","-usage","--u","-u","/usage","/u"]
    WordListFile=["--file","-file","/file","--f","-f","/f","--input","-input","/input"]
    WordListAuto=["--auto","-auto","/auto","--a","-a","/a","--default","-default","/default"]
    if len(sys.argv)==1 or str(sys.argv[1]) in WordListUsage:
        usage()
    elif len(sys.argv)>=2 and str(sys.argv[1]) in WordListFile:
        default()
    elif len(sys.argv)>=2 and str(sys.argv[1]) in WordListAuto:
        auto()
    else:
        print("\033[0;31mAn unexpected error was caused.\033[00m")
        exit(1)



def usage():
    print("Usage: python3 main.py OPTION")
    print("")
    print("OPTIONS:")
    print("     --help, -help: display this help message.")
    print("")
    print("OPTIONS/ARGS:")
    print("     --file /var/log/lastlog: Lastlog file location")
    print("     --outfile ./lastlog.csv: Lastlog.csv file location.")
    print("     --auto: Automatic identification and extraction (works only on Unix-like systems).")
    print("")
    print("EXAMPLES:")
    print("     python3 ./main.py --file /var/log/lastlog --outfile ./lastlog.csv")
    print("     python3 ./main.py --auto")
    print("")
    exit(0)



def func_lastlogtocsv(lastlog_path, csv_path):
    with open(lastlog_path, "rb") as lastlog_in:
        if csv_path:
            with open(csv_path, "wt", encoding="utf8") as out:
                lastlog_to_csv(lastlog_in, out)




def Ask_Yes_Or_No(question):
    answer = input(question + " (Y/N): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("\033[0;31mA response is required to continue.\033[00m\n")
        answer = input(question + "(Y/N): ").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False

def auto():
    if os.name == 'nt':
        print("\033[0;31mWarning : The --auto option only works on Linux-like systems.\033[00m")
        print("")
        print("\033[0;31mExit of the program.\033[00m")
        exit(1)
    else:
        lastlog_path='/var/log/lastlog'
        csv_path='./lastlog.csv'
        print("Selected lastlog file : "+lastlog_path)
        print("Selected csv path : "+csv_path)
        print("")
        with open(lastlog_path, "rb") as lastlog_in:
            if csv_path:
                with open(csv_path, "wt", encoding="utf8") as out:
                    lastlog_to_csv(lastlog_in, out)



def default():
    if len(sys.argv)==2:
        print("\033[0;31mWarning : You must specify arguments to the parameters. If you don't want to specify any file, the file /var/log/lastlog will be used by default for input and ./lastlog.csv for output. Note that if you want to use the default settings, you can use the --auto parameter (works only under Unix-like systems).\033[00m")
        print("")

        if Ask_Yes_Or_No("Do you want to continue with /var/log/lastlog as default input and ./lastlog.csv as default output"):
            auto()
        
        else:
            print("\033[0;31mExit of the program.\033[00m")
            exit(1)

    elif len(sys.argv)==3 or len(sys.argv)==5:
        lastlog_path=str(sys.argv[2])
        csv_path=str(sys.argv[4])

        print("Selected lastlog file : "+lastlog_path)
        print("Selected csv path : "+csv_path)
        print("")
        with open(lastlog_path, "rb") as lastlog_in:
            if csv_path:
                with open(csv_path, "wt", encoding="utf8") as out:
                    lastlog_to_csv(lastlog_in, out)

    elif len(sys.argv)==4 or len(sys.argv)>=6:
        print("\033[0;31mInconsistency in the number of parameters and arguments.\033[00m")
        exit(1)

    else:
        print("\033[0;31mAn unexpected error was caused.\033[00m")
        exit(1)



if __name__ == "__main__":
    clear()
    Check_UserInput()   
