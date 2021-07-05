
.. post:: July 06, 2021
   :tags: newsletter

#####################################
Write the Docs Newsletter – July 2021
#####################################

Good morning, afternoon, or evening, documentarians! It's Beth and the newsletter team with a last summer update before we head off on a little aestival break. We'll be back in September :) 

I don't have any big announcements for you this month, so we'll head straight into the stories from Slack!

-----------------------------------------
What's best for your images - JPG or PNG?
-----------------------------------------

JPG or PNG? Which is the best format to use? Does it even matter which you pick? Well, the Write the Docs community has chimed in to answer your pressing questions, and it seems like PNG is the clear winner. `Portable Network Graphics <https://en.wikipedia.org/wiki/Portable_Network_Graphics>`__, or PNG, offers unmatched clarity for screenshots in online docs and doesn’t degrade when opened and saved like the alternative JPG or JPEG. Compression in PNG is also better since it’s a lossless image format and not a lossy one like JPG, meaning it preserves all of an image’s details. Another advantage of PNG is that it supports transparency, whereas JPG is best for gradient images.

Curious to know if there’s something better than PNG? There is, and it’s called `WebP <https://developers.google.com/speed/webp>`__, a format that works for both lossy and lossless compression. If you have a tool that exports to WebP, use it instead of PNG or JPG for enhanced web images. Otherwise, stick with PNG for clear, detailed, high-contrast images.

For more help choosing the right format, check out `this article by Allison Boatman <https://www.techsmith.com/blog/jpg-vs-png/>`__ or `this one by Shane Melaugh <https://thrivethemes.com/jpeg-vs-png/>`__.

-------------------------------------
Designing a tech writer career ladder
-------------------------------------

What does a technical writing career ladder look like? This month while discussing how to set one up, we saw a few examples - `GitLab's technical writer ladder <https://about.gitlab.com/job-families/engineering/technical-writer/>`__, and `career-ladders.dev/docs <https://career-ladders.dev/docs>`__. Some community members saw value in aligning title levels across functions. So a standard progression applied to tech writing could look something like this:

* Associate Technical Writer / Technical Writer I
* Technical Writer / Technical Writer II
* Senior Technical Writer / Team Lead
* Staff Technical Writer / Manager
* Principal Technical Writer / Director
* Distinguished Technical Writer (?!)

Many felt including "Distinguished" was a bit unusual. It's nice to have it there to have something to shoot for - to show what a tech writing role can look like at that level. But it's okay for a company just not to be able to support someone at that level, when Distinguished usually means people who have an ecosystem-wide or industry-wide impact.

Even the other high levels can be challenging to reach, especially as an individual contributor. Many companies need managers  much more than high-level ICs, or simply don't have scope to do work at such a high level. But there was general agreement on the importance of having clear standards for what each level means. It can be really frustrating if someone wants to get promoted but the ground keeps shifting.

How long should it take to reach the "senior" level? Surprise surprise, there's no clear answer. We see 5 years mentioned a lot in job adverts, but some folks said it took as little as 2 with the right domain knowledge. Of course, seniority shouldn't purely about the number of years you've been in the role - most felt it was more to do with your skill level, and the breadth and level of responsiblity you take on. Take these titles with a pinch of salt, though, because what they mean can vary wildly between different companies. For on what it means to be senior, see `Distinguishing between junior vs senior tech writers </blog/newsletter-june-2018/#junior-vs-senior-technical-writers>`__ from the June 2018 newsletter.

-------------------
Doc history and Git
-------------------

When you're creating a new version of docs for a release, how important is it to keep the docs for old releases? The simple answer is to keep all history, just in case - you never know when you'll need it. But some docs are so outdated that the original writeup is incredibly unlikely to be relevant.

How to keep the history depends on how you want to use it. If you're using Git and you just want to be able to check the history, you can see it with `git log`. Though it can take some archaelogical work to follow the trail when files get moved.

But what if you want to publish those old docs? One option is to copz your old files alongside your new ones. It's possible to copy the files while retaining their history, but `it takes some effort <https://devblogs.microsoft.com/oldnewthing/20190919-00/?p=102904>`__. However, be aware that Git doesn't track files exactly. It tracks some content (blobs—sequences of bytes), and trees of file names that point to blobs, but it doesn't actually track those things together, which is why that blog post has to use merges to copy the history. It's fighting the way Git wants to work. It might be simpler to copy the file with a commit message saying where it was copied from, to help someone track down the history if they need to.

If you can publish from something other than HEAD, you can do something much simpler: just use Git's tagging system to mark the commit for an old release, and then publish from that tag. Some teams use different branches for different releases, which would make this even more straightforward.

-------------------------------
What we’re reading and learning
-------------------------------

The #bipoc group’s been discussing the following materials on diversity, inclusion, and equity. Want to join the conversation? Please join us in the `#bipoc Slack channel <https://app.slack.com/client/T0299N2DL/C016STMEWJD>`__!

A short read: `This article <https://www.axios.com/linkedin-erg-pay-affinity-groups-17b9a060-0ef3-4226-aae2-a3dbe56908f9.html>`__ on Axios talks about LinkedIn starting to pay ERG leaders, usually a volunteer position, for their work.

A medium read: `this Great Place To Work article <https://www.greatplacetowork.com/resources/blog/9-proven-strategies-to-improve-diversity-equity-inclusion-at-your-workplace>`__ highlights strategies to improve inclusion and equity in the workplace.

For a much more in-depth exploration (several weeks), Coursera now has two free courses on Anti-Racism offered by the University of Colorado, Boulder: `one <https://www.coursera.org/learn/antiracism-1>`__ and `two <https://www.coursera.org/learn/antiracism-2>`__.

----------------
From our sponsor
----------------

This month’s newsletter is sponsored by ClickHelp:

.. raw:: html

    <hr>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="width:100%; max-width: 600px;">
      <tbody>
        <tr>
          <td width="75%">
              <p>
              ClickHelp, a modern cloud technical writing platform, announces the Rainbow update! Now you can write and review technical content, manage translations, and publish the result in one integrated solution. Create multi-language documentation sites easier!
              </p>
              <p>
              Read more: <a href="https://clickhelp.com/clickhelp-technical-writing-blog/clickhelp-june-2021-rainbow-update-overview/?utm_source=write-the-docs&utm_medium=text-link&utm_campaign=write-the-docs-newsletter">ClickHelp Rainbow Overview</a>
              </p>
          </td>
          <td width="25%">
            <a href="https://clickhelp.com/clickhelp-technical-writing-blog/clickhelp-june-2021-rainbow-update-overview/?utm_source=write-the-docs&utm_medium=banner-link&utm_campaign=write-the-docs-newsletter">
              <img style="margin-left: 15px;" alt="ClickHelp" src="/_static/img/sponsors/clickhelp.jpg">
            </a>
          </td>
        </tr>
      </tbody>
    </table>
    <hr>

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

------------------
Featured job posts
------------------

- ` Senior Technical Writer <https://jobs.writethedocs.org/job/409/senior-technical-writer-engineering/>`__, Squarespace (New York, NY)
- `Technical Writer <https://jobs.writethedocs.org/job/413/technical-writer-remote-usa/>`__, Socure (Remote - US)
- `Technical Writer (Chinese Traditional) <https://jobs.writethedocs.org/job/415/technical-writer-chinese-traditional-taipei-remote-possible/>`__, Gandi Asia Co. Ltd (Taipei / remote possible)
- `Senior Technical Writer <https://jobs.writethedocs.org/job/416/senior-technical-writer/>`__, Appian (Remote)
- `Developer Documentation Lead <https://jobs.writethedocs.org/job/421/developer-documentation-lead/>`__, Chainlink Labs (Remote)
- `Senior Technical Writer for Developer Documentation <https://jobs.writethedocs.org/job/424/senior-technical-writer-for-developer-documentation/>`__, Avalara (Brighton, UK)

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

------------------------
Virtual events coming up
------------------------

- 06 July, 8:30 EDT (Florida, US) - `Morning social <https://www.meetup.com/write-the-docs-florida/events/qpvdfsycckbjb/>`__
- 13 July, 19:00 MDT (Calgary, Canada) - `Write the Docs Calgary Meetup <https://www.meetup.com/wtd-calgary/events/279034139/>`__
- 14 July, 12:00 CDT (Texas, US) - `Virtual lunch social <https://www.meetup.com/WriteTheDocs-ATX-Meetup/events/279149149/>`__
- 15 July, 12:00 EDT (Florida, US) - `GitLab for technical writers <https://www.meetup.com/write-the-docs-florida/events/278548840/>`__
- 15 July, 18:00 EDT (Indianapolis, US) - `Summer Meet and Greet <https://www.meetup.com/Write-the-Docs-Indy/events/278756631/>`__
- 20 July, 8:30 EDT (Florida, US) - `Morning social <https://www.meetup.com/write-the-docs-florida/events/qpvdfsycckbbc/>`__
