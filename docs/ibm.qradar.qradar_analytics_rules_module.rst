.. _ibm.qradar.qradar_analytics_rules_module:


*********************************
ibm.qradar.qradar_analytics_rules
*********************************

**Qradar Analytics Rules Management resource module**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module allows for modification, deletion, and checking of Analytics Rules in QRadar




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary of Qradar Analytics Rules options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Check if the rule is enabled</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fields</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>average_capacity</li>
                                    <li>base_capacity</li>
                                    <li>base_host_id</li>
                                    <li>capacity_timestamp</li>
                                    <li>creation_date</li>
                                    <li>enabled</li>
                                    <li>id</li>
                                    <li>identifier</li>
                                    <li>linked_rule_identifier</li>
                                    <li>modification_date</li>
                                    <li>name</li>
                                    <li>origin</li>
                                    <li>owner</li>
                                    <li>type</li>
                        </ul>
                </td>
                <td>
                        <div>List of params filtered from the Rule config</div>
                        <div>NOTE, this param is valid only via state GATHERED.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>The sequence ID of the rule.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>The name of the rule.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>range</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Parameter to restrict the number of elements that are returned in the list to a specified range.</div>
                        <div>NOTE, this param is valid only via state GATHERED.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>merged</li>
                                    <li>gathered</li>
                                    <li>deleted</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in</div>
                        <div>The state <em>gathered</em> will get the module API configuration from the device and transform it into structured data in the format as per the module argspec and the value is returned in the <em>gathered</em> key within the result.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    # Using MERGED state
    # -------------------

    - name: DISABLE Rule 'Ansible Example DDoS Rule'
      ibm.qradar.qradar_analytics_rules:
        config:
          name: 'Ansible Example DDOS Rule'
          enabled: false
        state: merged

    # RUN output:
    # -----------

    #   qradar_analytics_rules:
    #     after:
    #       average_capacity: null
    #       base_capacity: null
    #       base_host_id: null
    #       capacity_timestamp: null
    #       creation_date: 1658929682568
    #       enabled: false
    #       id: 100443
    #       identifier: ae5a1268-02a0-4976-84c5-dbcbcf854b9c
    #       linked_rule_identifier: null
    #       modification_date: 1658929682567
    #       name: Ansible Example DDOS Rule
    #       origin: USER
    #       owner: admin
    #       type: EVENT
    #     before:
    #       average_capacity: null
    #       base_capacity: null
    #       base_host_id: null
    #       capacity_timestamp: null
    #       creation_date: 1658929682568
    #       enabled: true
    #       id: 100443
    #       identifier: ae5a1268-02a0-4976-84c5-dbcbcf854b9c
    #       linked_rule_identifier: null
    #       modification_date: 1658929682567
    #       name: Ansible Example DDOS Rule
    #       origin: USER
    #       owner: admin
    #       type: EVENT


    # Using GATHERED state
    # --------------------

    - name: Get information about the Rule named "Ansible Example DDOS Rule"
      ibm.qradar.qradar_analytics_rules:
        config:
          name: "Ansible Example DDOS Rule"
        state: gathered

    # RUN output:
    # -----------

    #   gathered:
    #     average_capacity: null
    #     base_capacity: null
    #     base_host_id: null
    #     capacity_timestamp: null
    #     creation_date: 1658918848694
    #     enabled: true
    #     id: 100443
    #     identifier: d6d37942-ba28-438f-b909-120df643a992
    #     linked_rule_identifier: null
    #     modification_date: 1658918848692
    #     name: Ansible Example DDOS Rule
    #     origin: USER
    #     owner: admin
    #     type: EVENT

    - name: Get information about the Rule with ID 100443
      ibm.qradar.qradar_analytics_rules:
        config:
          id: 100443
        state: gathered

    # RUN output:
    # -----------

    #   gathered:
    #     average_capacity: null
    #     base_capacity: null
    #     base_host_id: null
    #     capacity_timestamp: null
    #     creation_date: 1658918848694
    #     enabled: true
    #     id: 100443
    #     identifier: d6d37942-ba28-438f-b909-120df643a992
    #     linked_rule_identifier: null
    #     modification_date: 1658918848692
    #     name: Ansible Example DDOS Rule
    #     origin: USER
    #     owner: admin
    #     type: EVENT

    - name: TO Get information about the Rule ID with a range
      ibm.qradar.qradar_analytics_rules:
      config:
        range: 100300-100500
        fields:
          - name
          - origin
          - owner
      state: gathered

    # RUN output:
    # -----------

    # gathered:
    #   - name: Devices with High Event Rates
    #     origin: SYSTEM
    #     owner: admin
    #   - name: Excessive Database Connections
    #     origin: SYSTEM
    #     owner: admin
    #   - name: 'Anomaly: Excessive Firewall Accepts Across Multiple Hosts'
    #     origin: SYSTEM
    #     owner: admin
    #   - name: Excessive Firewall Denies from Single Source
    #     origin: SYSTEM
    #     owner: admin
    #   - name: 'AssetExclusion: Exclude DNS Name By IP'
    #     origin: SYSTEM
    #     owner: admin
    #   - name: 'AssetExclusion: Exclude DNS Name By MAC Address'
    #     origin: SYSTEM
    #     owner: admin

    - name: Delete custom Rule by NAME
      ibm.qradar.qradar_analytics_rules:
        config:
          name: 'Ansible Example DDOS Rule'
        state: deleted

    # RUN output:
    # -----------

    #   qradar_analytics_rules:
    #     after: {}
    #     before:
    #       average_capacity: null
    #       base_capacity: null
    #       base_host_id: null
    #       capacity_timestamp: null
    #       creation_date: 1658929431239
    #       enabled: true
    #       id: 100444
    #       identifier: 3c2cbd9d-d141-49fc-b5d5-29009a9b5308
    #       linked_rule_identifier: null
    #       modification_date: 1658929431238
    #       name: Ansible Example DDOS Rule
    #       origin: USER
    #       owner: admin
    #       type: EVENT

    # Using DELETED state
    # -------------------

    - name: Delete custom Rule by ID
      ibm.qradar.qradar_analytics_rules:
        config:
          id: 100443
        state: deleted

    # RUN output:
    # -----------

    #   qradar_analytics_rules:
    #     after: {}
    #     before:
    #       average_capacity: null
    #       base_capacity: null
    #       base_host_id: null
    #       capacity_timestamp: null
    #       creation_date: 1658929431239
    #       enabled: true
    #       id: 100443
    #       identifier: 3c2cbd9d-d141-49fc-b5d5-29009a9b5308
    #       linked_rule_identifier: null
    #       modification_date: 1658929431238
    #       name: Ansible Example DDOS Rule
    #       origin: USER
    #       owner: admin
    #       type: EVENT



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>after</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The configuration as structured data after module completion.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format of the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration as structured data prior to module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format of the parameters above.</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ansible Security Automation Team (@justjais) <https://github.com/ansible-security>
