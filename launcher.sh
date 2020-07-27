#!/bin/bash

conda activate
cd
cd environments/GSM
python getRSSIevent.py & echo > $! /home/williamdlukito/environments/GSM/myprocess.pid
