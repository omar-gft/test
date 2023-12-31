This playbook remediates Prisma Cloud AWS EC2 alerts.  It calls the following sub-playbooks to perform the remediation:
- AWS Default Security Group Does Not Restrict All Traffic
- AWS Security Groups Allow Internet Traffic
- AWS Security Groups With Inbound Rule Overly Permissive To All Traffic
- AWS Security Groups allow internet traffic from internet to FTP-Data port (20)
- AWS Security Groups allow internet traffic from internet to FTP port (21)
- AWS Security Groups allow internet traffic to SSH port (22)
- AWS Security Group allows all traffic on SSH port (22)
- AWS Security Groups allow internet traffic from internet to Telnet port (23)
- AWS Security Groups allow internet traffic from internet to SMTP port (25)
- AWS Security Groups allow internet traffic from internet to DNS port (53)
- AWS Security Groups allow internet traffic from internet to Windows RPC port (135)
- AWS Security Groups allow internet traffic from internet to NetBIOS port (137)
- AWS Security Groups allow internet traffic from internet to NetBIOS port (138)
- AWS Security Groups allow internet traffic from internet to CIFS port (445)
- AWS Security Groups allow internet traffic from internet to SQLServer port (1433)
- AWS Security Groups allow internet traffic from internet to SQLServer port (1434)
- AWS Security Groups allow internet traffic from internet to MYSQL port (3306)
- AWS Security Groups allow internet traffic from internet to RDP port (3389)
- AWS Security Groups allow internet traffic from internet to MSQL port (4333)
- AWS Security Groups allow internet traffic from internet to PostgreSQL port (5432)
- AWS Security Groups allow internet traffic from internet to VNC Listener port (5500)
- AWS Security Groups allow internet traffic from internet to VNC Server port (5900)


## Dependencies

This playbook uses the following sub-playbooks, integrations, and scripts.

### Sub-playbooks

* Prisma Cloud Remediation - AWS Security Groups Allows Internet Traffic To TCP Port
* Prisma Cloud Remediation - AWS EC2 Security Group Misconfiguration

### Integrations
* Builtin
* PrismaCloud v2

### Scripts

IsIntegrationAvailable

### Commands
* closeInvestigation
* prisma-cloud-alert-dismiss

## Playbook Inputs

---

| **Name** | **Description** | **Default Value** | **Required** |
| --- | --- | --- | --- |
| AutoUpdateEC2 | Update AWS EC2 instance automatically? | no | Optional |
| policyId | Get the Prisma Cloud policy ID. | incident.labels.policy | Optional |

## Playbook Outputs

---
There are no outputs for this playbook.

## Playbook Image

---

![Prisma Cloud Remediation - AWS EC2 Instance Misconfiguration v2](../doc_files/Prisma_Cloud_Remediation_-_AWS_EC2_Instance_Misconfiguration_v2.png)
