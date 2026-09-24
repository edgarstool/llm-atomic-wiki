---
title: "REST API URL and Endpoints"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/api-url-and-endpoints.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# REST API URL and Endpoints

YouTrack's REST API is available by the following URL:

```HTML
{YouTrack-Service-URL}/api
```

This page explains how REST API URLs are formed. To browse the list of available REST API resources and endpoints, see the [Resources](api-resources.html) section in the [REST API reference](rest-api-reference.html).

## YouTrack Server REST API URL

`<YouTrack Service URL>` is the base URL of the YouTrack service in your network environment. For example, you have your company's server `www.example.com` and a YouTrack service. You can configure YouTrack to be accessible by `www.example.com/youtrack` or, let's say `youtrack.example.com`.

`/api` is the context path for the REST API of your YouTrack service. Append this path to the YouTrack service URL to get the URL for the REST API.

For the sample service URLs above, REST API URLs are as follows:

| YouTrack Service URL | YouTrack REST API URL |
| --- | --- |
| `https://www.example.com/youtrack` | `https://www.example.com/youtrack/api` |
| `https://youtrack.example.com` | `https://youtrack.example.com/api` |

Here are the examples of the endpoint URLs to get the profile of the current user:

* For `www.example.com/youtrack`: ```HTML https://www.example.com/youtrack/api/users/me ```

* For `youtrack.example.com`: ```HTML https://youtrack.example.com/api/users/me ```

## YouTrack Cloud REST API URL

`<YouTrack Service URL>` is the base URL of your YouTrack Cloud instance.

If your YouTrack Cloud instance is hosted on `myjetbrains.com`, its service URL must have the `/youtrack` context appended. For example, `https://example.myjetbrains.com/youtrack`.

`/api` is the context path for the REST API of your YouTrack service. Append this path to the YouTrack service URL to get the URL for the REST API.

For the instances hosted on default YouTrack Cloud domains, REST API URLs are as follows:

| YouTrack Service URL | YouTrack REST API URL |
| --- | --- |
| `https://example.youtrack.cloud` | `https://example.youtrack.cloud/api` |
| `https://example.myjetbrains.com/youtrack` | `https://example.myjetbrains.com/youtrack/api` |

Here are the examples of the endpoint URLs to get the profile of the current user:

* For `example.youtrack.cloud`: ```HTML https://example.youtrack.cloud/api/users/me ```

* For `example.myjetbrains.com`: ```HTML https://example.myjetbrains.com/youtrack/api/users/me ```

## Custom Endpoints

Custom REST endpoints are user-defined endpoints that let you extend the YouTrack REST API. Custom endpoints can be added to YouTrack by installing an app that contains one or more [HTTP Handlers](apps-reference-http-handlers.html). These custom endpoints let you introduce additional capabilities into the YouTrack REST API to meet your specific needs.

When you call a custom REST endpoint, you invoke its corresponding HTTP handler. The endpoints used are based on the scope property assigned to the handler.

| Scope | URL |
| --- | --- |
| `issue` | <host>/api/issues/<issueId>/extensionEndpoints/app/handler/endpoint |
| `article` | <host>/api/articles/<articleId>/extensionEndpoints/app/handler/endpoint |
| `project` | <host>/api/admin/projects/<projectId>/extensionEndpoints/app/handler/endpoint |
| `user` | <host>/api/users/<userId>/extensionEndpoints/app/handler/endpoint |
| `global` | <host>/api/extensionEndpoints/app/handler/endpoint |

Set the following variables to match your app:

* `app` — the name of your app.

* `handler` — the name of the file that contains the HTTP handler script in the app package without the `.js` file extension.

* `endpoint` — the path from the declaration. For example, `"path": "/endpoint"`

Each API request requires the same permissions as the scope entity. For example, the endpoint /api/issues/DEMO-1/extensionEndpoints/app/handler/endpoint is accessible to any user who has permission to access the issue with the ID DEMO-1. Global endpoints are accessible to all users except the guest account.



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/api-url-and-endpoints.html](https://www.jetbrains.com/help/youtrack/devportal/api-url-and-endpoints.html) · fetched 2026-09-22 08:34 Asia/Taipei*
