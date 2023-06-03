echo "Input y or n:"
read a

if [ $a = "y" ] || [ $a = "Y" ] 
 then echo "OK"
 elif [ $a = "n" ] || [ $a = "N" ]
 then echo "NG"
 else echo "Please input y or n."
fi
