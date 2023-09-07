Log Analytics is a service that helps you collect and analyze data generated by resources in your cloud and on-premises environments.

Full documentation for this integration is available in the [reference docs](https://xsoar.pan.dev/docs/reference/integrations/azure-log-analytics).


## Authorize Cortex XSOAR for Azure Log Analytics

You need to grant Cortex XSOAR authorization to access Azure Log Analytics.

1. Access the [authorization flow](https://oproxy.demisto.ninja/ms-azure-log-analytics). 
2. Click the **Start Authorization Process** button. 
   You will be prompted to grant Cortex XSOAR permissions for your Azure Service Management. 
3. Click the **Accept** button. 
   You will receive your ID, token, and key. You need to enter this information, when you configure the Azure Log Analytics integration instance in Cortex XSOAR.

## Authorize Cortex XSOAR for Azure Log Analytics (Self-Deployed Configuration)
To use a self-configured Azure application, you need to add a new Azure App Registration in the Azure Portal. To add the registration, go to the [Microsoft article](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app).

### Required permissions
- Azure Service Management - permission `user_impersonation` of type `Delegated`
- Log Analytics API - permission `Data.Read` of type `Delegated`

In the self-deployed mode, you can authenticate by using one of the following flows:
- Authentication code flow
- Client Credentials flow

### Authentication Code flow

---
1. Enter your client ID in the **ID** parameter. 
2. Enter your client secret in the **password** parameter.
3. Enter your tenant ID in the **Token** parameter.
4. Enter your redirect URI in the **Redirect URI** parameter.
5. Save the integration settings.
6. Run the `!azure-log-analytics-generate-login-url` command in the War Room and follow the instruction.


### Authorize Cortex XSOAR for Azure Log Analytics (Client-Credentials Configuration)

---
Follow these steps for client-credentials configuration.

1. In the instance configuration, select the **client-credentials** checkbox.
2. Enter your Client ID in the **ID/Client ID** parameter. 
3. Enter your Client Secret in the **password** parameter.
4. Enter your Tenant ID in the **Tenant ID** parameter.
5. Run the ***azure-log-analytics-test*** command to test the connection and the authorization process.

### Azure Managed Identities Authentication
##### Note: This option is relevant only if the integration is running on Azure VM.
Follow one of these steps for authentication based on Azure Managed Identities:

- ##### To use System Assigned Managed Identity
   - Select the **Use Azure Managed Identities** checkbox and leave the **Azure Managed Identities Client ID** field empty.

- ##### To use User Assigned Managed Identity
   1. Go to [Azure Portal](https://portal.azure.com/) -> **Managed Identities**
   2. Select your User Assigned Managed Identity -> copy the Client ID -> paste it in the **Azure Managed Identities Client ID** field in the instance settings.
   3. Select the **Use Azure Managed Identities** checkbox.

For more information, see [Managed identities for Azure resources](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview).
## Get the Additional Instance Parameters

To get the **Subscription ID**, **Workspace Name**, **Workspace ID** and **Resource Group** parameters, in the Azure Portal, go to **Log Analytics workspaces > YOUR-WORKSPACE > Settings** and click the **Workspace Settings** tab.