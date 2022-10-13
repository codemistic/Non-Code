## Git

Git is a version-control system for tracking changes in computer files and coordinating work on those files among multiple people

### Configuration

```sh
git config --global user.email      # set global user email
git config --global user.name       # set global user name
git config --list                   # list global user details
```

#### Initialize a git repo

```sh
git init
```

#### Clone a repo

```sh
git clone [url]
```

## Commits

```sh
git add .                           # Add all files
git commit -m "commit message"      # commit
git status                          # Shows the modified files in working directory which are staged for next commit
git reset [fileName]                # Unstages file while retaining changes in present working directory
git stash                           # to keep uncommitted changes (both staged and unstaged) for later use
git reflog                          # Shows a log of changes to the local repository's HEAD
```

## Inspect

```sh
git diff                            # Shows diff of what is changed but not staged
git diff --staged                   # Shows diff of what is staged but not committed
git diff branch2...branch1          # Shows diff of what is in branch1 that is not in branch2
git diff HEAD                       # Shows difference between working directory and last commit
git diff --cached                   # Shows difference between staged changes and last commit
```

## Branches

```sh
git branch                  # list all local branches
git branch [branch-name]    # creates a new branch with given name
git checkout [branch-name]  # switch to given branch
git merge [branch]          # merge the specified branch’s history into the current one
git log                     # Shows current branch's commit history
git log -p                  # Display the full diff of each commit
git log --stat              # Include which files were altered and the relative number of lines altered

```

## Update

```sh
git remote -v                      # to view see the actual URLs for each alias
git remote add [aliasName] [url]   # to create a new connection record to a remote repository with a local alias
git remote rm [aliasName]          # Removes aliasName
git fetch [alias]                  # to download contents from a remote repository
git push [remote] [branch]         # to upload local repository content to a remote repository
git push [remote] --force          # to forcefully upload your local repository content to remote, Use only when you are very sure
git pull                           # to update the local version of a repository from a remote
```

## Stash

```sh
git stash push "add style to our site"  # Save your local modifications to a new stash entry
git stash list                          # List the stash entries that you currently have
git stash pop stash@{0}                 # Remove a single stashed state from the stash list and apply it on top of the current working tree state
git stash clear                         # Remove all stashed entries
```

## Rebase main branch into feature branch

```sh
git checkout feature
git fetch origin main
git rebase origin/main
```
