# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests tools.validators.instance_validator.instance_parser"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import instance_parser
from absl.testing import absltest

_TESTCASE_PATH = os.path.join('.', 'tests', 'fake_instances')

class ParserTest(absltest.TestCase):

  def testInstanceValidatorDetectDuplicateKeys(self):
    parse, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_duplicate_keys.yaml'))
    self.assertIsNone(parse)
    self.assertIsNotNone(err)

  def testInstanceValidatorDetectMissingColon(self):
    parse, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_missing_colon.yaml'))
    self.assertIsNone(parse)
    self.assertIsNotNone(err)

  def testInstanceValidatorDetectImproperSpacing(self):
    parse, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_spacing.yaml'))
    self.assertIsNone(parse)
    self.assertIsNotNone(err)

  def testInstanceValidatorDetectImproperTabbing(self):
    parse, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_tabbing.yaml'))
    self.assertIsNone(parse)
    self.assertIsNotNone(err)

  def testInstanceValidatorParseProperFormat(self):
    parse, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_building_type.yaml'))
    self.assertIsNone(err)
    self.assertIsNotNone(parse)

  def testInstanceValidatorParseProperConnections(self):
    parse, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_building_connections.yaml'))
    self.assertIsNone(err)
    self.assertIsNotNone(parse)

  def testInstanceValidatorDetectImproperTranslationCompliance(self):
    parse, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_translation_compliant.yaml'))
    self.assertIsNone(parse)
    self.assertIsNotNone(err)

  def testInstanceValidatorDetectImproperTranslationKeys(self):
    parse, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_translation_keys.yaml'))
    self.assertIsNone(parse)
    self.assertIsNotNone(err)

  def testInstanceValidatorDetectImproperUnitsKeys(self):
    parse, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_translation_units_format.yaml'))
    self.assertIsNone(parse)
    self.assertIsNotNone(err)

if __name__ == '__main__':
  absltest.main()
