#!/bin/bash
RED='\033[0;31m' #For Coloured Headings
NC='\033[0m'

#find -name "$1" -printf "%s\n" 
echo -n -e "${RED}File Size in Bytes -> ${NC}"
wc -c < "$1"
echo ""
echo -n -e "${RED}Number of Lines -> ${NC}"
cat $1 | wc -l
echo ""
echo -n -e "${RED}Number of Words -> ${NC}"
cat $1 | wc -w
echo ""
echo -e "${RED}Count of Words per Line :- ${NC}"
count=1
while read i; do
{
	echo -n "Line No: $count - Count of Words: "
	wc -w <<< "$i"
	((count=count+1))
}
done < $1
echo ""
echo -e "${RED}Repeated Words with count${NC}"
grep -wo '[[:alnum:]]\+' $1 | sort | uniq -cd | awk '{print "Word: " $2 " - Count  of repetition: " $1}'
echo ""
