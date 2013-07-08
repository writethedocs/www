#########################
Feedback over conventions
#########################

**Associate feedback to conventions**.
And even better, whenever you can, replace conventions by feedback.


**********************
Example: code coverage
**********************

Let's start with a story about code coverage...

The team we work in states about code coverage in documentation:

  Developers make sure that their tests cover most code.

**Good motivation: we have a convention.**

But that is not enough. When a developer checks code coverage, how can he tell
whether the result is good or bad?

Let's setup a recipe to get feedback about the convention:

  Run ``make coverage``.
  As a result, you get global code coverage ratio.
  If this ratio is greater than 80%, it's good, else it's bad.

**It's getting better: we can get feedback on demand.**

Still, it is not enough. It belongs to each developer to respect the
convention, i.e. developers can ignore it. With time, developers may forget
it. New developers won't see it... Soon, the convention becomes unused, and the
documentation becomes obsolete. How can we make the convention restrictive?

Let's plug some code coverage tool in our continuous integration service. So
that we automatically get feedback:

* we receive a notification (or see a big red light) when the rule is broken
  (code coverage is less than 80%).
* we can do basic accountancy, using coverage history: does it increase or
  decrease? When did it break? Which commits broke the rule?

**Great! Everybody automatically gets feedback.**

Now the whole team owns the convention: if one fails, the team has to perform
something or get a big noisy red alert. So, the convention is visible, it is
concrete, obvious. Nobody can ignore it. 

Then, we can safely remove the convention from the documentation. The team no
longer needs to maintain the convention in documentation: it's live! The
convention will be maintained (and self-documented) as scripts and
configuration applied to continuous integration service.

Let's compare it to `the fable of the chicken and the pig`_:

* by writing down conventions, you get involved.
* by replacing conventions by feedback, you get committed.


****************
Classic patterns
****************

Here is a list of frequently encountered use cases, where you can get feedback
instead of writing down conventions:

* "No test, no commit".
  Use commit hooks or a continuous integration service to get feedback when
  tests get broken.

* Coding standards.
  Plug a "coding standards reviewer" into a continuous integration service.

  As an example, for Python code, make your build fail if `flake8`_ reports
  errors.

* "No TODO in PROD". Write a test or a commit hook that fail if "TODO" string
  is found in code.

* "No debug in PROD". Write a test or a commit hook... where "debug"
  definition depends on your language.
  
  As an example, for Python, check for "pdb" and "print".


**********
References
**********

.. target-notes::

.. _`the fable of the chicken and the pig`:
   https://en.wikipedia.org/wiki/The_Chicken_and_the_Pig
.. _`flake8`: http://pypi.python.org/pypi/flake8/
