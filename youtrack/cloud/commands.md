---
title: "Update Issues with Commands"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/commands.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Update Issues with Commands

Commands let you modify the attributes of an issue or a set of issues in a single operation. For example, you can assign an issue, change the issue type, raise the priority, link to another issue, add tags, and even post a comment.

![The Apply Command dialog with multiple updates to apply in a single operation.](https://resources.jetbrains.com/help/img/youtrack/2026.2/new-command.png)

Using commands lets you update issues quickly without having to click through multiple menus. They provide a keyboard-centric alternative that reduces the need to constantly switch between keyboard and mouse during data entry. This can save a significant amount of time, especially when dealing with a large number of issues or tasks. YouTrack remembers your recent commands so you can quickly and consistently reuse them to update issues in a consistent manner.

## Access the Apply Command Dialog

In order to apply updates to multiple issues in a single operation, you need to YouTrack's dedicated interface for commands, the Apply Command dialog.

The Apply Command dialog is basically an extension of the interface for viewing issues in YouTrack. It is accessible from any issue view, including the Issues list, single issue view, and the popup windows used on agile boards and Gantt charts.

Procedure: To open the Apply Command dialog:

1. From the main navigation menu, select ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/issues.svg) Issues.

2. Open an issue in preview mode or single issue view.

3. Open the ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/more-options.svg) Show more menu in the issue toolbar and select ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/terminal.svg) Open command dialog.

You can also open the Apply Command dialog using a keyboard shortcut. This lets you keep your hands on the keyboard when updating an issue.

You can choose whether to open the command dialog using a predefined keyboard shortcut or by pressing any alphanumeric key. You can set this preference by selecting one of the available options for the Hotkey configuration.

![Hotkey configuration options for the Apply Command dialog.](https://resources.jetbrains.com/help/img/youtrack/2026.2/command-hotkey-configuration.png)

The standard keyboard shortcut to open the dialog is `Ctrl` + `Alt` + `J`. You can also opt to open the dialog when pressing any key. This applies to any alphanumeric key on a standard keyboard. Keys with auxiliary functions, like `Backspace`, `Enter`, and `Tab` are not mapped to this action.

## Working with Commands

The Apply Command dialog lets you apply a collection of updates to an issue in a single operation. Instead of updating the value for a single field or attribute using the mouse, you can provide instructions for multiple changes and apply them all at once.

Each command consists of a space-delimited keyword-value pair. For example:

* To assign the selected issue or a set of issues to yourself, enter `for me`.

* To assign issues to yourself and change their state to In progress, enter `for me state in progress`.

* To set the value for any field, enter the name of the field followed by the desired value.

As soon as you start typing, YouTrack displays a completion list with matching keywords or values.

![Completion suggestions in the Apply Command dialog.](https://resources.jetbrains.com/help/img/youtrack/2026.2/command-completion.png)

For link commands that reference other issues, YouTrack supports full-text search. This feature lets you filter the list of issues to match your search criteria without having to specify the exact issue ID. For example, you can enter `duplicates toolbar` to show only issues that contain the word "toolbar" and select an issue from the list.

## Apply Commands to Issues

With commands, you can apply changes to multiple issues quickly and efficiently.

The required permissions vary based on the type of command to be applied.

Procedure: To apply a command to one or more issues:

> **Tip:**
> Requires permissions: Read Issue, Update Issue, Update Watchers, Create Comment, Link Issues, Update Work Item

1. From the main navigation menu, select ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/issues.svg) Issues.

2. Select one or more issues in the Issues list.

* To select multiple issues, use the arrow keys and Space bar or hold `Shift` and press the `Up Arrow` or `Down Arrow`.

3. Press `Ctrl` + `Alt` + `J` or any alphabetic key, depending on your current hotkey configuration.

You can also click the ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/terminal.svg) Open command dialog button in the toolbar.

* The Apply Command dialog opens.

4. In the Command input field, enter one or more commands.

5. Enter an optional comment in the Comment text box.

6. Click the Apply button or press `Ctrl` + `Enter`.

* The command is applied and the comment is added to the selected issues.

To discard the commands and the comment, click the Cancel button or press `Esc`.

> **Note:**
> This procedure can also be applied when working with issues on agile boards, Gantt charts, and single issue view.

For a list of commands that can be applied to issues, see  [Command Reference](command-reference.html).

## Apply Commands Without Notification

When you apply commands without notification, the updates are applied to the selected issues without sending update notifications to users who subscribe to these changes.

This feature comes in handy when you apply batch changes to several issues at once and don't want to spam your team with notifications. You might choose to apply commands without notification when, for example, you move issues to the next release version or add issues to the backlog.

This option is only visible when you have permission to apply commands without notification in a project. To perform this action, you need all the permissions that are required to apply commands to an issue, plus the Apply Commands Silently permission.

Procedure: To apply a command without notification:

1. From the main navigation menu, select ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/issues.svg) Issues.

2. Select one or more issues in the Issues list.

3. Press `Ctrl` + `Alt` + `J` or any alphabetic key, depending on your current hotkey configuration.

* The Apply Command dialog opens.

!['Apply Command' dialog with 'Apply without notification' highlighted.](https://resources.jetbrains.com/help/img/youtrack/2026.2/apply-command-without-notice.png)

4. In the Command input field, enter a command.

5. Enter an optional comment in the Comment field.

6. Click the Apply without notice button or press `Ctrl` + `Shift` + `Enter`.

Click the Apply without notice button or press `Control` + `Shift` + `Return`.

* The command is applied and the comment is added to the selected issues without generating notification messages.

> **Note:**
> This procedure can also be applied when working with issues on agile boards, Gantt charts, and single issue view.

## Sample Commands

The following table provides a few examples of common YouTrack commands:

| Command | Description |
| --- | --- |
| `assigned to me priority major`      or      `for me priority major`   | Assigns the selected issues to the current user, sets the priority of each issue to Major. |
| `state fixed`                   | Sets the value of the State field for the selected issues to Fixed. |
| `region europe` | Sets the value of the Region field to Europe. |
| `duplicates TS-2405`                   | Adds a Duplicates link in the selected issues to the issue with the ID TS-2405. An Is duplicated by link for each selected issue is also added to the issue with the ID TS-2405.  |
| `type Cosmetics tag fix it this week` | Associates the selected issue with the "fix it this week" tag and sets the value of the Type field to Cosmetics. |
| `remove tag fix it this week` | Removes the "fix it this week" tags from the selected issues. |
| `remove Fix versions 2025.3` | Removes the value 2025.3 from the multi-value Fix versions field for the selected issues, while preserving any other values in the field. |
| `project TeamCity` | Moves the selected issues to the TeamCity project. |
| `subsystem Documentation` | Moves the selected issues to the Documentation subsystem. |

For more examples that show you how to reference various issue attributes, see [Command Reference](command-reference.html).

## See also

### How-Tos

[Apply Commands in VCS Commits](apply-commands-in-vcs-commits.html)

### Reference

[Command Reference](command-reference.html)



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/commands.html](https://www.jetbrains.com/help/youtrack/cloud/commands.html) · fetched 2026-09-22 08:34 Asia/Taipei*
