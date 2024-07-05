=========================================
Contributing to the Write the Docs guide
=========================================

If you want to contribute an awesome documentation guide, you've come to the right place. 
Welcome! Read on to understand what our guides are and how you can help.

Ways to contribute
-------------------

We encourage contributions from anyone regardless of professional or tool experience. 
Contributions are treated with respect if they respect the current effort and state of 
our guide.

The guide at Write the Docs is meant to address all aspects of software 
documentation. There are several ways to contribute to the content:

* Fork, branch, and submit a pull request.
* `Submit an issue <https://github.com/writethedocs/www/issues>`_ to suggest new content 
or to file bugs against existing content.

Where to start
--------------

We especially need contributions in these areas:

* :ref:`Tools and best practices for documenting APIs <api-documentation>`.
* Documentation best practices.
* Developer tools or docs-as-code toolchains and workflows.
* High-level discussions of common tools. 

For help finding where a new set of topics best fit into the rest of 
the guide, ask in Slack or file a GitHub issue.

Guidelines
-----------

The guide is not a place to plug your favorite toolchain, even if it's open source. 
Follow these guidelines for discussing tools: 

* Ensure your content is of interest to a general audience.
* Avoid advocacy.
* Present specific use cases, how problems were solved, and what 
worked or didn't work well. 
* Consider first creating a GitHub issue or contacting one of the guide editors.

Keep content focused on general principles and best practices instead of arguing over minor 
points at the expense of major principles of clarity and communication. Avoid preferential 
editing that only offers your personal preferences for dealing with a particular writing 
situation. For example, if you recommend a particular word choice, tell the audience why it 
matters.

Use a friendly and encouraging tone. It's a good way to write docs in general, so practice 
with docs about docs!

When linking to resources, attribute the links appropriately and mention why the resources 
are useful.

Some files in the guide are written in `Markdown </guide/writing/markdown/>`_, and some 
are written in `reStructured Text (rST) </guide/writing/reStructuredText/>`_. We prefer rST 
although either format is acceptable.










Editing the Write the Docs website
===============================================

If you've never worked with Git and GitHub, use this section to get started. 

To suggest small changes, `submit issues <https://github.com/writethedocs/www/issues>`_ via 
the GitHub interface. 

For changes that span multiple files, create a fork and branch, work locally (although you can 
do most things in the GitHub interface in your branch), and keep your fork in sync with the main 
repository.

We encourage you to learn some of the basic tools we use but, if you don't want to deal with 
GitHub, email attachments or inline text to guide@writethedocs.org.

Prerequisites
-------------

1. `Create a GitHub account`_.
2. `Download and install Git`_.
3. Open a terminal window and follow the instructions to `associate your
   GitHub username with your local Git installation`_.

   1. In macOS: Open the **Terminal** app.
   2. In Windows: From the Start Menu, open **Git Bash**.

4. In the repo UI, find the file name corresponding to an `existing issue`_ or page you want to improve. 

For example, ``/docs/documentarians.rst`` creates https://www.writethedocs.org/documentarians/. 

5. Review formatting guidelines for the Markup style the file uses. The example file above uses `reStructuredText (.rst) Markup`_. Other Markup styles include Markdown (.md) and AsciiDoc (.adoc).

Update a guide in git
----------------------

1.  Visit the `Write the Docs www project`_.

2.  Click **Fork** in the upper-right corner to create a
    copy of the project in your GitHub account. The new page for the
    forked project opens.

3.  Click the **Clone or download** button and copy the https URL from
    the project page.

4.  Open a terminal window to run ``git`` commands.

    1. In macOS: Open the **Terminal** app.
    2. In Windows: From the Start Menu, open **Git Bash**.

5.  Navigate to or create the directory to where you want to clone the repository. 

6.  In your terminal window, type ``git clone``, followed by a space,
    and then paste the project URL:

    ::

       git clone https://github.com/myname/www.git

6.  Press Enter. The command copies files from GitHub to a folder named
    ``www`` on your local machine.

7.  In the terminal window, go to the ``www`` directory.

    ::

       cd www

8.  Create and switch to a branch. Using the commands below,
    replace ``branch-name`` with a name that briefly describes the
    changes you’ll make, preferably use dashes between words. For
    example, ``important-typo-fix``.

    a. Create a branch with:

       ::

          git branch branch-name

       Switch to the branch:

       ::

          git checkout branch-name

    b. Alternatively, use one command to perform both steps at once:

       ::

          git checkout -b branch-name

9. Open the ``www`` folder on your computer.

10. | Open the file you wish to edit using a text editor like `Sublime
      Text`_ or `Visual Studio Code`_, then save the file.

11. In your terminal window, type:

    ::

       git status

    This will show you all the files that you have updated.

12. If your changes look accurate, enter the following in your terminal window:

   ::

      git add -A

   This will add any new and changed files to your local project.

13. To save your changes, enter the following in your terminal window:

   ::

      git commit -m "Your message"

   This will save all of your edited files. Replace ``Your message``
   with a description of the update you made. *Protip*: Learn how
   to `write a good commit message`_.

   You can repeat the same process to add multiple commits in your
   branch.

14. Send your commit(s) to your GitHub project using ``git push``. Enter the following in your terminal window:

   ::

      git push -u origin branch-name

15. Create a `GitHub pull request`_ in the `Write the Docs www project`_.

.. _existing issue: https://github.com/writethedocs/www/issues
.. _RST primer: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _Create a GitHub account: https://github.com/join
.. _Download and install Git: https://git-scm.com/downloads
.. _associate your GitHub username with your local Git installation: https://help.github.com/en/articles/setting-your-username-in-git
.. _Write the Docs www project: https://github.com/writethedocs/www
.. _Sublime Text: https://www.sublimetext.com
.. _Visual Studio Code: https://code.visualstudio.com/
.. _write a good commit message: https://chris.beams.io/posts/git-commit/
.. _GitHub pull request: https://help.github.com/en/articles/creating-a-pull-request

Community
----------------

The Write the Docs community is available for help, questions, or discussion:

- `Slack <https://www.writethedocs.org/slack/>`_
- `Conferences <https://www.writethedocs.org/conf/>`_
- `Local meetups <https://www.writethedocs.org/meetups>`_
