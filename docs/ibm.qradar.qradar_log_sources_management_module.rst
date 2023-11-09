.. _ibm.qradar.qradar_log_sources_management_module:


****************************************
ibm.qradar.qradar_log_sources_management
****************************************

**Qradar Log Sources Management resource module**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module allows for addition, deletion, or modification of Log Sources in QRadar




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary of Qradar Log Sources options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>average_eps</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The average events per second (EPS) rate of the log source over the last 60 seconds.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>coalesce_events</b>
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
                        <div>If events collected by this log source are coalesced based on common properties, the condition is set to &#x27;true&#x27;. If each individual event is stored, then the condition is set to &#x27;false&#x27;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Description of log source</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>If the log source is enabled, the condition is set to &#x27;true&#x27;; otherwise, the condition is set to &#x27;false&#x27;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>gateway</b>
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
                        <div>If the log source is configured as a gateway, the condition is set to &#x27;true&#x27;; otherwise, the condition is set to &#x27;false&#x27;. A gateway log source is a stand-alone protocol configuration. The log source receives no events itself, and serves as a host for a protocol configuration that retrieves event data to feed other log sources. It acts as a &quot;gateway&quot; for events from multiple systems to enter the event pipeline.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>group_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The set of log source group IDs this log source is a member of. Each ID must correspond to an existing log source group.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Log Source Identifier (Typically IP Address or Hostname of log source)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>internal</b>
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
                        <div>If the log source is internal (when the log source type is defined as internal), the condition is set to &#x27;true&#x27;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>language_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The language of the events that are being processed by this log source. Must correspond to an existing log source language. Individual log source types can support only a subset of all available log source languages, as indicated by the supported_language_ids field of the log source type structure</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Name of Log Source</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol_parameters</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The set of protocol parameters</div>
                        <div>If not provided module will set the protocol parameters by itself</div>
                        <div>Note, parameter will come to use mostly in case when facts are gathered and fired with some modifications to params or in case of round trip scenarios.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>The ID of the protocol type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>The unique name of the protocol type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The allowed protocol value.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol_type_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Type of protocol by id, as defined in QRadar Log Source Types Documentation</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>requires_deploy</b>
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
                        <div>Set to &#x27;true&#x27; if you need to deploy changes to enable the log source for use; otherwise, set to &#x27;false&#x27; if the log source is already active.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The status of the log source.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>last_updated</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>last_updated</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>messages</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>last_updated</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>last_updated</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>store_event_payload</b>
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
                        <div>If the payloads of events that are collected by this log source are stored, the condition is set to &#x27;true&#x27;. If only the normalized event records are stored, then the condition is set to &#x27;false&#x27;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>target_event_collector_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The ID of the event collector where the log source sends its data. The ID must correspond to an existing event collector.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The type of the log source. Must correspond to an existing log source type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Type of resource by name</div>
                </td>
            </tr>

            <tr>
                <td colspan="3">
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
                                    <li>replaced</li>
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

    - name: Add Snort n Apache log sources to IBM QRadar
      ibm.qradar.qradar_log_sources_management:
        config:
          - name: "Snort logs"
            type_name: "Snort Open Source IDS"
            description: "Snort IDS remote logs from rsyslog"
            identifier: "192.0.2.1"
          - name: "Apache HTTP Server logs"
            type_name: "Apache HTTP Server"
            description: "Apache HTTP Server remote logs from rsyslog"
            identifier: "198.51.100.1"
        state: merged

    # RUN output:
    # -----------

    #   qradar_log_sources_management:
    #     after:
    #     - auto_discovered: false
    #       average_eps: 0
    #       coalesce_events: true
    #       creation_date: 1654727311444
    #       credibility: 5
    #       description: Snort IDS remote logs from rsyslog
    #       enabled: true
    #       gateway: false
    #       group_ids:
    #       - 0
    #       id: 181
    #       internal: false
    #       language_id: 1
    #       last_event_time: 0
    #       log_source_extension_id: null
    #       modified_date: 1654727311444
    #       name: Snort logs
    #       protocol_parameters:
    #       - id: 1
    #         name: incomingPayloadEncoding
    #         value: UTF-8
    #       - id: 0
    #         name: identifier
    #         value: 192.0.2.1
    #       protocol_type_id: 0
    #       requires_deploy: true
    #       status:
    #         last_updated: 0
    #         messages: null
    #         status: NA
    #       store_event_payload: true
    #       target_event_collector_id: 7
    #       type_id: 2
    #       wincollect_external_destination_ids: null
    #       wincollect_internal_destination_id: null
    #     - auto_discovered: false
    #       average_eps: 0
    #       coalesce_events: true
    #       creation_date: 1654727311462
    #       credibility: 5
    #       description: Apache HTTP Server remote logs from rsyslog
    #       enabled: true
    #       gateway: false
    #       group_ids:
    #       - 0
    #       id: 182
    #       internal: false
    #       language_id: 1
    #       last_event_time: 0
    #       log_source_extension_id: null
    #       modified_date: 1654727311462
    #       name: Apache HTTP Server logs
    #       protocol_parameters:
    #       - id: 1
    #         name: incomingPayloadEncoding
    #         value: UTF-8
    #       - id: 0
    #         name: identifier
    #         value: 198.51.100.1
    #       protocol_type_id: 0
    #       requires_deploy: true
    #       status:
    #         last_updated: 0
    #         messages: null
    #         status: NA
    #       store_event_payload: true
    #       target_event_collector_id: 7
    #       type_id: 10
    #       wincollect_external_destination_ids: null
    #       wincollect_internal_destination_id: null
    #     before: []

    # Using REPLACED state
    # --------------------

    - name: Replace existing Log sources to IBM QRadar
      ibm.qradar.qradar_log_sources_management:
        state: replaced
        config:
          - name: "Apache HTTP Server logs"
            type_name: "Apache HTTP Server"
            description: "REPLACED Apache HTTP Server remote logs from rsyslog"
            identifier: "192.0.2.1"

    # RUN output:
    # -----------

    #   qradar_log_sources_management:
    #     after:
    #     - auto_discovered: false
    #       average_eps: 0
    #       coalesce_events: true
    #       creation_date: 1654727944017
    #       credibility: 5
    #       description: REPLACED Apache HTTP Server remote logs from rsyslog
    #       enabled: true
    #       gateway: false
    #       group_ids:
    #       - 0
    #       id: 183
    #       internal: false
    #       language_id: 1
    #       last_event_time: 0
    #       log_source_extension_id: null
    #       modified_date: 1654727944017
    #       name: Apache HTTP Server logs
    #       protocol_parameters:
    #       - id: 1
    #         name: incomingPayloadEncoding
    #         value: UTF-8
    #       - id: 0
    #         name: identifier
    #         value: 192.0.2.1
    #       protocol_type_id: 0
    #       requires_deploy: true
    #       status:
    #         last_updated: 0
    #         messages: null
    #         status: NA
    #       store_event_payload: true
    #       target_event_collector_id: 7
    #       type_id: 10
    #       wincollect_external_destination_ids: null
    #       wincollect_internal_destination_id: null
    #     before:
    #     - auto_discovered: false
    #       average_eps: 0
    #       coalesce_events: true
    #       creation_date: 1654727311462
    #       credibility: 5
    #       description: Apache HTTP Server remote logs from rsyslog
    #       enabled: true
    #       gateway: false
    #       group_ids:
    #       - 0
    #       id: 182
    #       internal: false
    #       language_id: 1
    #       last_event_time: 0
    #       log_source_extension_id: null
    #       modified_date: 1654727311462
    #       name: Apache HTTP Server logs
    #       protocol_parameters:
    #       - name: identifier
    #         value: 198.51.100.1
    #       - name: incomingPayloadEncoding
    #         value: UTF-8
    #       protocol_type_id: 0
    #       requires_deploy: true
    #       status:
    #         last_updated: 0
    #         messages: null
    #         status: NA
    #       store_event_payload: true
    #       target_event_collector_id: 7
    #       type_id: 10
    #       wincollect_external_destination_ids: null
    #       wincollect_internal_destination_id: null

    # Using GATHERED state
    # --------------------

    - name: Gather Snort n Apache log source from IBM QRadar
      ibm.qradar.qradar_log_sources_management:
        config:
          - name: "Snort logs"
          - name: "Apache HTTP Server logs"
        state: gathered

    # RUN output:
    # -----------

    # gathered:
    #   - auto_discovered: false
    #     average_eps: 0
    #     coalesce_events: true
    #     creation_date: 1654727311444
    #     credibility: 5
    #     description: Snort IDS remote logs from rsyslog
    #     enabled: true
    #     gateway: false
    #     group_ids:
    #     - 0
    #     id: 181
    #     internal: false
    #     language_id: 1
    #     last_event_time: 0
    #     log_source_extension_id: null
    #     modified_date: 1654728103340
    #     name: Snort logs
    #     protocol_parameters:
    #     - id: 0
    #       name: identifier
    #       value: 192.0.2.1
    #     - id: 1
    #       name: incomingPayloadEncoding
    #       value: UTF-8
    #     protocol_type_id: 0
    #     requires_deploy: true
    #     status:
    #       last_updated: 0
    #       messages: null
    #       status: NA
    #     store_event_payload: true
    #     target_event_collector_id: 7
    #     type_id: 2
    #     wincollect_external_destination_ids: null
    #     wincollect_internal_destination_id: null
    #   - auto_discovered: false
    #     average_eps: 0
    #     coalesce_events: true
    #     creation_date: 1654727944017
    #     credibility: 5
    #     description: Apache HTTP Server remote logs from rsyslog
    #     enabled: true
    #     gateway: false
    #     group_ids:
    #     - 0
    #     id: 183
    #     internal: false
    #     language_id: 1
    #     last_event_time: 0
    #     log_source_extension_id: null
    #     modified_date: 1654728103353
    #     name: Apache HTTP Server logs
    #     protocol_parameters:
    #     - id: 0
    #       name: identifier
    #       value: 192.0.2.1
    #     - id: 1
    #       name: incomingPayloadEncoding
    #       value: UTF-8
    #     protocol_type_id: 0
    #     requires_deploy: true
    #     status:
    #       last_updated: 0
    #       messages: null
    #       status: NA
    #     store_event_payload: true
    #     target_event_collector_id: 7
    #     type_id: 10
    #     wincollect_external_destination_ids: null
    #     wincollect_internal_destination_id: null

    - name: TO Gather ALL log sources from IBM QRadar
      tags: gather_log_all
      ibm.qradar.qradar_log_sources_management:
        state: gathered

    # Using DELETED state
    # -------------------

    - name: Delete Snort n Apache log source from IBM QRadar
      ibm.qradar.qradar_log_sources_management:
        config:
          - name: "Snort logs"
          - name: "Apache HTTP Server logs"
        state: deleted

    # RUN output:
    # -----------

    #   qradar_log_sources_management:
    #     after: []
    #     before:
    #     - auto_discovered: false
    #       average_eps: 0
    #       coalesce_events: true
    #       creation_date: 1654727311444
    #       credibility: 5
    #       description: Snort IDS remote logs from rsyslog
    #       enabled: true
    #       gateway: false
    #       group_ids:
    #       - 0
    #       id: 181
    #       internal: false
    #       language_id: 1
    #       last_event_time: 0
    #       log_source_extension_id: null
    #       modified_date: 1654728103340
    #       name: Snort logs
    #       protocol_parameters:
    #       - id: 0
    #         name: identifier
    #         value: 192.0.2.1
    #       - id: 1
    #         name: incomingPayloadEncoding
    #         value: UTF-8
    #       protocol_type_id: 0
    #       requires_deploy: true
    #       status:
    #         last_updated: 0
    #         messages: null
    #         status: NA
    #       store_event_payload: true
    #       target_event_collector_id: 7
    #       type_id: 2
    #       wincollect_external_destination_ids: null
    #       wincollect_internal_destination_id: null
    #     - auto_discovered: false
    #       average_eps: 0
    #       coalesce_events: true
    #       creation_date: 1654727944017
    #       credibility: 5
    #       description: Apache HTTP Server remote logs from rsyslog
    #       enabled: true
    #       gateway: false
    #       group_ids:
    #       - 0
    #       id: 183
    #       internal: false
    #       language_id: 1
    #       last_event_time: 0
    #       log_source_extension_id: null
    #       modified_date: 1654728103353
    #       name: Apache HTTP Server logs
    #       protocol_parameters:
    #       - id: 0
    #         name: identifier
    #         value: 192.0.2.1
    #       - id: 1
    #         name: incomingPayloadEncoding
    #         value: UTF-8
    #       protocol_type_id: 0
    #       requires_deploy: true
    #       status:
    #         last_updated: 0
    #         messages: null
    #         status: NA
    #       store_event_payload: true
    #       target_event_collector_id: 7
    #       type_id: 10
    #       wincollect_external_destination_ids: null
    #       wincollect_internal_destination_id: null



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
                      <span style="color: purple">list</span>
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
                      <span style="color: purple">list</span>
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
