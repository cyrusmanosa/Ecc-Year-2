 for i in $@
do 
 if test -e $i 
  then  echo "${i} copy to bak directory."
  cp $i bak
  else 
   echo "${i} is not found." 
 fi
done 
