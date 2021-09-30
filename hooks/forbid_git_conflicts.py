from __future__ import print_function
import argparse
import sys

# This allows `is_textfile` to be imported properly in different environments
try:
    from .helpers import is_textfile
except ImportError:
    import helpers

    is_textfile = helpers.is_textfile

# forbid-git-conflicts: off
CONTAINS_CONFLICT_STRINGS = [
    "<<<<<<<",
    ">>>>>>>",
]
EXACT_CONFLICT_STRINGS = [
    "=======",
    "HEAD",
]
# forbid-git-conflicts: on


def find_git_conflicts(filename):
    """
    Check the given file for any of the CONFLICT_STRINGS.

    Potential false-positives:

      - If any of the git conflicts are in a comment, this may report them as a
        failure even though it may not actually cause any issue.

    :param filename {str}: file name with relative path
    :return {bool}: True if conflicts are found else False
    """
    with open(filename, mode="r") as file_checked:
        git_conflicts = []
        ignore = False
        for line_number, line in enumerate(file_checked, start=1):
            ignore = is_ignore_enabled(line, ignore)
            if not ignore and (has_contained_conflict(line) or has_exact_conflict(line)):
                num_spaces = " " * (6 - len(str(line_number)))
                git_conflicts.append("{}:{}{}{}".format(filename, line_number, num_spaces, line.lstrip()))

        return git_conflicts


def has_contained_conflict(content):
    """
    Check if the provided content contains a match for any of the
    CONTAINS_CONFLICT_STRINGS values.

    Lines may have extra content and still be considered a conflict.

    :param content {str}: content to be checked for conflicts
    :return {bool}:
        True if the provided content contains a match for any of the
        CONFLICT_STRINGS values.
    """
    return any(conflict_string in content.rstrip("\n") for conflict_string in CONTAINS_CONFLICT_STRINGS)


def is_ignore_enabled(content, ignore):
    """
    Check if the provided content contains a match for any of the
    CONTAINS_CONFLICT_STRINGS values.

    :param content {str}: content to be checked for conflicts
    :param ignore {bool}: True if "ignore" is currently enabled, otherwise False
    :return {bool}: True if the check should be enforced, otherwise false
    """
    flag = "on" if ignore else "off"
    return not ignore if "forbid-git-conflicts: {}".format(flag) in content else ignore


def has_exact_conflict(content):
    """
    Check if the provided content contains a match for any of the
    CONTAINS_CONFLICT_STRINGS values.

    Lines must be an exact match (no extra content) to be considered a conflict.

    :param content {str}: content to be checked for conflicts
    :return {bool}:
        True if the provided content is an exact match for any of the
        EXACT_CONFLICT_STRINGS values.
    """
    return any(conflict_string == content.rstrip("\n") for conflict_string in EXACT_CONFLICT_STRINGS)


def main(argv=None):
    """
    Parse each line of the staged files to check for left over Git conflicts.

    Errors will be thrown for any lines that:
      - contain one of the CONTAINS_CONFLICT_STRINGS
      - or are equal to one of the EXACT_CONFLICT_STRINGS

    :return {int}: 1 if failure else 0
    """
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="File names to check")
    args = parser.parse_args(argv)
    filenames = args.filenames

    # Find files with conflicts
    python_files = [filename for filename in filenames if is_textfile(filename)]
    files_with_conflicts = []
    for text_file in python_files:
        files_with_conflicts += find_git_conflicts(text_file)

    # Return response
    exit_code = 0
    if files_with_conflicts:
        exit_code = 1
        print("Git Conflicts Detected in file(s): \n - {}".format(" - ".join(files_with_conflicts)))

    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
