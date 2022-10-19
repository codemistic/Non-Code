#### Git is an example of a distributed version control system commonly used for open source and commercial software development.

> Let's go :
initalize git in files/directories.
```
git init
``` 
1.Clone the repository in your local system.
```
git clone https://github.com/<your-user-name>/<repo-name>
``` 
2.Connect to remote
```
git remote add origin <url>
```
3.To check the current status of the repository.
```
git status
```
4.To add specific file to the staging area.
```
git add <file-name>
```
5.To add all changed file to staging area.
```
git add .
```
6.To unstage a certain file
```
git restore --stagged <filename>
```
7.To see recent changes in the repository.
```
git diff
```
8.To give a message and commit.
```
git commit -m "your-message"
```
9.To see the commit history.
```
git log
```
10.To see last specific commits (eg. Last 3 commits).
```
git log -3
```
11.To discard the specific commit.
```
git revert <commit-token>
```
12.To undo the commit and bring back changes to staging area.
```
git reset --soft HEAD <no._of_commit_to_revert>
```
13.To show remote URLs
```
git remote -v
```
14.To fetch the changes from origin to your local system.
```
git pull origin
```
15.To create a branch named branch-name.
```
git branch <branch-name> 
```
16.To make changes in the specific branch.
```
git checkout <branch-name>
```
17.To merge sub branch to main branch.
```
git merge <branch-name>
```
18.To delete a specific branch.
```
git branch -d <branch-name> 
```
19.To push the recent commits.
```
git push origin <branch-name>
```
20.Connect to remote
```
git remote add origin <url>
```
21.To push the current branch and set the remote as upstream
```
git push --set-upstream origin master
```
22.To rename branch name.
```
git branch -m <branch-name>
```
23.change url for git remote repo
```
git remote set-url origin
```
 


