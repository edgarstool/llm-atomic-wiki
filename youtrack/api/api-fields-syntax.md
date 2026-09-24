---
title: "Fields Syntax"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/api-fields-syntax.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Fields Syntax

In YouTrack REST API, when you send an HTTP request to a resource, by default, the server sends back only the database ID and `$type` of the resource entity. To receive an attribute in the response from server, you must specify it explicitly in the `fields` parameter of a request.

## How to Find Available Field Names

The field names that you can use in the `fields` parameter match the attributes of the entity returned by the resource that you request.

To find the available field names for a specific request, open the reference page for the corresponding entity. For example, if a request returns an `Issue`, check the [Issue](api-entity-Issue.html) entity reference. If it returns a `User`, check the [User](api-entity-User.html) entity reference.

To browse the available entity reference pages, open the [Entities](api-entities.html) section of the API reference.

To request nested data, use the same structure as the JSON object in the response. For example, an Issue entity has attributes named `project` (entity) and `customFields` (array of entities), so you can request nested attributes as `project(name)` or `customFields(id,name,value(name))`.

If you are not sure which attributes you need, start with a small set of top-level fields, inspect the response, and then extend the `fields` parameter with nested attributes.

## Samples

### Request without Fields Parameter

Here we use a default request without providing the `fields` parameter.

#### Request

```CURL
curl -X GET 'https://example.youtrack.cloud/api/users/me' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer perm:am9obi5kb2U=.UG9zdG1hbiBKb2huIERvZQ==.jJe0eYhhkV271j1lCpfknNYOEakNk7' \
-H 'Cache-Control: no-cache'
```

#### Response body

In response, the server sends the entity ID:

```JSON
{
    "id": "1-2"
}
```

### Request with Fields Parameter

Here we use the `fields` request parameter to specify explicitly which attributes of the entity should be returned in the response body: `id`, `login`, `name`, and `email` of the current user.

#### Request

```CURL
curl -X GET \
'https://example.youtrack.cloud/api/users/me?fields=id,login,name,email' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer perm:am9obi5kb2U=.UG9zdG1hbiBKb2huIERvZQ==.jJe0eYhhkV271j1lCpfknNYOEakNk7' \
-H 'Cache-Control: no-cache'
```

#### Response body

In response, the server sends the requested attributes:

```JSON
{
    "email": "john.doe@example.com",
    "login": "john.doe",
    "name": "John Doe",
    "id": "1-2"
}
```

### Request with Nested Fields

For entities with nested objects, you can request attributes from child objects and collections as well. In the following example, the `fields` parameter requests the issue ID and summary, the project name, and selected data for custom fields.

#### Request

```CURL
curl -X GET \
'https://example.youtrack.cloud/api/issues?fields=id,idReadable,summary,project(name),customFields(id,name,value(name,login,fullName))' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer perm:am9obi5kb2U=.UG9zdG1hbiBKb2huIERvZQ==.jJe0eYhhkV271j1lCpfknNYOEakNk7' \
-H 'Cache-Control: no-cache'
```

#### Response body

In response, the server sends only the requested top-level and nested attributes:

```JSON
[
    {
        "customFields": [
            {
                "name": "Priority",
                "value": {
                    "name": "Major",
                    "$type": "EnumBundleElement"
                },
                "id": "92-1",
                "$type": "SingleEnumIssueCustomField"
            },
            {
                "name": "Assignee",
                "value": {
                    "login": "jane.doe",
                    "fullName": "Jane Doe",
                    "name": "Jane Doe",
                    "$type": "User"
                },
                "id": "94-0",
                "$type": "SingleUserIssueCustomField"
            }
        ],
        "project": {
            "name": "Sample Project",
            "$type": "Project"
        },
        "summary": "REST API lets you create issues!",
        "idReadable": "SP-13",
        "id": "2-142",
        "$type": "Issue"
    }
]
```



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/api-fields-syntax.html](https://www.jetbrains.com/help/youtrack/devportal/api-fields-syntax.html) · fetched 2026-09-22 08:34 Asia/Taipei*
