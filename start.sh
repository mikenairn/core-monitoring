#!/usr/bin/bash

set -o errexit
set -o nounset
set -o pipefail

# Add nagios user
htpasswd -c -b -s /etc/nagios/passwd ${NAGIOS_USER} ${NAGIOS_PASSWORD}

# Generate command config
/opt/rhmap/make-nagios-commands-cfg.py

# Generate fhservices config
/opt/rhmap/make-nagios-fhservices-cfg.py

exec /usr/bin/supervisord -c /etc/supervisord.conf
