import csv
import os
import random
import sys

from sendgrid import SendGridAPIClient, Email, Personalization
from sendgrid.helpers.mail import Mail

passes = {}

with open('passes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        discount_code = ''.join(random.choices('BCDFGHKMNPQRSTVWXYZ2356789', k=10))
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
    f.write('Code*,Type [Flat|Percent]*,Value*,Quantity,Available From,Available To,Min. Tickets,Max. Tickets,Only Show Attached Tickets,Reveal Secret Tickets,Description for Organizer,Virtual Student Ticket,Virtual Independent Ticket,Virtual Corporate Ticket,Student or Unemployed Ticket,Independent Ticket,Corporate Ticket,Give to our grants program,Staff,Saturday Hike,Volunteer,Speaker Ticket,Sponsor Ticket,Opportunity Grant,Virtual Pass Free Ticket\n')
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
            'N',
            'Y',
        ]
        f.write(','.join(row) + '\n')

input('Discounts file generated, press enter to send out emails - after uploading discounts to tito')

for ticket_id, p in list(passes.items()):
    url = 'https://ti.to/writethedocs/write-the-docs-prague-2020/discount/' + p['discount_code']
    print(f'Email to {p["email"]}, cc {p["cc"]}: {url}')

    text = f"""
Hello,

Earlier this year, you purchased a ticket for the Write the Docs Portland
conference. You chose to convert your ticket to a virtual pass, which includes
access to the Write the Docs Prague conference, on October 18-20, 2020.

To attend this conference, you will have to register. You can do so for free
using the following link:
{url}

This link is valid for one registration and is sent to the holder of Portland
ticket {ticket_id} and the person who ordered that ticket. If multiple tickets
were registered or ordered by you, you may receive multiple emails, each 
allowing you to register one ticket.

If you will not be participating in our Prague conference, you can ignore
this mail. For full details on the conference, see:
https://www.writethedocs.org/conf/prague/2020/

If you have any further questions, please contact prague@writethedocs.org.

Write the Docs
"""

    message = Mail(
        from_email='prague@writethedocs.org',
        to_emails=p['email'],
        subject='Your Write the Docs Prague 2020 Virtual Pass',
        plain_text_content=text,
    )
    if p['email'] != p['cc']:
        message.personalizations[0].add_cc(Email(p['cc']))
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
    except Exception as e:
        print(e)
