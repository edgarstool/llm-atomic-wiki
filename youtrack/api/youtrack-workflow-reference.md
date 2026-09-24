---
title: "Workflows (Dev)"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/youtrack-workflow-reference.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Workflows

Workflows in YouTrack let you customize and automate the lifecycle of issues in your project. With workflows, you can notify teams about events, enforce policies, execute periodic tasks, and support existing business processes.

## Pure Workflows and Apps

Workflow rules are JavaScript modules that automate behavior in YouTrack. They use the shared backend runtime and the `@jetbrains/youtrack-scripting-api` package.

An app can include workflow rules together with widgets, HTTP handlers, custom MCP tools, settings, and other app components. A pure workflow is a rule-only package created and managed with the dedicated workflow tools in YouTrack.

Pure workflows are the long-standing YouTrack automation model and remain useful for focused, project-level automation. For new solutions that may combine automation with UI, endpoints, configuration, or distribution through JetBrains Marketplace, start with an [app](apps-get-started.html).

The rule code uses the same constructors, rule contexts, requirements, transaction model, and JavaScript API in either package type. See [Workflow Rule Types](Workflow-Rules.html) for shared rule authoring guidance.

## Workflows in JavaScript

YouTrack lets you write workflows in JavaScript. You can write a workflow in any IDE that supports JavaScript, pack it into a ZIP file, and upload it to YouTrack.

> **Note: Webinar**
> [Watch a webinar](https://youtu.be/Jv6vGUPlLNk) that shows you how to work with the built-in workflow editor and write workflows in JavaScript.

In addition, we built a web-based workflow editor inside YouTrack. Here, you can write a workflow from scratch without leaving YouTrack.

## What's a Workflow?

In YouTrack, a pure workflow is a set of rules that can be attached to a project. These rules define a lifecycle for issues in a project and automate changes that can be applied to issues.

When you create a workflow, you can attach it to a project and activate specific rules. A workflow can contain several rules, but you can choose which combination of rules you want to activate in different projects. YouTrack lets you attach a workflow to several projects and enable or disable rules for each project individually.

## Workflow Scope

Workflows are best suited for automation that reacts to changes in issues and related entities in projects where the workflow is attached. Use them to enforce issue lifecycle rules, update issue fields, add comments or tags, manage links and work items, send notifications, and run scheduled checks against issue search results.

Some workflow rules can also work with articles, comments, and attachments. However, most workflow automation is still centered on an issue, a project, or another entity that triggers a rule. A workflow runs in the context of this entity and the rule requirements that you declare in the script.

Workflow requirements let you reference custom fields, field values, projects, users, groups, tags, saved searches, and issue link types that must be available for the rule to work. These requirements act as dependencies for the rule. They don't turn workflows into a tool for administering the YouTrack instance.

For tasks like creating or restructuring custom fields, managing projects, administering users or groups, assigning roles and permissions, or changing global configuration, use the YouTrack administration UI, [YouTrack REST API](youtrack-rest-api.html), or [YouTrack JavaScript Ecosystem](apps-documentation.html) instead.

## Default Workflows

YouTrack provides several default workflows that cover the most general use cases. For example, workflows that automatically assign an issue to a subsystem owner or process duplicate issue.

Many default workflows are auto-attached. These workflows are attached automatically to all new projects.

## Custom Workflows

If you need a workflow that supports a specific use case, you can write your own. You can either customize a default workflow to support your use case or create a new workflow.

> **Note: YouTrack Subreddit**
> If you're having a hard time getting your workflows to do what you want, [join us on Reddit](https://www.reddit.com/r/YouTrack/). Connect with other users to find real solutions to challenging situations.

You can also use custom workflows that have been uploaded to the Custom Workflow Repository in [GitHub](https://github.com/JetBrains/youtrack-workflows).

## Workflow Constructor

If you are not familiar with JavaScript, give the [Workflow Constructor](https://www.jetbrains.com/help/youtrack/cloud/workflow-constructor.html) a try instead. You can build workflows using the constructor without any programming knowledge.



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/youtrack-workflow-reference.html](https://www.jetbrains.com/help/youtrack/devportal/youtrack-workflow-reference.html) · fetched 2026-09-22 08:34 Asia/Taipei*
