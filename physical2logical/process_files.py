import re
from os.path import relpath

from physical2logical.aligner import aligner
from physical2logical.config import replacer_reg, renamer_reg, aligner_reg, src_files_pattern
from physical2logical.logger import logger
from physical2logical.renamer import renamer
from physical2logical.replacer import replacer


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
        logger.debug(f"File not changed, {source_file}")
        result_file.write("EMPTY_FILE\n")
    else:
        logger.debug(f"File changed {source_file}")


def process_files(root_path, is_recursive, result_file):
    logger.info(f"START processing files in '{root_path}'")
    if root_path.is_file():
        process_file(root_path, result_file)
    else:
        for pattern in src_files_pattern:
            all_files_gen = root_path.rglob(pattern) if is_recursive else root_path.glob(pattern)
            all_files_list = list(all_files_gen)
            logger.info(f"Found {len(all_files_list)} files for pattern {pattern}")
            for file in all_files_list:
                if file.is_file():
                    rel_path = relpath(file, root_path)
                    logger.debug(f"Use {file}")
                    if result_file:
                        process_results(rel_path, file, result_file)
                    else:
                        changed = process_file(file, None)
                        if changed:
                            logger.info(f"Modifying {rel_path}")
                            file.write_text(changed)

    logger.info_("DONE processing files.")


def analyze_files(root_path, is_recursive, result_file):
    logger.info_(f"Analyzing files in {root_path} ...")
    return process_files(root_path, is_recursive, result_file)


def update_files(root_path, is_recursive):
    logger.info_(f"Updating files  in {root_path} ...")
    return process_files(root_path, is_recursive, None)
