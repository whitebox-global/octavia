#    Copyright 2014 Hewlett-Packard Development Company, L.P.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import uuid

from octavia.amphorae.backends.health_daemon import status_message
from octavia.tests.unit import base


class TestEnvelope(base.TestCase):
    def setUp(self):
        super(TestEnvelope, self).setUp()

    def test_message_hmac(self):
        self.skipTest("This test is broken and will be fixed in CR# 201882")
        statusMsg = {'seq': 42,
                     'status': 'OK',
                     'id': str(uuid.uuid4())}
        sme = status_message.encode(statusMsg, 'samplekey1')

        self.assertTrue(status_message.checkhmac(sme, 'samplekey1'))
        self.assertFalse(status_message.checkhmac(sme, 'samplekey2'))
