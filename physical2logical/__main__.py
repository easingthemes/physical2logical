from physical2logical.analyze import analyze
from physical2logical.arguments import get_args
from physical2logical.process_files import update_files


def cli():
    is_analyze, is_recursive, root_path, result_file = get_args()

    if is_analyze:
        analyze(root_path, is_recursive, result_file)

    else:
        update_files(root_path, is_recursive)
