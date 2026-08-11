#!/bin/bash
cd /home/ec2-user/devops-web-project
pkill -f "python3.11 app.py" || true
nohup python3.11 app.py > app.log 2>&1 &
