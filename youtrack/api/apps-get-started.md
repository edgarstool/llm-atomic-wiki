---
title: "Apps"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/apps-get-started.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Apps

YouTrack apps are the primary package type for custom YouTrack functionality. An app can combine frontend widgets, backend JavaScript modules, settings, storage, custom MCP tools, and workflow rules.

Use the topics in this section to build, configure, test, and distribute apps.

| Topic | Description |
| --- | --- |
| [App Quick Start Guide](apps-quick-start-guide.html) | Create your first app following this quick start guide. |
| [Apps FAQ](apps-faq.html) | Find answers to common questions about planning, building, configuring, and distributing apps. |
| [Install an App from Marketplace](install-apps-from-marketplace.html) | Install apps from JetBrains Marketplace and update them from YouTrack. |
| [Enhanced DX for TypeScript Apps](apps-enhanced-dx-typescript.html) | Build apps with the experimental TypeScript-based Enhanced DX, including file-based routing and generated API types. |
| [App Package Overview](app-overview.html) | Get an overview of an app package structure and its main parts. |
| [App Manifest](app-manifest.html) | Learn more about the app manifest and the information stored there. |
| [Widgets](apps-widgets.html) | Add frontend widgets to supported locations in YouTrack. |
| [App Settings](app-settings.html) | Learn how to add settings that can be configured to customize and personalize features supported by your apps. |
| [Extension Properties](apps-extension-properties.html) | Learn how to extend core entities in YouTrack using custom properties. |
| [App Permissions](app-permissions.html) | Check the list of available permissions that let you manage who has access to the widgets supported by your apps. |
| [Authentication for Apps](apps-authentication.html) | Learn about the authentication approach and the permissions required to work with apps. |
| [App Visibility](app-visibility.html) | Learn how visibility can be used to limit access to an app in YouTrack. |
| [Global and Project Scopes](apps-global-project-level.html) | Learn how scopes are used to define availability for different features. |
| [Launch Checklist](app-launch-checklist.html) | Make sure that your app is ready for general use by checking all boxes in the launch checklist. |
| [App Use Cases](apps-use-cases.html) | Follow tutorials that demonstrate how apps solve practical use cases. |
| [App Reference](apps-reference.html) | Browse reference documentation for app modules and widget locations. |

## Sample Apps

Software Developers from the YouTrack team at JetBrains have published a collection of apps to a [public repository on GitHub](https://github.com/JetBrains/youtrack-apps). Feel free to browse the source code and use it as a springboard to develop your own widgets.

You can also explore the source code of the built-in YouTrack Demo App in YouTrack. The same source code is available in the [YouTrack Demo App repository](https://github.com/JetBrains/youtrack-demo-app).

## Apps and Pure Workflows

Workflow rules are backend JavaScript modules that can be included in an app package alongside widgets, HTTP handlers, custom MCP tools, settings, and storage declarations. The rules use the same constructors and JavaScript API whether the package contains only workflow rules or combines several module types.

For new development, start with an app when you expect the solution to grow, combine module types, or be distributed through JetBrains Marketplace. Create a [pure workflow](Quick-Start-Guide-Workflows-JS.html) when you only need rule-based automation and want to author and manage the rule-only package with the dedicated workflow tools in YouTrack.

If your app includes workflow rules, use the [Workflow Rule Types](Workflow-Rules.html) reference.

## YouTrack Subreddit

If you're having a difficult time getting your app to work the way you want it to, [join us on Reddit](https://www.reddit.com/r/YouTrack/). Connect with other users to find real solutions to challenging situations.



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/apps-get-started.html](https://www.jetbrains.com/help/youtrack/devportal/apps-get-started.html) · fetched 2026-09-22 08:34 Asia/Taipei*
