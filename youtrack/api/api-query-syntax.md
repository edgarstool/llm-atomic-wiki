---
title: "Query Syntax"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/api-query-syntax.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Query Syntax

To filter issues or tags that you receive from a server in response to your request, you need to specify the `query` parameter in the request.

> **Note:**
> You can only use queries in GET requests that work with collections of issues or tags.

* When working with collections of issues, the `query` parameter represents a search query and has the same syntax with the adjustment for URL encoding. For details about YouTrack search queries, refer to the [Search Query Reference](https://www.jetbrains.com/help/youtrack/cloud/search-and-command-attributes.html).

* When working with collections of tags, you can use the `query` parameter to filter a list of tags by the tag name.

## Samples

Let's see how queries work on a sample request for the issues list.

### Request without Query Parameter

First, let's get an unfiltered list of issues without the `query` parameter. Here's a sample request:

```CURL
curl -X GET \
'https://example.youtrack.cloud/api/issues?fields=id,summary,project(name)' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer perm:amFuZS5kb2U=.UkVTVCBBUEk=.wcKuAok8cHmAtzjA6xlc4BrB4hleaX' \
-H 'Cache-Control: no-cache' \
-H 'Content-Type: application/json'
```

In response, the server sends the following:

```JSON
[
  {
    "project":{
      "name":"Demo Project",
      "$type":"Project"
    },
    "summary":"Welcome to your YouTrack!",
    "id":"2-99",
    "$type":"Issue"
  },
  {
    "project":{
      "name":"Demo Project",
      "$type":"Project"
    },
    "summary":"Create Issues",
    "id":"2-106",
    "$type":"Issue"
  },
  {
    "project":{
      "name":"Sample Project",
      "$type":"Project"
    },
    "summary":"REST API lets you create issues!",
    "id":"2-142",
    "$type":"Issue"
  },
  {
    "project":{
      "name":"Sample Project",
      "$type":"Project"
    },
    "summary":"Issue from REST #1",
    "id":"2-0",
    "$type":"Issue"
  }
]
```

### Request with Query Parameter

Now, let's use the `query` request parameter to filter the list of issues by the `name` of the project. Here's a sample request:

```SHELL
curl -X GET \
'https://example.youtrack.cloud/api/issues?fields=id,summary,project(name)&query=project:%20%7BSample%20Project%7D' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer perm:amFuZS5kb2U=.UkVTVCBBUEk=.wcKuAok8cHmAtzjA6xlc4BrB4hleaX' \
-H 'Cache-Control: no-cache' \
-H 'Content-Type: application/json'
```

To the sample request with the `query` parameter, the response body contains data only for matching issues:

```JSON
[
  {
    "project":{
      "name":"Sample Project",
      "$type":"Project"
    },
    "summary":"REST API lets you create issues!",
    "id":"2-142",
    "$type":"Issue"
  },
  {
    "project":{
      "name":"Sample Project",
      "$type":"Project"
    },
    "summary":"Issue from REST #1",
    "id":"2-0",
    "$type":"Issue"
  }
]
```

Finally, let's use a bit more complex query. Here, we are looking for issues that are assigned to the user "john.doe", are not yet resolved, and contain the word "summary". Here's a sample request:

```SHELL
curl -X GET \
'https://example.youtrack.cloud/api/issues?fields=id,summary,project(name)&query=for:%20john.doe%20%23Unresolved%20summary' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer perm:amFuZS5kb2U=.UkVTVCBBUEk=.wcKuAok8cHmAtzjA6xlc4BrB4hleaX' \
-H 'Cache-Control: no-cache' \
-H 'Content-Type: application/json'
```

Here's the response from the server:

```JSON
[
  {
    "project":{
      "name":"Sample Project",
      "$type":"Project"
    },
    "summary":"New summary",
    "id":"2-42",
    "$type":"Issue"
  }
]
```



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/api-query-syntax.html](https://www.jetbrains.com/help/youtrack/devportal/api-query-syntax.html) · fetched 2026-09-22 08:34 Asia/Taipei*
