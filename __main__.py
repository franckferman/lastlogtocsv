#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from sys import argv
import argparse
import csv
import struct
from functools import partial
from typing_extensions import Literal, Protocol
from typing import Any, Dict, List, Optional
import argparse
from traceback import print_exc


class ReadBin(Protocol):
    def read(self, size: int) -> bytes:
        pass

"""
This code defines a class called ReadBin which inherits from the Protocol class. 
The read method takes an integer argument representing the number of bytes to read, 
and returns a bytes object containing the data read.
"""

class WriteText(Protocol):
    """Represent a text writer file."""
    def write(self, data: str) -> int:
        pass

"""
This code defines a class called WriteText, which represents a text file that can be written to. 
The write() method takes a string as input and returns an integer.
"""

def lastlog_to_csv(
    lastlog_in: ReadBin,
    csv_out: WriteText,
) -> None:
    format="I32s256s"
    structure=struct.Struct(format)
    writer=csv.writer(csv_out, lineterminator="\n")
    for block in iter(partial(lastlog_in.read, structure.size), b""):
        if any(block):
            timestamp: int
            line: bytes
            host: bytes
            timestamp, line, host = structure.unpack(block)
            writer.writerow((timestamp,
                             line.rstrip(b"\x00").decode("utf8"),
                             host.rstrip(b"\x00").decode("utf8")))

"""
The "lastlog_in" variable is a file object opened in binary mode for reading. 
The "csv_out" variable is a file object opened in text mode for writing.

The "format" variable is a string used by the struct module to describe the format of the data in the lastlog file. 
The "structure" variable is a struct.Struct object created from the "format" string.

cf. Strukturierte Blöcke (https://de.wikibooks.org/wiki/Benutzer:Schmidt2/Druckversion_Python_unter_Linux) :
While log files are mostly text files, there are occasionally system files that have a block-oriented structure. 
For example, the file /var/log/lastlog is a sequence of blocks of fixed length. 
Each block represents the time of the last login, the associated terminal, and the hostname of the computer from which one logged in. 
The user with the user ID 1000 has the thousandth block. The user root with the user ID 0 has the zeroth block.
Once you have found out how the file is structured and which data types are behind the individual entries, you can rebuild the block type with Python's struct module. 
This is what the format string is for, which in the following example mimics the data type of a lastlog entry in a compact form. 
We specify the last login time of the user with user ID 1000, mimicking part of the Unix lastlog command.
"""

def clear():
    os.system("cls" if os.name=="nt" else "clear")



def get_banner(my_banner):
     def wrapper():
        clear()
        banner="""
 ▄█          ▄████████    ▄████████     ███      ▄█        ▄██████▄     ▄██████▄  
███         ███    ███   ███    ███ ▀█████████▄ ███       ███    ███   ███    ███ 
███         ███    ███   ███    █▀     ▀███▀▀██ ███       ███    ███   ███    █▀  
███         ███    ███   ███            ███   ▀ ███       ███    ███  ▄███        
███       ▀███████████ ▀███████████     ███     ███       ███    ███ ▀▀███ ████▄  
███         ███    ███          ███     ███     ███       ███    ███   ███    ███ 
███▌    ▄   ███    ███    ▄█    ███     ███     ███▌    ▄ ███    ███   ███    ███ 
█████▄▄██   ███    █▀   ▄████████▀     ▄████▀   █████▄▄██  ▀██████▀    ████████▀  
▀                                               ▀                                 
    ███      ▄██████▄        ▄████████    ▄████████  ▄█    █▄                     
▀█████████▄ ███    ███      ███    ███   ███    ███ ███    ███                    
   ▀███▀▀██ ███    ███      ███    █▀    ███    █▀  ███    ███                    
    ███   ▀ ███    ███      ███          ███        ███    ███                    
    ███     ███    ███      ███        ▀███████████ ███    ███                    
    ███     ███    ███      ███    █▄           ███ ███    ███                    
    ███     ███    ███      ███    ███    ▄█    ███ ███    ███                    
   ▄████▀    ▀██████▀       ████████▀   ▄████████▀   ▀██████▀                 
"""
        print(banner)
        print("")
        my_banner()

     return wrapper

#Python Decorator



@get_banner
def Check_UserInput():
    WordlistUsage=["--help","-help","/help","--h","-h","/h","--usage","-usage","/usage"]
    WordlistInput=["--file","-file","/file","--f","-f","/f","--input","-input","/input","--i","-i","/i"]
    WordlistOutput=["--output","-output","/output","--outputfile","-outputfile","/outputfile","--out","-out","/out","--o","-o","/o"]
    WordlistAuto=["--auto","-auto","/auto","--a","-a","/a","--automatic","-automatic","/automatic","--default","-default","/default"]
    
    if len(sys.argv)==1 or str(sys.argv[1]) in WordlistUsage:
        usage()

    elif len(sys.argv)>=2 and str(sys.argv[1]) in WordlistInput:
        lastlogtocsv()

    elif len(sys.argv)==2 and str(sys.argv[1]) in WordlistAuto:
        auto()

    else:
        print("\033[0;31mAn unexpected error was caused.\033[00m")
        exit(1)



def usage():
    print("Usage: python3 main.py OPTION")
    print("")
    print("OPTIONS:")
    print("     --help, -help: display this help message.")
    print("     --auto: Automatic identification and extraction (works only on Unix-like systems).")
    print("")
    print("OPTIONS/ARGS:")
    print("     --file /var/log/lastlog: Lastlog file location")
    print("     --outfile ./lastlog.csv: Lastlog.csv file location.")
    print("")
    print("EXAMPLES:")
    print("     python3 ./main.py --file ./lastlog --outfile ./lastlog.csv")
    print("     python3 ./main.py --auto")
    print("")
    exit(0)



def Ask_Yes_Or_No(Question):
    Answer=input(Question+" (Y/N): ").lower().strip()
    print("")
    while not(Answer=="y" or Answer=="yes" or \
    Answer=="n" or Answer=="no"):
        print("\033[0;31mA response is required to continue.\033[00m\n")
        Answer = input(Question + " (Y/N): ").lower().strip()
        print("")
    if Answer[0]=="y":
        return True
    else:
        return False



def auto():
    if os.name=='nt':
        print("\033[0;31mWarning : The --auto option only works on Linux-like systems.\033[00m")
        exit(1)
    else:
        default_lastlog_path='/var/log/lastlog'
        default_csv_path='./lastlog.csv'

        lastlog_path=default_lastlog_path
        csv_path=default_csv_path
        
        print("Path to the lastlog file : "+lastlog_path)
        print("Path to the csv file : "+csv_path)
        
        with open(lastlog_path, "rb") as lastlog_in:
            if csv_path:
                with open(csv_path, "wt", encoding="utf8") as csv_out:
                    lastlog_to_csv(lastlog_in, csv_out)



def lastlogtocsv():
    if len(sys.argv)==2:
        print("""\033[0;31mWarning : You must specify arguments to the parameters.
            If you don't want to specify any file, the file /var/log/lastlog will be used by default for input and ./lastlog.csv for output.
            Note that if you want to use the default settings, you can use the --auto parameter (works only under Unix-like systems).\033[00m""")
        print("")

        if Ask_Yes_Or_No("Do you want to continue with /var/log/lastlog as default input and ./lastlog.csv as default output"):
            auto()
        
        else:
            exit(1)

    elif len(sys.argv)==3 or len(sys.argv)==5:
        lastlog_path=str(sys.argv[2])
        csv_path=str(sys.argv[4])

        print("Selected lastlog file : "+lastlog_path)
        print("Selected csv path : "+csv_path)

        with open(lastlog_path, "rb") as lastlog_in:
            if csv_path:
                with open(csv_path, "wt", encoding="utf8") as csv_out:
                    lastlog_to_csv(lastlog_in, csv_out)

    elif len(sys.argv)==4 or len(sys.argv)>=6:
        print("\033[0;31mInconsistency in the number of parameters and arguments.\033[00m")
        exit(1)

    else:
        print("\033[0;31mAn unexpected error was caused.\033[00m")
        exit(1)



if __name__ == "__main__":
    Check_UserInput()
