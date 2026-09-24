---
title: "Permanent Token Authorization"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/authentication-with-permanent-token.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Permanent Token Authorization

Permanent tokens give you secure access to YouTrack from your client applications and scripts. Compared to OAuth 2.0, authorization with a permanent token has the following advantages:

* Secure token-based authorization — authorize access without implementing a complex OAuth 2.0 authorization flow to obtain access tokens.

* Simple management — create your own permanent tokens in your user profile. If you suspect that your connection has been compromised, you can delete the token at any time and generate a new one.

* Scoped access — choose the service scope that the token can access. Permanent tokens only authorize actions that are allowed by the selected token scope and your account permissions.

To learn how to create or delete a permanent token in your user profile, see [Manage Permanent Tokens](Manage-Permanent-Token.html).

## Sample Request

The following sample shows a REST API call which utilizes a permanent token as the `Bearer` attribute of the `Authorization` header.

Request:

YouTrack Server:

```CURL
curl -X GET \
'https://youtrack.example.com/api/admin/projects?fields=id,name,shortName,createdBy%28login,name,id%29,leader%28login,name,id%29' \
-H 'Authorization: Bearer perm:cm9vdA==.dG9rZW4=.rNZ38ije7uiWwnUTRDdyFDdUkoPUPi' \
-H 'Accept: application/json' \
-H 'Content-Type: application/json'
```

YouTrack Cloud:

```CURL
curl -X GET \
'https://example.youtrack.cloud/api/admin/projects?fields=id,name,shortName,createdBy%28login,name,id%29,leader%28login,name,id%29' \
-H 'Authorization: Bearer perm:am9obi5kb2U=.UG9zdG1hbiBKb2huIERvZQ==.jJe0eYhhkV271j1lCpfknNYOEakNk7' \
-H 'Accept: application/json' \
-H 'Cache-Control: no-cache' \
-H 'Content-Type: application/json'
```

Response:

```JSON
HTTP 200 OK
Cache-Control → no-cache, no-store, no-transform, must-revalidate
Content-Encoding → gzip
Content-Length → 208
Content-Type → application/json;charset=utf-8
Date →Tue, 07 Aug 2018 11:01:17 GMT
Server → YouTrack
Vary →Accept-Encoding, User-Agent
X-Content-Type-Options →nosniff
X-Frame-Options →SAMEORIGIN
X-XSS-Protection →1; mode=block
[
    {
        "shortName": "RAP",
        "leader": {
            "login": "john.doe",
            "name": "John Doe",
            "id": "1-2"
        },
        "createdBy": {
            "login": "john.doe",
            "name": "John Doe",
            "id": "1-2"
        },
        "name": "Rest Api Project",
        "id": "0-2"
    },
    {
        "shortName": "SP",
        "leader": {
            "login": "root",
            "name": "John Smith",
            "id": "1-1"
        },
        "createdBy": {
            "login": "root",
            "name": "John Smith",
            "id": "1-1"
        },
        "name": "Sample Project",
        "id": "0-0"
    }
]
```



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/authentication-with-permanent-token.html](https://www.jetbrains.com/help/youtrack/devportal/authentication-with-permanent-token.html) · fetched 2026-09-22 08:34 Asia/Taipei*
