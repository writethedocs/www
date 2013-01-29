# -*- coding: utf-8 -*-
"""Tests around project's documentation."""
from contextlib import contextmanager
from os import chdir, getcwd
from os.path import (abspath, dirname, exists, getmtime, isabs, isdir, isfile,
                     join)
from subprocess import Popen, PIPE
import time
from unittest import TestCase


@contextmanager
def cd(path):
    """Change working directory temporarily."""
    former_cwd = getcwd()
    try:
        # Cd to project's root.
        chdir(path)
        yield
    finally:
        chdir(former_cwd)


class SphinxDocumentationBuilder(object):
    """Encapsultates documentation build and stores build result."""
    def __init__(self, project_dir,
                 command=['make', 'documentation'],
                 build_dir=join('var', 'docs', 'html'),
                 build_file='index.html',
                 ):
        """Initialize some attributes."""
        self.project_dir = project_dir
        """Path to project's root dir."""

        if not isabs(build_dir):
            build_dir = join(self.project_dir, str(build_dir))
        self.build_dir = build_dir
        """Path to documentation build directory.

        Must be either relative to :py:attr:`project_dir` or absolute.

        """

        if not isabs(build_file):
            build_file = join(self.build_dir, str(build_file))
        self.build_file = build_file
        """Path to a file that is created during build."""

        self.command = command
        """Command to run documentation build, as a list of arguments."""

        self.exit_code = None
        """Exit code of command run.

        It's an integer, except when command hasn't been run yet (``None``).

        """

        self.stdout = None
        """Standard output (STDOUT) of command run.

        It's a string, except when command hasn't been run yet (``None``).

        """

        self.stderr = None
        """Standard error output (STDERR) of command run.

        It's a string, except when command hasn't been run yet (``None``).

        """

        self.previous_build_time = None
        """Time of previous build, if any.

        Is ``None`` if build hasn't been made already.

        """

    def build(self, force=False):
        """Build the documentation.

        Runs :py:attr:`command` only once, except if ``force``.

        Populates :py:attr:`exit_code`, :py:attr:`stdout` and
        :py:attr:`stderr`.

        .. note::

           ``sphinx-build`` echoes 'making output directory\n' to STDERR. This
           method strips this text from stderr.

        """
        with cd(self.project_dir):
            if not force and self.exit_code is not None:
                return
            # First, if files to be generated already exist, remember their
            # modification time.
            # We need this because we don't build in a temporary directory.
            self.previous_build_time = self.get_build_time()
            # Run build.
            process = Popen(self.command, stdout=PIPE, stderr=PIPE)
            self.exit_code = process.wait()
            self.stdout, self.stderr = process.communicate()
            # sphinx-build echoes 'making output directory\n' to STDERR.
            # Ignore it.
            self.stderr = self.stderr.replace('Making output directory...\n',
                                              '')

    def get_build_time(self):
        """Return time of last build, or None if no build was performed."""
        if exists(self.build_file):
            return time.ctime(getmtime(self.build_file))


class DocumentationBuildTestCase(TestCase):
    """Make sure documentation builds without errors or warnings."""
    @classmethod
    def setUpClass(cls):
        """Class setup: initialize a class-level documentation builder.

        The ``doc_builder`` class attribute makes it possible to share builds,
        i.e. to run documentation build only once and thus speedup tests.

        """
        tests_dir = dirname(abspath(__file__))
        project_dir = dirname(tests_dir)
        cls.doc_builder = SphinxDocumentationBuilder(project_dir)

    def test_exit_code(self):
        """Documentation build exits with code 0."""
        self.doc_builder.build()
        msg = """Command "%s" exited with code %d, expected %d""" % (
            ' '.join(self.doc_builder.command), self.doc_builder.exit_code, 0)
        self.assertEqual(self.doc_builder.exit_code, 0, msg)

    def test_stderr(self):
        """Documentation build doesn't report errors."""
        self.doc_builder.build()
        msg = """Command "%s" reported errors or warnings on STDERR:\n\n%s""" \
              % (' '.join(self.doc_builder.command), self.doc_builder.stderr)
        self.assertEqual(self.doc_builder.stderr, '', msg)

    def test_build_created(self):
        """Documentation build creates and populates build directory."""
        self.doc_builder.build()
        self.assertTrue(isdir(self.doc_builder.build_dir))
        self.assertTrue(isfile(self.doc_builder.build_file))
        if self.doc_builder.previous_build_time is not None:
            latest_build_time = self.doc_builder.get_build_time()
            self.assertGreater(latest_build_time,
                               self.doc_builder.previous_build_time)
