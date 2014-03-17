csvcut -c 2,1 ~/Downloads/EU\ Schedule\ -\ Schedule.csv |head -n 19 | cut -c1-4,8- > _data/eu2014-day1.csv
head -n 1 _data/eu2014-day1.csv > _data/eu2014-day2.csv
csvcut -c 2,1 ~/Downloads/EU\ Schedule\ -\ Schedule.csv |tail -n 18 | cut -c1-4,8- >> _data/eu2014-day2.csv
