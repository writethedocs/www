Salary Surveys
===============

We run these annually, and publish annonimised results but not the full data.

Convert from Google Doc to ReStructuredText
-------------------------------------------

1. In Google Docs, save the survey as HTML.
2. Use `pandoc <https://pandoc.org/>`__ to convert to RST::

      pandoc -s -f html -t rst SalarySurvey2020.html > survey.rst

3. If the output is full of `rubrics` and single-cell tables like this: ::

      +-------------------------------------------------------------+
      | .. rubric:: What we asked                                   |
      |    :name: h.p5d0g4ykb8x1                                    |
      |    :class: c15                                              |
      |                                                             |
      | 1. What is the basis of your employment?                    |
      |                                                             |
      | -  I am an employee                                         |
      | -  I am an independent contractor, freelance operator, or   |
      |    self-employed                                            |
      | -  I was an employee, but am not currently employed         |
      | -  I was an independent contractor, freelance operator, or  |
      |    self-employed, but do not currently have work            |
      +-------------------------------------------------------------+

   use something like the script in `docs/_scripts/fix_gdocs2rst.py` to clean it up.

   (and possibly do a search and replace to add the `rubric` back to the 2020 doc and a few other tweaks)

4. Add images to `docs/surveys/salary-survey/images`, and include them manually.

5. Add custom CSS to `_static/css/survey.css`.

6. Triple check output. 😈