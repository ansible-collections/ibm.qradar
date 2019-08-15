#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2019, Adam Miller (admiller@redhat.com)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: qradar_deploy
short_description: Trigger a qradar configuration deployment
description:
  - This module allows for INCREMENTAL or FULL deployments
version_added: "2.9"
options:
  type:
    description:
     - Type of deployment
    required: false
    type: str
    choices:
      - "INCREMENTAL"
      - "FULL"
    default: "INCREMENTAL"
notes:
  - This module does not support check mode because the QRadar REST API does not offer stateful inspection of configuration deployments

author: "Ansible Security Automation Team (https://github.com/ansible-security)
'''

EXAMPLES = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text

from ansible.module_utils.urls import Request
from ansible.module_utils.six.moves.urllib.parse import quote
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible_collections.ansible_security.community.plugins.module_utils.qradar import QRadarRequest

import json

def main():

    argspec = dict(
        type=dict(choices=['INCREMENTAL', 'FULL'], required=False, default='INCREMENTAL'),
    )

    module = AnsibleModule(
        argument_spec=argspec,
        supports_check_mode=False
    )

    qradar_request = QRadarRequest(
        module,
        headers={"Content-Type": "application/json", "Version": "9.1"},
        not_rest_data_keys=['state', 'type_name', 'identifier']
    )

    qradar_return_data = qradar_request.post_by_path('api/staged_config/deploy_status')

    if to_text("No changes to deploy") in to_text(qradar_return_data['message']):
        module.exit_json(
            msg="No changes to deploy",
            qradar_return_data=qradar_return_data,
            changed=False
        )
    else:
        module.exit_json(
            msg="Successfully initiated {0} deployment.".format(module.params['type']),
            qradar_return_data=qradar_return_data,
            changed=True
        )

if __name__ == '__main__':
    main()
