#!/bin/bash

cd $(dirname "$0")"/.."

uv run make html

# Portland
# This assumes we don't email speakers before the start of the year of the conference.

portland_date=$(date +%Y)
portland_file="_build/html/conf/portland/$portland_date/cfp-email-templates/index.html"

printf "Linting Portland CFP email templates in $portland_file \\n\\n"

# Remove false positive
sed -i '/page-banner/d' $portland_file

# Check for location
if grep -i berlin $portland_file; then
    printf "\nFound Berlin in Portland template\n\n"
fi

# Check for date
if grep $(($portland_date-1)) $portland_file; then
    printf "\nFound last year in Portland template\n\n"
fi

# Check URLs
# first grep defines string for URLs (ewww)
# second grep filters on URLs we think we care about (avoiding all the others in the page) (also ewww)
urls=$(cat $portland_file | grep -o -E 'https?://[^,)"<]+' | tr ',' '\n' | grep -E 'writethedocs.org|docs.google|pretalx|flickr|youtube' |  sort | uniq)

for each in $urls; do
    if curl -s --head $each | head -n 1 | grep "200\|301\|302" > /dev/null; then
        : #printf "URL OK:\\n"
    else
        printf "URL NOT OK: $each\\n"
    fi
done

