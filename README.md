-   [Installation instructions](#installation-instructions)
-   [Unix Shell](#unix-shell)
    -   [Intro comments about \"shell\"](#intro-comments-about-shell)
    -   [Very brief Bash intro](#very-brief-bash-intro)
-   [Why are we here?](#why-are-we-here)
-   [Setup](#setup)
    -   [Inspect your configuration](#inspect-your-configuration)
    -   [Identify yourself](#identify-yourself)
    -   [Line Endings](#line-endings)
    -   [Editor](#editor)
    -   [Updating remotes](#updating-remotes)
    -   [(Optional) Change name of default
        branch](#optional-change-name-of-default-branch)
-   [Creating a repository](#creating-a-repository)
    -   [Create a directory](#create-a-directory)
    -   [Tell Git to make a repository](#tell-git-to-make-a-repository)
    -   [Check status (we will do this a
        lot)](#check-status-we-will-do-this-a-lot)
-   [Tracking changes](#tracking-changes)
    -   [Add a file](#add-a-file)
    -   [Commit cycle](#commit-cycle)
    -   [Getting help](#getting-help-1)
    -   [First stage, then commit](#first-stage-then-commit)
    -   [View commit history in the
        log](#view-commit-history-in-the-log)
    -   [Show changes to Workspace and
        Index](#show-changes-to-workspace-and-index)
    -   [What goes in a commit?](#what-goes-in-a-commit)
    -   [Directories aren\'t content](#directories-arent-content)
-   [Exploring history](#exploring-history)
    -   [Add more text to Workspace](#add-more-text-to-workspace)
    -   [View subsets of project
        history](#view-subsets-of-project-history)
    -   [`diff` using a commit ID instead of the HEAD
        offset](#diff-using-a-commit-id-instead-of-the-head-offset)
    -   [Restore the Workspace to a clean
        state](#restore-the-workspace-to-a-clean-state)
-   [Moving through time](#moving-through-time)
    -   [Check out an old version of a
        file](#check-out-an-old-version-of-a-file)
    -   [Don\'t lose your head](#dont-lose-your-head)
-   [Branching and merging](#branching-and-merging)
    -   [Create a new branch and switch to
        it](#create-a-new-branch-and-switch-to-it)
    -   [Create a new file](#create-a-new-file)
    -   [Switch back to master and
        merge](#switch-back-to-master-and-merge)
-   [Local conflicts](#local-conflicts)
    -   [Create and edit a \"pepper\"
        branch](#create-and-edit-a-pepper-branch)
    -   [Switch back to main branch and create a conflicting
        edit](#switch-back-to-main-branch-and-create-a-conflicting-edit)
    -   [Attempt to merge \"pepper\"
        branch](#attempt-to-merge-pepper-branch)
    -   [Resolve conflicts and create
        commit](#resolve-conflicts-and-create-commit)
-   [Ignoring Things](#ignoring-things)
    -   [Create some output files](#create-some-output-files)
    -   [Create .gitignore](#create-.gitignore)
    -   [Add ignore criteria to your .gitignore
        file](#add-ignore-criteria-to-your-.gitignore-file)
-   [(Optional) Github](#optional-github)
    -   [Git != Github](#git-github)
    -   [Set up new repository](#set-up-new-repository)
    -   [Configure remotes and push from
        local](#configure-remotes-and-push-from-local)
    -   [Check that you are up to date](#check-that-you-are-up-to-date)
-   [(Optional) Collaborating](#optional-collaborating)
    -   [Clone your repository](#clone-your-repository)
    -   [Edit trees.txt](#edit-trees.txt)
    -   [Update and push](#update-and-push)
    -   [Collaboration models](#collaboration-models)
-   [(Optional) Collaboration
    conflicts](#optional-collaboration-conflicts)
    -   [Person 1 edits
        \~/Desktop/garden/shopping_list.txt](#person-1-edits-desktopgardenshopping_list.txt)
    -   [Person 2 edits \~/Desktop/garden-clone/shopping_list.txt
        *without*
        pulling](#person-2-edits-desktopgarden-cloneshopping_list.txt-without-pulling)
    -   [Edit conflict, stage, commit, and
        push](#edit-conflict-stage-commit-and-push)
-   [Version control with Python source vs. iPython
    notebooks](#version-control-with-python-source-vs.-ipython-notebooks)
-   [Git command summary](#git-command-summary)
-   [Graphical User Interfaces](#graphical-user-interfaces)
    -   [Pro](#pro)
    -   [Cons](#cons)
-   [Next steps (intermediate Git)](#next-steps-intermediate-git)
-   [Credits](#credits)
-   [References](#references)

# Installation instructions

1.  Up-to-date installation instructions for Git and Bash are available
    here:
    <https://libguides.ucmerced.edu/software-carpentry/git/install>
2.  Create a Github account here: <https://github.com/>

# Unix Shell

## Intro comments about \"shell\"

-   Broadly speaking, there is a tension between making computer systems
    fast and making them easy to use.
-   A common solution is to create a 2-layer architecture: A fast,
    somewhat opaque core surrounded by a more friendly scriptable
    interface (also referred to as \"hooks\" or an \"API\"). Examples of
    this include video games, Emacs and other highly customizable code
    editors, and high-level special-purpose languages like Stata and
    Mathematica.
-   Unix shell is the scriptable **shell** around the operating system.
    It provides a simple interface for making the operating system do
    work, without having to know exactly how it accomplishes that work.

## Very brief Bash intro

### File system layout

-   Minimal example:
    <https://swcarpentry.github.io/shell-novice/02-filedir/index.html>
-   \"directory\" == folder
-   Your files are in \"/home/\<your login\>\"or \"/Users/\<your
    login\>\"
-   Trees are upside-down in computer science

### Who are you?

``` bash
whoami
```

### Where are you?

``` bash
pwd                             # Print Working Directory
```

### What\'s in this directory?

Command flags modify what a command does.

``` bash
ls                              # List directory contents
ls -a                           # ... and include hidden files
```

### Getting help

``` bash
man ls                          # Manual for "ls"
ls --help                       # In-line help info; should work in Windows
```

-   You can navigate through the man page using the space bar and arrow
    keys
-   Quit man with \"q\"
-   Online references are available for Windows users who don\'t have
    man pages: <https://linux.die.net/>

### Changing directories

When a command is followed by an argument, it acts on that argument.

``` bash
cd Desktop
ls *.pdf                        # List all files ending in ".pdf"
cd ..                           # go up one directory
```

### History and pipes

The terminal saves your command history (typically 500 or 1000 commands)

-   You can see previous commands using the up/down arrows
-   You can edit the command that\'s currently visible and run it

Once your command history gets big, you might want to search it:

``` bash
history
history | grep ls               # pipe the output of history into search
```

# Why are we here?

![Git creates a history of code snapshots. If you haven\'t updated a
file since your previous snapshot, Git will re-use the old version of
that file to save space
(<https://git-scm.com/>).](images/snapshots.png "Snapshot History")

![](images/git_bisect_1.jpg "Bisect 1")

![](images/git_bisect_2.jpg "Bisect 2")

![](images/git_bisect_3.jpg "Bisect 3")

![](images/git_bisect_4.jpg "Bisect 4")

-   Move backwards and forwards in time using save points in your code
    history.
-   Control what goes into a save point
-   Collaborate
-   Explore alternative versions of your project without destroying
    prior work
-   Useful for text files, less useful for binary files (most of the
    useful features are text-oriented)

# Setup

## Inspect your configuration

``` bash
git config --list                   # or -l
git config --list --show-origin     # where is this setting coming from?
```

## Identify yourself

All git commands are 2-part verbs, followed by flags and arguments. Use
quotes if you have spaces in your arguments (e.g. user name):

``` bash
git config --global user.name "Gilgamesh"
git config --global user.email gilgamesh@uruk.gov
```

## Line Endings

``` bash
git config --global core.autocrlf input  # Unix and MacOS
git config --global core.autocrlf true   # Windows
```

## Editor

You can use any text editor, but you want a sensible default in case Git
opens one for you:

``` bash
git config --global core.editor nano
```

## Updating remotes

1.  Only push the current branch (more about this later):

    ``` bash
    git config --global push.default simple
    ```

2.  Merge, don\'t rebase (more about this later):

    ``` bash
    git config --global pull.rebase false
    ```

## (Optional) Change name of default branch

``` bash
git config --global init.defaultBranch main
```

# Creating a repository

We are going to create and track plans for our garden.

## Create a directory

``` bash
cd ~/Desktop
mkdir garden
cd garden
```

## Tell Git to make a repository

``` bash
git init
ls
ls -a
```

![Base your new work on the most recent
snapshot.](images/local-repository.png "Workspace or Working Tree")

-   Git uses this special subdirectory to store all the information
    about the project, including all files and sub-directories located
    within the project\'s directory. If we ever delete the \`.git\`
    subdirectory, we will lose the project\'s history.
-   Only one version of a file is visible; the rest are available in the
    database

## Check status (we will do this a lot)

``` bash
git status
```

# Tracking changes

You can edit with nano or with the text editor of your choice. We\'ll
try to show the editor and the command line side-by-side.

## Add a file

``` bash
touch shopping_list.txt
nano shopping_list.txt
```

``` example
1. Cherry tomatoes
```

Save and quit. You can verify that you\'ve saved your changes in Bash:

``` bash
ls
cat shopping_list.txt
```

## Commit cycle

Manually assemble your next save point in the Staging area (\"Index\").
When you\'re happy with it, commit it to the repository to create a new
version of your project.

![Build a new save point (\"commit\") in the Staging
Area.](images/git-staging-area.svg "First Commit")

![Commits include additions and
deletions](images/git-committing.svg "Commit with multiple files")

``` bash
git status
git add shopping_list.txt
git status
git commit -m "Start shopping list for garden"
git status
```

-   Commit messages should be useful; eventually there will be a lot of
    them (we\'ll come back to this)
-   There are multiple synonym for each of these locations:
    -   Workspace or Working Tree
    -   Staging Area, Index, or Cache
    -   Repository or Commit History

## Getting help

``` bash
# Concise help
git add -h

# Verbose help
man git-add
```

## First stage, then commit

1.  Edit the file

    ``` example
    1. Cherry tomatoes
    2. Italian basil
    ```

    ``` bash
    git status
    git diff
    ```

2.  If you try to commit the file before you add it to the Staging area,
    nothing happens

    ``` bash
    git commit -m "Add basil"
    git status
    ```

3.  You have to add the file to the Staging area, then commit

    ``` bash
    git add shopping_list.txt
    git commit -m "Add basil"
    ```

## View commit history in the log

``` bash
git log
git log --oneline
```

1.  You can identify a commit by unique ID or by HEAD offset (H,
    HEAD\~1, HEAD\~2,...)
2.  HEAD is a pointer to the most recent commit (of the active branch)

### (Optional) Additional log options

``` bash
git log --oneline --graph       # Useful if you have many branches
git log --author=~Gilgamesh
git log --since=5.days          # or weeks, months, years
```

## Show changes to Workspace and Index

1.  Edit the file

    ``` example
    1. Cherry tomatoes
    2. Italian basil
    3. Jalapenos
    ```

2.  By default, `diff` shows changes to Workspace

    ``` bash
    git status
    git diff
    ```

3.  Once the file is added to Staging, `diff` no longer shows changes

    ``` bash
    git add shopping_list.txt
    git status
    git diff
    ```

4.  You can examine Staging instead

    ``` bash
    git diff --staged               # or "--cached"
    git commit -m "Add peppers"
    git status
    ```

## What goes in a commit?

1.  Staging area is for creating sensible commits. You can edit multiple
    files and only add a subset of them to a given commit. This makes it
    easier to look back at your work.
2.  A commit should be a coherent functional chunk (whatever that
    means). One way to think about it: If you wanted to cleanly undo
    your work, what would that look like?

## Directories aren\'t content

1.  Try to commit an empty directory

    ``` bash
    mkdir flowers
    git status
    git add flowers
    git status
    ```

2.  Now add files and try again

    ``` bash
    touch flowers/roses flowers/tulips
    git status
    git add flowers
    git commit -m "Initial thoughts on flowers"
    ```

# Exploring history

## Add more text to Workspace

``` example
1. Cherry tomatoes
2. Italian basil
3. Jalapenos
4. Cayenne peppers
```

## View subsets of project history

``` bash
# NB: This is identical to "git diff" with no argument
# git diff HEAD shopping_list.txt

# Show all changes back to this point
git diff HEAD~1 shopping_list.txt
git diff HEAD~3 shopping_list.txt

# Show changes for just HEAD~3
git show HEAD~3 shopping_list.txt

# Show changes in range of commits
git diff HEAD~3..HEAD~1 shopping_list.txt
```

### Range syntax also works for logs

``` bash
git log HEAD~3..HEAD~1
```

## `diff` using a commit ID instead of the HEAD offset

``` bash
# Theoretically you can do this
# git diff f22b25e3233b4645dabd0d81e651fe074bd8e73b shopping_list.txt

# Use reduced 7-character ID from "git log --oneline"
git diff f22b25e shopping_list.txt
```

## Restore the Workspace to a clean state

``` bash
# We have unstaged changes
git status

# Revert the working tree to the most recent commit
git restore shopping_list.txt

# Check whether your editor is automatically updating!
cat shopping_list.txt

# The old way of doing it:
# git checkout HEAD shopping_list.txt
```

# Moving through time

## Check out an old version of a file

![Check out an old commit to view
it](images/git-checkout.svg "Checkout")

``` bash
git checkout f22b25e shopping_list.txt

# Alternatively, you can use the HEAD offset:
git checkout HEAD~3 shopping_list.txt

# View the changed file in the Working Tree
cat shopping_list.txt

# These changes are also in the Staging area; you can create a new commit
# that includes the older file version.
git status
git diff
git diff --staged

# Go back to the most recent version
git checkout HEAD shopping_list.txt
```

**Instructor\'s note:** Update drawing with files moving in and out of
working tree/staging area

## Don\'t lose your head

What if you want to see a previous version of the whole project?

``` bash
# Detached HEAD moves the whole HEAD pointer back to an earlier version
git checkout HEAD~2
git status
git log --oneline

# Move HEAD back to latest commit by checking out the branch name
git checkout master
```

**Instructor\'s note:** Update drawing with moving HEAD pointer

-   You can also check out a tag.
-   Unfortunately some of these terms, like \"checkout\", are
    overloaded. Think about what you want to do to your history, then
    look up the appropriate command.

# Branching and merging

![Git branching and Merging
(<https://imgur.com/gallery/YG8In8X/new>)](images/branch-merge.png "Branching and Merging")

## Create a new branch and switch to it

![Check out the branch to work on it
(1)](images/branch-old.png "Main branch")

![Check out the branch to work on it
(2)](images/branch-new.png "Feature branch")

``` bash
# Create a new branch
git branch feature

# Show all branches
git branch

# Switch to new branch
git switch feature
git branch
git status
```

## Create a new file

``` bash
touch feature.txt
nano feature.txt
```

``` example
This is a new feature we're trying out
```

``` bash
git status
git add feature.txt
git commit -m "Added a trial feature"
```

## Switch back to master and merge

![Pre-merge history](images/basic-merging-1.png "Pre-merge history")

![Post-merge history](images/basic-merging-2.png "Post-merge history")

``` bash
# File doesn't exist on the master branch
git switch master
ls

# Merging the feature branch adds your changes
git merge feature
ls
```

-   This is simplest possible case: All of the new changes were in one
    branch (Fast-Forward merge moves branch tag)
-   A branch history with competing changes is shown in the Conflicts
    section below (Recursive merge, which resembles the octopus diagram)

# Local conflicts

## Create and edit a \"pepper\" branch

``` bash
git branch pepper
git switch pepper
```

``` example
1. Cherry tomatoes
2. Italian basil
3. Jalapenos
4. Cayenne peppers
```

``` bash
git add shopping_list.txt
git commit -m "Added peppers to pepper branch"
```

## Switch back to main branch and create a conflicting edit

``` bash
git switch master
```

``` example
1. Cherry tomatoes
2. Italian basil
3. Jalapenos
4. Garlic
```

``` bash
git add shopping_list.txt
git commit -m "Added garlic to main branch"
```

## Attempt to merge \"pepper\" branch

``` bash
git merge pepper
```

## Resolve conflicts and create commit

Edit the file to resolve the conflict. You can delete one of the two
lines, combine them, or make any other changes. Delete the conflict
markers before staging the file (the lines beginning in \"\<\", \"=\",
and \"\>\").

``` example
<<<<<<< HEAD
4. Garlic
=======
4. Cayenne peppers
>>>>>>> dabb4c8c450e8475aee9b14b4383acc99f42af1d
```

``` bash
git add shopping_list.txt
git commit -m "Added garlic to main branch"
```

# Ignoring Things

## Create some output files

``` bash
mkdir results
touch a.dat b.dat c.dat results/a.out results/b.out
ls
git status
```

## Create .gitignore

``` bash
touch .gitignore
ls -a
```

## Add ignore criteria to your .gitignore file

``` example
*.dat
results/
```

``` bash
# We are ignoring .dat files and tracking .gitignore
git status
git add .gitignore
git commit -m "Ignore output files"
```

-   Ignoring complicated directory structures can be tricky, come talk
    to me
-   You should generally ignore archives (zip, tar), images (png, jpg),
    binaries (dmg, iso, exe), compiler output, log files, and .DS_Store
    (Mac)

# (Optional) Github

![Coordinate with co-authors.](images/distributed.png "Pre-merge state")

## Git != Github

-   easy collaboration
-   sync between machines
-   off-site backup
-   peer review

## Set up new repository

-   Create new repository (visual instructions here:
    <https://swcarpentry.github.io/git-novice/07-github/index.html>)
-   Call it \"garden\"
-   Find HTTPS string that identifies repository

## Configure remotes and push from local

``` bash
git remote add origin https://github.com/devnich/garden.git
git remote -v
git push origin master          # you should get a password prompt
```

If you configure your origin as upstream, you can just do:

``` bash
git push
```

## Check that you are up to date

`pull` is a shortcut for `fetch` + `merge`

``` bash
git pull
```

# (Optional) Collaborating

**Instructor\'s note:** Demo this section with two terminal windows, one
for \"garden\" and one for \"garden-clone\"

## Clone your repository

``` bash
git clone https://github.com/devnich/garden.git ~/Desktop/garden-clone
cd garden-clone
touch trees.txt
```

## Edit trees.txt

``` example
1. Plum
2. Pluot
3. Aprium
```

## Update and push

``` bash
pwd                             # we are in ~/Desktop/garden-clone
git status
git add trees.txt
git commit -m "I like plums"
git push
cd ../garden                   # now we are in ~/Desktop/garden
ls
git pull
ls
```

## Collaboration models

cf.
<https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models>

### Shared Repository workflow

1.  Clone repository
2.  Create new branch
3.  Push branch to shared repository
4.  Request merge

### Fork-and-Pull workflow

1.  Fork repository
2.  Clone forked repository
3.  Create branch (optional)
4.  Push changes to forked repository
5.  Create pull request for original repository

# (Optional) Collaboration conflicts

## Person 1 edits \~/Desktop/garden/shopping_list.txt

``` example
1. Cherry tomatoes
2. Italian basil
3. Jalapenos
4. Scotch bonnet peppers
```

``` bash
git add shopping_list.txt
git commit -m "Added more peppers our copy"
git push origin master
```

## Person 2 edits \~/Desktop/garden-clone/shopping_list.txt *without* pulling

``` example
1. Cherry tomatoes
2. Italian basil
3. Jalapenos
4. Garlic
```

``` bash
git add shopping_list.txt
git commit -m "Added garlic to rival copy"

# Rejected because Git can't merge changes cleanly
git push origin master

# Pulling results in a local conflict
git pull origin master
```

## Edit conflict, stage, commit, and push

Edit the file to resolve the conflict. You can delete one of the two
lines, combine them, or make any other changes. Delete the conflict
markers before staging the file (the lines beginning in \"\<\", \"=\",
and \"\>\").

``` example
<<<<<<< HEAD
4. Garlic
=======
4. Cayenne peppers
>>>>>>> dabb4c8c450e8475aee9b14b4383acc99f42af1d
```

You may want to enable a default merge tool:

``` bash
git config --global merge.tool meld
```

-   Open source merge tools include Vimdiff, Meld, Kdiff, Gitfiend, Git
    Cola, etc. There are many other options!
-   Always pull before you push
-   To minimize conflicts, do your work on a separate branch

# Version control with Python source vs. iPython notebooks

.ipynb files contain a lot of JSON boilerplate that isn\'t code

# Git command summary

Git commands are about moving stuff between trees:
<https://ndpsoftware.com/git-cheatsheet.html>

# Graphical User Interfaces

## Pro

1.  Viewing history is a much better experience

## Cons

1.  Not fully functional (missing commands and command options)
2.  Git is still complicated. Menus and buttons don't change that.
3.  Accidental button presses are scary

# Next steps (intermediate Git)

### Useful commands

-   `git blame`: See who changed each line of a file
-   `git bisect`: Find out when a change was introduced (good man page)
-   `git add --patch`: Stage a part of a file (\"hunk\") instead the
    entire file
-   `git -i <command>`: Run a command interactively, confirming each
    step

### Restore, Revert, and Reset

Each of these is a different answer to the question, \"How do I get back
to where I was?\" They are listed from least dangerous to most
dangerous.

-   `git-restore`: Restore files in the working tree from the index or
    from another commit. This command does not update your branch.
-   `git-revert`: Make a new commit that reverts the changes made by
    other commits (good man page)
-   `git-reset`: Update your branch, moving the tip in order to add or
    remove commits from the branch (i.e. it moves the HEAD pointer
    around and then takes additional actions base on the options you
    provide). This operation changes the commit history.

### Dangerous but useful commands

These commands are potentially dangerous because they rewrite history.
You should never change or delete history that you have shared with
other people.

-   `git reset`: Delete uncommitted changes
-   `git reset --hard`: Delete some of your commits to get back to an
    earlier project state. Cannot be undone!
-   `git rebase`: Rewrite the history of branch A to include branch B.
    This is different than merging branch B into branch A; merging
    retains your project history, whereas rebasing rewrites that
    history.
-   `git squash`: Convert multiple commits into a single commit. This
    also rewrites your project history.

### Dangerous commands you should avoid

-   `git cherry-pick`: Copy a single commit from a different branch.
    This rewrites your project history piecemeal, which can make it
    difficult to merge branches in the future.

# Credits

1.  <https://dlstrong.github.io/git-novice/>
2.  <https://git-scm.com/book/en/v2>
3.  <https://gitlab.com/liibre/curso/-/wikis/material>
4.  <https://swcarpentry.github.io/git-novice/reference>
5.  <https://swcarpentry.github.io/shell-novice/reference/>
6.  <https://twitter.com/jay_gee>

# References

1.  The Pro Git book: <https://git-scm.com/book/en/v2>
2.  Graphical user interfaces for Git (useful for visualizing diffs and
    merges):
    <https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Graphical-Interfaces>
3.  Git for Advanced Beginners: <http://think-like-a-git.net>
4.  \"Git is built on a graph. Almost every Git command manipulates this
    graph. To understand Git deeply, focus on the properties of this
    graph, not workflows or commands.\":
    <https://codewords.recurse.com/issues/two/git-from-the-inside-out>
5.  A Visual Git Reference:
    <https://marklodato.github.io/visual-git-guide/index-en.html>
6.  Visual cheat sheet: <https://ndpsoftware.com/git-cheatsheet.html>
