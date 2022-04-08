#!/bin/bash

awk '!/^$/' quotes.txt > quotes.temp && mv quotes.temp quotes.txt
