#!/bin/bash
RED='\033[0;31m' #For Coloured Headings
NC='\033[0m'

read -p "Enter the String : " str
rev_str=$(rev <<< $str)
echo -n -e "${RED}String in Reverse -> ${NC}"
echo $rev_str
echo ""

count=24
alphabets=({a..z})
rev_str="${rev_str//${alphabets[25]}/'|'}"
while (( $count>-1 ))
do
	rev_str="${rev_str//${alphabets[$count]}/${alphabets[$count+1]}}"
	let count--
done
rev_str="${rev_str//'|'/${alphabets[0]}}"

count1=24
alphabets1=({A..Z})
rev_str="${rev_str//${alphabets1[25]}/'|'}"
while (( $count1>-1 ))
do
	rev_str="${rev_str//${alphabets1[$count1]}/${alphabets1[$count1+1]}}"
	let count1--
done
rev_str="${rev_str//'|'/${alphabets1[0]}}"
echo -n -e "${RED}Encrypted String in Reverse -> ${NC}"
echo $rev_str
echo ""

let half=${#str}/2
echo -n -e "${RED}String in Half Reverse Form -> ${NC}"
echo -n ${str:0:$half} | rev
echo ${str:$half}
