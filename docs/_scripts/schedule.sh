cat ~/Downloads/Talk\ schedule\ generator\ -\ Day1.csv |csvcut -x -c 1,3 | head -n 19 | tail -n 18 | csvjson -i 4 | pbcopy
cat ~/Downloads/Talk\ schedule\ generator\ -\ Day1.csv |csvcut -x -c 1,3 | tail -n 16 | csvjson -i 4 | pbcopy

# Paste into an online JSON -> YAML converter