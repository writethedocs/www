=========================================
Contributing to the Write the Docs guide
=========================================

If you want to contribute to an awesome documentation guide, you've come to the right place. 
Welcome! Read on to understand what our guides are and how you can help.

Ways to contribute
-------------------

We encourage contributions from anyone regardless of professional or tool experience. 
Contributions are treated with respect if they respect the current effort and state of 
our guide.

The guides at Write the Docs are meant to address all aspects of software 
documentation. There are several ways to contribute to the content:

* For changes that span multiple files :ref:`create a fork, a branch, and a pull request <update-guide-in-git>`.
* `Submit an issue`_ to suggest small changes, new content, or to file bugs against existing content.

We encourage you to learn some of the basic tools we use, but if you don't want to deal with 
GitHub, email attachments or inline text to guide@writethedocs.org.

Where to start
--------------

We especially need contributions in these areas:

* :ref:`Tools and best practices for documenting APIs <api-documentation>`.
* Documentation best practices.
* Developer tools or docs-as-code toolchains and workflows.
* High-level discussions of common tools. 

For help finding where a new set of topics best fit into the rest of 
the guide, `ask in Slack`_, or `file a GitHub issue`_.

Guidelines
-----------

Follow these guidelines for discussing tools: 

* Ensure your content is of interest to a general audience.
* Avoid advocacy and plugs about your favorite toolchain, even if it's open source.
* Present specific use cases, how problems were solved, and what worked or didn't work well. 
* Consider to first `file a GitHub issue`_ or contact one of the guide editors at guide@writethedocs.org.

Keep content focused on general principles and best practices instead of arguing over minor 
points at the expense of major principles of clarity and communication. Avoid preferential 
editing that only offers your personal preferences for dealing with a particular writing 
situation. For example, if you recommend a particular word choice, tell the audience why it 
matters.

Use a friendly and encouraging tone. It's a good way to write docs in general, so practice 
with docs about docs!

When linking to resources, attribute the links appropriately and mention why the resources 
are useful.

Some files in the guide are written in `Markdown`_, and some 
are written in `reStructured Text (rST)`. We prefer rST 
although either format is acceptable.

Prerequisites
--------------

1. `Create a GitHub account`_.
2. `Download and install Git`_.
3. Open a terminal window and follow the instructions to `associate your
   GitHub username with your local Git installation`_.

   1. In macOS: Open the **Terminal** app.
   2. In Windows: From the Start Menu, open **Git Bash**.

4. In the repo UI, find the file name corresponding to an `existing issue`_ or page you want to improve. 

For example, ``/docs/documentarians.rst`` creates https://www.writethedocs.org/documentarians/. 

5. Review formatting guidelines for the Markup style the file uses. The example file above uses `reStructuredText (.rst) Markup`_. Other Markup styles for our guides include Markdown (.md).

.. _update-guide-in-git:

Update a guide in Write the Docs via a pull request
----------------------------------------------------

If you've never worked with Git and GitHub, use this section to get started. 

**In the GitHub UI:**

1.  `Fork the Write the Docs www project`_.

2.  Click **Create fork**.

3.  Click **< > Code**. 

4.  Copy the HTTPS URL for cloning the repository.

**In a terminal window:**

1.  Open a terminal.

    * In macOS: open the **Terminal** app.
    * In Windows: from the Start Menu, open **Git Bash**.

2.  Go to a directory for storing the cloned repository. 

3.  Type ``git clone``, followed by a space,
    and then paste the project URL:

       ::

          git clone https://github.com/myname/www.git

    git clone copies files from GitHub to a folder named ``www`` on your computer.

4.  Go to the ``www`` directory:

       ::

          cd www

5.  Create a new branch:

       ::

          git branch branch-name

    Replace ``branch-name`` with a brief description of your proposed changes. 
    Use dashes between words. For example: ``git branch important-typo-fix``.

6. Switch to the new branch:

       ::

          git checkout branch-name

**In any text editor like `Sublime Text`_ or `Visual Studio Code`_:**

1. Open the file you want to edit.

2. Edit and save the file.

**In a terminal window:**

1. List the files you updated.

       ::

          git status

2. If the list of updated files looks accurate, add any new or changed files to your local git project:

       ::

          git add -A

3. Save your changes:

       ::

          git commit -m "Your message"

   git commit saves all of your edited files. Replace ``Your message``
   with a description of the update you made. Learn how
   to `write a good commit message`_.

   You can repeat the same process to add multiple commits to your branch.

4. Send your commit(s) to your GitHub project:

       ::

          git push -u origin branch-name

   Remember to replace ``branch-name`` with the branch name you created earlier.

5. Create a `GitHub pull request`_ in the `Write the Docs www project`_.

Community
----------

The Write the Docs community is available for help, questions, or discussion:

- `Slack <https://www.writethedocs.org/slack/>`_
- `Conferences <https://www.writethedocs.org/conf/>`_
- `Local meetups <https://www.writethedocs.org/meetups>`_
- `Newsletter <https://www.writethedocs.org/newsletter/>`_


.. _existing issue: https://github.com/writethedocs/www/issues
.. _ask in Slack: https://www.writethedocs.org/slack
.. _Markdown: /guide/writing/markdown/
.. _Fork the Write the Docs www project: https://github.com/writethedocs/www/fork
.. _file a GitHub issue: https://github.com/writethedocs/www/issues/new
.. _Submit an issue: https://github.com/writethedocs/www/issues/new
.. _reStructuredText (.rst) Markup: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _Create a GitHub account: https://github.com/join
.. _Download and install Git: https://git-scm.com/downloads
.. _associate your GitHub username with your local Git installation: https://help.github.com/en/articles/setting-your-username-in-git
.. _Write the Docs www project: https://github.com/writethedocs/www
.. _Sublime Text: https://www.sublimetext.com
.. _Visual Studio Code: https://code.visualstudio.com/
.. _write a good commit message: https://chris.beams.io/posts/git-commit/
.. _GitHub pull request: https://help.github.com/en/articles/creating-a-pull-request
