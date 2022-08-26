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

for recipient in sys.stdin:
    discount_code = 'GRANT-' + ''.join(random.choices('BCDFGHKMNPQRSTVWXYZ2356789', k=10))
    codes.append((recipient.strip(), discount_code))


with open('grants.csv', 'w') as f:
    f.write(
        'Code*,Type [Flat|Percent]*,Value*,Quantity,Only Show Attached Tickets,Reveal Secret Tickets,Description for Organizer,Opportunity Grant\n')

    for recipient, discount_code in codes:
        row = [
            discount_code,
            'Percent',
            '100',
            '1',  # number of tickets
            'Y',  # only show attached
            'Y',  # reveal secret tickets that are attached
            f'Grant program for {recipient}',
            'Y',
        ]
        f.write(','.join(row) + '\n')

input('Discounts file generated, press enter to send out emails - after uploading discounts to tito')

for recipient, discount_code in codes:
    url = 'https://ti.to/writethedocs/write-the-docs-prague-2022/discount/' + discount_code
    print(f'Email to {recipient}: {url}')

    text = f"""
Hello,

Thanks for applying to the Opportunity Grant program for Write the Docs.
I’m happy to inform you that we will provide you with a free ticket for the upcoming Prague conference!

The ticket can be registered on the following URL:
{url}

Please let us know if you have any further questions.

Write the Docs
"""

    recipients = [{'email': recipient, 'type': 'to'}]

    try:
        mandrill_client = mandrill.Mandrill()
        message = {
            'from_email': 'prague@writethedocs.org',
            'from_name': 'Write the Docs Prague',
            'subject': 'Write the Docs Prague Opportunity Grant',
            'text': text,
            'to': recipients,
        }
        result = mandrill_client.messages.send(message=message)
        # print(result)

    except mandrill.Error as e:
        print('A mandrill error occurred: %s - %s' % (e.__class__, e))
        raise
