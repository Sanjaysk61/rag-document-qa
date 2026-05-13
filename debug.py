import os
from pathlib import Path

env_path = Path(__file__).parent / ".env"

print("Looking for .env at:", env_path)
print("File exists:", env_path.exists())

# Also print the actual contents if found
if env_path.exists():
    print("Contents:", env_path.read_text())
else:
    print("Files in this folder:", list(Path(__file__).parent.iterdir()))