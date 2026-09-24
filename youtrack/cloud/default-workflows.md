---
title: "Default Workflows"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/default-workflows.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Default Workflows

YouTrack provides several default workflows that cover the most general use cases. For example, workflows that automatically assign an issue to a subsystem owner or process duplicate issues.

Many default workflows are auto-attached. These workflows are attached automatically to all new projects.

## Edit Default Workflows

You can customize the default workflows to support your actual use cases like any other workflow on your YouTrack server. For each workflow on the Workflows page, the date of the most recent change and the change author are displayed in the Last Update column.

## Restore Default Workflows

If needed, you can roll back default workflows to their initial state with the restore options on the Workflows page.

![Workflows page showing workflows restore.](https://resources.jetbrains.com/help/img/youtrack/2026.2/workflows-restore.png)

The following options are available:

| Option | Description |
| --- | --- |
| Restore all | Reverts the changes to all default workflows. |
| Restore selected | Reverts the changes to all selected default workflows. |

When you upgrade YouTrack, updates are only applied to default workflows that have not been modified. If you want to apply updates to an edited workflow, use the Restore all or Restore selected option. These options overwrite the default workflows with the definitions that are stored in the database. Any changes that you've made to default workflows are lost. If you wish to keep your changes, make a copy of the default workflow with another name before you restore the default workflow definitions.

> **Note:**
> The restore options are available only when one or more default workflows have been modified. If all default workflows already match the definitions that are stored in the database, the options remain disabled.



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/default-workflows.html](https://www.jetbrains.com/help/youtrack/cloud/default-workflows.html) · fetched 2026-09-22 08:34 Asia/Taipei*
