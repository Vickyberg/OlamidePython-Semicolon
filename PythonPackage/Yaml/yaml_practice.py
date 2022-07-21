import pathlib
import yaml

file_path = pathlib.Path("./config.yaml").resolve()
text = {'name': 'Ola', 'age': 18, 'children': ["Ope", "Oye"]}
with file_path.open(mode="w") as f:
    yaml.dump(text, f)