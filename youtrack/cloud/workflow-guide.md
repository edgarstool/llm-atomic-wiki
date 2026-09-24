---
title: "Workflows"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/workflow-guide.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Workflows

Workflows in YouTrack let you customize and automate the lifecycle of issues in your project. With workflows, you can notify teams about events, enforce policies, execute periodic tasks, and support existing business processes.

## What's a Workflow?

In YouTrack, a workflow is a set of rules that can be attached to a project. These rules define a lifecycle for issues in a project and automate changes that can be applied to issues.

When you create a workflow, you can attach it to a project and activate specific rules. A workflow can contain several rules, but you can select which combination of rules you want to activate in different projects. YouTrack lets you attach a workflow to several projects and enable or disable rules for each project individually. For detailed instructions, see [Manage Workflows for Multiple Projects](attach-workflow-to-projects.html).

## Workflows and Apps

Workflows are part of the ecosystem for apps in YouTrack. Like other apps, workflows are used to enhance and customize functionality in YouTrack. When you create, upload, or install a workflow, it is included in the list of apps that are available for use in the system.

Before apps were introduced, workflows were the primary means of customization and automation in YouTrack. To minimize disruption for existing users, we still retain the interfaces for managing workflows separately from apps at the global and project level. However, the options for attaching and activating workflows in specific projects work exactly the same way on both the workflow and app administration pages.

Workflows can be included in an app package alongside widgets for other extension points. When this happens, these workflows are identified by the app that provides their functionality in the workflow list.

## Default Workflows

YouTrack provides several default workflows that cover the most general use cases. For example, workflows that automatically assign an issue to a subsystem owner or process duplicate issue.

Many default workflows are auto-attached. These workflows are attached automatically to all new projects.

For a complete list of the workflows that are bundled with YouTrack, see [Default Workflows](default-workflows.html).

## Custom Workflows

If you need a workflow that supports a specific use case, you can write your own. You can either customize a default workflow to support your use case or create a new workflow. For more information, see [Edit a Workflow](edit-workflow.html) and [Create a Workflow](create-workflow.html).

> **Note: YouTrack Subreddit**
> If you're having a hard time getting your workflows to do what you want them to, [join us on Reddit](https://www.reddit.com/r/YouTrack/). Connect with other users to find real solutions to challenging situations.

You can also use custom workflows that have been uploaded to the Custom Workflow Repository in [GitHub](https://github.com/JetBrains/youtrack-workflows) or as apps from the [JetBrains Marketplace.](https://plugins.jetbrains.com/)

## Workflow Constructor

The [Workflow Constructor](workflow-constructor.html) is a no-code tool that lets you transform a routine process into an automated workflow. Mix and match various conditions to determine exactly when the workflow rule should run, then specify what you want to happen with a range of available actions.

The constructor doesn't support all the conditions and actions that are available using workflows, but it covers the most typical use cases.

## Workflows in JavaScript

Workflows in YouTrack are written in JavaScript, even when built using the Workflow Constructor. If you're comfortable writing code, you can script automations that aren't supported using the drag-and-drop interface. You can write a workflow in any IDE that supports JavaScript, pack it into a ZIP file, and upload it to YouTrack.

> **Note: Webinar**
> [Watch a webinar](https://youtu.be/Jv6vGUPlLNk) that shows you how to work with the built-in workflow editor and write workflows in JavaScript.

In addition, we built a web-based workflow editor inside YouTrack. Here, you can write a workflow from scratch without leaving YouTrack.

For more information about workflows in JavaScript, refer to the corresponding section in the [Developer Portal for YouTrack and Hub](https://www.jetbrains.com/help/youtrack/devportal/Workflows-in-JavaScript.html).

## Workflow Filter

You can filter the list of workflows displayed on the Workflows administration page. Use the filter buttons to display all workflows or only those workflows app-based or user-created.

You can continue to filter your workflow list by name.

![Attach workflow to selected projects.](https://resources.jetbrains.com/help/img/youtrack/2026.2/workflow-filter.png)



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/workflow-guide.html](https://www.jetbrains.com/help/youtrack/cloud/workflow-guide.html) · fetched 2026-09-22 08:34 Asia/Taipei*
