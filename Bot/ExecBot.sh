#!/bin/bash
python3 app.py
while [ 1 == 1 ]; do
    python3 automate.py
    wait 86400
done