#!/bin/bash

for i in `find . -name "*.rst"`; do
  sed -i 's/:template: 2017\/eu/:template: 2017\/au/' $i
done
