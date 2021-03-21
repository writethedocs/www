Community spotlight interviewing guide
======================================

Community spotlight goals
-------------------------

The primary goal of the community spotlight is to provide a resource for new technical writers to gain insight into the careers of established tech writers and use that to inform the choices in starting and shaping their own career.

Intended audience
~~~~~~~~~~~~~~~~~

The interview content in the Community Spotlight is designed to be a resource for novice tech writers or non-tech writers that are considering becoming technical writers.

Content and structure
~~~~~~~~~~~~~~~~~~~~~

Each interview follows a standard content structure. Each writeup begins with a small 1 or 2 sentence summary that introduces the interview subject. That then leads into key takeaways. Key takeaways should present 2-3 of the most useful pieces of information from the interview. The body of the write up is laid out in thirds.

* The first third outlines and summarizes the overall career path for the interviewee. 
* The second third elaborates some of the unique experiences touched on in the career summary. 
* The final third offers advice from the interviewee to the reading audience.

The last component of the write up gives the Slack username of the interview subject along with a couple of the WTD Slack channels that they like to browse. This gives the reader the opportunity to interact with the community further and follow up on any information that particularly resonated.

*The final write up should be between 800-1,400 words total.*

Interview setup
~~~~~~~~~~~~~~~

Interviews can be conducted through whatever medium is most convenient for both parties, but the most success has been found so far by speaking in real time via voice. Slack is most commonly used by the WTD community to communicate, and is a convenient option.

Interviews should take roughly 20-40 minutes to complete:

* The first 10-15 minutes should be used to cover the career story of the interview subject.
* The next 10-20 should be used to elaborate on the unique aspects that you the interview deem relevant to the audience. 
* The last 5-7 minutes should be used to ask the interview what advice they would give to an aspiring tech writer.

Recording the interview can be done with whatever tools the interview feels most comfortable using. If the interview is done through VoIP on a computer, Audacity is a good tool for recording audio. Instructions on recording computer audio with Audacity can be found in the `Audacity manual`_.

Asking questions
~~~~~~~~~~~~~~~~

The two staple questions of each interview are a variation of "What has been the story of your technical writing career so far?" and "What advice would you give to aspiring technical writers looking to break into the field?" These questions act as bookends to introduce the reader to the experience of the interview and then leave the reader with some practical advice to take with them. Every other question asked is up to the interviewer's discretion, and forming these questions often come as a response to the career story given by the interviewee.

A general tip for crafting these questions on the fly is to ask the interviewee what their experience was like during a period in their life that you as the interviewer would like for insight. For example, you may ask, "What was your like working as a freelance writer? " or "What was your experience like transitioning from hardware documentation to software." From there, you can dive into topics that you think provide the most educational value for the intended audience.

A resource for generalized questions can be found in the `general questions resource`_.

Converting the interview into text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the interview, the interview should be left with a 20-40 minute audio recording and some written notes about the conversation. Assuming the audio recording is of sufficient quality, automated transcription tools can be used to convert the audio into text. Currently, Amazon's AWS transcription is the best tool available, and step by step instructions to use that tool can be found in the `AWS Getting Started resource`_. Once transcribed, you will have a roughly 3,000-8,000 word document to edit and revise. 

Editing the transcript into the first draft
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each interview should contain the career summary of the interview subject along with the advice they would give to new writers. Those answers together will total roughly 400-700 words and will generally be about half of the first draft. The content of the other half of the document is up to the interviewers discretion.

When considering what to include in the other half, the interviewer should consider the audience and what aspects of the interviewee's experience provides the most utility for an inexperienced tech writer. For example, a conversation about document design may be interesting, but a conversation about working as a freelance writer would be more relevant, and more broadly relevant to the intended audience. Preference should also be given to topics that haven't been thoroughly covered by other write ups.

Preparing the draft for a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before committing the draft publicly and submitting the pull request to the WTD repo, the draft should be sent its respective interviewee so that they may clarify answers or remove any personal information. Once the interviewee has accepted the draft as being appropriate for publishing, the document can be committed publicly to your own personal fork of the main WTD website repo. Each interview should go in it's own branch.

Formatting and other extra considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every interview is written in RST. For an example of what the RST formatting should look like, you can reference `this example`_ or any of the other documents in the community-spotlight directory of the repository.

Companies and well known technologies or tools should link out to relevant web pages. Company links should redirect to their careers page, if available. Technology and tools links should redirect to the standard resource for learning that technology or the WTD page if it exists.

General questions resource
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Education**

* What formal education do you have?
       * Would you consider pursuing more formal education?

* Where have you learned the skills that you use for your work?

**Work**
    
* What is the story of your career so far?

* What other jobs have you had?
    * How has that experience influenced your work now?    
    * How long did it take between learning you wanted to become a tech writer and getting that first job?

* Do you see yourself remaining in this field long-term?

**Job specific**

* What is your title?
    
* How long have you worked as a tech writer?

* What are your responsibilities?
    * Have they changed since you first started?

* How much creative control do you have when creating documentation?
    * Do you have the freedom to experiment with processes?
        * Is this typical in the domain you work in?

* How collaborative is your work?
    * Do you work with other writers?

* What tools and techniques do you regularly use?
    * Did you learn these before or after starting?
    
* Is the nature of your work consistent or do you find yourself considering new challenges regularly?

**Advice**

* What should an aspiring tech writer be able to do before searching for a job?

* How does the reality of your job differ from the expectations you had before becoming a tech writer?

* What motivated you to pursue tech writing rather than a related field?(advertising, journalism, STEM)

Conference speaker interview recommendations
--------------------------------------------

Goals recommendation
~~~~~~~~~~~~~~~~~~~~

The goal of the speaker interviews is to allow the speakers to introduce themselves and their backgrounds and also talk about the motivations behind their presentations. These interviews can act as a way of introducing a presentation topic and that topic's relevance to generate more interest for the talk.

Intended audience
~~~~~~~~~~~~~~~~~

The most logical intended audience for this content would be conference attendees. But in some cases these presentations receive a long life after the conference as recordings or presentation files on the internet. With this in mind, accessibility in both distribution and content style should be considered so that people other than technical writing professionals can benefit.

Conducting the interviews and potential formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Speaker interviews should follow a fairly consistent structure to allow for easy collection and distribution:

* One potential solution is to create a google form or a similar survey tool that can be sent to speakers or included as part of proposal guidelines. The text aggregated by the form could than organized and distributed using an automated script. 
* Another potential solution that would allow for more unique content would be to follow the community spotlight model and have a person contact speakers personally arrange the content and distribution

There are numerous content structure types that could be applicable to this project, and some may be more appropriate than others with respect to the methods used to collect information and the conferences themselves:

* One basic structure would be to create a  2 part writeup based on the project goals. The first part would introduce the speaker and their qualifications. The second part would outline the motivations for producing the presentation the value it provides.
* Another basic structure could be to introduce the speaker and motivations as short introductions, and use the judgement of another person to ask relevant questions that may come in an audience Q&A

Miscellaneous recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Completing this project and creating a well defined process for producing this content could be a good fit for another Write the Docs intern.

It may be a good idea to test formats on previous conference presentations before applying the project to an upcoming conference.

.. _audacity manual: https://manual.audacityteam.org/man/tutorial_recording_audio_playing_on_the_computer.html

.. _AWS Getting Started resource: https://aws.amazon.com/getting-started/tutorials/create-audio-transcript-transcribe/

.. _this example: https://raw.githubusercontent.com/writethedocs/www/master/docs/hiring-guide/community-spotlight/interview-ravind-kumar.rst
