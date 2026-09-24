---
title: "MCP Tools"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/ai-tools.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# MCP Tools

> **Note:**
> Available since YouTrack version 2025.3

Model Context Protocol (MCP) is a new standard that enables apps like chatbots and other AI tools talk to other services, like YouTrack, in a consistent and safe way. The YouTrack MCP server gives these tools real-time access to read and update issues in YouTrack, using your own account permissions. It includes a set of built-in tools you can use to find, create, and update things like issues and comments.

For the instructions on how to configure the connection between your AI client and YouTrack, see [YouTrack documentation](https://www.jetbrains.com/help/youtrack/server/model-context-protocol-server.html).

When your MCP client supports OAuth authorization, it can connect to YouTrack without storing a permanent token locally. For details about OAuth clients, preregistered MCP clients, and CIMD client auto-creation, see [OAuth Clients](OAuth-authorization-in-youtrack.html#oauth-clients).

Our predefined MCP tools let you view, create, and update issues, projects, and users. For more information about predefined MCP tools in YouTrack, see [Predefined MCP Tools](predefined-ai-tools.html).

You can also create custom MCP tools and include them in your custom YouTrack app. Custom tools are backend JavaScript modules that use the same scripting API as workflows and other backend app modules. For instructions on how to create your own MCP tools, see [Custom MCP Tools](custom-ai-tools.html). For shared scripting guidance, see [YouTrack JavaScript API](Workflows-in-JavaScript.html).

## Security

When using the YouTrack MCP server, you're letting your AI agent perform various tasks, such as creating and updating issues on your behalf. The YouTrack team has thoroughly considered possible security concerns when developing our predefined MCP tools. For this reason, predefined MCP tools are read-only.

If you want to modify any of the predefined MCP tools, copy them into a separate app package and update the code. For details on how to write custom MCP tools, see [Custom MCP Tools](custom-ai-tools.html).

## Monitoring Changes Made by AI Tools

For additional security, YouTrack admins may want to monitor changes made by AI tools. They can implement such monitoring using workflow rules. On-change workflow rules can determine whether a change is made by an MCP request and run custom logic for such cases.

You can check whether an LLM performed a change through an MCP request by using `isMcpRequest` method of the [context object](context.html) in a workflow rule that gets triggered on changes.

Here is an example of a simple on-change workflow rule that implements additional monitoring and tags all issues updated by an LLM with a special tag:

```JAVASCRIPT
const entities = require('@jetbrains/youtrack-scripting-api/entities');

exports.rule = entities.Issue.onChange({
    title: 'Mark issues touched by an LLM via MCP with a tag',
    guard: (ctx) => ctx.isMcpRequest, // triggers only on MCP change requests
    action: (ctx) => ctx.issue.addTag('by-ai')
});
```



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/ai-tools.html](https://www.jetbrains.com/help/youtrack/devportal/ai-tools.html) · fetched 2026-09-22 08:34 Asia/Taipei*
