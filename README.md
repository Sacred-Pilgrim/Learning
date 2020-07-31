# Learning
My first repository for GitHub
This serves as a tutorial for using GitHub for the very first time.

# Update after 2years
After using the following [School Github Profile](https://github.com/u16220073), an extra  [course from udemy](https://www.udemy.com/course/git-and-github-crash-course/?couponCode=NEW_COURSE2) was taken to further improve understanding of git & github.

The following are the few notes made from the course...
NB: commands used here work for git bash and may be different on cmd
1) You can Use "git diff" to check the difference between the current version of a tracked file vs the last time you commited it. [view more](https://www.atlassian.com/git/tutorials/saving-changes/git-diff#:~:text=git%20diff%20is%20a%20multi,%2C%20branches%2C%20files%20and%20more.&text=The%20git%20diff%20command%20is,state%20of%20a%20Git%20repo.)
2) You can use "git ls-files" to list all the files that are part of the GIT repo.
   If you want to list all files for a specific branch, e.g. master use [git ls-tree -r master --name-only](https://superuser.com/questions/429693/git-list-all-files-currently-under-source-control) 
3) For you to push into a private repo, you need to configure an ssh connection.
   This is how you do it:
   a) run "ssh-keygen -t rsa -b 4096 -C <youremail>
      i) you will be asked to enter the filename you wish to save your ssh key in ( by default it is C:/users/<userprofilename>/.ssh/id_rsa)
      you can leave as default or specify a different filename (with that same path e.i C:/users/<userprofilename>/.ssh/diff_id_rsa)
      ii) you will asked for a passphrase (press enter to leave it as default)
      iii) you will asked for a passphrase again (press enter to leave it as default)
   b) change directories to c:/.ssh using "cd ~/.shh"
   c) run "eval (ssh-agent -s)"
   d) run "ssh-add id_rsa ( or whatever you named your ssh key file to be)
   e) run "clip < id_rsa.pub ( or whatever you named your ssh key file to be but add the .pud at the end)
   
   login to your github account then go to settings>SSH and GPG keys
   f) click "new ssh key"
   g) enter the title of the key and paste content from your clipboard to the key field (press ctrl+V) then click "add ssh key"
      you'll be required to confirm your password.
 If all was done well without problems you should be able to push to your private repo
