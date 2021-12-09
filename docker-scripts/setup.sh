# !/usr/bin/env bash

printenv | grep -v "no_proxy" >> /etc/environment
/app/docker-scripts/add_port_number.sh
cron
tail -F /var/log/cron.log