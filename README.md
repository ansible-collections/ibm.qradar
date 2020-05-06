# IBM QRadar Ansible Collection

## Tech Preview

This is the [Ansible
Collection](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html)
provided by the [Ansible Security Automation
Team](https://github.com/ansible-security) for automating actions in [IBM
QRadar SIEM](https://www.ibm.com/us-en/marketplace/ibm-qradar-siem).

This Collection is meant for distribution via
[Ansible Galaxy](https://galaxy.ansible.com/) as is available for all
[Ansible](https://github.com/ansible/ansible) users to utilize, contribute to,
and provide feedback about.

### Using IBM QRadar Ansible Collection

An example for using this collection to manage a log source with [IBM QRadar](https://www.ibm.com/security/security-intelligence/qradar) is as follows.

`inventory.ini` (Note the password should be managed by a [Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html) for a production environment.
```
[qradar]
qradar.example.com

[qradar:vars]
ansible_network_os=ibm.qradar.qradar
ansible_user=admin
ansible_httpapi_pass=SuperSekretPassword
ansible_httpapi_use_ssl=yes
ansible_httpapi_validate_certs=yes
ansible_connection=httpapi
```
#### Using the modules with Fully Qualified Collection Name (FQCN)

With [Ansible
Collections](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html)
there are various ways to utilize them either by calling specific Content from
the Collection, such as a module, by its Fully Qualified Collection Name (FQCN)
as we'll show in this example or by defining a Collection Search Path as the
examples below will display.

`qradar_with_collections_example.yml`
```
---
- name: Testing URI manipulation of QRadar with FQCN
  hosts: qradar
  gather_facts: false
  tasks:
    - name: create log source
      ibm.qradar.qradar_log_source_management:
        name: "Ansible Collections Example Log Source"
        type_name: "Linux OS"
        state: present
        description: "Ansible Collections Example Log Source Description"
```

#### Define your collection search path at the Play level

Below we specify our collection at the
[Play](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html)
level which allows us to use the `qradar_log_source_management` module without
the need for the FQCN for each task.

`qradar_with_collections_example.yml`
```
---
- name: Testing URI manipulation of QRadar
  hosts: qradar
  gather_facts: false
  collections:
    - ibm.qradar
  tasks:
    - name: create log source
      qradar_log_source_management:
        name: "Ansible Collections Example Log Source"
        type_name: "Linux OS"
        state: present
        description: "Ansible Collections Example Log Source Description"
```

#### Define your collection search path at the Block level

Another option for Collection use is below. Here we use the
[`block`](https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html)
level keyword instead of [Play](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html)
level as with the previous example. In this scenario we are able to use the
`qradar_log_source_management` module without the need for the FQCN for each
task but with an optionally more specific scope of Collection Search Path than
specifying at the Play level.

`qradar_with_collections_block_example.yml`
```
---
- name: Testing URI manipulation of QRadar
  hosts: qradar
  gather_facts: false
  tasks:
    - name: collection namespace block
      block:
        - name: create log source
          qradar_log_source_management:
            name: "Ansible Collections Example Log Source"
            type_name: "Linux OS"
            state: present
            description: "Ansible Collections Example Log Source Description"
      collections:
        - ibm.qradar
```

### Directory Structure

* `docs/`: local documentation for the collection
* `license.txt`: optional copy of license(s) for this collection
* `galaxy.yml`: source data for the MANIFEST.json that will be part of the collection package
* `playbooks/`: playbooks reside here
  * `tasks/`: this holds 'task list files' for `include_tasks`/`import_tasks` usage
* `plugins/`: all ansible plugins and modules go here, each in its own subdir
  * `modules/`: ansible modules
  * `lookups/`: lookup plugins
  * `filters/`: Jinja2 filter plugins
  * ... rest of plugins
* `README.md`: information file (this file)
* `roles/`: directory for ansible roles
* `tests/`: tests for the collection's content
