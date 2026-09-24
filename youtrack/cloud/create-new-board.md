---
title: "Create an Agile Board"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/create-new-board.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Create an Agile Board

You can create an agile board in YouTrack and customize its settings to support different agile methodologies. Whether you follow scrum, kanban, a combination of the two, or a concoction that is only known to your imagination, YouTrack's agile boards are flexible enough to accommodate.

You can create and share a board with your team, or build a personal board to manage your own work.

## Permissions

The only permission that is actually required to create an agile board in YouTrack is Read Issue. As long as you have permission to read issues, you can create a board and monitor the progress of issues in the project. For example, users with the default Issue Reader role in a project can create a board and use it to track issues. However, this role has a limited set of permissions. Their ability to interact with issues on the board is restricted.

To create and configure a board that you and your team can use to update issues in a project, you need permission to perform a wider range of actions. If you encounter any problems when you follow this setup, check that you have access to the following permissions:

| Action | Permission |
| --- | --- |
| Add projects to the board. | The list of projects is restricted to projects where you have the Read Issue permission. Read Project permission is not required. |
| Let other users view and use the board. | Requires membership in a group where the Share Custom View feature is active. To learn more about this feature, see [Optional Features](experimental-features.html#group-specific-features).     To be able to view and select users in the corresponding settings, you also need the Read User Basic permission.     To view and select groups, you must belong to a group where the Read Groups feature is active or have either Update Project or Low-level Admin Read permission.   |
| Add issues to the board. | Requires Create Issue. |

The Can view and use the board and Can edit board settings options set the visibility for your board. When both options are set to Owner, your board is private. However, if you use the Can view and use the board option to restrict the visibility of the board, users with the Low-level Administration permission can access and edit the settings for this board as well.

## Creating a Board

This procedure walks you through the basic steps. For more detail, browse the other topics in this section of the documentation.

Procedure: To create an agile board:

1. From the main navigation menu, select ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/agile-board.svg) Agile Boards.

* If you already have access to one or more boards, the board that you last viewed is displayed.

* If you don't have access to any of the boards in your installation, the Create an Agile Board page opens immediately. If this is the case, skip to step 3 and select a template for your board.

2. Click the New... button, and select Board.

![Agile board creation menu with Board highlighted.](https://resources.jetbrains.com/help/img/youtrack/2026.2/agile-board-create-menu.png)

3. Select a template:

![New Agile Board page with the five board templates available.](https://resources.jetbrains.com/help/img/youtrack/2026.2/agile-templates.png)

| Template | Description |
| --- | --- |
| Scrum board | Pre-configured for scrum development teams. Automatically set for tracking feature development over a series of scheduled sprints. |
| Kanban board | Pre-configured for teams that follow a kanban methodology. Also a great option for personal boards. |
| Version-based board | Pre-configured to link sprints to the value in a custom field that stores a `version` type. Designed to mimic the behavior of agile boards in earlier versions of YouTrack where you can use a query to filter the visibility of cards on the board. |
| Custom board | Generated with a default configuration that you adjust to any work flow. |
| Personal board | A kanban-style board that shows only issues that are assigned to the current user. |

For a list of settings that are pre-configured each template, see [Agile Board Templates](agile-board-templates.html).

* The New Board page opens. ![New Scrum Board form with empty Name and Projects fields.](https://resources.jetbrains.com/help/img/youtrack/2026.2/new-board-settings.png)

4. Enter a name for the new board.

5. Add projects that you want to manage on the board.

![New Scrum Board form with Team Scrum and YouTrack Mobile selected.](https://resources.jetbrains.com/help/img/youtrack/2026.2/new-board-projects.png)

If you want to manage multiple projects on the board, click the Add all projects where I am team member link. You can add and remove projects as required.

6. Configure the visibility settings of the board. Select the users and groups and project teams whose members can view and use the board and edit board settings.

* For the Can view and use the board setting, use the issue readers option to automatically grant read access to any user who has Read Issue permission in the projects that are listed in the Projects setting.

* For the Can edit board settings setting, use the project updaters option to automatically grant access to any user who has Update Project permission in the projects that are listed in the Projects setting.

![New Scrum Board form with projects and board visibility permissions configured.](https://resources.jetbrains.com/help/img/youtrack/2026.2/new-board-visibility.png)

By default, the Can view and use the board and Can edit board settings settings are set to Owner. This means that the new board is private. However, if you make the board visible to other users, users with the Low-level Administration permission in this group can access and edit the settings for this board as well.

7. Click the Create board button.

* The agile board is created and ready for use.

* YouTrack lets you freely reconfigure your agile boards as you fine-tune and adapt your project management methodologies. If you want to experiment with additional settings, click the ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/settings.svg) icon in the toolbar to expand the Board Settings panel. To learn more about the settings for agile boards, see [Agile Board Settings](agile-board-settings.html).

## See also

### How-Tos

[Configure an Agile Board](configure-agile-board.html) [Merge Board Columns](merged-columns.html)



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/create-new-board.html](https://www.jetbrains.com/help/youtrack/cloud/create-new-board.html) · fetched 2026-09-22 08:34 Asia/Taipei*
