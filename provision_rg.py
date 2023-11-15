# Import the needed credential and management objects from the libraries.

import os

from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

# Acquire a credential object using CLI-based authentication.
credential = AzureCliCredential()

# Retrieve subscription ID from environment variable.
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential, subscription_id)

# Provision the resource group.
rg_result = resource_client.resource_groups.create_or_update(
    "PythonAzureExample-rg", {"location": "west us 2"}
)

# Within the ResourceManagementClient is an object named resource_groups,
# which is of class ResourceGroupsOperations, which contains methods like
# create_or_update.
#
# The second parameter to create_or_update here is technically a ResourceGroup
# object. You can create the object directly using ResourceGroup(location=
# LOCATION) or you can express the object as inline JSON as shown here. For
# details, see Inline JSON pattern for object arguments at
# https://learn.microsoft.com/azure/developer/python/sdk
# /azure-sdk-library-usage-patterns#inline-json-pattern-for-object-arguments

print(
    f"Provisioned resource group {rg_result.name} in \
        the {rg_result.location} region"
)

# The return value is another ResourceGroup object with all the details of the
# new group. In this case the call is synchronous: the resource group has been
# provisioned by the time the call returns.

# To update the resource group, repeat the call with different properties, such
# as tags:
rg_result = resource_client.resource_groups.create_or_update(
    "PythonAzureExample-rg",
    {
        "location": "west us 2",
        "tags": {"environment": "test", "department": "tech"},
    },
)

print(f"Updated resource group {rg_result.name} with tags")
