#!/bin/bash
RED='\033[0;31m' #For Coloured Headings
NC='\033[0m'

echo "Enter the Array with comma separated elements"
read -p "-> " in
in="${in//,/ }"
read -a array <<< $in

len=${#array[*]}

for ((i=0; i<$len; i++))
do
{
	for ((j=0; j<$len-$i-1; j++))
	do
	{
		if [ "${array[j]}" -gt "${array[$((j+1))]}" ]
		then
		{
			temp=${array[$j]}
			array[$j]=${array[$((j+1))]}
			array[$j+1]=$temp
		}
		fi
	}
	done
}
done
echo ""
echo -e "${RED}Sorted Array is :-"
echo ${array[*]}
