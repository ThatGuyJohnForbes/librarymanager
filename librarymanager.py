#!/usr/bin/env python3

import os
import asyncio
import tmdb

def check_dir(path):
    files = os.listdir(path)
    for f in files:
        print(f)

if __name__ == "__main__":
    dirs = [x[0] for x in os.walk('.') if x[0] != '.' and x[0] != ".."]
    for dir in dirs:
        check_dir(dir)


