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
