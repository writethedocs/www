:template: 2017/au-index.html

.. raw:: html

      <div class="container">
        <div class="row">
          <div class="col-xs-12">

            <div class="main-container main-container--home">

              <section class="buy-ticket">
                <div class="row">
                  <div class="col-xs-12 col-md-5 text-center">
                    <p class="buy-ticket__p buy-ticket__p--first">
                      Melbourne, Australia
                      <span>|</span>
                      November 24, 2017
                    </p>
                  </div>
                  <div class="col-xs-12 col-md-7 text-xs-center text-md-right">
                    <div class="buy-ticket__2nd-col">
                      <a href="#news" class="btn btn-primary button button--narrow buy-ticket__talk">What's new?</a>
                      <p class="buy-ticket__p">|</p>
                      <a href="https://ti.to/writethedocs/write-the-docs-day-australia-2017" class="btn btn-primary button button--narrow buy-ticket__ticket">Buy a ticket!</a>
                    </div>
                  </div>
                </div>
              </section>

              <!-- Schedule -->
              <section class="section">
                <div class="row">
                  <div class="col-xs-12">
                    <div class="section__header subheader">
                      <span class="subheader__yellow"></span>
                      <h2 class="subheader__header">Schedule Overview</h2>
                      <a href="/conf/au/2017/schedule/" class="subheader__more">See full schedule</a>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="schedule-home">
                    <div class="schedule-home__line"></div>
                    <div class="col-xs-12 col-sm-4 text-center">
                      <div class="schedule-home__tile">
                        <div class="schedule-home__date">
                          November 24
                        </div>
                        <p class="schedule-home__day">
                          Morning
                        </p>
                        <p class="schedule-home__desc">
                          Join us for a <a href="/conf/au/2017/schedule/#morning">writing sprint</a>, either on an open source project or bring your own!
                        </p>
                      </div>
                    </div>
                    <div class="col-xs-12 col-sm-4 text-center">
                      <div class="schedule-home__tile">
                        <div class="schedule-home__date">
                          November 24
                        </div>
                        <p class="schedule-home__day">
                          Afternoon
                        </p>
                        <p class="schedule-home__desc">
                         The main <a href="/conf/au/2017/schedule/#afternoon">talk track</a>: five short talks about documentation.
                        </p>
                      </div>
                    </div>
                    <div class="col-xs-12 col-sm-4 text-center">
                      <div class="schedule-home__tile schedule-home__tile--last">
                        <div class="schedule-home__date">
                          November 24
                        </div>
                        <p class="schedule-home__day">
                          Evening
                        </p>
                        <p class="schedule-home__desc">
                          Join other documentarians for a chat about the weather over dinner. Partners welcome. Details coming soon.
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </section>

              <!-- Speakers -->
              {% set conf = "eu-2017" %}
              {% set speakers = eu_2017_speakers %}

              <section class="section">
                <div class="row">
                   <div class="col-xs-12">
                    <div class="section__header subheader">
                      <span class="subheader__yellow"></span>
                       <h2 class="subheader__header">Speakers</h2>
                     </div>
                   </div>
                 </div>
                 <div class="row">

                   {% for talk in speakers %}

                      {% for speaker in talk.speakers %}
                      <div class="col-xs-6 col-md-1-5 text-center">
                        <a href="speakers/#speaker-{{ speaker.slug }}">
                        <div class="person">
                          <img src="/_static/img/speakers/{{ speaker.img_file }}" alt="{{speaker.name}}" class="person__img" style="border-radius: 50%"/>
                          <p class="person__name">{{speaker.name}}</p>
                        </div>
                        </a>
                      </div>

                      {% endfor %}

                   {% endfor %}
                 </div>
              </section>

              <section class="section" id="news">
                <div class="row">
                  <div class="col-xs-12">
                    <div class="section__header subheader">

                      <span class="subheader__yellow"></span>
                      <h2 class="subheader__header">Latest News</h2>
                      <a href="news/" class="subheader__more">Read all news</a>
                    </div>
                  </div>
                </div>

                <div class="row">
                <div class="col-xs-12 col-md-4">
                  <a href="news/announcing-presentations-ticket-update/" class="well news__tile">
                    <h3 class="well__title">
                      Announcing presentations!
                    </h3>
                    <p class="well__paragraph">
                    We are excited to announce presentations for our first ever Australian day event...
                    </p>
                    <div class="well__time">
                      <span>12:00</span>|<span>October 5, 2017</span>
                    </div>
                  </a>
                </div>

                <div class="row">
                <div class="col-xs-12 col-md-4">
                  <a href="news/announcing-schedule/" class="well news__tile">
                    <h3 class="well__title">
                      Announcing talk Schedule
                    </h3>
                    <p class="well__paragraph">
                    Our website is now updated with the final schedule for
                    the talks...
                    </p>
                    <div class="well__time">
                      <span>12:00</span>|<span>October 5, 2017</span>
                    </div>
                  </a>
                </div>

                <div class="row">
                <div class="col-xs-12 col-md-4">
                  <a href="news/announcing-events-volunteers/" class="well news__tile">
                    <h3 class="well__title">
                      Announcing Events and Call for Volunteers
                    </h3>
                    <p class="well__paragraph">
                    The day event is now just under two months away, and we hope
                    you’re getting geared up...
                    </p>
                    <div class="well__time">
                      <span>12:00</span>|<span>October 1, 2017</span>
                    </div>
                  </a>
                </div>

              </section>

              </section>
              
              <!-- Sponsors -->
              <section class="section section--last">

                <div class="row">
                  <div class="col-xs-12">
                    <div class="section__header subheader">
                      <span class="subheader__yellow"></span>
                      <h2 class="subheader__header">Sponsors</h2>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col-sm-8 col-sm-offset-2">
                    <p>The conference wouldn't be nearly as great as it is without our wonderful corporate sponsors.
                    Thanks to these folks for supporting the community.</p>
                  </div>
                </div>

.. .. include:: /include/conf/2017-au-sponsors.rst

.. raw:: html

              <div class="row">
                <div class="col-sm-8 col-sm-offset-2">
                <br />
                <h3>
                  In kind sponsors
                </h3>
                </div>
              </div>

                <div class="row">
                  <div class="col-sm-8 col-sm-offset-2">
                    <p>Write the Docs is also helped out by companies that give their employees time to work on the conference.</p>
                  </div>
                </div>

.. include:: /include/conf/2017-au-sponsors-in-kind.rst

.. raw:: html

              <div class="row">
                <div class="col-sm-8 col-sm-offset-2">
                <br />
                <h3>
                  Media Sponsors
                </h3>
                </div>
              </div>

                <div class="row">
                  <div class="col-sm-8 col-sm-offset-2">
                    <p>These folks will be helping cover the conference so people who can't attend still get all the good information that is being presented!</p>
                  </div>
                </div>

.. .. include:: /include/conf/2017-au-sponsors-media.rst

.. raw:: html

              </section>

            </div>
          </div>
        </div>
      </div>
