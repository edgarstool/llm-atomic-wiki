---
title: "Update Issue Custom Fields"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/api-how-to-update-custom-fields-values.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Update Issue Custom Fields

Use the REST API to update values of issue custom fields.

## Summary

To update a value of an issue custom field:

1. Use Update Issue request:

```CURL
POST /api/issues/{issueID}?[fields]
```

2.  In the `fields` request parameter specify fields you want to get in response. For example, field id and full value info. This will help you to confirm that your changes are applied.

3.  In the request body specify the `id` or `name`, `$type` and value json for each issue custom field that you need to update.

## Step-by-Step

Procedure:

1. To update issue custom fields, send a `POST` request to the target issue. You can use either issue id or issues's entity id to reference issue.

```CURL
POST /api/issues/{issueID}?[fields]
```

2. In the `fields` request parameter specify the attributes of the returned entity that you want to get in response. For example, `id`, `name` of an issue custom field and all attributes of its `value`. This will help to verify that your changes were applied.

3. In the request body specify the `id` or `name`, `$type` and value json for each issue custom field that you need to update.

To form value json you need to get id of the value (bundleElement) you want to post. For that:

* Get corresponding Project Custom Field: ```CURL GET /api/admin/projects/{projectID}/customFields/{fieldID} ```

* Get `bundle` from supported attributes for Project Custom Field: ```CURL GET /api/admin/projects/{projectID}/customFields/{fieldID}?fields=bundle(values(id,name,$type),aggregatedUsers(id,name,$type)) ```

So, the final request is:

```CURL
curl -X POST \
'https://example.youtrack.cloud/api/issues/SP-8?fields=customFields(id,name,value(avatarUrl,buildLink,color(id),fullName,id,isResolved,localizedName,login,minutes,name,presentation,text))' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <YouTrack_token>' \
-H 'Content-Type: application/json' \
-d '{
"customFields": [
{"name":"Assignee","$type":"SingleUserIssueCustomField","value":{"login":"jane.doe"}},
{"name":"Priority","$type":"SingleEnumIssueCustomField","value":{"name":"Major"}},
{"name":"Fix versions","$type":"MultiVersionIssueCustomField","value":[{"name":"2019.1"}]},
{"name":"Requester email","$type":"SimpleIssueCustomField","value":"test@example.com"},
] }'
```

4. To confirm that the target issue custom fields currently are set to corresponding values, let's check the response from the server:

```JSON
{
    "customFields":[
        {
            "id":"92-1",
            "name":"Priority",
            "value":{
                "localizedName":null,
                "color":{
                    "id":"18"
                },
                "name":"Major",
                "id":"67-2"
            }
        },
        ...
        {
            "id":"94-0",
            "name":"Assignee",
            "value":{
                "login":"jane.doe",
                "avatarUrl": "/hub/api/rest/avatar/90704ebe-c211-4906-a328-4f16ca82a5ea?s=48",
                "fullName":"Jane Doe",
                "name":"Jane Doe",
                "id":"1-3"
            }
        },
        ...
        {
            "id":"92-4",
            "name":"Fix versions",
            "value":[
                {
                    "id":"133-19",
                    "name":"2019.1",
                    "color":{
                        "id":"3"
                    }
                }
            ]
        }
        ...
        {
            "id":"92-6",
            "name":"Requester email",
            "value":"test@example.com"
        }
        ...
    ]
}
```



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/api-how-to-update-custom-fields-values.html](https://www.jetbrains.com/help/youtrack/devportal/api-how-to-update-custom-fields-values.html) · fetched 2026-09-22 08:34 Asia/Taipei*
