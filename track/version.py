# version.py
APP_NAME = "SquirrelPy"
VERSION = "1.0.3"
BUILD = 42

def bump_build():
  global BUILD
  BUILD += 1
  with open(__file__, "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
  if line.startswith("BUILD"):
    lines[i] = f"BUILD = {BUILD}\n"

with open(__file__, "w") as f:
  f.writelines(lines)
  
APP_NAME ="SquirrelPy"
MAJOR = 1
MINOR = 0
PATCH = 3
BUILD = 42

def version_string():
    return f"{MAJOR}.{MINOR}.{PATCH} (build {BUILD})"
