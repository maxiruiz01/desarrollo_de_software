#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    nombre = sys.argv[1].capitalize()
else:
    nombre = ""
print(f"Hola {nombre}")
