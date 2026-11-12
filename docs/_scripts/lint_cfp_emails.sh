#!/bin/bash

cd $(dirname "$0")"/.."

# Uncomment next line if you have't already built the docs
#uv run make html

# Portland
# This assumes we don't email speakers before the start of the year of the conference.


for conference in 'berlin' 'portland'; do

    conf_date=$(date +%Y)
    conf_file="_build/html/conf/$conference/$conf_date/cfp-email-templates/index.html"

    printf "Linting $conference CFP email templates in $conf_file \\n\\n"

    # Remove false positive
    sed -i '/page-banner/d' $conf_file

    # Check for Portland in Berlin templates
    if [ "$conference" = "berlin" ] && grep -i portland $conf_file; then
        printf "\n❌Found Portland in $conference template\n\n"
    fi

    # Check for Berlin in Portland templates
    if [ "$conference" = "portland" ] && grep -i berlin $conf_file; then
        printf "\n❌Found Berlin in $conference template\n\n"
    fi

    # Check for date
    if grep $(($conf_date-1)) $conf_file; then
        printf "\n❌ Found last year in $conference template\n\n"
    fi

    # Check URLs
    # first grep defines string for URLs (ewww)
    # second grep filters on URLs we think we care about (avoiding all the others in the page) (also ewww)
    urls=$(cat $conf_file | grep -o -E 'https?://[^,)"<]+' | tr ',' '\n' | grep -E 'writethedocs.org|pretalx|flickr|youtube' |  sort | uniq)

    for each in $urls; do
        if curl -s --head $each | head -n 1 | grep "200\|301\|302" > /dev/null; then
            : #printf "URL OK:\\n"
        else
            printf "\n❌URL NOT OK: $each\\n"
        fi
    done

done

