# Transform the spreadsheet source of truth (with time calulations) for the schedule into YAML
# 1. Pip install cvskit yq
# 2. Save the spreadsheet in  to your local Download directory
# 3. Adjust `head -n 19` and `tail -n 18` as needed if you added or removed lines

cat ~/Downloads/Talk\ schedule\ generator\ -\ Schedule.csv |csvcut -x -c 1,3 | head -n 19 | tail -n 18 | csvjson -i 4 | yq -y
cat ~/Downloads/Talk\ schedule\ generator\ -\ Schedule.csv |csvcut -x -c 1,3 | tail -n 16 | csvjson -i 4 | yq -y

# :-( Paste each output into `talks_day1:` and `talks_day2:` and indent :-(