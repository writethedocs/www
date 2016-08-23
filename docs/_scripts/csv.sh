# NA 2016
cat ~/Downloads/Final\ Talks\ -\ Schedule.csv |csvcut -x -c 2,3| head -n 25 |csvjson -i 4 > ../data/na-2016-day-1.json
cat ~/Downloads/Final\ Talks\ -\ Schedule.csv |csvcut -x -c 2,3| tail -n 27 |csvjson -i 4 > ../data/na-2016-day-2.json

#EU 2016

cat ~/Downloads/Final\ Talks\ EU\ 2016\ -\ Schedule.csv | csvcut -x -c 1,2 | head -n 25 | csvjson -i 4 > ../data/eu-2016-day-1.json
cat ~/Downloads/Final\ Talks\ EU\ 2016\ -\ Schedule.csv | csvcut -x -c 1,2 | tail -n 24 | csvjson -i 4 > ../data/eu-2016-day-2.json