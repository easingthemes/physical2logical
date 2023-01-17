import argparse
from pathlib import Path

from analyze import analyze
from process_files import update_files

parser = argparse.ArgumentParser(description='Convert CSS physical properties to logical')
parser.add_argument('source',
                    default='.',
                    help='Path to source directory / file.')
parser.add_argument('-r', '--recursive',
                    default='None',
                    action='store_true',
                    help='Process all files from source directory.')
parser.add_argument('-a', '--analyze',
                    action='store_true',
                    default='None',
                    help='Dry Run - Create a report with all changes (without actual source file changes).')
parser.add_argument('-f', '--filename',
                    default='report.html',
                    help='Path to file where to save reports (used only with -a/--analyze flag)')

args = parser.parse_args()

root_path = Path(args.source or ".")
result_file = args.filename or "report.html"
is_recursive = args.recursive
is_analyze = args.analyze

if is_analyze:
    analyze(root_path, is_recursive, result_file)

else:
    update_files(root_path, is_recursive)
