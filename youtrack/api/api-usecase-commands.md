---
title: "Apply Commands to Issues"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/api-usecase-commands.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Apply Commands to Issues

This page shows examples of how to apply a command to one or more issues in YouTrack using its REST API. Just as the commands in UI, its REST API implementation lets you perform operations with one or several issues much faster and easier.

## Summary

To apply a command to issues, send a `POST` request to the `/api/commands` endpoint with a request body that contains the command query and the target issues. You can also add optional attributes to add a comment, restrict comment visibility, or suppress notifications.

## Step-by-Step

Procedure: To apply a command to issues:

> **Tip:**
> Required permissions: Update Issue

1. Choose the command query that you want to apply to the issue or issues. Use the same command syntax that you use in the YouTrack user interface.

2. Identify the target issue or issues. You can identify issues by their database entity ID, for example `"id":"2-1234"`, or their human-readable ID, for example `"idReadable":"SDP-345"`.

3. Build the request body. A minimal request body contains the `query` to apply and a collection of `issues` that identify the target issues.

4. Optional. Add command attributes such as `comment`, `visibility`, or `silent` when you need to add a comment, restrict comment visibility, or suppress notifications.

5. Send a `POST` request to the commands endpoint:

```
/api/commands
```

## Minimal Request to Apply a Command

The following request applies a command with a minimal request body.

```
curl -X POST 'https://example.youtrack.cloud/api/commands' \
-H 'Authorization: Bearer <YouTrack_token>' \
-H 'Content-Type: application/json' \
-d '{
"query": "Fixed",
"issues": [ { "id": "2-17" } ] }'
```

For the sample minimal request without the `fields` parameter, the server sends a response with the `200 OK` status and an empty body.

## Command with Restricted Comment Visibility

The following request assigns the specific issue to the current user and adds a new comment with restricted visibility.

```
curl -X POST 'https://example.youtrack.cloud/api/commands' \
-H 'Authorization: Bearer <YouTrack_token>' \
-H 'Content-Type: application/json' \
-d '{
  "query":"for me ",
  "issues":[{"id":"2-15"}],
  "silent":false,
  "comment":"Still cannot reproduce.",
  "visibility":
    {
    "$type":"CommandLimitedVisibility",
    "permittedGroups":[{"id":"3-2"}]
    }
  }'
```

The following request adds a tag to three issues and assigns them to user "jane.doe".

```
curl -L -X POST 'https://example.youtrack.cloud/api/commands' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer <YouTrack_token>' \
--data-raw '{
"query":"tag To deploy for jane.doe",
"issues":[{"idReadable":"SP-3967"},{"idReadable":"SP-4032"},{"idReadable":"SP-3990"} ]
}'
```

## Apply a Command Silently

Now let's apply a command silently. That is, the following request instructs YouTrack to not send notifications about the change. Such silent commands come handy when you need to update a significant number of issues simultaneously; For example, when you plan the next version release, or a milestone, and need to set or change version field.

To apply a command silently, all you need to do is to specify in the request payload the attribute `"silent"` set to `true`. In this sample we identified issues by their database entity `id`, not "idReadable" as in previous samples.

```CURL
curl -L -X POST 'https://example.youtrack.cloud/api/commands' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer <YouTrack_token>' \
--data-raw '{
"query":"Fix version 2021.1 ",
"issues":[{"id":"2-8456"},{"id":"2-8475"},{"id":"2-8476"},{"id":"2-8477"},{"id":"2-8480"},{"id":"2-8481"},{"id":"2-8482"},{"id":"2-8485"},
{"id":"2-8486"},{"id":"2-8489"},{"id":"2-8490"},{"id":"2-9000"},{"id":"2-9010"},{"id":"2-9011"} ],
"silent":true
}'
```



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/api-usecase-commands.html](https://www.jetbrains.com/help/youtrack/devportal/api-usecase-commands.html) · fetched 2026-09-22 08:34 Asia/Taipei*
