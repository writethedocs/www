Contribute to the Write the Docs Website
========================================

Welcome! The Write the Docs website covers many areas of software documentation
and has been put together by various members of the community. 
If you find something that seems like it could be improved,
see how to contribute to making it better.

If you're interested in contributing to the code behind the website, see the `README for the repo <https://github.com/writethedocs/www/blob/main/README.md>`__.

.. contents::
    :local:
    :depth: 3

How to contribute
-----------------

Anyone can contribute regardless of professional or tool experience.
There are several ways to contribute:

* :ref:`Edit a single page in the GitHub UI <update-page-in-github>`.
* :ref:`Edit files using Git <edit-in-git>`.
* To suggest larger changes or new content or note bugs in existing content `submit an issue`_.

What to contribute
------------------

Feel free to suggest any small improvements that you can find.
If it just changes a few words, it's easier to see the proposed changes as a direct suggestion.

If you want to make larger changes, first `submit an issue`_.
This opens a space to discuss the change before anyone invests too much time into it.

What to consider when contributing
----------------------------------

When contributing to the website, keep these guidelines in mind:

- Review the `website style guide </style-guide/>`__.
- For file format, see the guides for `reStructuredText (.rst)`_ and `Markdown`_.
- For changes to the software documentation guide, see the `guide contributing guidelines </guide/contributing/>`__

.. _update-page-in-github:

Edit a single page in the GitHub UI
-----------------------------------

If you have a `GitHub account`_, you can edit pages directly in the GitHub UI.
To do so, follow these steps:

1. In the `Write the Docs www repository`_, find the file for the content you want to improve, usually in the ``docs`` directory. 

   For example, https://www.writethedocs.org/documentarians/ comes from the file `/docs/documentarians.rst <https://github.com/writethedocs/www/blob/main/docs/documentarians.rst>`__. 
2. Review formatting guidelines for the file's markup.
   For example, ``/docs/documentarians.rst`` uses `reStructuredText (.rst)`_.
   Other pages use `Markdown`_.
3. Click **✏️ Fork this repository and edit the file**.
4. Make your edits.
5. Click **Commit changes...**.
6. Give your changes a short, meaningful message to explain them.
7. Click **Propose changes**.
8. Enter a title for your changes (can be the same as the message in Step 6) and optionally a description for any more context about why you are proposing the change.
9. Click **Create pull request**.

You can now see your proposed changes in the `list of pull requests <https://github.com/writethedocs/www/pulls>`__.
The pull request automatically gets a preview build so you can see your proposed changes in context.

.. _edit-in-git:

Edit files using Git
--------------------

This section goes through all the steps you need to edit one or more files for the website using Git.
You don't need previous experience using Git to follow these steps.

To edit files using Git, you need:

- A `GitHub account`_
- `Git installed on your computer <https://git-scm.com/downloads>`__
- `Your GitHub email set also in Git <https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address>`__

To suggest changes to the Write the Docs website, follow these steps:

1. In GitHub, `fork the Write the Docs www project <https://github.com/writethedocs/www/fork>`__
2. Click **Code**.
3. Copy the URL to clone the repository.
4. Open a terminal.

   - In macOS: open the **Terminal** app.
   - In Windows: from the Start Menu, open **Git Bash**.

5. Open the directory where you want to store the files.
6. Run the following command (replace ``GIT_URL`` with the URL from Step 3)::

     git clone GIT_URL

   This copies the files into a new ``www`` directory.
7. Go to the ``www`` directory (run ``cd www``).
8. Create a new branch (a place to store your proposed changes)::

     git checkout -b BRANCH_NAME

   Replace ``BRANCH_NAME`` with a brief description of your proposed changes with hyphens instead of spaces
   (for example, ``git checkout -b fix-important-typo``).
9. Find the files for the content you want to improve, usually in the ``docs`` directory. 

   For example, https://www.writethedocs.org/documentarians/ comes from the file ``docs/documentarians.rst``. 
10. Review formatting guidelines for the file's markup.
    For example, ``docs/documentarians.rst`` uses `reStructuredText (.rst)`_.
    Some other pages use `Markdown`_.
11. Make your edits and save the files.
12. In your terminal, check what files have been changed by running ``git status``.
13. If the list looks correct, make the files as ready by running ``git add -A``.
14. Save the changes by running ``git commit -m "MESSAGE"``.
    Replace ``MESSAGE`` with a short, meaningful message to explain the changes,
    for example ``git commit -m "Fixed an important typo"``
15. Push the changes to your GitHub fork by running this command::

      git push --set-upstream origin BRANCH_NAME

    Replace ``BRANCH_NAME`` with the name from Step 8.
16. In GitHub, open your fork and `create a pull request against the Write the Docs repository <https://help.github.com/en/articles/creating-a-pull-request>`__.
    The title can be the same as the message in Step 14
    and the description can optionally include any necessary context for the change.

Get help
--------

If you have questions or need assistance in contributing,
ask in the `#wtd-website channel in Slack <https://writethedocs.slack.com/archives/C09E84GAW>`__.

.. _GitHub account: https://github.com/join
.. _Markdown: /guide/writing/markdown/
.. _reStructuredText (.rst): /guide/writing/reStructuredText/
.. _submit an issue: https://github.com/writethedocs/www/issues/new
.. _Write the Docs www repository: https://github.com/writethedocs/www
