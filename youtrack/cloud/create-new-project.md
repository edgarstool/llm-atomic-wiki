---
title: "Create a Project"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/create-new-project.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Create a Project

Any time you're ready to start working on a new goal or initiative, create a dedicated project to help you track and manage your efforts.

When you create a project in YouTrack, the following operations are performed automatically:

* You are granted the Project Admin role in the project.

* You are set as the Project owner in the general project settings.

* You are added to the project team. This assignment grants you any roles that are assigned to members of the project team in the project.

* You are added to the set of values for the Assignee field for issues in the project.

* A saved search with the name Unassigned in <project ID> is automatically generated with your user account as its owner. This saved search uses the query `project: <project ID> #{Unassigned}`. You are automatically subscribed to notifications when new issues are created in the project. You can access and update this saved search at any time in your YouTrack profile. For more information, see [Tags and Saved Searches](tags-and-saved-searches.html).

Procedure: To create a project:

> **Tip:**
> Requires permissions: Create Project, Read Project Basic.
>
>
>
> To create a project within an organization, the Update Organization permission is required.

1. From the main navigation menu, select ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/project.svg) Projects.

2. On the Projects page, click the New project button.

* The first page of the project setup assistant opens.

![New Project dialog with the Scrum project template selected.](https://resources.jetbrains.com/help/img/youtrack/2026.2/project-setup-assistant-step-one.png)

3. Choose which template you want to use to create the project. You can select from a set of predefined project templates or a custom project template.

* For a description of the predefined project types, see [Project Templates](project-templates.html).

* For a description of custom project templates, see [Custom Project Templates](custom-project-templates.html).

Select a template to display a detailed description. Click the Use this template button to continue to the next step in the setup assistant.

![Scrum project template dialog with Name, ID, and Project owner fields.](https://resources.jetbrains.com/help/img/youtrack/2026.2/project-setup-assistant-step-two.png)

4. Enter a name for your project.

5. Click the image thumbnail to upload a custom logo.

6. If you want to customize additional settings in your project, click to expand the More settings section of the page. The following settings are available:

| Setting | Description |
| --- | --- |
| Project ID | Enter a value to customize the auto-generated project ID. This value must be unique in the system. |
| Starting number | To start numbering issues with a number other than 1, enter a value in the Starting Number input field.   |
| Description | Enter an optional description of the project.   |
| Organization | Select an optional organization to which the new project should belong.   |

7. When done, click the Create project button.

* A new project with the specified settings is created.

* The project profile page opens. Here, you can add users to the project team. To configure advanced project settings, select Settings in the project navigation menu. For more information, see [Configure a Project](configuring-a-project.html).

* You are granted the Project Admin role in the new project.

* You are set as the Project owner in the general project settings.

* You are added to the project team. This assignment grants you the Contributor role in the project.

* You are added to the set of values for the Assignee field for issues in the project. Any user or group that is later added to the project team is also added to the set of values for the Assignee field.

* A saved search with the name Unassigned in <project ID> is automatically generated with your user account as its owner. This saved search uses the query `project: <project ID> #{Unassigned}`. You are automatically subscribed to notifications when new issues are created in the project. You can access and update this saved search at any time in your YouTrack profile. For more information, see [Tags and Saved Searches](tags-and-saved-searches.html).

## See also

### System Administration

[Manage Project Members and Access](manage-project-access.html) [Configure a Project](configuring-a-project.html) [Manage Assignees](manage-assignees.html)



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/create-new-project.html](https://www.jetbrains.com/help/youtrack/cloud/create-new-project.html) · fetched 2026-09-22 08:34 Asia/Taipei*
