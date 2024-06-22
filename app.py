import json

import yaml


class YamlToJsonConverter:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def convert(self):
        try:
            with open(self.yaml_file, 'r') as f:
                yaml_data = yaml.safe_load(f)
                json_data = json.dumps(yaml_data, indent=4)
                return json_data
        except FileNotFoundError:
            return "Error: YAML file not found."


if __name__ == "__main__":
    yaml_file_path = "sample.yaml"
    converter = YamlToJsonConverter(yaml_file_path)
    json_output = converter.convert()
    print(json_output)
