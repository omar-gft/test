Enrichment of Domain IOC types - sub-playbook for IOC Assessment & Enrichment playbook

## Dependencies
This playbook uses the following sub-playbooks, integrations, and scripts.

### Sub-playbooks
This playbook does not use any sub-playbooks.

### Integrations
* Digital Shadows

### Scripts
* Print
* AddEvidence

### Commands
* ds-search

## Playbook Inputs
---

| **Name** | **Description** | **Default Value** | **Required** |
| --- | --- | --- | --- |
| IoC_Domain | A Digital Shadows ShadowSearch query containing domains | Domain.Name | Optional |

## Playbook Outputs
---

| **Path** | **Description** | **Type** |
| --- | --- | --- |
| DBotScore.Indicator | Indicator Value | string |
| DBotScore.Type | Indicator Type | string |