---
title: "Create an Issue (API)"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/api-howto-create-issue.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Create an Issue

Use the REST API to create a new issue with the default values for issue custom fields.

## Summary

To create an issue, you need to know the entity ID of the project to which the issue should be reported. To get the project ID, see [Get a Project ID](api-usecase-get-project-id.html).

The user account that sends the request must have the Create Issue permission in the target project.

## Step-by-Step

Procedure:

1. Get the ID of the project where you want to create the issue. For instructions, see [Get a Project ID](api-usecase-get-project-id.html). This sample uses the project ID `0-0`.

2. Send a `POST` request to create a new issue in the target project:

```CURL
curl -X POST \
https://example.youtrack.cloud/api/issues \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <YouTrack_token>' \
-H 'Content-Type: application/json' \
-d '{
"project":{"id":"0-0"},
"summary":"REST API lets you create issues!",
"description":"Let'\''s create a new issue using YouTrack'\''s REST API."
}'
```

The request body must contain at least the target `project` and issue `summary`. In this example, the `description` attribute is optional.

In the body of the response, the server returns the entity id of the created issue:

```JSON
{
    "id": "2-38",
    "$type": "Issue"
}
```

That's it: We created a new issue. All custom fields of the issue are set to their default values.

> **Note:**
> Please note that you cannot simultaneously create a new issue and add attachments to it. You can attach files only to an already existing issue.



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/api-howto-create-issue.html](https://www.jetbrains.com/help/youtrack/devportal/api-howto-create-issue.html) · fetched 2026-09-22 08:34 Asia/Taipei*
