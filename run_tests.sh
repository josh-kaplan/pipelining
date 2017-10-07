#!/bin/bash
# 
# Josh Kaplan
# _jk@jhu.edu
# 
# Builds all programs and executes tests

echo -n "Cleaning Up Old files ............... "
make clean > /dev/null
echo "OK"

echo -n "Building timer ...................... "
make timer > /dev/null
echo "OK"

echo -n "Building p1 ......................... "
make p1 > /dev/null
echo "OK"

echo -n "Building p2 ......................... "
make p2 >/dev/null
echo "OK"

echo "########################################"
echo "##           Running Tests            ##"
echo "########################################"

echo -n "Running p1 .......................... "
nice -20 ./timer nice -20 ./p1 > p1.dat
echo "OK"

echo -n "Running p2 .......................... "
nice -20 ./timer nice -20 ./p2 > p2.dat
echo "OK"

sleep 10

echo -n "Running p2 .......................... "
nice -20 ./timer nice -20 ./p2 >> p2.dat
echo "OK"

echo -n "Running p1 .......................... "
nice -20 ./timer nice -20 ./p1 >> p1.dat
echo "OK"

sleep 5

echo -n "Running p1 .......................... "
nice -20 ./timer nice -20 ./p1 >> p1.dat
echo "OK"

echo -n "Running p2 .......................... "
nice -20 ./timer nice -20 ./p2 >> p2.dat
echo "OK"

echo "########################################"
echo "##           Tests Complete           ##"
echo "########################################"

echo -n "Displaying results .................. "
python results.py
echo "OK"
echo "Complete"