# swagger-client
These APIs provide services for manipulating Harbor project.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ArtifactApi(swagger_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
label = swagger_client.Label() # Label | The label that added to the artifact. Only the ID property is needed.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Add label to artifact
    api_instance.add_label(project_name, repository_name, reference, label, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ArtifactApi->add_label: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/api/v2.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ArtifactApi* | [**add_label**](docs/ArtifactApi.md#add_label) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/labels | Add label to artifact
*ArtifactApi* | [**copy_artifact**](docs/ArtifactApi.md#copy_artifact) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts | Copy artifact
*ArtifactApi* | [**create_tag**](docs/ArtifactApi.md#create_tag) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags | Create tag
*ArtifactApi* | [**delete_artifact**](docs/ArtifactApi.md#delete_artifact) | **DELETE** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference} | Delete the specific artifact
*ArtifactApi* | [**delete_tag**](docs/ArtifactApi.md#delete_tag) | **DELETE** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags/{tag_name} | Delete tag
*ArtifactApi* | [**get_addition**](docs/ArtifactApi.md#get_addition) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/additions/{addition} | Get the addition of the specific artifact
*ArtifactApi* | [**get_artifact**](docs/ArtifactApi.md#get_artifact) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference} | Get the specific artifact
*ArtifactApi* | [**list_artifacts**](docs/ArtifactApi.md#list_artifacts) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts | List artifacts
*ArtifactApi* | [**list_tags**](docs/ArtifactApi.md#list_tags) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags | List tags
*ArtifactApi* | [**remove_label**](docs/ArtifactApi.md#remove_label) | **DELETE** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/labels/{label_id} | Remove label from artifact
*AuditlogApi* | [**list_audit_logs**](docs/AuditlogApi.md#list_audit_logs) | **GET** /audit-logs | Get recent logs of the projects which the user is a member of
*GcApi* | [**create_gc_schedule**](docs/GcApi.md#create_gc_schedule) | **POST** /system/gc/schedule | Create a gc schedule.
*GcApi* | [**get_gc**](docs/GcApi.md#get_gc) | **GET** /system/gc/{gc_id} | Get gc status.
*GcApi* | [**get_gc_history**](docs/GcApi.md#get_gc_history) | **GET** /system/gc | Get gc results.
*GcApi* | [**get_gc_log**](docs/GcApi.md#get_gc_log) | **GET** /system/gc/{gc_id}/log | Get gc job log.
*GcApi* | [**get_gc_schedule**](docs/GcApi.md#get_gc_schedule) | **GET** /system/gc/schedule | Get gc&#39;s schedule.
*GcApi* | [**update_gc_schedule**](docs/GcApi.md#update_gc_schedule) | **PUT** /system/gc/schedule | Update gc&#39;s schedule.
*IconApi* | [**get_icon**](docs/IconApi.md#get_icon) | **GET** /icons/{digest} | Get artifact icon
*PingApi* | [**ping_get**](docs/PingApi.md#ping_get) | **GET** /ping | Ping Harbor to check if it&#39;s alive.
*PreheatApi* | [**create_instance**](docs/PreheatApi.md#create_instance) | **POST** /p2p/preheat/instances | Create p2p provider instances
*PreheatApi* | [**create_policy**](docs/PreheatApi.md#create_policy) | **POST** /projects/{project_name}/preheat/policies | Create a preheat policy under a project
*PreheatApi* | [**delete_instance**](docs/PreheatApi.md#delete_instance) | **DELETE** /p2p/preheat/instances/{preheat_instance_name} | Delete the specified P2P provider instance
*PreheatApi* | [**delete_policy**](docs/PreheatApi.md#delete_policy) | **DELETE** /projects/{project_name}/preheat/policies/{preheat_policy_name} | Delete a preheat policy
*PreheatApi* | [**get_execution**](docs/PreheatApi.md#get_execution) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions/{execution_id} | Get a execution detail by id
*PreheatApi* | [**get_instance**](docs/PreheatApi.md#get_instance) | **GET** /p2p/preheat/instances/{preheat_instance_name} | Get a P2P provider instance
*PreheatApi* | [**get_policy**](docs/PreheatApi.md#get_policy) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name} | Get a preheat policy
*PreheatApi* | [**get_preheat_log**](docs/PreheatApi.md#get_preheat_log) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions/{execution_id}/tasks/{task_id}/logs | Get the log text stream of the specified task for the given execution
*PreheatApi* | [**list_executions**](docs/PreheatApi.md#list_executions) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions | List executions for the given policy
*PreheatApi* | [**list_instances**](docs/PreheatApi.md#list_instances) | **GET** /p2p/preheat/instances | List P2P provider instances
*PreheatApi* | [**list_policies**](docs/PreheatApi.md#list_policies) | **GET** /projects/{project_name}/preheat/policies | List preheat policies
*PreheatApi* | [**list_providers**](docs/PreheatApi.md#list_providers) | **GET** /p2p/preheat/providers | List P2P providers
*PreheatApi* | [**list_providers_under_project**](docs/PreheatApi.md#list_providers_under_project) | **GET** /projects/{project_name}/preheat/providers | Get all providers at project level
*PreheatApi* | [**list_tasks**](docs/PreheatApi.md#list_tasks) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions/{execution_id}/tasks | List all the related tasks for the given execution
*PreheatApi* | [**manual_preheat**](docs/PreheatApi.md#manual_preheat) | **POST** /projects/{project_name}/preheat/policies/{preheat_policy_name} | Manual preheat
*PreheatApi* | [**ping_instances**](docs/PreheatApi.md#ping_instances) | **POST** /p2p/preheat/instances/ping | Ping status of a instance.
*PreheatApi* | [**stop_execution**](docs/PreheatApi.md#stop_execution) | **PATCH** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions/{execution_id} | Stop a execution
*PreheatApi* | [**update_instance**](docs/PreheatApi.md#update_instance) | **PUT** /p2p/preheat/instances/{preheat_instance_name} | Update the specified P2P provider instance
*PreheatApi* | [**update_policy**](docs/PreheatApi.md#update_policy) | **PUT** /projects/{project_name}/preheat/policies/{preheat_policy_name} | Update preheat policy
*ProjectApi* | [**create_project**](docs/ProjectApi.md#create_project) | **POST** /projects | Create a new project.
*ProjectApi* | [**delete_project**](docs/ProjectApi.md#delete_project) | **DELETE** /projects/{project_name_or_id} | Delete project by projectID
*ProjectApi* | [**get_logs**](docs/ProjectApi.md#get_logs) | **GET** /projects/{project_name}/logs | Get recent logs of the projects
*ProjectApi* | [**get_project**](docs/ProjectApi.md#get_project) | **GET** /projects/{project_name_or_id} | Return specific project detail information
*ProjectApi* | [**get_project_deletable**](docs/ProjectApi.md#get_project_deletable) | **GET** /projects/{project_name_or_id}/_deletable | Get the deletable status of the project
*ProjectApi* | [**get_project_summary**](docs/ProjectApi.md#get_project_summary) | **GET** /projects/{project_name_or_id}/summary | Get summary of the project.
*ProjectApi* | [**head_project**](docs/ProjectApi.md#head_project) | **HEAD** /projects | Check if the project name user provided already exists.
*ProjectApi* | [**list_projects**](docs/ProjectApi.md#list_projects) | **GET** /projects | List projects
*ProjectApi* | [**update_project**](docs/ProjectApi.md#update_project) | **PUT** /projects/{project_name_or_id} | Update properties for a selected project.
*ReplicationApi* | [**get_replication_execution**](docs/ReplicationApi.md#get_replication_execution) | **GET** /replication/executions/{id} | Get the specific replication execution
*ReplicationApi* | [**get_replication_log**](docs/ReplicationApi.md#get_replication_log) | **GET** /replication/executions/{id}/tasks/{task_id}/log | Get the log of the specific replication task
*ReplicationApi* | [**list_replication_executions**](docs/ReplicationApi.md#list_replication_executions) | **GET** /replication/executions | List replication executions
*ReplicationApi* | [**list_replication_tasks**](docs/ReplicationApi.md#list_replication_tasks) | **GET** /replication/executions/{id}/tasks | List replication tasks for a specific execution
*ReplicationApi* | [**start_replication**](docs/ReplicationApi.md#start_replication) | **POST** /replication/executions | Start one replication execution
*ReplicationApi* | [**stop_replication**](docs/ReplicationApi.md#stop_replication) | **PUT** /replication/executions/{id} | Stop the specific replication execution
*RepositoryApi* | [**delete_repository**](docs/RepositoryApi.md#delete_repository) | **DELETE** /projects/{project_name}/repositories/{repository_name} | Delete repository
*RepositoryApi* | [**get_repository**](docs/RepositoryApi.md#get_repository) | **GET** /projects/{project_name}/repositories/{repository_name} | Get repository
*RepositoryApi* | [**list_repositories**](docs/RepositoryApi.md#list_repositories) | **GET** /projects/{project_name}/repositories | List repositories
*RepositoryApi* | [**update_repository**](docs/RepositoryApi.md#update_repository) | **PUT** /projects/{project_name}/repositories/{repository_name} | Update repository
*RobotApi* | [**create_robot**](docs/RobotApi.md#create_robot) | **POST** /robots | Create a robot account
*RobotApi* | [**delete_robot**](docs/RobotApi.md#delete_robot) | **DELETE** /robots/{robot_id} | Delete a robot account
*RobotApi* | [**get_robot_by_id**](docs/RobotApi.md#get_robot_by_id) | **GET** /robots/{robot_id} | Get a robot account
*RobotApi* | [**list_robot**](docs/RobotApi.md#list_robot) | **GET** /robots | Get robot account
*RobotApi* | [**refresh_sec**](docs/RobotApi.md#refresh_sec) | **PATCH** /robots/{robot_id} | Refresh the robot secret
*RobotApi* | [**update_robot**](docs/RobotApi.md#update_robot) | **PUT** /robots/{robot_id} | Update a robot account
*Robotv1Api* | [**create_robot_v1**](docs/Robotv1Api.md#create_robot_v1) | **POST** /projects/{project_name_or_id}/robots | Create a robot account
*Robotv1Api* | [**delete_robot_v1**](docs/Robotv1Api.md#delete_robot_v1) | **DELETE** /projects/{project_name_or_id}/robots/{robot_id} | Delete a robot account
*Robotv1Api* | [**get_robot_by_idv1**](docs/Robotv1Api.md#get_robot_by_idv1) | **GET** /projects/{project_name_or_id}/robots/{robot_id} | Get a robot account
*Robotv1Api* | [**list_robot_v1**](docs/Robotv1Api.md#list_robot_v1) | **GET** /projects/{project_name_or_id}/robots | Get all robot accounts of specified project
*Robotv1Api* | [**update_robot_v1**](docs/Robotv1Api.md#update_robot_v1) | **PUT** /projects/{project_name_or_id}/robots/{robot_id} | Update status of robot account.
*ScanApi* | [**get_report_log**](docs/ScanApi.md#get_report_log) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/scan/{report_id}/log | Get the log of the scan report
*ScanApi* | [**scan_artifact**](docs/ScanApi.md#scan_artifact) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/scan | Scan the artifact
*SysteminfoApi* | [**systeminfo_get**](docs/SysteminfoApi.md#systeminfo_get) | **GET** /systeminfo | Get general system info
*SysteminfoApi* | [**systeminfo_getcert_get**](docs/SysteminfoApi.md#systeminfo_getcert_get) | **GET** /systeminfo/getcert | Get default root certificate.
*SysteminfoApi* | [**systeminfo_volumes_get**](docs/SysteminfoApi.md#systeminfo_volumes_get) | **GET** /systeminfo/volumes | Get system volume info (total/free size).


## Documentation For Models

 - [Access](docs/Access.md)
 - [AdditionLink](docs/AdditionLink.md)
 - [AdditionLinks](docs/AdditionLinks.md)
 - [Annotations](docs/Annotations.md)
 - [Artifact](docs/Artifact.md)
 - [AuditLog](docs/AuditLog.md)
 - [AuthproxySetting](docs/AuthproxySetting.md)
 - [CVEAllowlist](docs/CVEAllowlist.md)
 - [CVEAllowlistItem](docs/CVEAllowlistItem.md)
 - [Error](docs/Error.md)
 - [Errors](docs/Errors.md)
 - [Execution](docs/Execution.md)
 - [ExtraAttrs](docs/ExtraAttrs.md)
 - [GCHistory](docs/GCHistory.md)
 - [GeneralInfo](docs/GeneralInfo.md)
 - [Icon](docs/Icon.md)
 - [Instance](docs/Instance.md)
 - [Label](docs/Label.md)
 - [Metadata](docs/Metadata.md)
 - [Metrics](docs/Metrics.md)
 - [NativeReportSummary](docs/NativeReportSummary.md)
 - [Permission](docs/Permission.md)
 - [Platform](docs/Platform.md)
 - [PreheatPolicy](docs/PreheatPolicy.md)
 - [Project](docs/Project.md)
 - [ProjectDeletable](docs/ProjectDeletable.md)
 - [ProjectMetadata](docs/ProjectMetadata.md)
 - [ProjectReq](docs/ProjectReq.md)
 - [ProjectSummary](docs/ProjectSummary.md)
 - [ProjectSummaryQuota](docs/ProjectSummaryQuota.md)
 - [ProviderUnderProject](docs/ProviderUnderProject.md)
 - [Reference](docs/Reference.md)
 - [Registry](docs/Registry.md)
 - [RegistryCredential](docs/RegistryCredential.md)
 - [ReplicationExecution](docs/ReplicationExecution.md)
 - [ReplicationTask](docs/ReplicationTask.md)
 - [Repository](docs/Repository.md)
 - [ResourceList](docs/ResourceList.md)
 - [Robot](docs/Robot.md)
 - [RobotCreate](docs/RobotCreate.md)
 - [RobotCreateV1](docs/RobotCreateV1.md)
 - [RobotCreated](docs/RobotCreated.md)
 - [RobotSec](docs/RobotSec.md)
 - [ScanOverview](docs/ScanOverview.md)
 - [Schedule](docs/Schedule.md)
 - [ScheduleObj](docs/ScheduleObj.md)
 - [StartReplicationExecution](docs/StartReplicationExecution.md)
 - [Storage](docs/Storage.md)
 - [SystemInfo](docs/SystemInfo.md)
 - [Tag](docs/Tag.md)
 - [Task](docs/Task.md)
 - [VulnerabilitySummary](docs/VulnerabilitySummary.md)


## Documentation For Authorization


## basic

- **Type**: HTTP basic authentication


## Author



