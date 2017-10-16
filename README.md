<p><img src="https://www.graylog.org/assets/logo-graylog-6ccfb3d4f7bfd0795c80bb616719f7d2f5151283f25c62aa0a6222994af2abeb.png" alt="graylog logo" title="graylog" align="right" height="60" /></p>

Ansible Role: graylog
=====================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-graylog.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-graylog) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.graylog-blue.svg)](https://galaxy.ansible.com/SoInteractive/graylog/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-graylog.svg)](https://github.com/SoInteractive/ansible-graylog/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Graylog2 log management

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.graylog
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.

TODO
----

Tests, tests, tests
