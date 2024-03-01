#!/bin/bash

PROJECT_HOME=`git rev-parse --show-toplevel`
PROJECT_NAME=algorithms
FILE_NAME=main.py

run()
{
    cd $PROJECT_HOME
    python3 $PROJECT_NAME/$FILE_NAME
}

if [ $# == 0 ] ; then
    echo "Give file to run in src dir as args!"
else
    FILE_NAME=$1
    run
fi