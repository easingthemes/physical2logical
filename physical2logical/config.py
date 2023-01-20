sides = {
    '-top': '-block-start',
    '-right': '-inline-end',
    '-bottom': '-block-end',
    '-left': '-inline-start',
}

renames = {
    # These are mostly unimplemented, might require https://github.com/csstools/postcss-logical
    'left': 'inset-inline-start',
    'right': 'inset-inline-end',
    'top': 'inset-block-start',
    'bottom': 'inset-block-end',

    'min-height': 'min-block-size',
    'max-height': 'max-block-size',
    'min-width': 'min-inline-size',
    'max-width': 'max-inline-size',
}

inline_start_end = {
    'left': 'inline-start',
    'right': 'inline-end',
}

aligns = {
    'text-align': {
        'left': 'start',
        'right': 'end',
    },
    # These are mostly unimplemented, might require https://github.com/csstools/postcss-logical
    'float': inline_start_end,
    'clear': inline_start_end,
}

replacer_reg = r'^( *)(margin|padding|border)(-(?:left|right|top|bottom))?(-(?:size|style|color))?( *: *)([^;\n]+);( *//.*)?$'
renamer_reg = r'^( *)(' + '|'.join(renames.keys()) + r')( *: *)([^;\n]+);( *//.*)?$'
aligner_reg = r'^( *)(text-align|float|clear)( *: *)(left|right)( *);'
src_files_pattern = ('*.scss', '*.css')


class Logger:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OK = '\033[92m'
    WARNING = '\033[93m WARNING: '
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
