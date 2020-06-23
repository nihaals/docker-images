from __future__ import annotations
import json
import os
from pathlib import Path
from typing import Dict, List

root_path = Path(__file__).parent


class Version:
    def __init__(self, path: str, tags: List[str]) -> None:
        self.name = path.split('/')[1].lower()
        self.path = path
        self.tags = tags


class Image:
    def __init__(self, path: str, versions: List[Version]) -> None:
        self.path = path
        self.name = self.path.title()
        self.image_name = self.path.lower()
        self.versions = versions

    @classmethod
    def from_path(cls, path: str) -> Image:
        image_path = root_path.joinpath(path)
        if image_path.joinpath('info.json').exists() is False:
            raise ValueError(f"Invalid file strucutre for {path}. No info.json")
        with open(os.path.join(path, 'info.json')) as fp:
            info_json = json.load(fp)
        aliases: Dict[str, str] = info_json['aliases']
        sub_paths: List[str] = []
        for sub_item in os.scandir(image_path):
            sub_item_path = image_path.joinpath(sub_item.name)
            if sub_item_path.is_dir() is False:
                continue
            if sub_item_path.joinpath('Dockerfile').exists() is False:
                raise ValueError(f"Invalid file strucutre for {path}/{sub_item.name}. Missing Dockerfile")
            sub_paths.append(sub_item_path.name)
        versions = [Version(f'{path}/{sub_path}', [sub_path]) for sub_path in sub_paths]
        for alias_new in aliases:
            alias_prev = aliases[alias_new]
            for version in versions:
                if version.name == alias_prev:
                    version.tags.append(alias_new)
                    break
            else:
                raise ValueError(f"No tag {alias_prev} in {path}")
        return cls(path, versions)

    def as_out(self) -> List[Dict[str, str]]:
        return [
            {
                'human-name': f'{self.name}: {version.tags[0]}' if len(self.versions) > 1 else self.name,
                'path': version.path,
                'image-name': self.image_name,
                'tags': ','.join(version.tags),
            }
            for version in self.versions
        ]


out = []
for sub_dir in os.scandir(root_path):
    if root_path.joinpath(sub_dir.name, 'info.json').exists() is False:
        continue
    out.extend(Image.from_path(sub_dir.name).as_out())


print(json.dumps({'include': out}))
