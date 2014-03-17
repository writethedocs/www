tail -n +2 ~/Downloads/EU\ Schedule\ -\ Schedule.csv | csvcut -c 2,1 |head -n 18 | cut -c1-4,8- > _data/eu2014-day1.csv
tail -n +2 ~/Downloads/EU\ Schedule\ -\ Schedule.csv | csvcut -c 2,1 |tail -n 18 | cut -c1-4,8- > _data/eu2014-day2.csv
