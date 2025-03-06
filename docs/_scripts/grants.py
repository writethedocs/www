import csv
import random
import sys

import mandrill

# This script reads grant recipients from stdin.
# Each recipient is assigned a random discount code.
#
# Then, it writes a discounts CSV for upload in tito. This may need adjustment
# per conference, as the ticket types may be slightly different. After user
# confirmation that passes were uploaded, it sends every user an email with
# their pass details.
#
# To run, set your mandrill token in ~/.mandrill.key, update the tito field header
# and count, and make sure the e-mail and subject are up to date.


codes = []
conference_name = "Write the Docs Portland 2025"
conference_email = "portland@writethedocs.org"
conference_tito_slug = "write-the-docs-portland-2025"

for recipient in sys.stdin:
    discount_code = 'GRANT-' + ''.join(random.choices('BCDFGHKMNPQRSTVWXYZ2356789', k=10))
    codes.append((recipient.strip(), discount_code))


with open('grants.csv', 'w') as f:
    f.write(
        '"Code*","Type [Flat|Percent]*","Value*","Quantity","Available From","Available To","Min. Tickets","Max. Tickets","Show Public Tickets","Show Secret Tickets","Source Code","Disable If Volume Pricing","Block Orders If Not Applicable","Description for Organizer","Virtual conference","Student Ticket","Independent Ticket","Corporate Ticket","Concierge Ticket","Livestream Ticket","Volunteer Ticket","Staff Ticket","Speaker Ticket","Sponsor Ticket","Opportunity Grant Ticket","Outreach Ticket","Hike Ticket"\n')

    for recipient, discount_code in codes:
        row = [
            discount_code,
            'Percent',
            '100',
            '1',  # number of tickets
            '', # available from
            '', # available to
            '1', # min tickets
            '1', # max tickets
            'only_attached',  # show public tickets
            'if_discount_code_available',  # show secret tickets
            '', # source code,
            '', # disable for volume
            '', # block orders if not avail
            f'Grant program for {recipient}', # descr
            # Ticket types
            'N',
            'N',
            'N',
            'N',
            'N',
            'N',
            'N',
            'N',
            'N',
            'N',
            'Y',
        ]
        f.write(','.join(row) + '\n')

input('Discounts file generated, press enter to send out emails - after uploading discounts to tito')

for recipient, discount_code in codes:
    url = f'https://ti.to/writethedocs/{conference_tito_slug}/discount/{discount_code}'
    print(f'Email to {recipient}: {url}')

    text = f"""
Hello,

Thanks for applying to the Opportunity Grant program for {conference_name}.
As part of your grant, you will receive a free ticket for the conference.

The ticket can be registered on the following URL:
{url}

Please let us know if you have any further questions.

Write the Docs
"""

    recipients = [{'email': recipient, 'type': 'to'}]

    try:
        mandrill_client = mandrill.Mandrill()
        message = {
            'from_email': conference_email,
            'from_name': conference_name,
            'subject': f'{conference_name} Opportunity Grant',
            'text': text,
            'to': recipients,
        }
        result = mandrill_client.messages.send(message=message)
        # print(result)

    except mandrill.Error as e:
        print('A mandrill error occurred: %s - %s' % (e.__class__, e))
        raise
