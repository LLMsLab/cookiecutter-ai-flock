# Understanding the `.gitignore` file

!!! tip "Should you commit `.gitignore` to git repositories?"
    Yes, `.gitignore` files should be commited.

## Introduction

When you make commits in a git repository, you choose which files to
stage and commit by using `git add FILENAME` and then git commit. But
what if there are some files that you never want to commit? It's too
easy to accidentally commit them (especially if you use `git add .` to
stage all files in the current directory). That's where a `.gitignore`
file comes in handy. It lets Git know that it should ignore certain
files and not track them.

!!!info
    The purpose of gitignore files is to ensure that certain files not
    tracked by Git remain untracked.

## How `.gitignore` works

Here's how it works. A `.gitignore` file is a plain text file where each
line contains a pattern for files/directories to ignore. Generally, this
is placed in the root folder of the repository.

## Literal File Names

The easiest pattern is a literal file name, for example:

```text title=".gitignore" title=".gitignore"
.DS_Store
```

This will ignore any files named `.DS_Store`, which is a common file on
macOS.

## Directories

You can ignore entire directories, just by including their paths and
putting a `/` on the end:

```text title=".gitignore" title=".gitignore"
node_modules/
logs/
```

If you leave the slash off of the end, it will match both files and
directories with that name.

## Wildcard

The `*` matches 0 or more characters (except the `/`). So, for example,
`*.log` matches any file ending with the `.log` extension.

Another example is `*~`, which matches any file ending with `~`, such as
`index.html~`

You can also use the `?`, which matches any one character except for the
`/`.

### Negation

You can use a prefix of `!` to negate a file that would be ignored.

```text title=".gitignore" title=".gitignore"
*.log
!example.log
```

In this example, `example.log` is not ignored, even though all other
files ending with `.log` are ignored.

But be aware, you can't negate a file inside of an ignored directory:

```text title=".gitignore" title=".gitignore"
logs/
!logs/example.log
```

Due to performance reasons, git will still ignore `logs/example.log`
here because the entire logs directory is ignored.

### Double Asterisk

`**`  can be used to match any number of directories.

- `**/logs`  matches all files or directories named logs (same as the
  pattern  `logs`)

- `**/logs/*.log`  matches all files ending with  `.log`  in a logs
  directory

- `logs/**/*.log`  matches all files ending with  `.log`  in the logs
  directory and any of its subdirectories

`**`  can also be used to match all files inside of a directory, so for
example  `logs/**`  matches all files inside of logs.

### Comments

Any lines that start with  `#`  are comments:

```text title=".gitignore" title=".gitignore"
1# macOS Files
2.DS_Store
```

## Automatically create `.gitignore` file from VS Code

The `gitignore` VS Code extension included in the list of recommended
extensions for this repository automates the creation of `.gitignore`
files.

### Usage

Start command palette (with `Ctrl`+`Shift`t+`P` or `F1`) and start
typing`Add gitignore`. Then select a programming language from the list.

It is possible to append multiple programming languages like Python and
R. Add first Python and then, if you try to add R you will see these
options:

```text title=".gitignore"
Append Append to existing .gitignore file
Overwrite Overwrite existing .gitignore file
```

Choose append and you will see the following message:

```text title=".gitignore"
Appended Python.gitignore to the existing .gitignore in the project root
```

!!! info "References"
    - [git
      documentation](https://git-scm.com/docs/gitignore#:~:text=A%20gitignore%20file%20specifies%20intentionally,gitignore%20file%20specifies%20a%20pattern)
    - [How to Use a `.gitignore`
      File](https://www.pluralsight.com/guides/how-to-use-gitignore-file)
