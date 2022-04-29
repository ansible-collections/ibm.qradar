.. _ibm.qradar.deploy_module:


*****************
ibm.qradar.deploy
*****************

**Trigger a qradar configuration deployment**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module allows for INCREMENTAL or FULL deployments




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
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>INCREMENTAL</b>&nbsp;&larr;</div></li>
                                    <li>FULL</li>
                        </ul>
                </td>
                <td>
                        <div>Type of deployment</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - This module does not support check mode because the QRadar REST API does not offer stateful inspection of configuration deployments



Examples
--------

.. code-block:: yaml

    - name: run an incremental deploy
      ibm.qradar.deploy:
        type: INCREMENTAL




Status
------


Authors
~~~~~~~

- Ansible Security Automation Team (@maxamillion) <https://github.com/ansible-security>
