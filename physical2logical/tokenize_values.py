def tokenize_values(string):
    # Original idea from https://stackoverflow.com/a/38212061/177275
    # Assume correct syntax / matching brackets
    brackets = 0
    start = 0
    results = []

    for idx, char in enumerate(string):
        if char == ' ':
            if start is not None and brackets == 0:
                results.append(string[start:idx])
                start = None
        else:
            if start is None:
                start = idx
            if char == '(' or char == '{':
                brackets += 1
            elif char == ')' or char == '}':
                brackets -= 1
                if brackets < 0:
                    raise ValueError(f'failed to tokenize "{string}"')
    if start is not None:
        results.append(string[start:])
    results2 = []
    idx = 0
    while idx < len(results):
        if len(results[idx]) > 1 or results[idx] not in ('-', '+', '/', '*'):
            results2.append(results[idx])
        else:
            results2[-1] += ' ' + results[idx] + ' ' + results[idx + 1]
            idx += 1
        idx += 1
    return results2
