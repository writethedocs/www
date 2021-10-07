from pathlib import Path
import sys
import argparse

docs_root = str(Path(__file__).resolve().parents[1])
sys.path.append(docs_root)

from _ext.core import load_conference_context_from_yaml

def print_schedule(shortcode, year):
    year_str = str(year)
    page = f'print-schedule-{shortcode}-{year}'
    conf_data = load_conference_context_from_yaml(shortcode, year, year_str, page)

    schedule = conf_data['schedule']
    for day, day_schedule in schedule.items():
        print(f'=== {day} ===')
        for item in day_schedule:
            try:
                display = item['data']['title'] + ' - ' + item['speaker_names']
            except KeyError:
                display = item['title']
            print(f'{item["time"]}: {display}')

        print()

    if conf_data.get('time_format'):
        print('Conference uses new format (supports time and duration in schedule)\n')
    else:
        print('Conference uses legacy format (supports time only, ignores duration)\n')

if __name__ == '__main__':
    description = """Print a conference schedule"""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(dest='shortcode', type=str,
                        help=f'conference shortcode')
    parser.add_argument(dest='year', type=int,
                        help=f'conference year')
    args = parser.parse_args()

    print_schedule(args.shortcode, args.year)
