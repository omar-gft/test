Find Public Cloud resources by FQDN using Prisma Cloud inventory
Supported Cortex XSOAR versions: 6.0.0 and later.


## Dependencies
This playbook uses the following sub-playbooks, integrations, and scripts.

### Sub-playbooks
* Prisma Cloud - Find Azure Resource by FQDN v2
* Prisma Cloud - Find GCP Resource by FQDN v2
* Prisma Cloud - Find AWS Resource by FQDN v2

### Integrations
This playbook does not use any integrations.

### Scripts
This playbook does not use any scripts.

### Commands
This playbook does not use any commands.

## Playbook Inputs
---

| **Name** | **Description** | **Default Value** | **Required** |
| --- | --- | --- | --- |
| FQDN | FQDN to look up |  | Required |
| CloudProvider | Public Cloud Provider \(AWS, Azure, GCP\) |  | Optional |

## Playbook Outputs
---

| **Path** | **Description** | **Type** |
| --- | --- | --- |
| PrismaCloud.Attribution | Prisma Cloud attributed asset information. | unknown |

## Playbook Image
---
![Prisma Cloud - Find Public Cloud Resource by FQDN](https://raw.githubusercontent.com/demisto/content/852016ad0103ba42e8b5c8f596246fd14a4e7a90/Packs/PrismaCloud/doc_files/Prisma_Cloud_-_Find_Public_Cloud_Resource_by_FQDN.png)