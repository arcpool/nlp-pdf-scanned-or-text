#To determine whether a given file is scanned or digital.

import subprocess

out=subprocess.getoutput([    
        '''
        value=""
        for file in *.pdf
do
 echo $file
 grep -aq '/Image/' "$file"
 if [ $? -eq 0 ]
 then
  image=true
 else
  image=false
 fi
 grep -aq '/Text' "$file"
 if [ $? -eq 0 ]
 then
  text=true 
 else
  text=false 
 fi
 #echo "Image="$image
 #echo "Text="$text

 if $image && $text
 then
  value="scanned"
  #echo "scanned"
 elif $text
 then
  #echo "text"
  value="text"
 else
  #echo "scanned"
  value="scanned"
 fi
 #echo "------"
 echo $value
done
#echo "Complete"
        
      '''])  

print(out)


#________________________________________________#
