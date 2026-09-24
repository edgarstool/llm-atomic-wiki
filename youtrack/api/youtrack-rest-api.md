---
title: "YouTrack REST API"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/youtrack-rest-api.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# YouTrack REST API

YouTrack REST API lets you perform programmatically various actions in the tracker:

* Import issues from your current bug tracking system — for smoother migration to YouTrack.

* Create, modify, and perform other operations with issues — so you can seamlessly integrate YouTrack into your environment. For example, via automated issue submission from third-party applications.

* Manipulate projects, custom fields and sets of values, agile boards, issue link types, and other parameters.

> **Note: User, Group, Project Team, Organization, and Role Management in YouTrack REST API Starting from 2026.1**
> Starting from version 2026.1, the YouTrack REST API includes user, group, project team, organization, and role–related endpoints, entities, properties, and resources that were previously available only in the Hub REST API. See the [YouTrack REST API reference](rest-api-reference.html) to explore the full set of available operations. To review additions and deprecations by version, see the [REST API changelog](api-changelog.html). For Hub endpoints that no longer return or update YouTrack data, see [Hub REST API Endpoints and Entities Deprecated in YouTrack 2026.1](hub-rest-api-deprecated-endpoints-2026-1.html).

## General Notes

The REST API returns and consumes data in JSON format. Regular [content negotiation](https://en.wikipedia.org/wiki/Content_negotiation) rules apply:

* You must provide the Authorization HTTP request header for each request. The recommended authorization method is using a permanent token. To learn how to obtain a permanent token, see [Manage Permanent Tokens](Manage-Permanent-Token.html). For details about supported authorization methods, see [Log in to YouTrack](api-log-in-to-youtrack.html).

* Use the Accept HTTP request header to indicate the expected response data format: `application/json`.

* Use the Content-Type HTTP request header for POST and PUT requests: `application/json`.

The REST API is always enabled. However, a system administrator can specify which sites (origins) are allowed to access YouTrack using REST. For more information, see [Managing Global Settings](https://www.jetbrains.com/help/youtrack/cloud/?server-configuration-settings#resource-sharing-settings).

## Tools and Client Libraries Based on the YouTrack REST API

Before you start using the REST API for your own development, take a look at a few tools that use the YouTrack REST API:

* [YouTrackSharp](https://github.com/JetBrains/YouTrackSharp) is a .NET library for accessing the YouTrack REST API. This library is also available from the [NuGet gallery](https://nuget.org/List/Packages/YouTrackSharp). > **Warning:** > YouTrackSharp covers a subset of the API offered by YouTrack. Should it prove insufficient for your needs, consider using YouTrack REST API directly.

* [YouTrack Mobile](https://github.com/JetBrains/youtrack-mobile) uses the REST API to pull data from a YouTrack installation and display it in a mobile app.

* [YouTrack Integration Plugin](https://github.com/jk1/youtrack-idea-plugin) for IntelliJ IDEA and other JetBrains IDEs uses the REST API to display issue-related information directly in an IDE.



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/youtrack-rest-api.html](https://www.jetbrains.com/help/youtrack/devportal/youtrack-rest-api.html) · fetched 2026-09-22 08:34 Asia/Taipei*
