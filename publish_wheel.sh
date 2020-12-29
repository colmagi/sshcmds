#!/bin/bash

script_dir=$(dirname $(readlink -f "$0"))
cur_dir=${PWD}

cd $script_dir || exit 1

python3 -m twine upload dist/*
exit_code=$?

cd $cur_dir || exit 1
exit $exit_cde