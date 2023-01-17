from commons import update_file
from config import renames


def renamer(match, result_file=None):
    # ^( *)(' + '|'.join(renames.keys()) + r')( *: *)([^;\n]+);( *//.*)?$
    original = match.group(0)
    spaces1 = match.group(1)
    typ = match.group(2)
    spaces2 = match.group(3)
    values = match.group(4)
    comment = match.group(5) or ''

    try:
        replaced = f"{spaces1}{renames[typ]}{spaces2}{values};{comment}"
        update_file(result_file, original, replaced)
        return replaced
    except KeyError:
        return original
