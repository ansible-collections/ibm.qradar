.. _ibm.qradar.rule_module:


***************
ibm.qradar.rule
***************

**Manage state of QRadar Rules, with filter options**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1

DEPRECATED
----------
:Removed in collection release after 2024-09-01
:Why: Newer and updated modules released with more functionality.
:Alternative: qradar_analytics_rules



Synopsis
--------
- Manage state of QRadar Rules, with filter options




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Manage state of a QRadar Rule by ID</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Manage state of a QRadar Rule by name</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>owner</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Manage ownership of a QRadar Rule</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>enabled</li>
                                    <li>disabled</li>
                                    <li>absent</li>
                        </ul>
                </td>
                <td>
                        <div>Manage state of a QRadar Rule</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    - name: Enable Rule 'Ansible Example DDoS Rule'
      qradar_rule:
        name: 'Ansible Example DDOS Rule'
        state: enabled




Status
------


- This module will be removed in a release after 2024-09-01. *[deprecated]*
- For more information see `DEPRECATED`_.


Authors
~~~~~~~

- Ansible Security Automation Team (@maxamillion) <https://github.com/ansible-security>
