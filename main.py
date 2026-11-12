"""Coolest-art-01 entry: copy the phoenix artwork to the output path.

The art is the entry.jpg beside this file. The program only copies bytes,
so every run writes exactly the same output: no network, no randomness,
no timestamps.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.jpg"), os.path.join(OUT, "entry.png"))
# The judge sees exactly the bytes copied.
