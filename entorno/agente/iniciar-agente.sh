#!/bin/sh
set -eu

test -f /var/log/si084_portal_access.log || touch /var/log/si084_portal_access.log
if ! grep -q 'si084_portal_access.log' /var/ossec/etc/ossec.conf; then
  awk '
    !done && /<\/ossec_config>/ {
      print "  <localfile>"
      print "    <location>/var/log/si084_portal_access.log</location>"
      print "    <log_format>apache</log_format>"
      print "  </localfile>"
      done = 1
    }
    { print }
  ' /var/ossec/etc/ossec.conf > /tmp/ossec.conf
  cat /tmp/ossec.conf > /var/ossec/etc/ossec.conf
  rm /tmp/ossec.conf
fi

/var/ossec/bin/wazuh-control start
tail -F /var/ossec/logs/ossec.log
