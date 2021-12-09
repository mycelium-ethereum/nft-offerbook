#!/usr/bin/env bash

echo "$(date): Adding your port number to the server script" >> /var/log/cron.log 2>&1
cd /app
/usr/local/bin/python3 add_port_number.py