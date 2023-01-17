import re
from os.path import relpath

from config import replacer_reg, renamer_reg, aligner_reg, src_files_pattern
from replacer import replacer
from renamer import renamer
from aligner import aligner


def process_file(source_file, result_file):
    def re_callback(callback):
        if result_file:
            return lambda match: callback(match, result_file)
        return callback

    code = source_file.read_text()
    res = re.sub(replacer_reg, re_callback(replacer), code, flags=re.MULTILINE)
    res = re.sub(renamer_reg, re_callback(renamer), res, flags=re.MULTILINE)
    res = re.sub(aligner_reg, re_callback(aligner), res, flags=re.MULTILINE)

    if res != code:
        return res

    return ""


def process_results(file_path, source_file, result_file):
    header = f"<tr style='background: silver'><td> File: </td><td> {file_path} </td></tr>\n"
    result_file.write(header)

    changed = process_file(source_file, result_file)

    if not changed:
        result_file.write("EMPTY_FILE\n")
        
    
def process_files(root_path, is_recursive, result_file):
    if root_path.is_file():
        process_file(root_path, result_file)
    else:
        for pattern in src_files_pattern:
            for file in (root_path.rglob(pattern) if is_recursive else root_path.glob(pattern)):
                if file.is_file():
                    source_file = root_path / file
                    rel_path = relpath(file, root_path)

                    if result_file:
                        process_results(rel_path, source_file, result_file)
                    else:
                        changed = process_file(source_file, None)
                        if changed:
                            print(f"Modifying {rel_path}")
                            source_file.write_text(changed)


def analyze_files(root_path, is_recursive, result_file):
    return process_files(root_path, is_recursive, result_file)


def update_files(root_path, is_recursive):
    return process_files(root_path, is_recursive, None)
