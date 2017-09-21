<!--- Author: Daniel Strohfeldt --->
# PythagoreanCupcake
A Project for Software Engineering Class at University of Wisconsin Milwaukee (Fall 2017)

# Project Contributors:
	- Daniel Strohfeldt
	- Matthew Flejter
	- David Jaeger
	- Joshua Sharkey
	- Zane Shahrin
	- Yubin Zheng

# Up and Running With GIT
This portion of the README will take you through the steps needed to get going with git.

## Installing Git
Here is a guide to get git installed on your machine.

### Mac OSX Users
I recommend getting homebrew if you don't already have this awesome package manager.
To install hombrew run this command in your terminal
```
	- $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Next install git by executing the following command in your terminal.
```
	- $ brew install git
```
If you don't want to install git using brew you can do so with git's osx installer hosted on sourceforge.
	- http://sourceforge.net/projects/git-osx-installer/

### Windows Users
Windows Users have a simple way of installing git as well.
Visit this page to get your bash terminal, and git tools.
	- https://git-for-windows.github.io/

Hit the download button and follow the install instructions.
Then open up the gitBASH application.

### Linux Users
If you're reading this document you should already know how to install git...
After all Linus is responsible.

## Beginning Git
Hooray you've painlessly installed git!
Now we will get to use the command line interface for this tool.
We'll start by configuring your git config.

To configure your user name and email run the following sequence of commands.
```
	- $ git config --global user.name "YOUR USERNAME"
	- $ git config --global user.email "EmailAssociatedWithGitHubAccount@some.com"
```

This will allow git to know your credentials when trying to create pull requests and use other various features of git.

### Cloning this Repository
Alright you should be all setup to clone this repository so that you can have your own local copy!

To clone the repository, you should move into a directory where you want the files to live.
```
	- $ cd your_safe_space
```

Next you will run the following command.
```
	- $ git clone https://github.com/DanielStrohfeldt/PythagoreanCupcake.git
```
This will copy all the files into a directory called PythagoreanCupcake.

### Opening your First Branch
Okay so now you have a local copy of the files and are able to start contributing
to the project, w00p! w00p!

To open a branch, which hopefully will be later merged into the master branch
run the following command with your credentials in the correct locations.

```
	- $ git checkout -b user/"user.name"/"branch_description"
```

You are now on your own branch. To see the working branch run the following command:

```
	- $ git branch
```

To see all currently open branches use the -a option

```
	- $ git branch -a
```

To see all of the commits behind the tip of your branch run the following command:

```
	- $ git log
```

### Making your First Pull Request
We've come a long way, now your ready to open your first pull request.

So to make your first pull request you should edit a file add a comment or something
which should be added to the code. Once you have editted a file go to the next step.
Check the status of your branch by running the following command:

```
	- $ git status
```

This will show which files have been editted and their current status.

To check the difference between your branch edits and the branch which you branched
from run the following command:

```
	- $ git diff
```

Now if you are satisfied with your edits. Continue on by adding them to a commit.
To do so run the following command:

```
	- $ git add filename
```

Your file has now been added to the commit.

Next create the commit by running the following command:

```
	- $ git commit -m "commit message goes here *describe your changes*"
```

Now you are ready to try get your changes pulled into mainline.
To do so run the following command:

```
	- $ git push origin HEAD
```

For more git related information read the git book!
	- https://git-scm.com/book/en/v1/Getting-Started
