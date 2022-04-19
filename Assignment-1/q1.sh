#!/bin/bash
RED='\033[0;31m' #For Coloured Headings
NC='\033[0m'

echo -e "${RED}Part A :${NC}"
awk '!/^$/' quotes.txt # > quotes.temp && mv quotes.temp quotes.txt
echo ""
echo -e "${RED}Part B :${NC}"
awk '!/^$/' quotes.txt | awk '!store[$0]++' #quotes.txt > quotes.temp && mv quotes.temp quotes.txt
