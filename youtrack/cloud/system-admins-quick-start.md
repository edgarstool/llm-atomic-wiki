---
title: "System Admin Quick Start Guide"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/system-admins-quick-start.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# System Admin Quick Start Guide

If you are responsible for the administration of a new YouTrack instance, here is a list of topics that you might find helpful. These topics are listed in the order that you would normally perform the tasks that are described on each page.

## Set Up a New YouTrack Site

When you're just getting started, you need to make sure that YouTrack is set up the way you want it and that the people who need to work with issues and manage projects have the appropriate level of access. Use the topics in this list to guide yourself through this process.

| Topic | Description |
| --- | --- |
| [Global Settings](managing-global-settings.html) | Check the global settings for your YouTrack server. There are several options that you should configure before you make the service available to other users.     On the Global Settings page, you can:       * Manage your YouTrack license.    * Set the default time zone.    * Set the visual presentation for fields that store date values.    * Change the system language.   |
| [YouTrack to YouTrack Migration](migrating-to-youtrack.html) | If you are migrating to YouTrack, learn how to import issues from another issue tracker. |
| [Roles](manage-roles.html) | YouTrack provides a handful of predefined default roles for managing user permissions. Familiarize yourself with these roles and the access rights that are enabled for users when they are assigned a role in a project.     The default roles provide standard levels of access for different types of users. You can add and remove permissions for the default roles or create your own.     The default Contributor role has the team option enabled. Users who are added to a project team that is assigned this role are granted this role in the project. The default Project Admin role is assigned to the project owner. For more information, see [Manage Project Members and Access](manage-project-access.html).   |
| [Groups](manage-user-groups.html) | Check your groups and verify which roles are assigned to them. If you want to assign a specific set of permissions to a group of users, create a group and grant one or more roles that grant access to the required set of permissions. Pay attention to any group that has the auto-join option enabled. New users are added to these groups automatically and inherit the roles that are assigned to these groups.     When you import issues from another issue tracker, the projects that these issues are assigned to are created automatically, as are groups for each project team. Members of these groups are assigned the default Contributor role.   |
| [Users](managing-users.html) | Add user accounts to the system. There are several options that you can use to create user accounts in YouTrack.       * [Create user accounts manually.](create-user-accounts.html#create-user-manually)    * [Invite new users to register.](create-user-accounts.html#InvitingNewUsers)    * [Let users register for their own accounts.](create-user-accounts.html#allow-self-registration)    * [Enable log in with credentials from an external authentication provider.](create-user-accounts.html#enable-auth)     When you let users register their own accounts or log in with an external authentication provider, use the Auto-join Groups option to grant users a specific set of permissions automatically.   |
| [Projects](managing-projects.html) | When you import issues from another issue tracker, the projects that these issues are assigned to are created automatically. If you want other users to manage these projects, edit each project and choose which user is assigned as the project owner.     By default, the Project Admin role is granted the Create Project permission. This permission grants users the ability to create projects in the global scope. If you want to let users create and manage their own projects, just add these users to a group that is assigned the Project Admin role or grant the role to the user directly in the Global project.    |

## Customize and Extend YouTrack

Once you have finished with the basic setup, there are a few more settings and features that you can configure at the global level as an administrator.

| Topic | Description |
| --- | --- |
| [Time Tracking](time-tracking.html) | The default time tracking settings use five 8-hour workdays from Monday to Friday.      You can also add work item types to the system. These work item types are available for use in all projects that have time tracking enabled.     Project managers can activate time tracking on a per-project basis.   |
| [Notification Templates](notification-templates.html) | If you want the messages that are sent by YouTrack to follow your brand identity, you can customize the messages that YouTrack sends over email.     Project managers can also customize notification templates on a per-project basis.   |
| [Workflows](workflow-guide.html) | Customize and automate how issues are processed by YouTrack by scripting workflows. You can write your own workflows, or download custom workflows from our repository in [GitHub](https://github.com/JetBrains/youtrack-workflows).     Anyone with low-level administrator permission can update the workflows for your YouTrack system.   |
| [Integrations](integrations.html) | Set up a standard integration to connect YouTrack with an external service.       * [Sync projects that have been imported into YouTrack to retrieve changes that are made in an external application](imports.html).    * [Fetch and process email messages from a specific address](mailbox-integration.html). Every email message that is sent to the mailbox is converted into an issue in YouTrack.    * [Connect YouTrack to a TeamCity server](integration-with-teamcity.html).    * [Connect YouTrack to a GitHub, GitLab, or Bitbucket repository](integration-with-version-control-systems.html).    * [Share and sync tickets between YouTrack and a connected Zendesk instance](integration-with-zendesk.html).     Enable and configure these integrations under the Integrations section of the Administration menu.   |
| [External Integrations](external-integrations.html) | Several third-party services let you connect to YouTrack from an external application. If you are the administrator for any of these tools in your organization, you can integrate them with YouTrack to enhance productivity.       * [Set up a connection and post notifications to Slack](slack-app-integration.html).    * [Set up an integration with Telegram](telegram-integration.html).    |



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/system-admins-quick-start.html](https://www.jetbrains.com/help/youtrack/cloud/system-admins-quick-start.html) · fetched 2026-09-22 08:34 Asia/Taipei*
