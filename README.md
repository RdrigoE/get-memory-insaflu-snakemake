# get-memory-insaflu-snakemake
Getting the appropriate memory resources of INSaFLU-Snakemake
```
git clone https://github.com/RdrigoE/get-memory-insaflu-snakemake.git
cd get-memory-insaflu-snakemake
mv gather_benchmarks ../path/to/insaflu_snakemake
```
At INSaFLU-Snakemake folder:
```
python ./gather_benchmarks/get_rule_info.py <file_to_create.yaml>
```

Then you can move it to the config folder and change the memory value in the constants.yaml file to your file name.

