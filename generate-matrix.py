import json
import os
from pathlib import Path
from typing import Self, TypedDict

ROOT_PATH = Path(__file__).parent
ROOT_IMAGES_PATH = ROOT_PATH.joinpath('images')


class InfoDict(TypedDict):
    aliases: dict[str, str]
    platforms: dict[str, list[str]]


class Version:
    """Represents a tag of an image."""

    def __init__(self, path: str, tags: list[str], platforms: list[str]) -> None:
        self.name = path.split('/')[1].lower()
        self.path = path
        self.tags = tags
        self.platforms = platforms


class Image:
    """Represents an image name. Contains `Version`s (tags)."""

    def __init__(self, path: str, versions: list[Version]) -> None:
        self.path = path
        self.name = self.path.title()
        self.image_name = self.path.lower()
        self.versions = versions

    @classmethod
    def from_path(cls, path: str) -> Self:
        """Create an `Image` from its path e.g. `'playground'`."""
        image_path = ROOT_IMAGES_PATH.joinpath(path)
        if image_path.joinpath('info.json').exists() is False:
            # Check if image directory has an `info.json`
            raise ValueError(f"Invalid file structure for {path}. No info.json")
        with open(ROOT_IMAGES_PATH.joinpath(path, 'info.json')) as fp:
            info_json: InfoDict = json.load(fp)

        sub_paths: list[str] = []  # List of paths of `Version`s
        for sub_item in os.scandir(image_path):
            sub_item_path = image_path.joinpath(sub_item.name)
            if sub_item_path.is_dir() is False:
                continue
            # Validate `Version` directory structure
            if sub_item_path.joinpath('Dockerfile').exists() is False:
                raise ValueError(f"Invalid file structure for {path}/{sub_item.name}. Missing Dockerfile")
            sub_paths.append(sub_item_path.name)
        versions = [Version(f'{path}/{sub_path}', [sub_path], info_json['platforms'][sub_path]) for sub_path in sub_paths]

        # Add aliases to list of tags each `Version` represents
        aliases = info_json['aliases']
        for alias_new in aliases:  # The tag that is not defined with a directory name
            # The tag defined by a directory name
            alias_prev = aliases[alias_new]
            for version in versions:
                if version.name == alias_prev:
                    version.tags.append(alias_new)
                    break
            else:
                raise ValueError(f"No tag {alias_prev} in {path}")
        return cls(path, versions)

    def as_out(self) -> list[dict[str, str]]:
        return [
            {
                'human-name': f'{self.name}: {version.tags[0]}' if len(self.versions) > 1 else self.name,
                'path': str(ROOT_IMAGES_PATH.joinpath(version.path).relative_to(ROOT_PATH)),
                'image-name': self.image_name,
                'tags': ','.join(version.tags),
                'platforms': ','.join(version.platforms)
            }
            for version in self.versions
        ]


if __name__ == '__main__':
    out = []
    for sub_dir in os.scandir(ROOT_IMAGES_PATH):
        if ROOT_IMAGES_PATH.joinpath(sub_dir.name, 'info.json').exists() is False:
            continue
        out.extend(Image.from_path(sub_dir.name).as_out())

    print(json.dumps({'include': out}))
