---
banner: _static/conf/images/photos/audience-closeup-berlin-55528225883.jpg
---

# Salary surveys

In 2019, we launched the first Write the Docs salary survey, to gather data about pay scales and benefits in our industry. The original goal was to help our community members better understand what an appropriate salary is and provide a basis for future negotiations. 

Overwhelmed by the positive response, we expanded the survey to collect information about remote work, attitudes towards pay transparency, and satisfaction about salaries, benefits and overall job situations. Based on community feedback, we've continued to refine the questions each year - especially for independent contractors, freelancers and the self-employed. 

{% if salary_survey.open %}
## Take the {{ salary_survey.year }} salary survey

The {{ salary_survey.year }} survey is open until {{ salary_survey.closes }}. The more people who answer, the more useful the results are for everyone.

<div class="cta-group">
  <a class="cta-button" href="{{ salary_survey.url }}">Take the {{ salary_survey.year }} survey</a>
</div>

{% endif %}
## Results

```{toctree}
:maxdepth: 1

salary-survey/2025
salary-survey/2024
salary-survey/2023
salary-survey/2022
salary-survey/2021
salary-survey/2020
salary-survey/2019
```
