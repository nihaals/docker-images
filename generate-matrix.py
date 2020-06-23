import json
import os
from pathlib import Path


paths = []
root = Path(__file__).parent
for sub_dir in os.scandir(root):
    sub_path = root.joinpath(sub_dir.name)
    if sub_path.joinpath('Dockerfile').exists():
        paths.append({
            'name': sub_path.name.title(),
            'path': sub_path.name,
            'image-name': sub_path.name.lower(),
        })

print(json.dumps(
    {
        'include': paths,
    }
))
