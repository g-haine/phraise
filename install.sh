#!/usr/bin/env bash
# Create or update the maintenance environment; never activate/deactivate it here.
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if ! command -v conda >/dev/null 2>&1; then
  printf 'Conda is required. Install Miniforge or Miniconda, then rerun this script.\n' >&2
  exit 1
fi
if [[ $# -gt 0 ]]; then
  printf 'Usage: bash install.sh\n' >&2
  exit 2
fi
if conda list --name phraise --json >/dev/null 2>&1; then
  conda env update --name phraise --file "$script_dir/phraise.yml"
else
  conda env create --name phraise --file "$script_dir/phraise.yml"
fi
printf '\nEnvironment ready. Run: conda activate phraise\n'
printf 'Tests: python -m unittest discover -s "%s/docs/tests" -v\n' "$script_dir"
