"""get_rule_graph"""
import os
import sys


def main():
    script_dir = "gather_benchmarks/"
    rules_path = "workflow/rules"
    rules_file_path = "/tmp/rules.csv"
    crawl_folder = "results/benchmark/"
    memory = "/tmp/max_rss.csv"
    identifier = "max_rss"
    yaml_file = sys.argv[1]
    # get rules with get_rules_benchmark.py
    os.system(
        f"python {script_dir}get_rules_benchmark.py {rules_path} {rules_file_path}"
    )
    # get rules crawler.py
    os.system(f"sed -i '{r's/{[a-zA-Z_]*}/*/g'}' {rules_file_path}")
    os.system(f"sed -i 's/benchmark/./g' {rules_file_path}")
    os.system(
        f"python {script_dir}crawler.py {crawl_folder} {rules_file_path} {memory} {identifier}"
    )
    os.system(
        f"python {script_dir}convert_csv_yaml.py {memory} {yaml_file}"
    )


if __name__ == "__main__":
    main()
