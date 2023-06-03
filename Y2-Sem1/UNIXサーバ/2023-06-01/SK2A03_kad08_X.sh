#08_1
whoami="SK2Aa03"
echo "Login user name is ${whoami}"

#08_2
x1="Login user is"
x2="Default shell is"
x3="Current directory is"
whoami="SK2A03"
echo "${x1} ${whoami}"
echo "${x2} ${SHELL}"
echo "${x3} ${PWD}"

#08_3
echo "Input y or n:"
read a
if [ $a = "y" ] || [ $a = "Y" ]
 then echo "OK"
 elif [ $a = "n" ] || [ $a = "N" ]
 then echo "NG"
 else echo "Please input y or n."
fi

#08_4
for i in $@
do
 if test -e $i
  then  echo "${i} copy to bak directory."
  cp $i bak
  else
   echo "${i} is not found."
 fi
done

#08_5
read a
if [[ $a =~ ^[c-t] ]] || [[ $a =~ ^[C-T] ]]
 then echo "CentOS"
 elif [[ $a =~ ^[u-z] ]] || [[ $a =~ ^[U-Z] ]]
 then echo "Ubuntu"
 else echo Red Hat
fi

#08_6
dir_exists(){
   if test -e "bak"
    then echo "bak direcotry is exists."
   fi
}

file_bkup(){
 for i in $1
  do
   if test -e $i
    then echo "$i direcotry is exists. "
    else
    echo " $i is not found. "
   fi
  done
    cp $2 bak
    echo "$2 is copied to bak."
}

dir_exists
file_bkup $@
