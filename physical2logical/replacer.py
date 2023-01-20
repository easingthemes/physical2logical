from physical2logical.commons import update_file
from physical2logical.config import sides
from physical2logical.tokenize_values import tokenize_values


def replacer(match, result_file=None):
    # ^( *)(margin|padding|border)(-(?:left|right|top|bottom))?(-(?:size|style|color))?( *: *)([^;\n]+);( *//.*)?$
    original = match.group(0)
    replaced = original
    spaces1 = match.group(1)
    typ = match.group(2)
    side = match.group(3) or ''
    extra = match.group(4) or ''
    spaces2 = match.group(5)
    values = match.group(6)
    comment = match.group(7) or ''
    # special lint controlling comment should be repeated
    dup_comment = comment if ('sass-lint:' in comment) else ''
    nl = "<br/>" if result_file else ""

    if not side:
        if typ == 'border':
            replaced = original
        else:
            tokens = tokenize_values(values)
            important = ' ' + tokens[-1] if tokens[-1] == '!important' else ''

            if important:
                tokens = tokens[:-1]

            if len(tokens) == 1:
                replaced = original  # single token stays as is
            elif len(tokens) == 2:  # top-bottom  right-left
                # The *-block shorthand is not yet supported,  see
                #   https://developer.mozilla.org/en-US/docs/Web/CSS/margin-block
                replaced = f"{spaces1}{typ}-block-start{extra}{spaces2}{tokens[0]}{important};{comment}{nl}\n" + \
                           f"{spaces1}{typ}-block-end{extra}{spaces2}{tokens[0]}{important};{dup_comment}{nl}\n" + \
                           f"{spaces1}{typ}-inline-start{extra}{spaces2}{tokens[1]}{important};{dup_comment}{nl}\n" + \
                           f"{spaces1}{typ}-inline-end{extra}{spaces2}{tokens[1]}{important};{dup_comment}{nl}"
            elif len(tokens) == 3:  # top  left-right  bottom
                replaced = f"{spaces1}{typ}-block-start{extra}{spaces2}{tokens[0]}{important};{comment}{nl}\n" + \
                           f"{spaces1}{typ}-block-end{extra}{spaces2}{tokens[2]}{important};{dup_comment}{nl}\n" + \
                           f"{spaces1}{typ}-inline-start{extra}{spaces2}{tokens[1]}{important};{dup_comment}{nl}\n" + \
                           f"{spaces1}{typ}-inline-end{extra}{spaces2}{tokens[1]}{important};{dup_comment}{nl}"
            elif len(tokens) == 4:  # top  left-right  bottom
                replaced = f"{spaces1}{typ}-block-start{extra}{spaces2}{tokens[0]}{important};{dup_comment}{comment}{nl}\n" + \
                           f"{spaces1}{typ}-block-end{extra}{spaces2}{tokens[2]}{important};{dup_comment}{nl}\n" + \
                           f"{spaces1}{typ}-inline-start{extra}{spaces2}{tokens[3]}{important};{dup_comment}{nl}\n" + \
                           f"{spaces1}{typ}-inline-end{extra}{spaces2}{tokens[1]}{important};{dup_comment}{nl}"
            else:
                raise ValueError(f'Unexpected number of tokens {len(tokens)} in {original} -- {tokens}')

    else:
        replaced = f"{spaces1}{typ}{sides[side]}{extra}{spaces2}{values};{comment}"

    update_file(result_file, original, replaced)
    return replaced
