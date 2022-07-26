import pathlib
import yaml

file_path = pathlib.Path("./config.yaml").resolve()
text = {'name': 'Ola', 'age': 18, 'children': ["Ope", "Oye"]}
with file_path.open(mode="w") as f:
    yaml.dump(text, f, sort_keys=False)

with file_path.open(mode='r', encoding='utf-8') as file:
    text_two = yaml.load(file, Loader=yaml.Loader)
    print(text)
    print(text_two)
# Both are used to save files
