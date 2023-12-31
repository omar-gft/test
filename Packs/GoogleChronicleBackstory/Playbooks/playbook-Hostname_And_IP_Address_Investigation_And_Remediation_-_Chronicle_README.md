This playbook receives ChronicleAsset type of indicators from its parent playbook "ChronicleAsset Investigation - Chronicle", performs enrichment and investigation for each one of them, provides an opportunity to isolate and block the hostname or IP address associated with the current indicator, and provides a list of isolated and blocked entities.

## Dependencies
This playbook uses the following sub-playbooks, integrations, and scripts.

### Sub-playbooks
* IP Enrichment - Generic v2
* Isolate Endpoint - Generic
* Block IP - Generic v2
* Isolate Endpoint - Generic V2
* Endpoint Enrichment - Generic v2.1

### Integrations
* GoogleChronicleBackstory

### Scripts
* DeleteContext
* Set

### Commands
* df-get-asset
* setIndicator
* ip

## Playbook Inputs
---

| **Name** | **Description** | **Default Value** | **Required** |
| --- | --- | --- | --- |
| chronicleasset_value | The value of the ChronicleAsset indicator. |  | Required |
| chronicleasset_hostname | The hostname associated with the ChronicleAsset. |  | Optional |
| chronicleasset_ip | The IP address associated with the ChronicleAsset. |  | Optional |
| chronicleasset_support_contact | The support email address for the ChronicleAsset. | incident.chronicleassetsupportcontact | Optional |
| auto_block_entities | Autoblock the detected suspicious IP Address\(es\). You can manually set this as "Yes" or "No" here or you can set it in a 'Chronicle Auto Block Entities' custom incident field. | incident.chronicleautoblockentities | Optional |
| skip_entity_isolation | Skip the isolation of entities. You can manually set this as "Yes" or "No" here or you can set it in a 'Chronicle Skip Entity Isolation' custom incident field. | incident.chronicleskipentityisolation | Optional |

## Playbook Outputs
---

| **Path** | **Description** | **Type** |
| --- | --- | --- |
| IsolatedEntities | List of the isolated entities. | unknown |
| PotentiallyBlockedIPs | List of potentially blocked IP Addresses. | unknown |

## Playbook Image
---
![Hostname And IP Address Investigation And Remediation - Chronicle](../doc_files/Hostname_And_IP_Address_Investigation_And_Remediation_-_Chronicle.png)