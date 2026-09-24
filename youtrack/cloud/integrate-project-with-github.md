---
title: "Integrate with GitHub"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/integrate-project-with-github.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Integrate with GitHub

Follow the instructions on this page to integrate your project with VCS repositories that are hosted on [github.com](https://github.com/) or a self-hosted GitHub Enterprise installation.

A GitHub integration enables the following features in YouTrack:

* Apply commands to YouTrack issues in commit messages. For more information, see [Apply Commands in VCS Commits](apply-commands-in-vcs-commits.html).

* Track commits that are related to specific issues in the activity stream for the issue in YouTrack. For more information, see [Commits](vcs-changes.html#view-edit-vcs-commits).

* Display the status of pull (merge) requests directly in the activity stream of any issue that is referenced in the title or description of the pull request. For details, see [Pull Requests](vcs-changes.html#pull-requests).

* Add links to YouTrack issues in commit messages or branch names. For more information, see [Link Issues in VCS Commits](map-issues-to-vcs-change-commit.html).

> **Note:**
> When you set up an integration with GitHub, you map your YouTrack project to a repository in GitHub. As a project administrator, you can set up this integration on a per-project basis.
>
>
>
> An administrator can enable and manage integrations with GitHub for any project in YouTrack. For more information, see [GitHub Integration](github-integration.html).

## Prerequisites

* YouTrack is accessible to inbound connections. Specifically, you need to make sure that your network doesn't block connections between your VCS server and YouTrack.

* If you authenticate with a GitHub App, the app is installed in the GitHub account or organization that owns the repository, and the app has access to the repository that you want to connect to YouTrack.

* If you authenticate with a GitHub App, you have the app ID and the private key in PEM format. YouTrack doesn't support encrypted private keys for GitHub App authentication.

* If you authenticate with a personal access token, the GitHub account that owns the token has either Admin or Owner permissions for the repository.

If you're integrating with a GitHub Enterprise installation and want to establish a secure (HTTPS) connection with the server, you may need to import the SSL certificate for your GitHub server into YouTrack.

* If your GitHub Enterprise server has a valid certificate that is signed by a well-known certificate authority (CA), the JVM vendor may have already added the root (CA) certificate to the certificate store. You should be able to connect to the server without importing its SSL certificate.

* If the certificate for your server is self-signed, you need to import the certificate and public key to establish a secure connection. For security, use this option only when both YouTrack and your GitHub Enterprise server run on a private computer network. This operation is only available to users with Low-level Admin Read and Low-level Admin Write permissions. For details, see [SSL Certificates](ssl-certificates.html).

## Create a GitHub App

If you want to authenticate the integration with a GitHub App, create and install the app in GitHub before you configure the VCS integration in YouTrack. For general instructions, see [Registering a GitHub App](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app) in the GitHub documentation.

Procedure: To create a GitHub App for YouTrack:

1. In GitHub, open the settings for the account or organization that owns the repository you want to connect to YouTrack.

2. From the settings navigation, select `Developer settings > GitHub Apps`, then click New GitHub App.

3. Enter a recognizable name for the app.

4. In the Homepage URL field, enter the base URL of your YouTrack site or another page that helps your team identify the app.

5. Leave the Callback URL field empty. YouTrack doesn't use the GitHub App user authorization flow for VCS integrations.

6. In the Webhook section, clear the Active option. YouTrack creates repository webhooks automatically when you save the VCS integration.

7. You don't need to select app-level webhook events in the Subscribe to events section. YouTrack subscribes the repository webhook it creates to the required events.

8. In the Repository permissions section, grant the app the following permissions. For more information, see [Choosing permissions for a GitHub App](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app) in the GitHub documentation.

| Permission | Access |
| --- | --- |
| Actions | Read-only |
| Contents | Read-only |
| Metadata | Read-only. This permission is applied automatically to GitHub Apps. |
| Pull requests | Read-only |
| Webhooks | Read & write |

9. Leave permissions that aren't listed here set to No access unless your organization needs them for another use of the same GitHub App.

10. Under Where can this GitHub App be installed?, select the installation option that matches how you want to use the app.

11. Click the Create GitHub App button.

12. In the app settings, copy the app ID and generate a private key.

* GitHub downloads the private key in PEM format.

13. Install the app in the GitHub account or organization that owns the repository, and grant the app access to the repository that you want to connect to YouTrack.

## Configure the GitHub Integration

The first step is to establish a connection between a project in YouTrack and a repository in GitHub. To connect with GitHub, you can use either GitHub App authentication or a personal access token.

GitHub App authentication grants access based on the app installation and doesn't bind the connection to a personal GitHub account. A personal access token grants YouTrack access to the repository based on the permissions that are granted to your GitHub account.

You can use the same GitHub App credentials for multiple integrations that use the same GitHub server connection.

> **Note:**
> All GitHub App-authenticated integrations that use the same GitHub server connection use the same GitHub App. Replacing the app changes it for every integration on this server. Make sure the replacement app has access to every repository that is connected to YouTrack through this server.

Procedure: To connect to a GitHub repository:

> **Tip:**
> Requires permissions: Update Project

1. From the main navigation menu, select ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/project.svg) Projects.

2. From the project list, select a project.

3. From the project navigation menu, select Settings.

4. In the project settings side panel, select Version Control.

5. Click the New VCS Integration button.

* The New VCS Integration dialog opens.

6. For the Server type, select GitHub.

![New VCS Integration dialog with GitHub selected as the server type.](https://resources.jetbrains.com/help/img/youtrack/2026.2/new-github-vcs-integration-project.png)

7. Paste the URL that points to your GitHub repository into the Repository URL input field.

8. From the Authentication type list, select the authentication method that you want to use.

> **Note:**
> To make sure you see information that is relevant to your setup, select the tab that corresponds with the authentication method you want to use.

GitHub App:

Select GitHub App.

If this is the first integration that uses a GitHub App for this server, enter the app ID and upload the private key file or paste the PEM content manually.

If another integration already uses a GitHub App for this server, YouTrack reuses the same app. To use another app, select Replace with another GitHub App, then enter the app ID and private key for the replacement app.

> **Note:**
> To replace the app, you need the Update Project permission for every project with a VCS integration connected to this GitHub server.

When you save the integration, YouTrack automatically identifies the app installation that has access to the repository.

Personal access token:

Select Personal access token, then paste your token into the Personal access token input field. If you don't already have an access token, follow these steps:

1. Click the Generate token link to open the New personal access token page in GitHub.

![GitHub personal access token form with the required scopes selected.](https://resources.jetbrains.com/help/img/youtrack/2026.2/new-personal-access-token-github.png)

2. Enter a description for the token.

3. When you access the New personal access token page using the link from YouTrack, all required scopes are selected for you. If you accessed this page directly, select the scopes for `repo`, `read.org`, and `admin:repo_hook`.

4. Click the Generate token button.

5. Copy the token to the clipboard.

![GitHub token page with the generated token and copy control.](https://resources.jetbrains.com/help/img/youtrack/2026.2/copy-github-token.png)

6. Switch back to the New VCS Integration dialog in YouTrack and paste the token into the Personal access token field.

9. Click the Save button.

* Your YouTrack project is integrated with the selected repository in GitHub.

* Commits from the GitHub repository that reference an issue in the project are displayed in the activity stream of the referenced issue.

* The sidebar displays additional settings for configuring the VCS integration. ![GitHub integration settings showing the connected repository.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-integration-settings-project.png)

To learn more about these settings, see [Integration Settings](#integration-settings).

## Advanced Server Settings

If you are unable to establish a connection to your repository using the basic settings on the New VCS Integration dialog, click the Show advanced server settings link.

![Advanced Server Settings with commit, issue, and pull-request URL patterns.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-advanced-server-settings-project.png)

You only need to enter values for these settings for new VCS integrations with the target server. If you already have a working integration with a single repository on the server, you can add integrations with other repositories without setting these parameters again.

Use the following guidelines to set the values for these settings:

| Setting | Description |
| --- | --- |
| URL | This setting is not relevant for connections to repositories in GitHub. For integrations with other VCS hosting services, this setting helps to identify the path to the repository.     The path to a GitHub repository always consists of two segments. Everything that precedes these two segments in the Repository URL setting is automatically recognized as the path to the server.   |
| SSL key | If your server environment is set up to require client SSL authentication, select the keystore that contains the private key for your YouTrack server. This key identifies your YouTrack server when it tries to establish a connection with GitHub. This setting is only used to support HTTPS authentication as required by connections to your internal network.     The list only displays SSL keys that are already imported into YouTrack. To learn how to generate keystores files and upload them to YouTrack, see [SSL Keys](ssl-key-stores.html).   |

## Integration Settings

By default, the VCS integration processes changes that are committed to the repository by any user in any branch. Any user who has access to the issue in YouTrack can view these changes in the issue activity stream.

If you only want to process changes by specific users in designated branches or restrict the visibility of VCS changes in YouTrack, you can customize the integration settings. Use the following settings to customize the integration:

| Setting | Description |
| --- | --- |
| Repository | Displays the path to the repository in the integrated version control system.     If needed, you can edit the location of the repository after you have set up the integration. For instructions, see [Edit Repository Settings](edit-repository-settings.html).    |
| Additional projects | Integrates the linked repository with one or more additional projects. This setting is only available in projects that are set as the Main YouTrack project for the VCS integration. |
| Committers | Restricts the ability to update issues with commands in commit messages to members of the specified group. VCS changes from users who are not members of the selected group are still attached to related issues, but any commands that are specified in their commits are ignored. |
| Processing scheme for VCS changes | Choose how to process VCS changes when the commit message references an issue ID. The following options are supported:       * Add commits, ignore commands: Add VCS changes to issues when a commit message references an ID that belongs to an issue in an integrated project. Any command in the commit message is ignored.    * Add commits in all projects, apply commands in main: Add VCS changes to issues when a commit message references an ID that belongs to an issue in an integrated project. Only apply commands to issues that belong to the currently selected main project. > **Note:** > When this option is selected, the Parse commits for issue comments option becomes available.    * Add commits and apply commands to all projects: Add VCS changes to issues when a commit message references an ID that belongs to an issue in an integrated project. Update issues in any integrated project when commit messages include commands. > **Note:** > * Scheme is available only when at least one Additional project is specified in the integration settings. > > * When this option is selected, the Parse commits for issue comments option becomes available.    |
| Monitored branches | Stores the names of the branches that you want to monitor for changes.       * Use `+` to include a branch.    * Use `-` to exclude a branch.    * For the `branch name`, use the fully qualified name of the branch. For example, `refs/heads/<branch name>`.    * Use `*` as a wildcard. This placeholder matches one or more characters in a string. For example, to include all feature branches, use: ```SHELL +:refs/heads/feature/* ``` You can only use one wildcard character per branch pattern. If you specify a pattern that contains more than one asterisk character, only the first is evaluated as a wildcard.    * To monitor all branches, leave the input field empty.     If the address that you entered as the Repository URL when you connected to the repository points to a specific branch, this branch is automatically added to the list of monitored branches when you set up the connection.    |
| Parse commits for issue comments |    > **Note:** > This option is shown in the UI only when either of the following processing schemes is selected: > > > > * Add commits in all projects, apply commands in main > > * Add commits and apply commands to all projects     When enabled, specific lines of text in commit messages are copied to issues as comments. When you copy parts of the commit message to the issue as comments, you can trigger @mention notifications and expose information to users who don't have access to VCS changes.     This setting does not affect how commit messages are shown in VCS changes. The entire commit message, including commands and issue comments, is always shown as part of the VCS change record in the activity stream.     You should only enable this option when:       * You want to mention other users in your commit messages and generate notifications when the text is copied to an issue comment.    * You restrict the visibility for VCS changes and want to make commit-related information visible to external users as comments.     To learn more about how YouTrack processes commit messages, see [Apply Commands in VCS Commits](apply-commands-in-vcs-commits.html).   |
| Check branch names for issue references | When enabled, the integration checks for references to issues in branch names for commits. This option was added for teams that use a branch-per-ticket process, so their developers don't have to mention issue IDs in their commit messages explicitly. |
| VCS changes visibility | Restricts the visibility of VCS changes to one or more groups of users in YouTrack. When unrestricted, the list of VCS changes is visible to any user who has permission to read the issue. |

## Available Actions

When you select an integrated version control system in the list, the following actions are available in the toolbar:

| Action | Description |
| --- | --- |
| Disable | Shuts off the connection between the integrated project and the VCS repository. The configuration is not changed and can be enabled at any time. |
| Edit | Opens the integration settings dialog in the sidebar for the selected project and repository. |
| Delete | Removes the settings for the integrated project from YouTrack.     This action also removes all VCS changes that were added to issues for commits in the linked repository.     While the action itself cannot be undone, you can use the Import action to restore VCS changes that were removed accidentally.   |
| Import commits and open pull requests | Checks the commit history in the linked repository and adds VCS changes to issues that are referenced in commit messages. This option is only available for integrations that are currently enabled.     You can use this action to restore VCS changes that were removed when an integration was accidentally deleted or to migrate links to issues in a new project.   |

## Troubleshooting

Condition — References to issues in VCS commits are not shown as VCS changes in YouTrack.

| Cause | Solution |
| --- | --- |
| The webhooks in the integrated VCS don't exist, are disabled, or are otherwise malformed. | Check the webhooks in the settings for your VCS repository. Make sure that the webhooks exist and that they are enabled.     If you suspect that there is a problem with a webhook, delete or disable it in the settings for your VCS and set up a new VCS integration in YouTrack.   |

Condition — Commands that are specified in VCS commits are not applied to issues in YouTrack.

| Cause | Solution |
| --- | --- |
| The users who commit changes to the repository are not members of the Committers group in the integration settings. | Either add the committers to the specified group in YouTrack or modify the selection in the integration settings. |
| The users who commit changes to the repository do not have permission to update issues in the connected project. | Either add these users to the project team or grant them a role in the project that includes the Read Issue and Update Issue permissions. |
| YouTrack can't find a user account that matches the author of the commit message. | The user must either use the same email address for their accounts in both YouTrack and GitHub or add the value that is stored as the Name in their GitHub profile to the list of VCS usernames in their Hub accounts.     For more information, see [Match Change Authors and YouTrack Users](match-commit-authors-and-youtrack-users.html).   |

Condition — You are unable to establish a connection between YouTrack and your GitHub Enterprise server. See if any of the following causes are present.

| Cause | Solution |
| --- | --- |
| The external service is unavailable. | Verify that your GitHub Enterprise server is running. |
| The connection is blocked by a firewall. | Open the ports in the firewall that are used by YouTrack and the GitHub Enterprise server. |
| The GitHub Enterprise server requires a secure connection. | Import the certificate for your GitHub Enterprise server into YouTrack. For instructions, see [SSL Certificates](ssl-certificates.html). |
| Your SSL certificate for the GitHub Enterprise server has expired. | Renew and import the updated certificate into YouTrack. For instructions, see [SSL Certificates](ssl-certificates.html). |

## See also

### User Guide

[View and Edit VCS Changes](vcs-changes.html) [Link Issues in VCS Commits](map-issues-to-vcs-change-commit.html) [Apply Commands in VCS Commits](apply-commands-in-vcs-commits.html)



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/integrate-project-with-github.html](https://www.jetbrains.com/help/youtrack/cloud/integrate-project-with-github.html) · fetched 2026-09-22 08:34 Asia/Taipei*
