from __future__ import print_function
import argparse, sys
from helpers import is_textfile


CONFLICT_STRINGS = ['<<<<<<<',
                    '>>>>>>>', ]


def contains_git_conflicts(filename):
    """
    Check the given file for any of the CONFLICT_STRINGS.

    Potential false-positives:

      - If any of the git conflicts are in a comment, this may report them as a
        failure even though it may not actually cause any issue.

    :return {bool}: True if conflicts are found else False
    """
    with open(filename, mode='rb') as file_checked:
        file_contents = file_checked.read()
        return any(conflict_string in file_contents for conflict_string in CONFLICT_STRINGS)


def main(argv=None):
    """
    Check files for any left over Git conflicts.
    """
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='File names to check')
    args = parser.parse_args(argv)
    filenames = args.filenames
    #  parser.add_argument('--files', '-f', help='File names to check')
    #  args = parser.parse_args(argv)
    #  filenames = args.files.split(',')

    # Find files with conflicts
    text_files = [filename for filename in filenames if is_textfile(filename)]
    files_with_conflicts = [text_file for text_file in text_files if contains_git_conflicts(text_file)]

    # Return response
    exit_code = 0
    if files_with_conflicts:
        exit_code = 1
        print('Git Conflicts Detected in file(s): \n - {}'.format('\n - '.join(files_with_conflicts)))

    return exit_code


if __name__ == '__main__':
    sys.exit(main(sys.argv))
