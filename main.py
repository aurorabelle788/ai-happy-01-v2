"""ai-happy-01 entry (Python 3.13, standard library only).

The image is the entry.png beside this file, and the program copies it to
/output/entry.png. The gate takes a whole PNG or JPEG of at most 1 MiB and
1024 by 1024 pixels, and the judge sees exactly the bytes copied.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
DST = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)

# Guardrail: fail loudly if the copy is ever incomplete, so a bad run
# is never mistaken for a valid entry.
if os.path.getsize(DST) != os.path.getsize(SRC):
    raise SystemExit("entry.png copy is incomplete")
