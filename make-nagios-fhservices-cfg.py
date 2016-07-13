#!/usr/bin/env python

import os

from jinja2 import Environment, FileSystemLoader, Template

fh_services_ping = ['fh-messaging', 'fh-metrics']
fh_services_health = ['fh-messaging', 'fh-metrics']

rhmap_admin_email = os.getenv('RHMAP_ADMIN_EMAIL', 'root@localhost')
rhmap_router_dns = os.getenv('RHMAP_ROUTER_DNS', 'rhmap.localhost')

template_file = '/opt/rhmap/fhservices.cfg.j2'
nagios_config_filename = '/etc/nagios/conf.d/fhservices.cfg'

template_basename = os.path.basename(template_file)
template_dirname = os.path.dirname(template_file)

j2env = Environment(loader=FileSystemLoader(template_dirname), trim_blocks=True)
j2template = j2env.get_template(template_basename)

j2renderedouput = j2template.render(fh_services_ping=fh_services_ping,
                                    fh_services_health=fh_services_health,
                                    rhmap_router_dns=rhmap_router_dns,
                                    rhmap_admin_email=rhmap_admin_email)

with open(nagios_config_filename, 'wb') as nagios_config_file:
    nagios_config_file.write(j2renderedouput)
