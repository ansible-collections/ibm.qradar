# Copyright (c) 2022 Red Hat
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

import tempfile
import unittest

from unittest.mock import MagicMock, patch

from ansible.playbook.task import Task
from ansible.template import Templar

from ansible_collections.ibm.qradar.plugins.action.qradar_analytics_rules import ActionModule


RESPONSE_PAYLOAD = {
    "average_capacity": "null",
    "base_capacity": "null",
    "base_host_id": "null",
    "capacity_timestamp": "null",
    "creation_date": "1658929682568",
    "enabled": False,
    "id": "100443",
    "identifier": "ae5a1268-02a0-4976-84c5-dbcbcf854b9c",
    "linked_rule_identifier": "null",
    "modification_date": "1658929682567",
    "name": "Ansible Example DDOS Rule",
    "origin": "USER",
    "owner": "admin",
    "type": "EVENT",
}

REQUEST_PAYLOAD = {
    "name": "Ansible Example DDOS Rule",
    "enabled": True,
}


class TestQradarAnalyticsRules(unittest.TestCase):
    def setUp(self):
        task = MagicMock(Task)
        # Ansible > 2.13 looks for check_mode in task
        task.check_mode = False
        play_context = MagicMock()
        # Ansible <= 2.13 looks for check_mode in play_context
        play_context.check_mode = False
        connection = patch(
            "ansible_collections.ibm.qradar.plugins.action.qradar_analytics_rules.Connection",
        )
        fake_loader = {}
        templar = Templar(loader=fake_loader)
        self._plugin = ActionModule(
            task=task,
            connection=connection,
            play_context=play_context,
            loader=fake_loader,
            templar=templar,
            shared_loader_obj=None,
        )
        self._plugin._task.action = "qradar_analytics_rules"
        self._task_vars = {}

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_qradar_analytics_rules_merged(self, connection):
        self._plugin.search_for_resource = MagicMock()
        self._plugin.search_for_resource.return_value = RESPONSE_PAYLOAD
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin._task.args = {
            "state": "merged",
            "config": REQUEST_PAYLOAD,
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["changed"])

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_qradar_analytics_rules_merged_idempotent(self, connection):
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin.search_for_resource = MagicMock()
        self._plugin.search_for_resource.return_value = RESPONSE_PAYLOAD
        self._plugin.api_return = "qradar_analytics_rules"
        self._plugin._task.args = {
            "state": "merged",
            "config": {
                "enabled": False,
                "name": "Ansible Example DDOS Rule",
            },
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertFalse(result["changed"])

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_qradar_analytics_rules_deleted(self, connection):
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin.search_for_resource = MagicMock()
        self._plugin.search_for_resource.return_value = RESPONSE_PAYLOAD
        self._plugin.api_return = "qradar_analytics_rules"
        self._plugin._task.args = {
            "state": "deleted",
            "config": {
                "name": "Ansible Example DDOS Rule",
            },
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["changed"])

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_qradar_analytics_rules_deleted_idempotent(self, connection):
        self._plugin.search_for_resource = MagicMock()
        self._plugin.search_for_resource.return_value = {}
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin._task.args = {
            "state": "deleted",
            "config": {
                "name": "Ansible Example DDOS Rule",
            },
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertFalse(result["changed"])

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_qradar_analytics_rules_gathered(self, connection):
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin.search_for_resource = MagicMock()
        self._plugin.search_for_resource.return_value = RESPONSE_PAYLOAD
        self._plugin.api_return = "qradar_analytics_rules"
        self._plugin._task.args = {
            "state": "gathered",
            "config": {"name": "Ansible Example DDOS Rule"},
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertEqual(result["gathered"], RESPONSE_PAYLOAD)
