#!/bin/bash

read a
result=$(nslookup $a | awk '/^Address:/ && !/#/ {print $2}')

echo "Input search url: ${a}"
echo "IP address: $result"
