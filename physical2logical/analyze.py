from physical2logical.logger import logger
from physical2logical.process_files import analyze_files


def analyze(root_path, is_recursive, result_file, pattern):
    f = open(result_file, "a+")
    f.truncate(0)

    header = "<table><thead>\n"
    header += "<tr><th> physical </th><th> logical </th></tr>\n"
    header += "</thead><tbody>\n"
    f.write(header)

    analyze_files(root_path, is_recursive, f, pattern)

    footer = "</tbody></table>\n"
    f.write(footer)

    f.close()

    with open(result_file, 'r') as file:
        lines = file.read().split("\n")

        for i in range(1, len(lines) + 1):
            text_match = "EMPTY_FILE"

            if lines[-i] == text_match:
                lines[-(i + 1)] = ""
                lines[-(i + 0)] = ""

        while "" in lines:
            lines.remove("")

        code_updated = "\n".join(lines)

        with open(result_file, 'w') as out:
            out.write(code_updated)
            out.close()

        logger.info_(f"Results file: {result_file}")
