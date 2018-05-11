How-to Use Git and Github
#########################


Introduction
============

Software developers use `Git <https://git-scm.com/>`_ and `GitHub <https://github.com/>`_ for version control of their source code. Documentation should be included with the software so it is necessary for technical writers to have knowledge of these tools. This document is a user guide for common Git commands to manage files stored on GitHub. The document explains how to set up and update a repository, and how to fork a repository so you can participate with open source projects. 

If you do not have Git installed or a GitHub account you will need to do that before you begin. It is beneficial to have basic knowledge of `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ or `Markdown <http://commonmark.org/>`_ because GitHub renders those markup languages. 

* `Install Git <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_. There are versions for MacOS, Linux, and Windows.
* Go to `GitHub <https://github.com/>`_ and click **Sign Up** to create an account.
 
.. note::
   You can manage your repositories via `HTTPS <https://help.github.com/articles/which-remote-url-should-i-use/>`_ or configure `SSH <https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/>`_.


Terminology
===========

There are some keywords to understand that will become more familiar as you use Git and GitHub.

* **Clone** - Copy of a GitHub repository that is stored on your computer. 
* **Gitignore** - A file in your repository that defines exclusions for file types or directories when data is pushed to your GitHub repository. 
* **Branch** - Each repository has a Master branch and can contain multiple development branches.
* **Remote** - Name that refers to the URL for a repository.  
* **Origin** - Remote name that references your GitHub repository. There are **fetch** and **push** URLs. 
* **Fork** - Copy of another person's repository. You can add, change, or delete files with no affect on the upstream repository.  
* **Upstream** - Remote name that references an upstream repository that you forked. There are **fetch** and **push** URLs.
* **Pull Request** - After you make changes to a forked repository, submit a **pull request** to merge your changes with the upstream repository.



Set Up a Repository
===================

To begin, create a repository so that you have full access to add, change, and delete files. The best way to learn Git and GitHub is to work with the tools. This will build a foundation of knowledge that you can apply to more complex tasks when you participate in open source projects.


.. _create-repo:

Create a Repository
-------------------

You can create a repository on your computer or on GitHub. For this example we will login to GitHub and create the repository and gain some familiarity with the user interface.  

#. On the top, right of the screen, click the plus sign (+).
#. Select **New Repository**.
#. Enter the repository information: 

   * Type a repository name and description. 
   * Select **Public**.
   * Click the box to initialize the repository with a README. 
   * Select any **gitignore** and **license**. These can be changed later.

#. Click the button: **Create Repository**.    



.. _clone-repo:

Clone a Repository
------------------

To download a GitHub repository to your computer use the :command:`git clone` command and the repository's URL. The cloned repository is where your work is performed. When you are satisfied with your changes you :command:`push` the updates to your GitHub repository. 

#. On your computer, create a root directory where your repositories will reside. 
#. On GitHub, navigate to your repository and click the button labeled **Clone or download**.
#. Select **Clone with SSH** or **Clone with HTTPS** and this is dependent upon whether you setup your GitHub account to use SSH or HTTPS.

   .. figure:: /_static/img/gitbasics/clone_ssh.png
      :scale: 75 %


   .. figure:: /_static/img/gitbasics/clone_https.png
      :scale: 75 %


#. Click the clipboard icon to copy the repository's URL. 
#. On your computer, open a terminal session and navigate to your repository directory.
#. Type :command:`git clone` and paste the URL. Press **Enter**.

   .. code-block:: shell

      git clone git@github.com:<username>/<repository_name>.git

        Cloning into 'repository_name'...
        remote: Counting objects: 5, done.
        remote: Compressing objects: 100% (3/3), done.
        remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
        Receiving objects: 100% (5/5), done.

#. After the repository is cloned, compare the contents of the cloned directory and your GitHub repository. They should be identical. 



.. _change-repo:

Change Repository Content
-------------------------

.. note::
   The :command:`git status` command is used to show how the repository changes as files are updated.    



#. To view the repository's status and verify there are no pending changes do a :command:`git status` and read the output.

   .. code-block:: shell

      git status
        On branch master
        Your branch is up to date with 'origin/master'.

        nothing to commit, working tree clean
     


#. Use a text editor such as `Microsoft Visual Studio Code <https://code.visualstudio.com/>`_ or `GitHub Atom <https://atom.io/>`_ to create a new file. Then run :command:`git status` and the output will display the new file and a message to use :command:`git add`.

   .. code-block:: shell

      git status
         
         On branch master
         Your branch is up to date with 'origin/master'.

         Untracked files:
         (use "git add <file>..." to include in what will be committed)

            newfile.md

         nothing added to commit but untracked files present (use "git add" to track)


#. To add the new file to tracking so that it can be committed to the repository, type :command:`git add <filename>`. A more efficient method is to use :command:`git add .` which is useful when there are multiple files to add. 

   .. code-block:: shell

      git add .


#. Do the :command:`git status` and you will see output that there are changes ready to be committed.

   .. code-block:: shell

      git status
    
        On branch master
        Your branch is up to date with 'origin/master'.

        Changes to be committed:
        (use "git reset HEAD <file>..." to unstage)

	      new file:   newfile.md



#. The new file is ready to be committed to the repository with the :command:`git commit` command. 

   * The command requires a brief message that describes the commit and is displayed on the GitHub repository. 
   * Use :command:`git commit -m "message text"`. 
   
   .. code-block:: shell
   
      git commit -m "Message about the commit"
       
      [master 8e30e03] New file
      1 file changed, 1 insertion(+)
      create mode 100644 newfile.md

   .. note:: 
      When you configured **Git** you specified a default text editor which opens when you submit the commit command without the **-m "message text"**.          



#. Perform the :command:`git status` command and read the output. The repository on your computer is now one commit ahead of the GitHub repository. If you list the contents of directory on your computer and compare it with the GitHub repository you will see that your new file does not exist on GitHub. 

   .. code-block:: shell

      git status
        
        On branch master
        Your branch is ahead of 'origin/master' by 1 commit.
        (use "git push" to publish your local commits)

        nothing to commit, working tree clean


.. tip::
   For more practice, use these suggestions to update other files in your respository:

   * Update your **license** file. GitHub explains the `repository licenses <https://help.github.com/articles/licensing-a-repository/>`_ and provides the license text at `choosealicense.com <https://choosealicense.com/>`_. 
   * Add an exclusion to your **gitignore**. For examples, refer to this `GitHub repository <https://github.com/github/gitignore>`_. 


.. _push-repo:

Update a Repository
-------------------

After files are updated in the cloned repository we need to :command:`push` the updates to the GitHub repository. 

#. To see how this works, use the :command:`git remote` command to display the repository's **fetch** and **push** URLs. 

   .. code-block:: shell

      git remote -v

        origin git@github.com:<username>/<repository_name>.git (fetch)
        origin git@github.com:<username>/<repository_name>.git (push)


#. When there is a committed file that is ready to be pushed up to the GitHub repository use the :command:`git push`. After a successful push the cloned repository and the GitHub repository are synchronized. 

   .. code-block:: shell

      git push origin master

         Counting objects: 6, done.
         Delta compression using up to 4 threads.
         Compressing objects: 100% (4/4), done.
         Writing objects: 100% (6/6), 590 bytes | 590.00 KiB/s, done.
         Total 6 (delta 1), reused 0 (delta 0)
         remote: Resolving deltas: 100% (1/1), done.
         To github.com:<username>/<repository_name>.git
         20fe071..c3bc10f  master -> master


#. Do the :command:`git status` command to confirm there are no discrepancies between the repositories.

   .. code-block:: shell

      git status

         On branch master
         Your branch is up to date with 'origin/master'.

         nothing to commit, working tree clean



Collaborate on an Open Source Project
=====================================

Open source projects are all about community, collaboration, and participation. When we find a project that sparks our creative interest we need to **fork** the repository, make changes that we hope will improve the project, and submit a **pull request** to merge our changes into the project. To emulate the process we will use the GitHub sample repository `octocat/Spoon-Knife <https://github.com/octocat/Spoon-Knife>`_. 


.. _fork-repo:

Fork a Repository
-----------------

The procedure to **fork** someone's repository into your GitHub profile amounts to a couple of clicks on GitHub. Then, clone the forked repository to your computer. 

#. Login to your GitHub account.
#. Find the repository for the project. For example, `octocat/Spoon-Knife <https://github.com/octocat/Spoon-Knife>`_.
#. On the top, right of the page, click the button labeled **Fork**.

   .. figure:: /_static/img/gitbasics/octocat_fork_button.png
      :scale: 75 %

#. Verify that your GitHub profile now has a fork of the octocat/Spoon-Knife repository. 

   .. figure:: /_static/img/gitbasics/octocat_forked_repo.png
      :scale: 75 %


#. Clone the forked repository. Refer to the section :ref:`Clone a Repository <clone-repo>`.



Create a Fork's Upstream Remote
-------------------------------

When repositories are forked multiple people have copies of the upstream repository. There are continuous adds, changes, and deletes so you need a method to keep your fork up-to-date. The solution is to configure an upstream remote so that you can merge data. 

#. On your computer, from the fork's repository use the command :command:`git remote` to display the current remotes.

   .. code-block:: shell

      git remote -v
   
         origin git@github.com:<username>/Spoon-Knife.git (fetch)
         origin git@github.com:<username>/Spoon-Knife.git (push)

#. To create the **upstream** remote we need to add the original repository's URL. Refer to the section :ref:`Clone a Repository <clone-repo>` about how to copy the URL. 

   .. code-block:: shell

      git remote add upstream git@github.com:octocat/Spoon-Knife.git


#. Use the :command:`git remote -v` and verify the upstream remote was added to your repository.

   .. code-block:: shell

      git remote -v
   
         origin git@github.com:<username>/Spoon-Knife.git (fetch)
         origin git@github.com:<username>/Spoon-Knife.git (push)
         upstream git@github.com:octocat/Spoon-Knife.git (fetch)
         upstream git@github.com:octocat/Spoon-Knife.git (push)   




Merge Upstream Data Into a Fork
-------------------------------

Before you begin to work on a forked repository you should merge the upstream repository into the cloned fork repository on your computer. This ensures that you have the most up-to-date files. Then :command:`push` your forked repository to your GitHub respository. 


#. Open a terminal session and change to the repository's directory. 
#. Run the following series of commands to merge changes from the upstream repository to your forked repository. If there are existing changes in your fork, they are not overwritten.  

   #. :command:`git fetch upstream`
   #. :command:`git checkout master`
   #. :command:`git merge upstream/master`


   .. code-block:: shell

      git fetch upstream

         From github.com:octocat/Spoon-Knife
         * [new branch]      change-the-title -> upstream/change-the-title
         * [new branch]      master           -> upstream/master
         * [new branch]      test-branch      -> upstream/test-branch

      git checkout master
     
         Already on 'master'
         Your branch is up to date with 'origin/master'.  

      git merge upstream/master
   
         Already up to date.   


#. After the fork on your computer is updated, use the :command:`push` command to update your GitHub fork.

   .. code-block:: shell

      git push origin master


Now your forked repository is ready for you to update some code or write a new document. For a reminder of the Git commands, refer to the sections :ref:`Change Repository Content <change-repo>` and :ref:`Update a Repository <push-repo>`. 


Submit a Pull Request
---------------------

Most of us do not have permission to change the upstream repository, so we submit a :command:`pull request`. The change is reviewed by an owner of the repository and when it is approved your brilliant code or document are merged from your forked repository into the upstream repository. 

#. Login to your GitHub account.
#. In your profile, navigate to your forked repository.
#. Click the button labeled **New Pull Request**.

   .. figure:: /_static/img/gitbasics/new_pull_request.png
      :scale: 75 %

#. Review the information on the **Comparing changes** page. 

   .. figure:: /_static/img/gitbasics/comparing_changes.png
      :scale: 40 %


#. Click the button labeled **Create pull request**.
#. On the **Open a pull request** page, include a comment about your pull request. 

   .. figure:: /_static/img/gitbasics/open_pull_request.png
      :scale: 75 %

#. To submit the pull request and have an official pull request number assigned, click the button labeled **Create pull request**. 

   .. figure:: /_static/img/gitbasics/pull_request_opened.png
      :scale: 75 %
   


.. _delete-repo:

Delete a Repository
===================

Nothing lasts forever and repositories are no exception. When you are 100% certain you are finished with a repository you can delete it from GitHub and your computer. You cannot undo and there is no recycle bin when you **delete** a GitHub repository. 


Delete a GitHub Repository
--------------------------

#. Login to your GitHub account.
#. Navigate to your repositories. 
#. Click **Settings**. 
#. Scroll to the bottom of the page and look for the **Danger Zone**.
#. Click the button labeled **Delete this repository**.

   .. figure:: /_static/img/gitbasics/delete_repo.png
      :scale: 75 %
   
   
Delete a Cloned Repository
--------------------------

On your computer, delete the repository's directory. On Windows or Mac computers make sure to empty the Recycle Bin or Trash. 




Conclusion
==========

The purpose of this user guide was to show how to use some common Git commands and work with a GitHub repository. My hope is that the information was useful to learn the syntax and concepts needed to manage repositories with Git and GitHub. 



Related Information
-------------------

Git and GitHub are well-documented which helps those of us who are casual users that need to collaborate on a project. 

* `Git documentation <https://git-scm.com/doc>`_
* `GitHub documentation <https://help.github.com/>`_



