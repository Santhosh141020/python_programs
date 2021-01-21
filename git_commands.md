# GIT COMMANDS

git init : to create repository

rm -rf .git : to delete an entire local repository

git status : to check status

git status -s : to get summarised

git add <file name> : to add the file to the staging

git add . : to add all local files in repository to the staging

git commit -m'comment' : To commit the files  

git checkout <filename> :To restore the files

git branch : to see the branches present

git branch <branch name> : to stay in master branch and to create branch

git checkout -b branch <branch_name> : to create and go inside that branch

git checkout <branch name> : to shift the branches

git merge <branch name> : to merge the branch with master branch

git branch -d <branchname> : to delete the branch but it does not delete if some file are not merged with master

git branch -D <branch name>: to delete directly 

git log : to get command history

git log -p -1 : to get history based on number specified

git diff : compares working tree with stagging area

git diff --staged : compares staging area with last commit

git commit -a -m"comment" : to directly commit without stagging

git stash -u : it moves the files in the working tree inside stash and clears the working tree

git stash list : it list the flies present in the stash

git stash show : it shows the modified to the files inside stash

git stash apply : it bring files from stash to working tree

git remote add <name usually origin> http link : to access te github repository

git clone httplink : to create a copy of remote repository in local file

get pull origin master  : to pull items from remote server

get push origin master : to push files  





### .gitignore

​	the file names or directories written in this file are ignored when we check status of the git  

​    it must be created as editable file using the editor u use



 