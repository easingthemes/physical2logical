import argparse
from pathlib import Path


def get_args():
    parser = argparse.ArgumentParser(description='Convert CSS physical properties to logical')
    parser.add_argument('source',
                        nargs='*',
                        default='.',
                        help='Path to source directory / file. Default "."')
    parser.add_argument('-r', '--recursive',
                        default='True',
                        action='store_true',
                        help='Process all files from source directory. Default: True')
    parser.add_argument('-a', '--analyze',
                        action='store_true',
                        default='True',
                        help='Dry Run - Create a report with all changes (without actual source file changes). '
                             ' Default: True')
    parser.add_argument('-f', '--filename',
                        default='report.html',
                        help='Path to file where to save reports (used only with -a/--analyze flag). Default: "report.html"')

    args = parser.parse_args()

    root_path = Path(args.source or ".")
    result_file = args.filename or "report.html"
    is_recursive = args.recursive
    is_analyze = args.analyze

    return is_analyze, is_recursive, root_path, result_file
