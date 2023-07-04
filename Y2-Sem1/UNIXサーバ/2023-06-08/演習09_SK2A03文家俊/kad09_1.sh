cat awk.dat | awk ' 
BEGIN { print "Start of File" }
{ print $0 } 
END { print "End of File" }
'
