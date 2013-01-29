# -*- coding: utf-8 -*-
"""Tests around project's documentation."""
from os import chdir, getcwd
from os.path import abspath, dirname, exists, getmtime, isdir, isfile, join
from subprocess import Popen, PIPE
import time
from unittest import TestCase


class DocumentationBuildTestCase(TestCase):
    """Make sure documentation builds without errors or warnings."""
    def __init__(self, *args, **kwargs):
        """Initialize some attributes."""
        super(DocumentationBuildTestCase, self).__init__(*args, **kwargs)

        self.former_cwd = None
        """Remember current working directory before tests are run."""

        tests_dir = dirname(abspath(__file__))
        self.project_dir = dirname(tests_dir)
        """Path to project's root dir."""

        self.build_dir = join(self.project_dir, 'var', 'docs', 'html')
        """Path to documentation build directory."""

        self.build_file = join(self.build_dir, 'index.html')
        """Path to a file that is created during build."""

        self.command = ['make', 'documentation']
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

    def setUp(self):
        """Setup."""
        super(DocumentationBuildTestCase, self).setUp()
        # Remember current working directory before tests are run.
        self.former_cwd = getcwd()
        # Cd to project's root.
        chdir(self.project_dir)

    def tearDown(self):
        """Teardown."""
        super(DocumentationBuildTestCase, self).tearDown()
        # Restore working directory.
        chdir(self.former_cwd)

    def build_documentation(self, force=False):
        """Run ``make documentation``.

        Runs :py:attr:`command` only once, except if ``force``.

        Populates :py:attr:`exit_code`, :py:attr:`stdout` and
        :py:attr:`stderr`.

        .. note::

           ``sphinx-build`` echoes 'making output directory\n' to STDERR. This
           method strips this text from stderr.

        """
        if not force and self.exit_code is not None:
            return
        # First, if files to be generated already exist, remember their
        # modification time.
        # We need this because we don't build in a temporary directory.
        if exists(self.build_file):
            self.previous_build_time = time.ctime(getmtime(self.build_file))
        # Run build.
        process = Popen(self.command, stdout=PIPE, stderr=PIPE)
        self.exit_code = process.wait()
        self.stdout, self.stderr = process.communicate()
        # sphinx-build echoes 'making output directory\n' to STDERR. Ignore it.
        self.stderr = self.stderr.replace('Making output directory...\n', '')

    def test_exit_code(self):
        """Documentation build exits with code 0."""
        self.build_documentation()
        msg = """Command "%s" exited with code %d, expected %d""" % (
            ' '.join(self.command), self.exit_code, 0)
        self.assertEqual(self.exit_code, 0, msg)

    def test_stderr(self):
        """Documentation build doesn't report errors (on STDERR)."""
        self.build_documentation()
        msg = """Command "%s" reported errors or warnings on STDERR:\n%s""" % (
            ' '.join(self.command), self.stderr)
        self.assertEqual(self.stderr, '', msg)

    def test_build_created(self):
        """Documentation build creates and populates build directory."""
        self.build_documentation()
        self.assertTrue(isdir(self.build_dir))
        self.assertTrue(isfile(self.build_file))
        if self.previous_build_time is not None:
            latest_build_time = time.ctime(getmtime(self.build_file))
            self.assertTrue(latest_build_time > self.previous_build_time)
