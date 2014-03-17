csvcut -c 2,1 ~/Downloads/EU\ Schedule\ -\ Schedule\ \(3\).csv |head -n 18 > _data/eu2014-day1.csv
csvcut -c 2,1 ~/Downloads/EU\ Schedule\ -\ Schedule\ \(3\).csv |tail -n 18 > _data/eu2014-day2.csv
