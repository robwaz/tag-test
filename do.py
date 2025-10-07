#!/usr/bin/env python3

import json
import yaml
from pathlib import Path

def convert_tags_json_to_yaml():
    # Find all tags.yml files
    base_path = Path.cwd()
    tags_yaml_files = base_path.glob('**/tags.yml')

    for yaml_file in tags_yaml_files:
        # Read the YAML file
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)

        # Remove the summary entry
        if 'summary' in data:
            del data['summary']

        # Write the YAML file back
        with open(yaml_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)

        print(f"Processed: {yaml_file}")

if __name__ == "__main__":
    convert_tags_json_to_yaml()
