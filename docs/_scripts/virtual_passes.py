import csv
import random
import sys

import mandrill

# This script reads three CSVs. One has the ticket IDs that chose a virtual
# pass in Portland 2020, one with the tickets for that conference, and one
# with the orders.
#
# Each pass is assigned a random discount code, and enriched with the
# intended email recipients.
# Then, it writes a discounts CSV for upload in tito. This may need adjustment
# per conference, as the ticket types may be slightly different. After user
# confirmation that passes were uploaded, it sends every user an email with
# their pass details.
# While running, it prints details of the passes/discounts it created.
#
# To run, you need the mentioned CSV files, update the tito field header
# and count, and make sure the e-mail and subject are up to date.

passes = {}

with open('passes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        discount_code = 'PASS-' + ''.join(random.choices('BCDFGHKMNPQRSTVWXYZ2356789', k=10))
        passes[row[0]] = {'discount_code': discount_code}

print(f'Found {len(passes.keys())} ticket IDs to assign passes')

with open('p2020-tickets.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        ticket_id = row[14]
        email = row[7]
        if ticket_id in passes:
            passes[ticket_id]['email'] = email

with open('p2020-orders.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        order_id = row[0]
        email = row[2]
        relevant_passes = [p for ticket_id, p in passes.items() if ticket_id.startswith(order_id)]
        for p in relevant_passes:
            p['cc'] = email

no_email = [k for k, v in passes.items() if 'email' not in v or 'cc' not in v]
if no_email:
    print('ERROR: No email found for: ', no_email)
    sys.exit()

with open('discounts.csv', 'w') as f:
    f.write(
        'Code*,Type [Flat|Percent]*,Value*,Quantity,Available From,Available To,Min. Tickets,Max. Tickets,Only Show Attached Tickets,Reveal Secret Tickets,Description for Organizer,Virtual Student Ticket,Publisher Sponsorship,First Draft Sponsorship,Opportunity Grant Sponsorship,Virtual Independent Ticket,Virtual Corporate Ticket,Give to our grants program,Staff,Volunteer,Speaker Ticket,Sponsor Ticket,Opportunity Grant,Virtual Pass Free Ticket\n')
    for ticket_id, p in passes.items():
        row = [
            p['discount_code'],
            'Percent',
            '100',
            '1',  # number of tickets
            '',  # available from
            '',  # available to
            '',  # min tickets
            '',  # max tickets
            'Y',  # only show attached
            'Y',  # reveal secret tickets that are attached
            f'From Portland {ticket_id}',
            # ticket types
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
            'N',
            'N',
            'Y',
        ]
        f.write(','.join(row) + '\n')

input('Discounts file generated, press enter to send out emails - after uploading discounts to tito')

for ticket_id, p in list(passes.items()):
    # p['email'] = 'sasha@writethedocs.org'
    # p['cc'] = 'sasha@mxsasha.eu'

    url = 'https://ti.to/writethedocs/write-the-docs-australia-2020/discount/' + p['discount_code']
    if not p['email'] and p['cc']:
        p['email'] = p['cc']
    print(','.join([p["email"], p['cc'], p['discount_code'], ticket_id, url]))
    # print(f'Email to {p["email"]}, cc {p["cc"]}: {url}')

    text = f"""
Hello,

Earlier this year, you purchased a ticket for the Write the Docs Portland
conference. You chose to convert your ticket to a virtual pass, which includes
access to the Write the Docs Australia & India conference, on December 3-4, 2020.
This conference will take place online and is scheduled in the AEDT timezone.

To attend this conference, you will have to register. You can do so for free
using the following link:
{url}

If you will not be participating in our Australia & India conference, you can
ignore this mail. For full details on the conference - we've just announced
the talks - see:
https://www.writethedocs.org/conf/australia/2020/

This link is valid for one registration and is sent to the holder of Portland
ticket {ticket_id} and the person who ordered that ticket. If multiple tickets
were registered or ordered by you, you may receive multiple registration links,
each allowing you to register one ticket.

If you have any further questions, please contact australia@writethedocs.org.

Write the Docs
"""

    recipients = [{'email': p['email'], 'type': 'to'}]
    if p['email'] != p['cc']:
        recipients.append({'email': p['cc'], 'type': 'cc'})

    try:
        mandrill_client = mandrill.Mandrill('ZCwNiwVaJKibbZMl9hcYfg')
        message = {
            'from_email': 'australia@writethedocs.org',
            'from_name': 'Write the Docs Australia & India',
            'subject': 'Your Write the Docs Australia & India 2020 Virtual Pass',
            'text': text,
            'to': recipients,
        }
        result = mandrill_client.messages.send(message=message)
        # print(result)

    except mandrill.Error as e:
        print('A mandrill error occurred: %s - %s' % (e.__class__, e))
        raise
