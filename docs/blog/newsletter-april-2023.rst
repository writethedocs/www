.. post:: April 07, 2023
   :tags: newsletter

######################################
Write the Docs Newsletter – April 2023
######################################

Hello again. April may or may not be the cruelest month, but there's no cruelty in our latest batch of news and views from the world of docs.

In conference news, the Portland conference has `announced its full schedule <https://www.writethedocs.org/conf/portland/2023/news/announcing-schedule/>`__. So check out the exciting talks you can see in person.

If in-person talks aren't your thing or Portland is a little too far away from you, the Atlantic conference is new this year. It's an online conference timed to be as convenient as possible for both Europe and the eastern parts of the Americas. If you have ideas you'd like to share, the `Call for Proposals <https://www.writethedocs.org/conf/atlantic/2023/cfp/>`__ is open until May 15. Check out the call to see some guidance on how to put together a good proposal and share your ideas with other documentarians.

In addition to our conferences, our community provides other learning resources through the website. A recent addition is a guide on `maintaining a portfolio <https://www.writethedocs.org/hiring-guide/portfolios/>`__. If you have other ideas to capture, fork the `website repository <https://github.com/writethedocs/www>`__ and open a pull request.

We've also captured some highlights of recent discussions right here. Let us know if you see something else we should include.

-------------------------
Building an API Portfolio
-------------------------

If you're new to API documentation but keen to learn more and demonstrate your skills, brace yourself: this month, the community delivered an idea-packed discussion about developing an API portfolio as you learn. 

One approach is to create a fake API and document it. You don't need to code -- for example, you can create an `OpenAPI <https://www.openapis.org/>`__ API design specification using `YAML <https://www.redhat.com/en/topics/automation/what-is-yaml>`__ and write the documentation in `Markdown <https://www.markdownguide.org/>`_. Here are a few things to keep in mind to help you succeed:

- Keep your API simple. You might be tempted to prove your skills, but documenting an elaborate API is overwhelming when you're still learning.
- Make sure your use case is clear. It's easier to document an API if its purpose and context makes sense.
- Use a familiar tool that you're comfortable with (even a traditional word processor) and aim for minimum viable documentation. You can migrate to new formats and tools later.
- Try to have some fun. For example, your API could be for an ice cream shop. `Swagger's API demo <https://petstore3.swagger.io/>`__ is for a pet store.
- Find someone to review your work and iterate based on their feedback.

Resources that can help with the fake API approach include `The Design of Web APIs <https://www.manning.com/books/the-design-of-web-apis>`__ by Arnaud Lauret and Tom Johnson's `free course on documenting APIs <https://idratherbewriting.com/learnapidoc/>`_.

A second approach is contributing to an open-source project with an API that has poor or nonexistent documentation. Here are some tips for this path:

- To find a project, think about a topic that interests you and then search for that topic along with "Open Source" and "API".
- Look for projects that are actively maintained to ensure someone reviews your contributions in a timely manner. It's not always obvious whether a project is active, so make your first contribution something quick like a typo fix to see how the maintainers respond. If your contribution isn't reviewed within a couple days or seems unwelcome, keep searching for another project.
- If possible, work with design-first projects that test the API code against the API design. If the API is code-first, there's a risk that each build will overwrite your work.
- If your contributions are ignored or rejected, try not to take it personally. You're likely to have many of the same challenges you'd have for any other docs work, including maintainers who may be unresponsive or too busy to help you get started.
- Consider `Google Season of Docs <https://developers.google.com/season-of-docs>`_, which connects interested writers with open-source projects that need documentation support.

------------------------------------
Measuring productivity of docs teams
------------------------------------

If your management is looking for measures of documentation productivity, what’s the best way to meet that need?

It’s a tricky problem because many metrics are obvious but unhelpful. Counting team commits is perilously close to bad measures like counting lines of code. Counting words added is almost the opposite of what you want! The number of initiatives launched also doesn’t tell you about their quality.

A bad metric can lead you down the wrong path. Consider Goodhart’s law: “As soon as a measure becomes a target, it ceases to be a good measure.”

One place to start is what you want to achieve, and then work backwards to a metric. If productivity means *velocity* to your team: perhaps tickets closed. If it's *solving problems* for your audience: possibly content satisfaction. For providing a *good service* to other teams: maybe backlog size growth. But be careful with what you’re aiming for. For example, a slow turnaround time can be good if it means well-thought out improvements to your users’ lives.

It’s worth digging into what management is really looking for. Authoring is not like manufacturing: the visible output (topics published, page views) isn't well correlated with effort. A better angle is impact on the business – such as the diagram at the end of this `article on the value of documentation <https://document360.com/blog/value-of-documentation/>`__. Depending on what your users say, your goal might be increasing time spent on the docs website or reducing support tickets.

Whatever you do, you should think it through. “What gets measured gets done”: if you measure quantity not quality, your docs will suffer.

------------------
Setting boundaries
------------------

As a documentarian, it’s common to seek feedback on your work from others, especially people who aren't exclusively focused on documentation. It’s important to remember that not everyone has the same level of expertise or understanding of the writing process. This can lead to reviewers overstepping boundaries or providing feedback that may not be helpful or relevant.

To set clear working boundaries, it’s best to share documentation standards, which can be rooted in technical writing principles such as task-based writing, minimalism, and structured content. Suppose you receive pushback after sharing the standards. For example, what if reviewers ask about what they were derived from? In that case, you could offer sources on the validity of the standards.

An `article by Dave Gash on information typing <https://medium.com/@davidagash/a-painless-introduction-to-information-typing-d06041013fd5>`__ might be a good place to start if you find yourself having to “show your work” in terms of standard technical writing practices. In the article, Gash clearly explains the importance of content structuring while providing examples to make things easily understandable to non-experts.

Setting boundaries with reviewers can be challenging, but it’s crucial to the writing process. By implementing these tips, you can communicate your expectations clearly, establish respectful boundaries, and ensure that the feedback you receive is helpful and constructive. Remember, you are the expert on your own writing and it’s okay to prioritize your own creative vision and process. By setting boundaries, you can work with your reviewers more effectively and ultimately create stronger, more compelling writing that stays true to your unique voice and vision.

-----------------------
Complexity of languages
-----------------------

Last month, an interesting discussion started from a somewhat innocuous posting: Is 'a unique' or 'an unique' correct?

From the English 'rule' about the 'sound' of a letter (such as u) determining whether to use 'a' or 'an', the discussion moved into the 'correct' order of a series of adjectives. Apparently, English learners know this as the Royal Order, but native speakers often don't even realize that there's a rule... they just put adjectives in the 'correct' order.

This lead to a discussion about the perception that many US English speakers are monolingual. Some posters discussed wanting to learn other languages; some mentioned other languages that they've learned... including the challenges of learning a second (or third) language. The consensus was that some rules get formalized when learning another language that native speakers know unconsciously. One person recommended watching `Loïc Suberville videos on YouTube <https://www.youtube.com/channel/UCywGsTdh_qqZUYmA2Gro2CA>`__. (His channel description: That French guy who doesn't understand French.)

Others mentioned that one challenge to learning English was the many loan words from other languages (leading to seemingly unexpected pronunciation and spelling issues), but others mentioned that all languages have loan words (with  English 'invading' many languages). Then some touched on the evolution of languages with loan words becoming standard vocabulary (such as Japanese using Chinese characters and pronunciation). Others mentioned that languages develop different dialects (such as Yiddish), which may be challenging for people who speak the same language but use a different dialect. This brought culture and history into the discussion as being inseparable from language.

The thread ended up reflecting on inconsistencies in other languages and how the ease of learning another language may depend the new language's relationship to your native language.

----------------
Events coming up
----------------

- 11 April, 08:30 EST (New England and Florida, USA) - `Focused conversation for documentarians <https://www.meetup.com/ne-write-the-docs/events/mvctctyfcgbpb/>`__
- 18 April, 17:30 AEST (Sydney, Australia) - `Navigating the future of tech writing | Lightning talks <https://www.meetup.com/write-the-docs-australia/events/291787201/>`__
- 25 April, 08:30 EST (New England and Florida, USA) - `Focused conversation for documentarians <https://www.meetup.com/ne-write-the-docs/events/mvctctyfcgbhc/>`__
- 25 April, 19:00 MDT (Calgary, Canada) - `Write the Docs Calgary Meetup <https://www.meetup.com/wtd-calgary/events/292346914/>`__
- 28 April, 12:00 MDT (Boulder/Denver, USA) - `Fourth Friday Write the Docs Co-working Social <https://www.meetup.com/write-the-docs-boulder-denver/events/xkrnctyfcgblc/>`__
- 4 May, 18:00 CEST (Stockholm, Sweden) - `Stockholm WTD meetup #7 <https://www.meetup.com/write-the-docs-stockholm/events/292409546/>`__
