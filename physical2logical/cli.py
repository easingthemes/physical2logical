import argparse
from pathlib import Path

from analyze import analyze
from process_files import update_files

parser = argparse.ArgumentParser()
parser.add_argument('source')
parser.add_argument('-r', '--recursive', action='store_true')
parser.add_argument('-a', '--analyze', action='store_true')
parser.add_argument('-f', '--filename')

args = parser.parse_args()

root_path = Path(args.source or ".")
result_file = args.filename or "report.html"
is_recursive = args.recursive
is_analyze = args.analyze

if is_analyze:
    analyze(root_path, is_recursive, result_file)

else:
    update_files(root_path, is_recursive)
