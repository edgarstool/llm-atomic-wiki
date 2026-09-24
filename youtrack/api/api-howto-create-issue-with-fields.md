---
title: "Create an Issue and Set Custom Fields"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/api-howto-create-issue-with-fields.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Create an Issue and Set Custom Fields

Use the REST API to create a new issue and set values for one or more custom fields.

> **Tip:**
> Read the [Custom Fields in REST API](api-concept-custom-fields.html)page for more info about the custom fields in REST API.

## Summary

To create an issue with a set value for a custom field, you need to obtain the following parameters:

* The entity ID of the project to which the new issue should belong. To get the project ID, see [Get a Project ID](api-usecase-get-project-id.html).

* `name` and `$type` of the custom field that you need to set.

* `name` of the value that you set for the custom field.

## Step-by-Step

The following procedure shows how to create a new issue and set values for a couple of issue fields. For the sample, we decided to set "Priority" and "Assignee" fields.

Procedure: To create an issue and set a value for a custom field

1. Get the ID of the project where you want to create the issue. For instructions, see [Get a Project ID](api-usecase-get-project-id.html). This sample uses the project ID `0-0` and the project short name `SP`.

2. Obtain the name and `$type` of the custom field that you need to set. You can send a GET request to the `/api/issues` endpoint with query parameters:

* `fields` parameter with a list of the issue attributes to return. For our case, we are particularly interested in custom fields. So, we can use the following string: ``` fields=project(name),idReadable,customFields(name,$type,value(name,login)) ```

* To narrow the results to issues in the target project, you can use the `query` parameter. For example, `query=in:SP` narrows the results for our particular target project.

* Optionally, use the `$top` query parameter to get a limited number of issue.

Here's the resulting request:

```SHELL
curl -X GET \
  'https://example.youtrack.cloud/api/issues?fields=idReadable,id,project(id,name),summary,description,customFields(name,$type,value(name,login))&query=in:SP&$top=1' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YouTrack_token>' \
```

In response, server returned the following data:

```JSON
[
    {
        "idReadable": "SP-47",
        "project": {
            "name": "Sample Project",
            "id": "0-0",
            "$type": "Project"
        },
        "customFields": [
            {
                "value": {
                    "name": "Show-stopper",
                    "$type": "EnumBundleElement"
                },
                "name": "Priority",
                "$type": "SingleEnumIssueCustomField"
            },
            {
                "value": {
                    "name": "Task",
                    "$type": "EnumBundleElement"
                },
                "name": "Type",
                "$type": "SingleEnumIssueCustomField"
            },
            {
                "value": {
                    "name": "Open",
                    "$type": "StateBundleElement"
                },
                "name": "State",
                "$type": "StateIssueCustomField"
            },
            {
                "value": {
                    "login": "jane.doe",
                    "name": "Jane Doe",
                    "$type": "User"
                },
                "name": "Assignee",
                "$type": "SingleUserIssueCustomField"
            },
            {
                "value": null,
                "name": "Subsystem",
                "$type": "SingleOwnedIssueCustomField"
            },
            {
                "value": [],
                "name": "Fix versions",
                "$type": "MultiVersionIssueCustomField"
            },
            {
                "value": [],
                "name": "Affected versions",
                "$type": "MultiVersionIssueCustomField"
            },
            {
                "value": null,
                "name": "Fixed in build",
                "$type": "SingleBuildIssueCustomField"
            }
        ],
        "$type": "Issue"
    }
]
```

From this response you can see the list of available fields and their types. You can also get the complete list of the available types for the issue custom fields on the [page](api-concept-custom-fields.html#type-issue-custom-fields).

3. Obtain the name of the value that you want to set for the target custom field. In general, it's enough to just know the name of the value - the way they are presented in the UI. For example, Show-stopper or Major for the Priority field, or In progress or Fixed for the State field. However, for some fields, like Fix version or Assignee, the list of available values might not be obvious. In this case, you need to get the set of values (bundle) that is used for this particular field in the target project.

4. To create a new issue, assign it to a specific user, and set its "Priority" field to `Show-stopper`, send a `POST` request with the body that contains ID of the project, summary of the new issue, and a json object for the `customFields` attribute that contains:

* The `name`, `$type`, and `value` of the Priority field.

* The `name`, `$type`, and `value` of the Assignee field.

Though the `description` attribute is not mandatory, we opted to specify it as well. Here's the resulting request:

```CURL
curl -X POST \
https://example.youtrack.cloud/api/issues \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <YouTrack_token>' \
-H 'Content-Type: application/json' \
-d '{
"project":{"id":"0-0"},
"summary":"REST API lets you create issues!",
"description":"Let'\''s create a new issue using YouTrack'\''s REST API.",
"customFields":[
{ "name":"Priority","$type":"SingleEnumIssueCustomField","value":{"name":"Show-stopper"}},
{ "name": "Assignee","$type": "SingleUserIssueCustomField","value": {"login":"jane.doe"}}
]
}'
```

In the response, the server returns only the entity id of the created issue and its $type, because we did not specify any `fields` parameters in the request:

```JSON
{
    "id": "2-38",
    "$type": "Issue"
}
```

> **Note:**
> Please note that you cannot simultaneously create a new issue and add attachments to it. You can attach files only to an already existing issue.



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/api-howto-create-issue-with-fields.html](https://www.jetbrains.com/help/youtrack/devportal/api-howto-create-issue-with-fields.html) · fetched 2026-09-22 08:34 Asia/Taipei*
