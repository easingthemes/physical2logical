import argparse
import os
import sys
from os.path import isfile
from pathlib import Path

from physical2logical.logger import logger


def log_and_exit(msg, callback):
    logger.error(f"{msg}")
    logger.empty()
    callback()
    sys.exit(1)


def is_valid_file_path(file_path):
    if os.path.exists(file_path):
        return True
    elif os.access(os.path.dirname(file_path), os.W_OK):
        return True
    else:
        return False


# can not write there
def get_args():
    parser = argparse.ArgumentParser(description='Convert CSS physical properties to logical')
    parser.add_argument('source',
                        help='Path to source directory or one file. Required')
    parser.add_argument('-r', '--recursive',
                        action=argparse.BooleanOptionalAction,
                        default=True,
                        help='Recursive process of all files from source directory.')
    parser.add_argument('-u', '--update',
                        action=argparse.BooleanOptionalAction,
                        default=False,
                        help='Update files.')
    parser.add_argument('-a', '--analyze',
                        action=argparse.BooleanOptionalAction,
                        default=False,
                        help='Dry Run - Create a report with all changes (without actual source file changes).')
    parser.add_argument('-f', '--filename',
                        default='./report.html',
                        help='Path to file where to save reports (used only with -a/--analyze flag).'
                             ' (default: "./report.html")')

    if len(sys.argv) < 2:
        return log_and_exit(f"Path to source directory or one file is required", parser)

    args = parser.parse_args()

    root_path = Path(args.source)
    result_file = args.filename or "./report.html"
    is_recursive = args.recursive
    is_analyze = args.analyze
    is_update = args.update

    def print_args():
        logger.info_(f"Params: \n"
                     f"\tsource: {root_path}\n"
                     f"\trecursive: {is_recursive}\n"
                     f"\tupdate: {is_update}\n"
                     f"\tanalyze: {is_analyze}\n"
                     f"\tresults file: {result_file}")
        logger.empty()

    def callback():
        print_args()
        parser.print_help()

    if not is_analyze and not is_update:
        return log_and_exit("Action missing: [-a | --analyze] or [-u | --update]", callback)

    if not args.filename:
        logger.warning(f"Report filename not defined,using default '{result_file}'")
        logger.empty()

    is_valid_result_file = is_valid_file_path(result_file)
    if not is_valid_result_file:
        return log_and_exit(f"Filename must be valid file path. Received: {result_file}", callback)

    return is_analyze, is_update, is_recursive, root_path, result_file
