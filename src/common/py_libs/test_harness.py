# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Cortex Test Harness functions."""

from google.cloud import bigquery

from common.py_libs import bq_helper


TEST_HARNESS_VERSION="5_0"


def get_test_harness_dataset(workload_path: str,
                            target_dataset_type: str,
                            location: str) -> str:

    """Generates test harness dataset name.

    Args:
        workload_path (str): workload path, such as "SAP", "SFDC",
                             "marketing.GoogleAds", "marketing.CM360" or "k9",
                             case-insensitive.
        target_dataset_type (str): dataset type as normally used in config.json,
                            such as "rawECC", "raw", "cdcS4", "cdc",
                            "processing", etc., case-insensitive.
        location (str): BigQuery location.

    Returns:
        str: Dataset name.
    """

    # Dataset name will be lower-case, letters, numbers and underscores.
    workload_prefix = workload_path.replace(".", "__")
    location = location.replace("-", "_")
    dataset_name = (f"{workload_prefix}__{target_dataset_type}__"
                    f"{TEST_HARNESS_VERSION}__{location}")

    return dataset_name.lower()


def load_dataset_test_data(bq_client: bigquery.Client,
                           test_harness_project_id: str,
                           workload_path: str,
                           target_dataset_type: str,
                           target_dataset_name: str,
                           target_project: str,
                           location: str):
    """Loads workload dataset test data by copying dataset from
       the test harness.

    Args:
        bq_client (bigquery.Client): BigQuery client.
        test_harness_project_id (str): Test harness source project id.
        workload_path (str): workload path, such as "SAP", "SFDC",
                             "marketing.GoogleAds", "marketing.CM360" or "k9",
                             case-insensitive.
        target_dataset_type (str): dataset type as normally used in config.json,
                                   such as "rawECC", "raw", "cdcS4", "cdc",
                                   "processing", etc., case-insensitive.
        target_dataset_name (str): Target dataset name.
        target_project (str): Test data destination project (not to confuse with
                              target project from config.json).
        location (str): BigQuery location.
    """
    bq_helper.copy_dataset(bq_client,
                           test_harness_project_id,
                           get_test_harness_dataset(workload_path,
                                                     target_dataset_type,
                                                     location),
                           target_project,
                           target_dataset_name,
                           location)
