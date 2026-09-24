---
title: "Predefined MCP Tools"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/predefined-ai-tools.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Predefined MCP Tools

> **Note:**
> Available since YouTrack version 2025.3

YouTrack provides you with a set of predefined MCP tools that you can use when you connect to the YouTrack MCP server from your favorite AI client.

## List of Predefined MCP Tools

Here is the list of predefined MCP tools that YouTrack exposes to the YouTrack MCP server users:

> **Note: Security**
> For security reasons, all predefined MCP tools are read-only. If you want to modify and update any predefined MCP tool, you can copy the corresponding script as part of a custom app package and add your changes. To learn how to create custom MCP tools, see [Custom MCP Tools](custom-ai-tools.html).

### search_issues

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `search_issues` | Searches for issues using YouTrack’s query language. The query can combine attribute filters, keywords, and free text.     Returns basic information for matching issues, including the issue ID, summary, project, resolved, reporter, created, updated. For full details, use `get_issue`. The response is paginated using the specified offset and limit.    | Find all open bugs assigned to me in the Mobile App project. |

### get_issue_fields_schema

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `get_issue_fields_schema` | Returns the JSON schema for custom fields in the specified project. Must be used to provide relevant custom fields and values for `create_issue` and `update_issue` actions. | Which fields are required to create issues in the Website Redesign project? |

### create_issue

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `create_issue` | Creates a new issue in the specified project.       * Use `get_issue_fields_schema` to discover `customFields` and their possible values for the target project. Important: some fields may be required for issue creation.    * Use the optional `permittedUsers` and `permittedGroups` arguments to restrict who can view the issue.     Returns the ID of the created issue and URL that opens the issue in a web browser. Use get_issue to get the full issue details.   | Create a new issue in the Backend API project with the summary "Fix authentication timeout" with a priority of High and assign it to @alex. Restrict the visibility to the Security Team group. |

### create_draft_issue

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `create_draft_issue` | Creates a new issue draft in the specified project. Draft issues are only visible to the current user and can be edited using `update_issue`. Returns the ID assigned to the issue draft and a URL that opens the draft in a web browser. | Start a draft issue in the Marketing Site project with the summary "Revise homepage hero section". |

### update_issue

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `update_issue` | Updates an existing issue and its fields. Can also be used to star issues and add votes. | Update issue WEB-132 by changing its state to In Progress and adding the label "frontend". |

### get_issue

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `get_issue` | Returns detailed information for an issue or issue draft, including the summary, description, URL, project, reporter (username), tags, votes, and custom fields. The `customFields` output property provides more important issue details, including Type, State, Assignee, Priority, Subsystem, and so on. Use `get_issue_fields_schema` for the full list of custom fields and their possible values. | Show me all details for issue ID BACK-249. |

### change_issue_assignee

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `change_issue_assignee` | Sets the value for the Assignee field in an issue to the specified user. | Reassign issue DEV-102 to @julia. |

### add_issue_comment

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `add_issue_comment` | Adds a new comment to the specified issue. Supports Markdown.     Use the optional `permittedUsers` and `permittedGroups` arguments to restrict who can view the issue.   | Add a comment to issue APP-56: "Great progress. Please include the API documentation before closing." Make the comment visible to the Feature Development team. |

### get_issue_comments

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `get_issue_comments` | Returns a list of issue comments with detailed information for each. The response is paginated using the specified offset and/or limit. | List all comments for issue UX-87. |

### get_saved_issue_searches

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `get_saved_issue_searches` | Returns saved searches marked as favorites by the current user. The output search queries can be used in `search_issues`. The response is paginated using the specified offset and/or limit. | Show me my saved searches. |

### manage_issue_tags

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `manage_issue_tags` | Adds a tag to or removes a tag from an issue. If a name is used, the first tag that matches the provided name is added. If no matching tags are found, an error message with suggestions for similar tags is returned. When successful, it returns the ID of the updated issue and the updated list of issue tags. | Add the tag "urgent" to issue API-144. |

### link_issues

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `link_issues` | Links two issues with the specified link type. Returns updated link counts for all target issue link types. | Link issue DOCS-12 to issue DEV-99 as "relates to". |

### create_article

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `create_article` | Creates a new article in the specified project. Returns the created article ID and URL.     Use the optional `permittedUsers` and `permittedGroups` arguments to restrict who can view the article.   | Copy the last output from this chat and create an article in the Compliance project. Restrict the visibility of the article to the Legal team. |

### update_article

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `update_article` | Updates an existing article. You can update the title, content, and parent article. Returns the updated article ID and URL.   | Copy the last output from this chat and add it to the end of the Trends to Watch article. |

### get_article

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `get_article` | Returns detailed information for an article, including title, content, sub-articles, tags, and visibility settings. Supports line-by-line scrolling for long articles. | Show me the full content of the Onboarding Guide article, including any sub-articles. |

### search_articles

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `search_articles` | Searches for articles in the knowledge base using YouTrack’s query language. The query can combine attribute filters, keywords, and free text.     Returns basic information about the article, including its ID, title, URL, parent article, and the lines where content matching the query was found. For full details, use `get_article`. The response is paginated using the specified offset and limit.   | Search for articles about API Authentication in the Developer Docs project created by @sarah. |

### find_projects

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `find_projects` | Finds projects whose names contain the specified substring (case-insensitive). Returns minimal information (ID and name) to help pick a project for `get_project`. The response is paginated using the specified offset and/or limit. | Find all projects with "CRM" in the name. |

### get_project

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `get_project` | Retrieves full details for a specific project. | Get full details for the "Customer Portal" project. |

### find_user_groups

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `find_user_groups` | Finds user groups or project teams whose names contain the specified substring (case-insensitive). The response is paginated using the specified offset and/or limit. | List all groups that include the word "Design". |

### get_user_group_members

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `get_user_group_members` | Lists users who are members of a specified group or project team. Project teams are essentially groups that are always associated with a specific project. The response is paginated using the specified offset and/or limit. | Show me the list of members in the QA Engineers group. |

### find_user

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `find_user` | Finds users by username or email. Returns profile data for the matching user. This includes the username, full name, email, and local time zone. | Find the user with email alex.rocha@company.com. |

### get_current_user

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `get_current_user` | Returns details about the currently authenticated user (me): username, email, full name, time zone. | Show my account details. |

### log_work

| Name | Description | Sample Prompt |
| --- | --- | --- |
| `log_work` | Adds a work item (spent time) to the specified issue. You can specify the duration in minutes, optional date, work type, description, and optional work item attributes. Use `get_project` to retrieve the `workTypes` and `workItemAttributesSchema` for the target project. | Log 90 minutes of work on issue DEV-203 with the description "Refactored payment module". |



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/predefined-ai-tools.html](https://www.jetbrains.com/help/youtrack/devportal/predefined-ai-tools.html) · fetched 2026-09-22 08:34 Asia/Taipei*
