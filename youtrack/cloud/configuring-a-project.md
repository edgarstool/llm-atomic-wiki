---
title: "Configure a Project"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/configuring-a-project.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Configure a Project

When you create a project, YouTrack opens to the project overview page. This page is also displayed when you select a project from the Projects list.

![Customer Service project overview with project navigation and the Project Team panel.](https://resources.jetbrains.com/help/img/youtrack/2026.2/youtrack-project-overview.png)

The project overview page gives you quick access to project administration pages.

## Project Team

The project team is created automatically when the project is created. The user who created the project is automatically added to the team. Users and groups that are added to the project team are granted the Contributor role in the project. For more information, see [Manage Project Members and Access](manage-project-access.html).

When you add users and groups to the project team, these changes are synchronized with the set of values for the Assignee field in the project.

* Single users who are added to the project team are added to the set of values for the Assignee field in the project.

* Groups that are added to the project team are also added to the set of values for the Assignee field in the project. Each member of the group can be set as the assignee for an issue in the project.

Users and groups who are removed from the project team are not removed from the set of value for the Assignee field. For more information, see [Manage Assignees](manage-assignees.html).

## Accessing Project Settings

YouTrack projects are highly customizable. To help you make sure that your project supports your team's needs and business logic, you can access the project settings from various locations in the user interface. These navigation options are only visible to users who have Update Project permissions in the project.

Project settings are available from the following locations:

* From the Projects list, click the ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/more-options.svg) More icon for the project you want to configure, then select Settings. ![Customer Service project actions menu with Settings highlighted.](https://resources.jetbrains.com/help/img/youtrack/2026.2/project-list-settings.png)

* On the project overview page, select Settings in the project navigation menu. This opens the project settings page, where the side panel lists the settings pages that are available for the project. ![Project overview actions menu with Edit highlighted.](https://resources.jetbrains.com/help/img/youtrack/2026.2/access-project-settings-project-overview.png)

* In single issue view, click the ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/settings.svg) settings icon next to the project name in the field panel and select any of the links that appear in the menu. ![Issue project menu with Project Settings highlighted.](https://resources.jetbrains.com/help/img/youtrack/2026.2/access-project-settings-issue.png)

## General Project Settings

The project Overview page displays a dashboard-like interface for the selected project. Select Settings in the project navigation menu to open the project settings page. The General tab opens by default.

![General Settings page with editable Name, ID, and Description fields.](https://resources.jetbrains.com/help/img/youtrack/2026.2/general-project-settings-edit.png)

Here, you can add or change information stored when the project was created and configure default visibility options for new items in the project.

![General Settings page showing project Name, ID, Description, and Project owner.](https://resources.jetbrains.com/help/img/youtrack/2026.2/general-project-settings.png)

| Setting | Description |
| --- | --- |
| Organization> | The organization the project is assigned to. Organizations let you add structure to your project management efforts by grouping resources and projects under one roof.     To change the organization, select an organization from the drop-down list.   |
| Name | The name of the project. The project name must be unique. |
| ID | The project ID. This value is used as a prefix for the issue ID in all the issues that are assigned to this project. The project ID must be unique.     When you change the project ID, YouTrack stores the ID previously used as an issue prefix in the project. This collection of values is shown in the Historical IDs setting, which is read-only. External links to issues that use historical project IDs are redirected to issues that use the current projectID.     The Historical IDs setting is only visible when the project has at least one historical ID.   |
| Logo | Stores an image used as the logo for the project. This helps distinguish between different projects in the Projects list.       * Click the icon to upload a custom logo for the project.    * Click the Reset to default button to restore the auto-generated image.    |
| Description | An optional description that explains what the project is meant to organize or accomplish. This information is displayed on the project overview page.     The rich text editor lets you format the project description text in Visual or Markdown mode.       * In Visual mode, the text is formatted exactly as shown. To learn more about formatting text in YouTrack, see [Rich Text Editor](rich-text-editor.html).    * In Markdown mode, the text is formatted using sequences of special characters as a lightweight markup language. The preview pane below the input field shows you what the text looks like with the formatting applied. This input field supports the standard Markdown implementation as described in the [CommonMark specification](https://spec.commonmark.org/0.29/). However, several extensions that are supported in issue fields are not available here. For details, see [Markdown Syntax](youtrack-markdown-syntax-issues.html#markdown-availability).    |
| Default visibility | A group or team that is set automatically as the initial default for the Visible to group in new issues and articles in this project. When configured, the default is only applied to new issues and articles. The visibility settings for existing issues and articles aren't affected.   |
| Recommended visibility options | A list of groups and teams that are displayed in the Recommended visibility options drop-down for issues and articles in the project. Use this setting to help users discover groups that are set up specifically to handle issues in your project.     This setting can reduce the available options for restricting visibility of issues and articles to the selected groups and teams.   |

## Project Settings

On the project settings page, the side panel gives you access to all the settings for your project. Each page provides access to the settings for a specific project feature. The following additional setting pages are available for all project types:

| Page | Description |
| --- | --- |
| People | Add users or groups to the project team. For more information, see [Manage Project Members and Access](manage-project-access.html). |
| Custom Fields | Customize the fields and values for issues in the project. YouTrack provides a set of predefined default fields, such as State, Priority, and Assignee. These fields are attached automatically to any new project created in YouTrack. You can edit or delete most predefined fields or create and attach new custom fields. For more information, see [Manage Custom Fields](manage-custom-fields-per-project.html).   |
| Notifications | Customize the From and Reply-to addresses associated with your project and configure the notification templates for your project. For more information, see [Manage Project Notification Settings](project-notification-templates.html). |
| Time Tracking | Enable time tracking for your project to let your team log their work for issues, track issue progress, and create time reports. For more information, see [Enable Time Tracking](enable-and-configure-time-tracking.html). |
| Workflows | Attach workflows to the project. As with fields, you have a set of predefined default workflows. Some workflows are auto-attached to new projects. In the Workflow tab, you can view the list of attached workflows, detach unnecessary workflows, and activate or deactivate workflow rules. For more information, see [Manage Workflows](manage-workflows.html). |
| Apps | Add apps to the project. Apps give you the power to extend YouTrack with additional functionality tailored to your specific needs. You can integrate with other tools, add widgets to display important data, and share workflows. For more information, see [Manage Apps](manage-apps.html). |

The following pages are exclusive to standard projects for issue tracking:

| Page | Description |
| --- | --- |
| Version Control | Integrate the project with a VCS repository, such as GitHub, GitLab, or BitBucket. For more information, see [Integrate with Version Control](integrate-with-version-control.html). |
| Build Servers | Select an existing connection or add a new connection to a TeamCity server. You can configure the mapping between the project and the TeamCity configuration. For more information, see [Integrate with TeamCity](configure-teamcity-integration.html). |

The following pages are exclusive to helpdesk projects:

| Page | Description |
| --- | --- |
| Authorized Reporters | Restrict ticket reporting to a hand-selected group of people. For more information, see [Restricted Helpdesk Projects](restrict-a-helpdesk-project.html). |
| SLA Policies | Set up rules and frameworks for handling incoming customer requests. For more information, see [SLA Policies](service-level-agreements.html). |
| Channels | Open lines of communication for submitting support requests in a helpdesk project. For more information, see [Channels](helpdesk-channels.html). |

## More Project Settings

Click the ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/more-options.svg) More icon next to the project name in the header to open additional project settings.

![Project Settings navigation with all settings categories displayed.](https://resources.jetbrains.com/help/img/youtrack/2026.2/youtrack-project-more-settings.png)

| Option | Description |
| --- | --- |
| Edit | Make changes to the general project settings. For more information, see  [General Project Settings](#general-project-settings). |
| Clone | Create a project that is similar but not identical to an existing project. This operation lets you create new projects without having to configure them from scratch. For more information, see [Clone a Project](clone-project.html). |
| Archive | Preserve a project and its information for future reference when it is no longer active but might be useful later. For more information, see [Archive a Project](archiving-a-project.html). |
| Convert to template |    When enabled, the current project is used as a custom template for new projects. The project is added to the list of available project types on the Create Project page. For more information, see [Custom Project Templates](custom-project-templates.html).     > **Warning:** > Projects that are marked as custom project templates are not accessible in the same way as active projects. The project is not available in the search context, cannot be referenced in search queries or commands, and is not available in the list for creating new issues. This behavior is similar to projects that have been archived. > > > > If you have an active project that you would like to use as a custom project template, you can clone it first, then mark the cloned project as a template. To learn how to clone a project, see [Clone a Project](clone-project.html).    |
| Delete | Delete a project and all the project data permanently. For more information, see [Delete a Project](remove-project.html). |



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/configuring-a-project.html](https://www.jetbrains.com/help/youtrack/cloud/configuring-a-project.html) · fetched 2026-09-22 08:34 Asia/Taipei*
