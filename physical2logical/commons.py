def collapse_if_equal(val1, val2):
    return val1 if val1 == val2 else f"{val1} {val2}"


def update_file(result_file, original, replaced):
    if not result_file or original == replaced:
        return

    result = f"<tr><td> {original.lstrip()} </td><td> {replaced.lstrip()} </td></tr>\n"
    result_file.write(result)
