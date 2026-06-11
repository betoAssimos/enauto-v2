# Lab 03 — Ansible (Blueprint 2.4)

## What this lab demonstrates
Use of ansible to configure the device, with cisco.ios using lines and src, a jinja template.

## Files
- `inventory.yml`
- `ansible.cfg` — basic config for ansible
- `01_gather_facts.yml` — gather facts
- `02_config_push.yml` — push config
- `03_config_template.yml` + `templates/ntp.j2` — use template + config push

## Write-safety convention
Ansible is idempotent, to test it, start running the playbook with --check, them use a -v or normal run to check the cahnged field and, after applyionog the config, run playbook again to see that Ansible do not apply config again if its present.