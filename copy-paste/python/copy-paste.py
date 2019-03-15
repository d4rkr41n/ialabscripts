#!/usr/bin/env python3
import argparse
import sys
import time

import pyautogui
import pyperclip


parser = argparse.ArgumentParser(description='Paste text from some source into the IA Lab (source defaults to STDIN if no other sources are provided).')

parser.add_argument('-c', "--clipboard", action="store_true", default=None, help='Indicate that you want to use the clipboard for input')
parser.add_argument('-d', "--delay", default=5, help='How long you want the script to wait before sending the text as keystrokes', type=float)
parser.add_argument('-f', "--file", default=None, help='Indicate that you want to use a file for input')
parser.add_argument('-td', "--typewrite-delay", default=.02, help='How long you want the delay to be between each character output as keystrokes from the source', type=float)

args = parser.parse_args()

print("You have {} seconds to set your cursor".format(args.delay))
time.sleep(args.delay)

source = ""

if args.clipboard:
    source = pyperclip.paste()
elif args.file:
    with open(args.file) as input_file:
        source = input_file.read()
else:
    source = sys.stdin.read()

pyautogui.typewrite(source, 0.02)
