---
title: "Custom MCP Tools"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/custom-ai-tools.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Custom MCP Tools

> **Note:**
> Available since YouTrack version 2025.3

In addition to the predefined MCP tools, you can create your own ones and let users of your YouTrack access them when they connect to the YouTrack MCP server from an AI client.

To add a custom MCP tool to YouTrack, add it to a custom app package. Then your YouTrack users can benefit from it when working with their AI clients. To learn how to create custom apps, see [App Quick Start Guide](apps-quick-start-guide.html).

Every custom MCP tool is a backend script written in JavaScript using the shared [YouTrack scripting API](YouTrack-Api-Documentation.html). This script must implement the dedicated `aiTool` rule type.

## Create a Custom MCP Tool

For security reasons, all predefined MCP tools are read-only. If you want to modify and update any predefined MCP tool, you can copy the corresponding script as a module of a custom app package and add your changes.

Procedure: To create a custom MCP tool:

> **Tip:**
> Requires permissions: Low-level Admin

1. Create an app package. For details, see [create an app package](apps-quick-start-guide.html#create-app-package).

2. In the app package, create a JavaScript module.

3. Implement your logic following the [format for custom MCP tools](#custom-ai-tool-format).

4. Optionally, add a custom tool prefix in the `manifest.json` file for the app.

5. Save the app package and upload it to YouTrack.

> **Note: Global MCP Tools**
> You don't need to attach apps containing MCP tools to any YouTrack project. All MCP tools are designed to work on the global system level.

When you upload an app with MCP tools to YouTrack, these tools become available for all users across all projects. MCP tools have the same level of access to YouTrack data as the user who is working with them.

For security reasons, custom tools must be explicitly included in the MCP endpoint URL for your connection. For example, `/mcp?customToolPackages=app-name1,app-name2` where `app-name1` and `app-name2` are the names of apps that define custom tools.

Every time a YouTrack admin adds a new custom MCP tool, users who connected to the YouTrack MCP server need to disable and enable the connection again to start using new tools.

## Custom MCP Tool Format

YouTrack MCP tools are written in JavaScript. They use the [YouTrack Workflow API](YouTrack-Api-Documentation.html) and follow the same syntax as YouTrack workflow rules. MCP tool scripts implement the dedicated `aiTool` rule type.

Here are the main elements of a custom MCP tool in JavaScript:

* The tool object must be exported from the JavaScript script as `aiTool`. For example: `exports.aiTool = { ... }`.

* The tool object consists of two parts: the tool descriptor and the tool action.

### Tool Descriptor

The tool descriptor includes the following elements:

| Element | Description | Required |
| --- | --- | --- |
| `name` | The name of the MCP tool. | Required |
| `description` | The description of the MCP tool. | Optional, but strongly recommended |
| `inputSchema` | The JSON schema for the tool input parameters. | Optional |
| `outputSchema` |    The JSON schema for the output.     Note that the MCP endpoints hide the output schema by default. It can be enabled if necessary using `/mcp?enableToolOutputSchema=true` query parameter.    | Optional |
| `annotations` | Tool annotations:       * `title`    * `readOnlyHint`    * `destructiveHint`    * `idempotentHint`    * `openWorldHint`    * `returnDirect`     For reference, see the [MCP specification](https://modelcontextprotocol.io/legacy/concepts/tools#available-tool-annotations).   | Optional |

These elements contain information about the function that's useful for the LLM.

### Tool Action

The tool action is a JavaScript function that implements the tool logic. Here are the descriptions of the input and the output of that function:

| Input | `ctx` - scripting context object.       * The context object provides a `ctx.arguments` object according to the JSON input schema (the tool parameters provided by the LLM).    * The arguments like `issueId` should be resolved in the code. For example: `entities.Issue.findById(ctx.arguments.issueId)`.    * The context object doesn't provide `ctx.issue`, `ctx.article`, or `ctx.user`.   |
| Output | The JavaScript function can return anything: `JSON object/array`, `string`, `null` or even not return anything (i.e. `undefined`).   |

Starting from YouTrack version 2026.2, custom MCP tools can also declare an `asyncFunctions` object. Use `ctx.invokeAsync()` from the tool action when the tool should return a result to the AI client immediately and continue follow-up work after the current transaction is complete. For details, see [Asynchronous Functions](async-functions.html).

### Tool Prefix

All custom MCP tools have special prefixes in their names. Tool prefixes are required for custom MCP tools in YouTrack to differentiate them from the predefined tools and to avoid name collisions with other custom tools.

When you set a prefix for the tool in the manifest, your tool will look like this in the list of tools: `<aiToolPrefix>_<tool_name>`.

You can set a prefix for your custom MCP tool by adding an `aiToolPrefix` value in the app manifest. Below you will find an example of a `manifest.json` file for the app package containing this MCP tool. The tool from the example will be shown in the list of tools as `test_<tool_name>`.

```JSON
{
    "name": "my-tools",
    "title": "My AI Tools",
    "description": "App description",
    "aiToolPrefix": "test"
}
```

If you don't set a tool prefix in the manifest, YouTrack will use the app name as the tool prefix. So, in the list of tools your tool will look like this: `<app_name>_<tool_name>`.

## Sample Custom MCP Tool

A sample app package implementing a custom MCP tool contains two files: a JavaScript file describing the logic and the app manifest.

### JavaScript Module

Here you can find an example of a JavaScript module implementing a custom MCP tool:

```JAVASCRIPT
const entities = require('@jetbrains/youtrack-scripting-api/entities');

exports.aiTool = {
  name: "get_issue_content",
  description: "Returns information about an issue by its ID",
  inputSchema: { // JSON Schema
    type: "object",
    properties: {
      issueId: {
        type: "string",
        description: "The issue ID (e.g. TEST-1234)"
      }
    },
    required: ["issueId"]
  },
  annotations: {
    title: "Get issue content",
    readOnlyHint: true,
    destructiveHint: false,
    idempotentHint: false,
    openWorldHint: false,
    returnDirect: false
  },
  execute: (ctx) => {
    const issue = entities.Issue.findById(ctx.arguments.issueId);
    return {
      id: issue.id,
      description: issue.description,
      state: issue.fields.State,
      assignee: issue.fields.Assignee?.login,
      project: {
        name: issue.project.name,
        key: issue.project.key
      }
    }
  },
  outputSchema: { // JSON Schema
    type: "object",
    properties: {
      id: {
        type: "string",
        description: "The issue ID"
      },
      description: {
        type: "string",
        description: "The issue description"
      },
      //...
    },
    required: ["id"]
  }
}
```



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/custom-ai-tools.html](https://www.jetbrains.com/help/youtrack/devportal/custom-ai-tools.html) · fetched 2026-09-22 08:34 Asia/Taipei*
