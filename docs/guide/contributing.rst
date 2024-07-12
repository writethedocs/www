=========================================
Contributing to the Write the Docs guide
=========================================

Welcome! The guides at Write the Docs are meant to address all aspects of software documentation. 
To contribute to a guide, read on to understand our guides and how you can help.

How to contribute
-------------------

Anyone can contribute regardless of professional or tool experience. Contributions that respect our guide's 
current effort and state are treated with respect.

There are several ways to contribute:

* :ref:`Edit a single guide directly in the GitHub UI <update-guide-via-github>`.
* :ref:`Edit files using Git <update-guide-in-git>`.
* `Submit an issue`_ to suggest small changes, new content, or to note bugs in existing content.

What to contribute
-------------------

We especially need contributions in these areas:

* :ref:`Tools and best practices for documenting APIs <api-documentation>`.
* Documentation best practices.
* Developer tools or docs-as-code toolchains and workflows.
* High-level discussions of common tools. 

For help organizing a new topic within the current guide, `ask in Slack`_, or `file a GitHub issue`_.

Contribution guidelines
-------------------------

* Use a friendly and encouraging tone. It's a good way to write docs, so practice with docs about docs!

* Attribute links and mention why linked resources are useful.

* Use `reStructuredText (.rst)`_ (`Markdown`_ is also acceptable).

* Focus content on general principles and best practices. Arguing over minor points impedes clarity. 

* Avoid enforcing personal preferences. For example, if you recommend a word choice, tell the audience why it matters.

Additionally, follow these guidelines when discussing tools: 

* Ensure your content is of interest to a general audience.
* Avoid advocacy and plugs about your favorite toolchain, even if it's open source.
* Present specific use cases, how problems were solved, and what worked or didn't work well. 
* Consider to first `file a GitHub issue`_ or contact a guide editor at guide@writethedocs.org.

.. _update-guide-via-github:

Editing a single guide via the GitHub UI
-------------------------------------------

1. In the `Write the Docs www project`_, find the file for the content you want to improve. 

For example, ``/docs/documentarians.rst`` creates https://www.writethedocs.org/documentarians/. 

2. Review formatting guidelines for the file's Markup style. For example, ``/docs/documentarians.rst`` uses `reStructuredText (.rst)`_.

3. Click the pencil icon to edit this file in your fork of the www repo.

4. Make your edits.

5. Click **Commit changes...**.

6. Click **Propose changes**.

7. Click **Create pull request**.

.. _update-guide-in-git:

Updating a guide via a pull request
-------------------------------------

If you've never worked with Git and GitHub, use this section to get started. 

Before you begin
~~~~~~~~~~~~~~~~~

1. `Create a GitHub account`_.
2. `Download and install Git`_.
3. Open a terminal window and follow the instructions to `associate your
   GitHub username with your local Git installation`_.

   1. In macOS: Open the **Terminal** app.
   2. In Windows: From the Start Menu, open **Git Bash**.

4. In the `Write the Docs www project`_, find the file name corresponding to an `existing issue`_ or page you want to improve. 

For example, ``/docs/documentarians.rst`` creates https://www.writethedocs.org/documentarians/. 

5. Review formatting guidelines for the Markup style the file uses. The example file above uses `reStructuredText (.rst)`_.

Create a pull request with your changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**In the GitHub UI:**

1. `Fork the Write the Docs www project`_.

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

**In your terminal window:**

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
.. _reStructuredText (.rst): /guide/writing/reStructuredText/
.. _Create a GitHub account: https://github.com/join
.. _Download and install Git: https://git-scm.com/downloads
.. _associate your GitHub username with your local Git installation: https://help.github.com/en/articles/setting-your-username-in-git
.. _Write the Docs www project: https://github.com/writethedocs/www
.. _Sublime Text: https://www.sublimetext.com
.. _Visual Studio Code: https://code.visualstudio.com/
.. _write a good commit message: https://chris.beams.io/posts/git-commit/
.. _GitHub pull request: https://help.github.com/en/articles/creating-a-pull-request
