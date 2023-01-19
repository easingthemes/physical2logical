# physical2logical

Convert CSS physical properties to logical.

Converts margins, padding, and borders to logical values, allowing RTL and vertical languages to show correctly.

## Usage

```commandline
css2logical [-h] [-r] [-a] [-f FILENAME] source

Convert CSS physical properties to logical

positional arguments:
  source                Path to source directory / file. Default '.'

options:
  -h, --help            show this help message and exit
  -r, --recursive       Process all files from source directory. Default: True
  -a, --analyze         Dry Run - Create a report with all changes (without actual source file changes). Default: True
  -f FILENAME, --filename FILENAME
                        Path to file where to save reports (used only with --analyze flag). Default: 'report.html'

```

Based on https://gist.github.com/nyurik/d438cb56a9059a0660ce4176ef94576f

![physical2logical-all-files.png](physical2logical-all-files.png)
