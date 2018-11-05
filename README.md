# pre-commit-hooks

> Example repositories of creating pre-commit hooks aren't necessarily easy to
> find. This repository is shadowed from several repositories, but namely
> [Lucas-C's pre-commit-hooks repository](https://github.com/Lucas-C/pre-commit-hooks)
> and some of the others mentioned on the [pre-commit hooks page](https://pre-commit.com/hooks.html).

### Example of .pre-commit-config.yaml

If you want to use some of these hooks as pre-commit hooks in your repository,
then create or add to your repo's `.pre-commit-config.yaml` file. If you don't
want some of the hooks, just delete the `id` line(s) from the config file.

```
repos:
-   repo: https://github.com/traviswaelbro/pre-commit-hooks
    rev: master
    hooks:
    -   id: forbid-git-conflicts
    -   id: forbid-set-trace
```

---

## Supported Hooks

### forbid-git-conflicts

Simple hook which iterates over all staged files to check for any lines that
have left over Git conflict markers.

* Does the line contain `<<<<<<<` or `>>>>>>>`?
* Is the line an exact match for `=======` or `HEAD`?

If either of those two criteria are found, pre-commit will fail the commit attempt.

#### Failure Output Example

```
[forbid-git-conflicts] Check for leftover Git conflicts.......................Failed
hookid: forbid-git-conflicts

Git Conflicts Detected in file(s):
 - helpers/example.py:18     <<<<<<< HEAD
 - helpers/example.py:20     =======
 - helpers/example.py:22     >>>>>>> master
```

---

### forbid-set-trace

Simple hook which iterates over all staged files to check for any lines that
have left over Git conflict markers.

* Does the line contain `<<<<<<<` or `>>>>>>>`?
* Is the line an exact match for `=======` or `HEAD`?

If either of those two criteria are found, pre-commit will fail the commit attempt.

#### Failure Output Example

```
[forbid-set-trace] Check for leftover debugging statements.......................Failed
hookid: forbid-set-trace

Debuggers Detected in file(s):
 - helpers/example.py:3      import pdb
 - helpers/example.py:92     pdb.set_trace()
 - helpers/example.py:101    __import__('ipdb').set_trace(context=15)

```
