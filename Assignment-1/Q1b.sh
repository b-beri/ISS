#!/bin/bash

awk '!store[$0]++' quotes.txt > quotes.temp && mv quotes.temp quotes.txt
