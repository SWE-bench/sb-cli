# Get Report Command

The `get-report` command retrieves evaluation results for a specific run.

## Usage

```bash
sb-cli get-report <subset> <split> <run_id> [options]
```

## Arguments

- `subset`: Dataset subset (`swe-bench-m`, `swe-bench_lite`, `swe-bench_verified`)
- `split`: Dataset split (`dev` or `test`)
- `run_id`: ID of the run to get results for

## Options

- `--output_dir`, `-o`: Directory to save report files (default: sb-cli-reports)
- `--overwrite`: Overwrite existing report files (0/1, default: 0)
- `--extra_arg`, `-e`: Additional arguments in KEY=VALUE format

## Report Format

The command outputs a summary to the console and saves the evaluation report as JSON:

1. `{subset}__{split}__{run_id}.json`: The full evaluation report
2. `{subset}__{split}__{run_id}.response.json`: Additional response data, when the service returns it

The console summary includes:
- Resolved instances (total and submitted)
- Submission statistics
- Error counts
- Pending evaluations

## Per-instance test logs

The report JSON contains evaluation results. The hosted CLI does not provide a download command for raw evaluator logs such as `test_output.txt`.

For a dataset split available to the [local SWE-bench evaluator](https://github.com/SWE-bench/SWE-bench#-usage), evaluate the same predictions locally to produce test output under `logs/evaluation/<run_id>/`. Local logs describe that local run. To compare outcomes, record the dataset split and evaluation image used.

For a hosted Multimodal leaderboard submission, follow the [submission guide](../submit-to-leaderboard.md) and include the hosted run ID.

## Examples

1. Basic usage:
```bash
sb-cli get-report swe-bench-m dev my_run_id
```

2. Custom output directory:
```bash
sb-cli get-report swe-bench-m dev my_run_id -o ./reports
```

3. Overwrite existing report:
```bash
sb-cli get-report swe-bench-m dev my_run_id --overwrite 1
```
