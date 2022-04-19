#!/bin/bash
if [ $#  -ne 2 ];
then
	echo "ERROR in no of Arguments";
else
	expr $1 \* $2;
fi

