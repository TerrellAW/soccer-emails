#!/bin/bash

source env.sh

email="$recipient"
data=$(<data/soccer.txt)

from="From: "$sender""
to="To: "$email""
subject="Subject: Soccer News"
text="$data"

printf -v message -- "%s\n" {"$from" "$to" "$subject" "$text"}

msmtp -a gmail "$email" <<< "$message"
