cat ~/Downloads/Final\ Talks\ -\ Schedule.csv |csvcut -x -c 2,3| head -n 25 |csvjson -i 4 > ../data/na-2016-day-1.json
cat ~/Downloads/Final\ Talks\ -\ Schedule.csv |csvcut -x -c 2,3| tail -n 27 |csvjson -i 4 > ../data/na-2016-day-2.json
