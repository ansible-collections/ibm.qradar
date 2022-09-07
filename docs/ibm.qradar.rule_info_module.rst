.. _ibm.qradar.rule_info_module:


********************
ibm.qradar.rule_info
********************

**Obtain information about one or many QRadar Rules, with filter options**


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
- This module obtains information about one or many QRadar Rules, with filter options




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
                        <div>Obtain only information of the Rule with provided ID</div>
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
                        <div>Obtain only information of the Rule that matches the provided name</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>origin</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>SYSTEM</li>
                                    <li>OVERRIDE</li>
                                    <li>USER</li>
                        </ul>
                </td>
                <td>
                        <div>Obtain only information of Rules that are of a certain origin</div>
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
                        <div>Obtain only information of Rules owned by a certain user</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>EVENT</li>
                                    <li>FLOW</li>
                                    <li>COMMON</li>
                                    <li>USER</li>
                        </ul>
                </td>
                <td>
                        <div>Obtain only information for the Rules of a certain type</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - You may provide many filters and they will all be applied, except for ``id`` as that will return only the Rule identified by the unique ID provided.



Examples
--------

.. code-block:: yaml

    - name: Get information about the Rule named "Custom Company DDoS Rule"
      ibm.qradar.rule_info:
        name: "Custom Company DDoS Rule"
      register: custom_ddos_rule_info

    - name: debugging output of the custom_ddos_rule_info registered variable
      debug:
        var: custom_ddos_rule_info




Status
------


- This module will be removed in a release after 2024-09-01. *[deprecated]*
- For more information see `DEPRECATED`_.


Authors
~~~~~~~

- Ansible Security Automation Team (@maxamillion) <https://github.com/ansible-security>"
