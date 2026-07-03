#!/bin/bash

./get_data.sh
python parse.py
./mail_soccer.sh
