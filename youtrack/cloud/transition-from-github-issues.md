---
title: "Transition from GitHub Issues"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/transition-from-github-issues.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Transition from GitHub Issues

GitHub Issues is a built-in tool that helps users track bugs, tasks, and feature requests for their projects directly within their repositories. One of the key advantages for developers who work with GitHub issues is its proximity to the codebase. This makes it easy to associate updates in the source code with the issue that describes the rationale for the change.

This guide shows you how software developers can configure a project in YouTrack and manage their issues directly from an IDE. This approach differs slightly from the experience you get when working with issues in GitHub but gives you a similar sense of connection between your issues and the fixes applied in your codebase.

Another benefit of this approach is that once you've set it up, you can manage almost all of your work without leaving your IDE. This reduces context-switching, which saves you time and effort.

> **Note: Availability**
> The working process described here is supported by the [YouTrack Integration](https://plugins.jetbrains.com/plugin/8215-youtrack-integration) plugin. This plugin is available for all JetBrains IDEs and Android Studio.

## Project Configuration

YouTrack's standard projects for issue tracking are specifically created for working with software development projects. If you're just starting out and want to set up a project, you can go with the Default project template. This project template contains all the fields you would typically want to see when tracking issues as a software development team. It also has some workflows that can help you automate repetitive actions.

The main thing you're going to want to do is integrate your YouTrack project with the repository where you store your source code. When connecting your project to a version control system, the following features are enabled:

* References to YouTrack issue IDs in commit messages and branch names are automatically converted into links when you push changes to the repository. These commits are automatically added to the list of VCS changes in the activity stream for the issue in YouTrack. Each VCS change includes a direct link to the change details in the code repository.

* You can enter issue-related commands in your commit messages. This lets you update the issue status or add comments without even opening YouTrack.

* You can review the status of pull (merge) requests directly in the activity stream of any issue that is referenced in the title or description of the pull request.

* If you set up a connection with a repository in GitHub, you can add links to the repository by pasting commit hashes into the summary, description, comment, or string-type custom field in YouTrack issues.

YouTrack supports integration with a wide range of version control systems, including GitHub. To learn how to set up a connection between your YouTrack project and your version control system, see [Integrate with Version Control](integrate-with-version-control.html).

When you set up the connection, pay attention to the following settings:

![GitHub Integration settings with repository and processing options displayed.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-transition-vcs-settings.png)

| Setting | Description |
| --- | --- |
| Processing scheme for VCS changes | The VCS integration always checks commit messages for references to YouTrack issues. This setting determines whether to check commit messages for commands as well.     Using commit messages to apply commands to issues can be a quick and easy way to update the status of an issue when you’ve applied a fix in the codebase. However, because the interface for composing a commit message doesn't provide suggestions or validate commands, you need to know and understand the syntax for applying commands in YouTrack.     The optimal setting depends on whether you and your team choose to take advantage of this feature or not. Some teams prefer to ignore commands in commit messages to avoid unintended updates. If you decide to ignore commands as well, make sure to share this information with your team. Otherwise, people who try to apply commands in their commit messages might think that their commands are formulated incorrectly.   |
| Check branch names for issue references | This setting is especially important if your team uses a branch-per-task approach. When enabled, YouTrack can associate commits with issues based on issue IDs in branch names. |

## IDE Integration

If you're responsible for updating and maintaining sections of your codebase, you'll want to set up an environment where you can commit changes and view the code. One of the advantages of working with YouTrack is that you can work with the YouTrack Integration plugin. This plugin enables the following features in your IDE:

* View a list of issues that match specific search criteria directly in your IDE.

* Receive update notifications without switching to your email client or external messaging client.

* Enter a search query to locate a specific issue in the list.

* Open an issue as a task to set the work context in your IDE.

* Open a command dialog in your IDE to apply commands to issues in YouTrack.

* Track and record time spent working on YouTrack issues.

* Access YouTrack issues from the VCS history and comments in Java code. These references to issue IDs are automatically formatted as links to YouTrack. This mimics the functionality of the [Issue Navigation](issue-navigation.html) plugin, so you don't have to enable it separately.

To learn how to install and use this plugin in your IDE, see [YouTrack Integration Plugin](youtrack-integration-plugin.html).

## Terminology

As YouTrack and GitHub are both used as tools for managing software development projects, the terminology used for each is very similar. However, a few terms used in GitHub mean something slightly different in YouTrack. Use this list of terms to help you figure out where to find what you're looking for in YouTrack.

Workflows
: YouTrack and GitHub both use the term workflow to describe actions that are meant to occur in a predictable sequence, automating repetitive manual tasks. The main difference here is that GitHub workflows use actions that can be triggered by events that take place in your repository. This type of automation is supported by GitHub Actions.
:
:
:
: Workflows in YouTrack are generally triggered by events that take place in YouTrack itself but can also be scripted to run when triggered by events in the repository using webhooks.
:
:
:
: If you're looking to recreate the functionality supported by a workflow in GitHub, you'll want to check out the workflows supported in YouTrack. For a basic introduction, see [Workflows](workflow-guide.html).

Labels
: A label in GitHub is used to categorize issues, pull requests, and discussions. Similar functionality is supported in YouTrack using a combination of tags and custom fields.
:
:
:
: * To learn more about working with tags in YouTrack, see [Tag Issues](using-tags.html).
:
: * To learn how to categorize issues using custom fields, see [Update Field Values](update-field-values.html).

Milestones
: Milestones provide an additional level of organization and progress tracking to GitHub projects. When you import issues from GitHub Issues to YouTrack, these milestones are imported as values for a custom field with the name Milestone. The corresponding value is assigned to each issue associated with a specific milestone.
:
:
:
: Even though YouTrack doesn't provide specific features related to milestones, you can still use the values stored in the Milestone field to generate reports, organize sprints, configure Gantt charts, and more.

## Your Daily Routine

When you’ve installed the YouTrack Integration plugin in your IDE and have set up a connection between your YouTrack project and your repository, you're ready to start resolving issues and handling pull requests. Your day-to-day process could look something like this:

### Prioritize Your Work

With the help of the YouTrack Integration plugin, figure out what you need to work on.

You can use the query input field to find issues that are relevant to your work.

![IDE YouTrack tool window showing issues that match a search query.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-search-query-in-ide.png)

For example, if your team follows Scrum, you can find all the unresolved issues assigned to the current sprint and sort them by priority with a query like:

```
Board <project name>: {Current sprint} sort by: Priority asc #Unresolved
```

The query input field accepts the same search arguments that are available in YouTrack, which means you can filter for whichever issues are most important at the time. To learn how to search for issues in YouTrack, see [Issue Search](search-for-issues.html).

### Create a Branch or Changelist

Once you know what you want to work on, switch your working context.

The YouTrack Integration plugin lets you take an issue from the list and open it as a task. Options in the Open Task dialog let you choose whether you want to create a changelist and continue working in the current branch or create a new branch.

![Open Task dialog with Update issue state, Create changelist, and Create branch enabled.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-new-changelist.png)

There's also an option in the dialog that lets you update the issue state when opening the task. Use this option to automatically move the issue to an in-progress state.

### Handle the Issue

Next, write the code that addresses the issue you've started to work on. Each file you add or update is added to the changelist associated with the issue in your IDE.

As you're working to resolve the issue, you may want to post updates or add comments to the issue. Here are some of the things you can do without ever leaving your IDE:

* If you want to update an issue, you can use the Apply Command dialog. This dialog opens when you select the Open Command Dialog option in the toolbar of the YouTrack Integration tool window. ![Apply Command dialog previewing a State update for the selected issue.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-transition-command-dialog.png) For example, if the issue you're working on hasn't been assigned directly to you, you can update it with the simple command `for me`. You can also update the visibility of the issue, set values for custom fields, add tags, links, and more. To learn more about commands in YouTrack, see [Update Issues with Commands](commands.html).

* If you just want to post a comment, use the Add Comment option to open the command dialog for the selected issue with the `comment` command prefilled. ![Apply Command dialog with a comment entered for the selected issue.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-transition-add-comment.png) Enter the comment that you want to post to the issue, then press the Apply button.

* If the time tracking feature is enabled in your YouTrack project, you can track the amount of time you spend working on the issue directly in the YouTrack Integration plugin. Different options help you manage how you post work items to issues as you use the IDE.

### Commit Your Changes

Once you've finished applying and testing the changes to your codebase, you should be ready to commit the changes to the repository.

When committing your changes, you're prompted to add a commit message. The default naming conventions used for changelists and branches in the IDE include references to the YouTrack issue.

* For changelists, it uses the issue ID and summary.

* For branches, it takes the issue ID.

![IDE Tasks settings showing changelist and feature-branch name formats.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-ide-naming-conventions.png)

When you push your changes to the remote repository, the VCS integration parses the commit message for references to YouTrack issues. It automatically recognizes the pattern used for YouTrack issue IDs and adds the commit to the activity stream in the referenced issue. This provides a direct link between the issue and the set of changes in the repository, which means that anyone who has access to the repository can review these changes and see what was done to address the issue.

![Issue activity entry linking a pushed commit to its hash.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-transition-vcs-change.png)

### Open a Pull Request

This step in the working process depends on the tools your team uses to manage changes in the repository. Some will let you create a pull request in the VCS and create a discussion thread for reviewing the code before merging. Others will support this process using a merge request.

If this feature is supported by the remote repository, YouTrack adds references to these events in the activity stream of the related issue.

![Issue activity showing a pull request opened, submitted, and merged.](https://resources.jetbrains.com/help/img/youtrack/2026.2/github-transition-pull-request.png)

Other users who have access to the repository can follow these links to read any discussions that took place when reviewing the code. It also allows you to access and review conflicts that were encountered when a pull request was rejected.



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/transition-from-github-issues.html](https://www.jetbrains.com/help/youtrack/cloud/transition-from-github-issues.html) · fetched 2026-09-22 08:34 Asia/Taipei*
