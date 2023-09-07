import sys
import csv
import yaml


def write_yaml(yaml_file_path: str, dump_dict: dict) -> None:
    with open(yaml_file_path, "w", encoding="utf-8") as file:
        yaml.dump(dump_dict, file)


def read_csv(file: str) -> list[list[str]]:
    with open(file, "r") as handler:
        reader = csv.reader(handler)
        return list(reader)[1:]


def read_yaml(yaml_file_path: str) -> dict:
    with open(yaml_file_path, encoding="utf-8") as yaml_file:
        return yaml.load(yaml_file, Loader=yaml.FullLoader)


def main():
    output = sys.argv[2]
    memory: dict[str, int] = {}

    backup_memory: dict[str, int] = read_yaml(
        "./gather_benchmarks/backup_memory.yaml")
    for line in read_csv(sys.argv[1]):
        memory[line[0]] = (int(float(line[1])) + 100) * 2

    for key in backup_memory:
        if key not in memory:
            memory[key] = backup_memory[key]

    write_yaml(output, memory)


if __name__ == "__main__":
    main()
