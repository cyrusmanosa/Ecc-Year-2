Ubuntu
debian
Redhat
CentOS
Fedora
#!bin/bash
#
ls -al | awk '
BEGIN{
  x = 0
  y = 0
}
{
 x++
 y+=$5
}
END{
    print "number of files: " x " capacity: " y " bites" 
}
'

ps aux | awk '
BEGIN{
 a = 0
 b = 0
}
{
 a+=$3
 b+=$4
}
END{
 printf("CPU: %.2f%% Memory%.2f%% in use",a,b)
}
'

#bin/bash
for i in $@
do
 sed -e s/-//g ${@} > phone2.dat
done


#!/bin/bash

read a
result=$(nslookup $a | awk '/^Address:/ && !/#/ {print $2}')

echo "Input search url: ${a}"
echo "IP address: $result"
