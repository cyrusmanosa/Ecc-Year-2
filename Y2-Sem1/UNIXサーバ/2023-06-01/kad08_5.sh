read a 

if [[ $a =~ ^[c-t] ]] || [[ $a =~ ^[C-T] ]]
 then echo "CentOS"
 elif [[ $a =~ ^[u-z] ]] || [[ $a =~ ^[U-Z] ]]
 then echo "Ubuntu"
 else echo Red Hat
fi
