#!/usr/bin/env python3
import argparse
import os

parser = argparse.ArgumentParser()


def installDependencies():
    print("Installing Dependencies...")
    os.system("pip3 install -r requirements.txt")


def runProject():
    print("Running Application")
    os.system("python3 application/app.py")


def cleanProject():
    print("Cleaning Project...")
    os.system("sudo rm -rf __pycache__")


parser.add_argument("--mode", required=True)

args = parser.parse_args()

if args.mode == "clean":
    cleanProject()
elif args.mode == "run":
    runProject()
elif args.mode == "get":
    installDependencies()
else:
    print("Invalid")
