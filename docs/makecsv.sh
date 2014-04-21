tail -n +2 ~/Downloads/EU\ Schedule\ -\ Schedule.csv | csvcut -x -c 2,1 |head -n 18 | cut -c1-4,8- > _data/eu2014-day1.csv
tail -n +2 ~/Downloads/EU\ Schedule\ -\ Schedule.csv | csvcut -x -c 2,1 |tail -n 19 | cut -c1-4,8- > _data/eu2014-day2.csv

tail -n +2 ~/Downloads/NA\ Schedule\ -\ Schedule.csv | csvcut -x -c 2,1 |head -n 25 > _data/na2014-day1.csv
tail -n +2 ~/Downloads/NA\ Schedule\ -\ Schedule.csv | csvcut -x -c 2,1 |tail -n 21 > _data/na2014-day2.csv
