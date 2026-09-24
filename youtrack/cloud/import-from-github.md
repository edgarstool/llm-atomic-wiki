---
title: "Import from GitHub"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/import-from-github.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Import from GitHub

The import from [GitHub](https://github.com) lets you migrate issues, comments, users, and other data from a GitHub repository to YouTrack.

A setup wizard navigates you through the import configuration process. It prompts you to enter the connection settings and lets you map a project in YouTrack to a repository in GitHub. If your repository has a custom set of fields for issues, you can edit the import script in YouTrack directly.

## Prerequisites

Before you import issues from GitHub to YouTrack, check the following requirements:

* Your GitHub projects that are hosted on [github.com](https://github.com/). Imports from GitHub Enterprise Server are not supported at this time.

* You have direct access to log in to the source application using a password or token. YouTrack's import engine doesn't support authentication through external authentication modules.

## Import Details

If the GitHub database contains references to entities that do not exist in YouTrack yet, they are created. The YouTrack user account you use to run the import should have permissions to create all imported entities. We recommend using an account with a System Admin role or the Low-level Admin Write permission to run the import.

Here is the list of entities that are imported from GitHub and their mapping to YouTrack entities:

| Entity in GitHub | Entity in YouTrack |
| --- | --- |
| Repository | Project |
| Issues | Issues |
| Comments | Comments |
| Users | Users |
| Custom fields | Custom fields |
| Attachments | Attachments |
| Markdown files (`*.md`) | Knowledge base articles |
| HTML files (`*.html`) | Knowledge base articles |
| reStructuredText files (`*.rst`) | Knowledge base articles |
| Repository collaborators | Project team members |

## Set up an Import from GitHub

Setting up an import from GitHub has two parts:

* First, you need to create a personal access token in GitHub

* Then you switch to YouTrack and configure the import.

Before you add a new import configuration, you need to create a personal access token that will grant access to the repository in GitHub. Then you can use the token for authorization when setting up the import in YouTrack.

### Create an Access Token in GitHub

To set up import of issues from GitHub, first, you need to create a personal access token for the GitHub account that you use to access issues in the GitHub repository.

Procedure: To create a personal access token in GitHub:

1. Log in to GitHub with an account that is granted administrative permissions.

2. In the upper-right corner of any page, click your profile photo, then click Settings.

3. In the left sidebar, click Developer settings, then Personal access tokens.

4. Click Generate new token and provide a description for the token.

5. Set the expiration date for the token if necessary.

6. Select the scopes for the token.

The base permission scopes differ for public and private repositories. Select the repository type that applies to your situation and select the corresponding scopes for your token.

Public:

* `repo`: * `repo:status` * `public_repo`

* `user`: * `read:user` * `user:email`

* `project`: * `read:project`

Private:

* `repo`: To import issues from a private repository, enable all `repo` scopes.

* `user`: * `read:user` * `user:email`

* `project`: * `read:project`

7. Click the Generate token button.

* The new personal access token is added to the list.

![The list of Personal access tokens.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-import-personal-tokens.png)

For more details on creating personal access tokens in GitHub, refer to the [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token).

### Configure an Import from GitHub in YouTrack

The setup wizard guides you through the setup process. To start in YouTrack, open `Administration > Integrations > Imports`, click New import, and select GitHub.

Procedure: To configure an import from GitHub:

> **Tip:**
> Requires permissions: Low-level Admin Write

1. From the main navigation menu, select ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/settings.svg) `Administration > Integrations > Imports`.

2. Click New import to open the setup dialog.

![New Import dialog listing supported source services.](https://resources.jetbrains.com/help/img/youtrack/2026.2/new-import-dialog.png)

3. Select GitHub.

* Settings for a New Import from GitHub are displayed.

![New Import from GitHub step with source and authentication fields.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-new-import-settings.png)

4. Enter values for the following settings:

| Setting | Description |
| --- | --- |
| GitHub repository URL | Enter the URL of the target repository. Since it's not a clone URL, do not include the `.git` suffix.    |
| Token | The [personal access token](#github-personal-access-token) that you have generated in GitHub for the user account that you use to access the target issues.     If you didn't generate a token for this import before you started to set it up, click the Generate token link to access GitHub and create it now.    |

If required by your GitHub installation, enable the Use SSL key for client authentication option.

5. Click the Next button.

* The second set of import settings is displayed.

![Import confirmation step with project mappings and the Start import button.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-import-settings-final.png)

6. Expand the Manage import for optional datasets section. Here you can configure the import engine to ignore certain parts of the source database during import.

| Setting | Description |
| --- | --- |
| Issue history | Disable this toggle to ignore historical changes of issues during import. |
| Issue links | Disable this toggle to ignore links between issues during import. |

By default, these toggles are enabled. This means that YouTrack will pull historical changes and issue links from the import source if the import script supports it.

> **Note:**
> If the import script doesn't handle issue history or issue links, enabling any of these toggles will not result in importing these datasets. To import issue history or issue links, update the import script.

7. Select the target project for the import. For more details about the project mapping configuration, see [Project Mapping](#project-mapping).

Optionally, enable the Continuous import toggle. When enabled, YouTrack will periodically poll the GitHub repository and import updated and new issues that were created since the last sync.

8. Click the Start import button.

* YouTrack will import found issues, articles, and users into the target YouTrack project.

* If the Continuous import option is enabled, YouTrack will periodically check the target GitHub repository for updated and new issues.

When you have set up an import, it is shown in the Imports list. To view configuration and import details, select an import configuration from the list.

![Import details showing the source URL, status, and imported item counts.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-import-details.png)

In the sidebar, YouTrack shows the import status and additional information about the imported data. Click the ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/refresh.svg) Resume button in the toolbar to import updates from the connected GitHub project.

You can also download the import log file to study and investigate when needed.

## Project Mapping

On the final step of the import setup, you can choose whether to create a new project for the import or import data into an existing project in YouTrack.

YouTrack recognizes when a web address has already mapped a source project by a previous import. Imported source projects that have already been mapped in YouTrack aren't selectable. You can create multiple import jobs from the same source without importing duplicate data.

![Project Mapping step pairing source projects with YouTrack projects.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-import-project-mapping.png)

Procedure: To configure project mapping:

1. From the main navigation menu, select ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/settings.svg) `Administration > Integrations > Imports`.

2. Locate the GitHub projects you want to import.

* YouTrack checks for existing YouTrack projects with corresponding names. If it finds a YouTrack project with the same name as the GitHub repository, YouTrack suggests it as the target project.

* If there is no existing YouTrack project with the corresponding name, YouTrack suggests creating a new one.

3. If you want to change the target project, select another option from the corresponding dropdown on the list.

4. Click Start import to finalize the setup and start importing.

* Import starts.

## Import Options

After the initial import, the following controls are available in the sidebar:

![Import details with Resume, Edit, and Delete actions.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-import-details-options.png)

| Control | Description |
| --- | --- |
| Disable/Enable | Disable or enable the import. This lets you keep the settings for an import even if you aren't using it. |
| Resume | Immediately imports any changes made in the connected GitHub repository after the previous import. |
| Edit | Opens the integration settings page in edit mode. Use this option to connect to a different GitHub repository, update the login credentials, or update project mapping. |
| Delete | Deletes the current import settings. Imported content remains unless you choose to permanently delete affected projects. For details, see [Delete an Import](delete-import.html). |
| Continuous import | YouTrack periodically checks the target GitHub repository and imports updated and new items created since the last sync. |
| Download import log | Downloads the import log. Use this option to view and investigate errors that occurred during import. |



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/import-from-github.html](https://www.jetbrains.com/help/youtrack/cloud/import-from-github.html) · fetched 2026-09-22 08:34 Asia/Taipei*
