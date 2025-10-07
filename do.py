#!/usr/bin/env python3

import json
import yaml
from pathlib import Path

def convert_tags_json_to_yaml():
    # Find all tags.json files
    base_path = Path.cwd()
    tags_json_files = base_path.glob('**/tags.json')

    for json_file in tags_json_files:
        # Read the JSON file
        with open(json_file, 'r') as f:
            data = json.load(f)

        # Write the YAML file in the same directory
        yaml_file = json_file.parent / 'tags.yml'
        with open(yaml_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)

        print(f"Converted: {json_file} -> {yaml_file}")

if __name__ == "__main__":
    convert_tags_json_to_yaml()
