#!/bin/bash

# Generate a random password with atleast lower, upper, numerical and special character
# https://stackoverflow.com/a/63008346

LEN=12
if [ "$1" != "" ]; then LEN="$1"; fi
echo "Len: $LEN"

until [ -z "$pw+x" ]
do
  pw=$(openssl rand -base64 $LEN) &&\
  [[ $(sed "s/[^[:upper:]]//g" <<< $pw | wc -c) -gt 1 ]] &&\
  [[ $(sed "s/[^[:lower:]]//g" <<< $pw | wc -c) -gt 1 ]] &&\
  [[ $(sed "s/[^0-9]//g" <<< $pw | wc -c) -gt 1 ]] &&\
  [[ $(sed "s/[[:alnum:]]//g" <<< $pw | wc -c) -gt 1 ]] && break
done
echo "$pw"
