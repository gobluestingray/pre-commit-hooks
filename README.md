# pre-commit-hooks

> Example repositories of creating pre-commit hooks aren't necessarily easy to
> find. This repository is shadowed from several repositories, but namely
> [Lucas-C's pre-commit-hooks repository](https://github.com/Lucas-C/pre-commit-hooks)
> and some of the others mentioned on the [pre-commit hooks page](https://pre-commit.com/hooks.html).

## Supported Hooks

### forbid-git-conflicts

Simple hook which iterates over all staged files to check for any lines that
have left over Git conflict markers.

* Does the line contain `<<<<<<<` or `>>>>>>>`?
* Is the line an exact match for `=======` or `HEAD`?

If either of those two criteria are found, pre-commit will fail the commit attempt.

#### .pre-commit-config.yaml Example

```
repos:
-   repo: https://github.com/traviswaelbro/pre-commit-hooks
    rev: master
    hooks:
    -   id: forbid-git-conflicts
```

#### Failure Output Example

```
[forbid-git-conflicts] Check for leftover Git conflicts.......................Failed
hookid: forbid-git-conflicts

Git Conflicts Detected in file(s):
 - helpers/example.py:17 | <<<<<<< HEAD
 - helpers/example.py:19 | =======
 - helpers/example.py:21 | >>>>>>> master
```
