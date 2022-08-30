-   [Installation instructions](#installation-instructions)
-   [Unix Shell](#unix-shell)
    -   [Intro comments about \"shell\"](#intro-comments-about-shell)
    -   [Very brief Bash intro](#very-brief-bash-intro)
-   [Why are we here?](#why-are-we-here)
-   [Setup](#setup)
    -   [Identify yourself](#identify-yourself)
    -   [Line Endings](#line-endings)
    -   [Editor](#editor)
    -   [Updating remotes](#updating-remotes)
    -   [(Optional) Change name of default
        branch](#optional-change-name-of-default-branch)
    -   [Inspect your configuration](#inspect-your-configuration)
-   [Creating a repository](#creating-a-repository)
    -   [Create a directory](#create-a-directory)
    -   [Tell Git to make a repository](#tell-git-to-make-a-repository)
    -   [Check status (we will do this a
        lot)](#check-status-we-will-do-this-a-lot)
-   [Tracking changes](#tracking-changes)
    -   [Add a file](#add-a-file)
    -   [Commit cycle](#commit-cycle)
    -   [Getting help](#getting-help-1)
    -   [Add more history](#add-more-history)
    -   [Add more history; look at Staging area vs
        Workspace](#add-more-history-look-at-staging-area-vs-workspace)
    -   [View commit history in the
        log](#view-commit-history-in-the-log)
    -   [Directories aren\'t content](#directories-arent-content)
-   [Exploring history](#exploring-history)
    -   [Add more text to Workspace](#add-more-text-to-workspace)
    -   [Inspect our changes](#inspect-our-changes)
    -   [Range syntax also works for
        logs](#range-syntax-also-works-for-logs)
    -   [Using unique ID instead of HEAD
        offset](#using-unique-id-instead-of-head-offset)
    -   [Restore the Workspace to a clean
        state](#restore-the-workspace-to-a-clean-state)
-   [Moving through time](#moving-through-time)
    -   [Checkout old version of a
        file](#checkout-old-version-of-a-file)
    -   [Don\'t lose your head](#dont-lose-your-head)
-   [Branching and merging](#branching-and-merging)
    -   [Create a new branch and switch to
        it](#create-a-new-branch-and-switch-to-it)
    -   [Create a new file](#create-a-new-file)
    -   [Switch back to master and
        merge](#switch-back-to-master-and-merge)
-   [Ignoring Things](#ignoring-things)
    -   [Create some output files](#create-some-output-files)
    -   [Create .gitignore](#create-.gitignore)
    -   [Ignore some files](#ignore-some-files)
-   [Github](#github)
    -   [Git != Github](#git-github)
    -   [Set up new repository](#set-up-new-repository)
    -   [Configure remotes and push from
        local](#configure-remotes-and-push-from-local)
    -   [Check that you are up to date](#check-that-you-are-up-to-date)
-   [Collaborating](#collaborating)
    -   [Clone your repository](#clone-your-repository)
    -   [Edit trees.txt](#edit-trees.txt)
    -   [Update and push](#update-and-push)
-   [Conflicts](#conflicts)
    -   [Person 1 edits
        \~/Desktop/garden/shopping_list.txt](#person-1-edits-desktopgardenshopping_list.txt)
    -   [Person 2 edits \~/Desktop/garden-clone/shopping_list.txt
        *without*
        pulling](#person-2-edits-desktopgarden-cloneshopping_list.txt-without-pulling)
    -   [Edit conflict, stage, commit, and
        push](#edit-conflict-stage-commit-and-push)
-   [Pull Requests](#pull-requests)
    -   [Shared Repository Workflow](#shared-repository-workflow)
-   [Graphical User Interfaces](#graphical-user-interfaces)
-   [Version control with source
    vs. notebooks](#version-control-with-source-vs.-notebooks)
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

```{=org}
#+CAPTION: Base your new work on the most recent snapshot.
```
```{=org}
#+ATTR_ODT: :width 12
```
![](images/local-repository.png "Workspace or Working Tree"){width="100px"}

-   Move backwards and forwards in time using save points in your code
    history.
-   Control what goes into a save point
-   Collaborate
-   Explore alternative versions of your project without destroying
    prior work
-   Useful for text files, less useful for binary files (most of the
    useful features are text-oriented)

# Setup

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

Only push the current branch (more about this later):

``` bash
git config --global push.default simple
```

Merge, don\'t rebase (more about this later):

``` bash
git config --global pull.rebase false
```

## (Optional) Change name of default branch

``` bash
git config --global init.defaultBranch main
```

## Inspect your configuration

``` bash
git config --list                   # or -l
git config --list --show-origin     # where is this setting coming from?
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

Git uses this special subdirectory to store all the information about
the project, including all files and sub-directories located within the
project\'s directory. If we ever delete the \`.git\` subdirectory, we
will lose the project\'s history.

## Check status (we will do this a lot)

``` bash
git status
```

# Tracking changes

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

![Build a new snapshot (\"commit\") in the Staging
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
# Concicse help
git add -h

# Verbose help
man git-add
```

## Add more history

Edit with editor of your choice:

``` example
1. Cherry tomatoes
2. Italian basil
```

``` bash
git status
git diff

# If you try to commit the file before you add it to the Staging area,
# nothing happens:
git commit -m "Add basil"
git status

# Add file to Staging area, then commit:
git add shopping_list.txt
git commit -m "Add basil"
```

**Instructor\'s note:** Update drawing with repository history going
back in time (H, H\~1, H\~2...)

## Add more history; look at Staging area vs Workspace

``` example
1. Cherry tomatoes
2. Italian basil
3. Jalapenos
```

``` bash
# By default, "diff" shows changes to Workspace
git status
git diff

# Once the file is added to Staging, "diff" no longer shows changes
git add shopping_list.txt
git status
git diff

# You can examine Staging instead
git diff --cached               # or "--staged"
git commit -m "Add peppers"
git status
```

-   Staging area is for creating sensible commits. You can edit multiple
    files and only add a subset of them to a given commit. This makes it
    easier to look back at your work.
-   What goes in a commit?
    -   A coherent functional chunk (whatever that means)
    -   If you wanted to cleanly roll back, what would that look like?

## View commit history in the log

``` bash
git log
git log --oneline
git log --oneline --graph       # Useful if you have many branches
git log --author=~Gilgamesh
git log --since=5.days          # or weeks, months, years
```

-   You can identify commit by unique ID or by HEAD offset
-   HEAD is a pointer to the most recent commit

## Directories aren\'t content

Try to commit an empty directory:

``` bash
mkdir flowers
git status
git add flowers
git status
```

Now add files and try again:

``` bash
touch flowers/roses flowers/tulips
git status
ls flowers
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

## Inspect our changes

``` bash
cat shopping_list.txt

# Identical to "git diff" with no argument
git diff HEAD shopping_list.txt

# Show all changes back to this point
git diff HEAD~1 shopping_list.txt
git diff HEAD~3 shopping_list.txt

# Show changes for just HEAD~3
git show HEAD~3 shopping_list.txt

# Show changes in range of commits
git diff HEAD~3..HEAD~1 shopping_list.txt
```

## Range syntax also works for logs

``` bash
git log HEAD~3..HEAD~1
```

## Using unique ID instead of HEAD offset

``` bash
git diff f22b25e3233b4645dabd0d81e651fe074bd8e73b shopping_list.txt

# Use reduced ID from "git log --oneline"
git diff f22b25e shopping_list.txt
```

## Restore the Workspace to a clean state

``` bash
git status                      # We have unstaged changes

# Revert the working tree to the most recent commit
git checkout HEAD shopping_list.txt
cat shopping_list.txt
```

# Moving through time

## Checkout old version of a file

![Check out an old commit to view
it](images/git-checkout.svg "Checkout")

``` bash
git checkout f22b25e shopping_list.txt   # or "git checkout HEAD~3 shopping_list.txt"
cat shopping_list.txt

# These changes are also in the Staging area; do a commit if you want to keep
# this older version
git status
git checkout HEAD shopping_list.txt      # get back the new version
```

**Instructor\'s note:** Update drawing with files moving in and out of
working tree/staging area

## Don\'t lose your head

What if you want to see a previous version of the whole project?

``` bash
# Detached HEAD moves the whole HEAD pointer back to an earlier version
git checkout HEAD~2
git status

# Move HEAD back to latest commit by checking out the branch name
git checkout master
```

-   You can also check out a tag.
-   Unfortunately some of these terms, like \"checkout\", are
    overloaded. Think about what you want to do to your history, then
    look up the appropriate command.

**Instructor\'s note:** Update drawing with moving HEAD pointer

# Branching and merging

```{=org}
#+CAPTION: Git branching and Merging (https://imgur.com/gallery/YG8In8X/new)
```
```{=org}
#+ATTR_ORG: :width 200px
```
![](images/branch-merge.png "Branching and Merging")

## Create a new branch and switch to it

``` bash
git checkout -b feature         # equivalent to "git branch feature" + "git checkout feature"
git branch                      # Show all branches
git status
```

![Check out the branch to work on it
(1)](images/branch-old.png "Main branch")

![Check out the branch to work on it
(2)](images/branch-new.png "Feature branch")

## Create a new file

``` bash
touch feature.txt
nano feature.txt
```

``` example
This is a new feature we're trying out
```

``` bash
git add feature.txt
git commit -m "Added a trial feature"
ls                              # We have a new file
```

## Switch back to master and merge

``` bash
git checkout master
ls                              # File doesn't exist on the master branch
git merge feature
ls                              # Merging the feature branch adds your changes
```

-   This is simplest possible case; all of the new changes were in one
    branch

**Instructor\'s note:** Draw the branch history with the merge
(Fast-Forward merge moves branch tag). A branch history with competing
changes is shown in the Conflicts section below (Recursive merge
resembles octopus graph)

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

## Ignore some files

``` example
*.dat
results/
```

``` bash
# We are ignoreing .dat files and tracking .gitignore
git status
git add .gitignore
git commit -m "Ignore output files"
```

-   Ignoring complicated directory structures can be tricky, come talk
    to me
-   You should generally ignore archives (zip, tar), images (png, jpg),
    binaries (dmg, iso, exe), compiler output, log files, and .DS_Store
    (Mac)

# Github

```{=org}
#+CAPTION: Coordinate with co-authors.
```
```{=org}
#+ATTR_ODT: :width 12
```
![](images/distributed.png "Distributed version control"){width="100px"}

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

``` bash
git pull
```

-   `pull` is a shortcut for `fetch` + `merge`

# Collaborating

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

# Conflicts

![A more complicated merge
(1)](images/basic-merging-1.png "Pre-merge state")

![A more complicated merge
(2)](images/basic-merging-2.png "gPost-merge state")

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

# Pull Requests

cf.
<https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>
Topics to discuss:

-   Shared Repository model vs. Fork-and-Pull model
-   Protected branches
-   Create a pull request
-   Request a PR review
-   Merging PR

## Shared Repository Workflow

1.  Clone repository
2.  Create branch
3.  Create pull request

# Graphical User Interfaces

-   Pro
    -   Viewing history is usually a much better experience
-   Cons
    -   Not fully functional (missing commands and command options)
    -   Git is still complicated. Menus and buttons don't change that.

# Version control with source vs. notebooks

-   .ipynb files contain a lot of JSON boilerplate that isn\'t code

# Next steps (intermediate Git)

### Useful commands that you should add to your repertoire

-   `git blame`: See who changed each line of a file
-   `git bisect`: Find out when a change was introduced (good man page)
-   `git revert`: Undo your recent commits (good man page)
-   `git add --patch`: Stage a part of a file (\"hunk\") instead the
    entire file
-   `git -i` \[command\]: Run a command interactively, confirming each
    step

### Potentially dangerous commands that are useful in certain circumstances. Use with caution!

-   `git reset`: Throw away uncommitted changes (there are many options
    that affect what gets thrown away; read the documentation)
-   `git reset --hard`: Throw away some of your commits to get back to
    an earlier project state. Cannot be undone!
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
