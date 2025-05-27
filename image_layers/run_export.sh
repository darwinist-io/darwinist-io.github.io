#!/bin/bash

PY_SCRIPT_PATH="export_layers_to_png.py"

GIMP_EXEC="/Applications/GIMP.app/Contents/MacOS/gimp"

"$GIMP_EXEC" --quit -i --batch-interpreter=python-fu-eval -b "import sys; sys.argv = ['script', '$IMAGE_PATH', '$OUTPUT_DIR']; exec(open('$PY_SCRIPT_PATH').read())"
