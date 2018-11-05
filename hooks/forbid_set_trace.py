from __future__ import print_function
import argparse, sys
from helpers import is_textfile


CONFLICT_STRINGS = ['pdb',
                    'set_trace', ]


def find_set_trace_conflicts(filename):
    """
    Check the given file for any hint of a set_trace or imported debugger.

    :param filename {str}: file name with relative path
    :return {bool}: True if forbidden code is found else False
    """
    with open(filename, mode='r') as file_checked:
        conflicts = []
        for line_number, line in enumerate(file_checked, start=1):
            if has_conflict(line):
                conflicts.append("{}:{} | {}".format(filename, line_number, line))

        return conflicts


def has_conflict(content):
    """
    Check if the provided content contains a match for any of the debugger
    related values.

    :param content {str}: content to be checked for conflicts
    :return {bool}:
        True if the provided content contains a match for any of the
        CONFLICT_STRINGS values.
    """
    return any(conflict_string in content.rstrip('\n') for conflict_string in CONFLICT_STRINGS)


def main(argv=None):
    """
    Parse each line of the staged files to check for left over debugging imports
    or statements.

    Errors will be thrown for any lines that contain:
      - 'pdb'
      - 'set_trace'

    :return {int}: 1 if failure else 0
    """
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='File names to check')
    args = parser.parse_args(argv)
    filenames = args.filenames

    # Find files with conflicts
    text_files = [filename for filename in filenames if is_textfile(filename)]
    files_with_conflicts = []
    for text_file in text_files:
        files_with_conflicts += find_set_trace_conflicts(text_file)

    # Return response
    exit_code = 0
    if files_with_conflicts:
        exit_code = 1
        print('Debuggers Detected in file(s): \n - {}'.format(' - '.join(files_with_conflicts)))

    return exit_code


if __name__ == '__main__':
    sys.exit(main(sys.argv))
