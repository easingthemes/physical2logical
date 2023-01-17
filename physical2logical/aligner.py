from commons import update_file
from config import aligns


def aligner(match, result_file=None):
    # ^( *)(text-align|float|clear)( *: *)(left|right)( *);
    original = match.group(0)
    spaces1 = match.group(1)
    typ = match.group(2)
    spaces2 = match.group(3)
    values = match.group(4)
    spaces3 = match.group(5)

    try:
        replaced = f"{spaces1}{typ}{spaces2}{aligns[typ][values]}{spaces3};"
        update_file(result_file, original, replaced)
        return replaced
    except KeyError:
        return original
