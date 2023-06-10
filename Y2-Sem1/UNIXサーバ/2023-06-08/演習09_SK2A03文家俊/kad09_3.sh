#bin/bash
for i in $@
do
 sed -e s/-//g ${@} > phone2.dat
done


