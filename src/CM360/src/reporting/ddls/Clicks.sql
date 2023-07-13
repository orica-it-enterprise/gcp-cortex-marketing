#-- Copyright 2023 Google LLC
#--
#-- Licensed under the Apache License, Version 2.0 (the "License");
#-- you may not use this file except in compliance with the License.
#-- You may obtain a copy of the License at
#--
#--     https://www.apache.org/licenses/LICENSE-2.0
#--
#-- Unless required by applicable law or agreed to in writing, software
#-- distributed under the License is distributed on an "AS IS" BASIS,
#-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#-- See the License for the specific language governing permissions and
#-- limitations under the License.

/* This is reporting level base view.
*
* This view is representing a table from CDC layer in reporting.
*/

SELECT
  account_id,
  advertiser_id,
  campaign_id,
  ad_id,
  impression_id,
  event_time,
  * EXCEPT (account_id, advertiser_id, campaign_id, ad_id, impression_id, event_time) -- noqa: L034
FROM `{{ project_id_src }}.{{ marketing_cm360_datasets_cdc }}.click`
