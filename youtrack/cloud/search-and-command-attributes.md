---
title: "Search Query Reference"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/search-and-command-attributes.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Search Query Reference

This page provides a list of attributes and keywords that are used in YouTrack query language. You'll also find a complete list of operators, symbols, and relative date parameters that are recognized in search queries.

Several references on this page are not available in [Simple Search](smart-filters.html). Switch to [Advanced Search](attribute-based-search.html) to access them.

## Issue Attributes

Every issue has base attributes that are set automatically by YouTrack. These include the issue ID, the user who created or applied the last update to the issue, and so on.

These search attributes represent an `<Attribute>` in the [Search Query Grammar](#search-query-grammar). Their values correspond to the `<Value>` or `<ValueRange>` parameter.

Attribute-based search uses the syntax `attribute: value`.

* You can specify multiple values for the target attribute, separated by commas.

* Exclude specific values from the search results with the syntax `attribute: -value`.

In many cases, you can omit the attribute and reference values directly with the `#` or `-` symbols. For additional guidelines, see [Advanced Search](attribute-based-search.html).

### attachment text

```
attachment text: <text>
```

Returns issues that include image attachments with the specified text.

| Values | Accepts text. Values are parsed as described for [Text Search](full-text-search.html). |
| Aliases | image text |
| Example | To find issues in the Design project that have images containing text `design mockup`, enter `project: Design attachment text: design mockup`.  |

### attachments

```
attachments: <text>
```

Returns issues that include attachments with the specified filename.

| Values | Accepts text. If the filename contains spaces, set multiple words in quotes or braces. |
| Example | To find unresolved issues that are assigned to me and have an attachment with a filename that starts with sketch, enter `#unresolved for: me attachments: sketch*`.  |

### Board

```
Board <board name>: <sprint name>
```

Returns issues that are assigned to the specified sprint on the specified agile board. To find issues that are assigned to agile boards with sprints disabled, use `has: <board name>`.

| Values | Accepts the name of a sprint. Enclose sprint names with more than one word in braces.     Substitute the sprint name with `{current sprint}` to find issues that are assigned to the current sprint. To learn how YouTrack identifies the current sprint, see [The Current Sprint](work-with-sprints.html#current-sprint).     This attribute can also be referenced as a single value with the syntax `#<sprint name>` or `-<sprint name>`.   |
| Example | To find all issues that are assigned to sprint 21 on the YouTrack Scrum board, enter `Board YouTrack Scrum: {sprint 21}`. |

### cc recipients

```
cc recipients: <user>
```

Returns tickets where the specified users are added as CCs.

| Values | Accepts a user. |
| Example | To find all tickets where the agent with the username minnie.terry is added as a CC recipient, enter `cc recipients: minnie.terry`.  |

### customer groups

```
customer groups: <group>
```

Returns helpdesk tickets that are shared with the specified customer group.

| Values | Accepts a customer group. |
| Example | To find all tickets that are shared with the customer group Acme Support, enter `customer groups: {Acme Support}`. |

### code

```
code: <text>
```

Returns issues that contain word forms that match the specified word or words that are formatted as code in the issue description or comments. This includes matches that are formatted as inline code spans, indented and fenced code blocks, and stack traces.

| Values | Accepts text. Values are parsed as described for [Text Search](full-text-search.html). |
| Example | To find unresolved issues in the TS project with the words hello and world that are formatted as code in a description or comment, enter `in: TS #unresolved code: {hello world}`.  |

### commented

```
commented: <date> | <period>
```

Returns issues to which comments were added on the specified date or within the specified period.

| Values | Accepts a date, custom period, or [relative date parameter](#relative-date-parameters).     This attribute also accepts a user or group, but the unfiltered list of auto-completion options shows date-related values first. To see suggestions for users and groups, use the [commenter](#commenter) attribute.   |
| Example | To find all issues in the YouTrack project that are assigned to the current user and were commented during the last week, enter `#YouTrack for: me commented: {Last Week}`.  |

### commenter

```
commenter: <user> | <group>
```

Returns issues that were commented by the specified user or by a member of the specified group.

| Values | Accepts a user or group. |
| Aliases | commented by |
| Example | To find all issues that were created today, assigned to the current user, and commented by the user with the username John, enter `created: today for: me commenter: John`. |

### comments

```
comments: <text>
```

Returns issues that contain word forms that match the specified word or words in a comment.

| Values | Accepts text. Values are parsed as described for [Text Search](full-text-search.html). |
| Example | To find issues in the JT project with the type Feature in the Agile management subsystem that contain the word burndown in one or more comments, enter `in: JT #Feature Subsystem: {Agile management} comments: burndown`.  |

### created

```
created: <date> | <period>
```

Returns issues that were created on a specific date or within a specified time frame.

| Values | Accepts a date, custom period, or [relative date parameter](#relative-date-parameters). This attribute also accepts a user or group, but the unfiltered list of auto-completion options shows date-related values first. To see suggestions for users and groups, use the [reporter](#reporter) attribute. |
| Example | To find all issues that were created today and are assigned to the current user, enter `#my #issues created: today` or `#my created: today`.  |

### description

```
description: <text>
```

Returns issues that contain word forms that match the specified word or words in the issue description.

| Values | Accepts text. Values are parsed as described for [Text Search](full-text-search.html). |
| Example | To find unresolved issues in the GR project with the string groovy.lang.resolve.CollectClassMembersUtil in the description, enter `in: GR #unresolved description: "groovy.lang.resolve.CollectClassMembersUtil"`.  |

### document type

```
document type: Issue | Ticket
```

Returns either issue or ticket type documents.

| Values | Accepts the keywords `Issue` or `Ticket`.   |
| Example | To find all tickets assigned to you without any issues assigned to you, enter `#{Assigned to me} document type: Ticket`. |

### Gantt

```
Gantt: <chart name>
```

Returns issues that are assigned to the specified Gantt chart.

| Values | Accepts the name of a Gantt chart. Enclose chart names with more than one word in braces.   |
| Example | To find all issues that are assigned to a Gantt chart named Migrate to YouTrack, enter `Gantt: {Migrate to YouTrack}`. |

### has

```
has: <attribute>
```

The `has` keyword functions as a Boolean search term. When used in a search query, it returns all issues that contain a value for the specified attribute. Use the minus operator (`-`) before the specified attribute to find issues that have empty values.

For example, to find all issues in the TST project that are assigned to the current user, have a duplicates link, have attachments, but do not have any comments, enter `in: TST for: me has: duplicates , attachments , -comments`.

You can use the `has` keyword in combination with the following attributes:

| Attribute | Description |
| --- | --- |
| [attachments](#attachments) | Returns issues that have attachments.     > **Note:** > Before the `has` syntax was introduced, we supported this query with the keyword `{has attachments}`. This syntax is still supported for backward compatibility but is not shown as an option in auto-completion.    |
| boards | Returns issues that are assigned to at least one agile board. When used with an exclusion operator (`-`), returns issues that aren't assigned to any boards.   |
| [Board &lt;board name&gt;](#board-name) | Returns issues that are assigned to the specified agile board. |
| [comments](#comments) | Returns issues that have one or more comments. |
| [description](#description) | Returns issues that do not have an empty description. |
| [&lt;field name&gt;](#search-attributes-custom-fields) | Returns issues that contain any value in the specified custom field. Enclose field names that contain spaces in braces. |
| [Gantt](#board-name) | Returns issues that are assigned to any Gantt chart. |
| [&lt;link type name&gt;](#issue-links) | Returns issues that have links that match the specified outward name or inward name. Enclose link names that contain spaces in braces.     For example, to find issues that are linked as subtasks to parent issues, use:      ``` has: {Subtask of} ```     To find issues that aren't linked to a parent issue, use:      ``` has: -{Subtask of} ```    |
| [links](#links) | Returns issues that have any issue link type. |
| [star](#tag) | Returns issues that have the star tag for the current user. |
| underestimation | Returns issues where the total spent time is greater than the original estimation value. |
| [vcs changes](#vcs-changes) | Returns issues that contain vcs changes. |
| [votes](#voter) | Returns issues that have one or more votes. |
| [work](#Time-Tracking-Search) | Returns issues that have one or more work items. |

### issue ID

```
issue ID: <issue ID>, #<issue ID>
```

Returns an issue that matches the specified issue ID. This attribute can also be referenced as a single value with the syntax `#<issue ID>` or `-<issue ID>`. When the search returns a single issue, the result is displayed in single issue view.

* If you don't use the syntax for an attribute-based search (`issue ID: <value>` or `#<value>`), the input is also parsed as a [text search](full-text-search.html). In addition to any issue that matches the specified issue ID, the search results include any issue that contains the specified ID in any text attribute.

* If you set the issue ID in quotes, the input is only parsed as a text search. The search results only include issues that contain the specified ID in a text attribute.

Note that even when an issue ID is parsed as a text search, the results do not include issue links. To find issues based on issue links, use the [links](#links) attribute or reference a [specific link type](#issue-links).

| Values | Accepts only an issue ID. |
| Example | To find an issue with the ID JT-4232, enter `issue ID: JT-4232` or `#JT-4232`.       * If you enter the search as `JT-4232`, the results include the issue JT-4232 and any issue that contains this substring in the summary, description, or comment text.    * If you enter the search as `"JT-4232"`, the results only include issues that contain this substring in the summary, description, or comment text.   |

### links

```
links: <issue ID>
```

Returns all issues that contain links to the specified issue.

| Values | Accepts only an issue ID. |
| Example | To find all issues in the TEST project that are linked to the issue ABC-4532, enter `in: TEST links: ABC-4532`.  |

### looks like

```
looks like: <issue ID>
```

Returns issues in which the issue summary or description contains words that are found in the issue summary or description in the specified issue. Issues that contain matching words in the issue summary are given higher weight when the search results are sorted by relevance.

| Values | Accepts only an issue ID. |
| Example | To find all issues in the TEST project that contain matching words that are used in the issue summary and description for ABC-4532, enter `in: TEST looks like: ABC-4532`.  |

### mentioned in

```
mentioned in: <issue id>
```

Returns issues with issue IDs referenced in the description or a comment of the target issue. Issue IDs in supplemental text fields aren't included in the search results.

| Values | Accepts only an issue ID. |
| Example |    To find all issues mentioned within the description or comments of issue JT-4232, enter `mentioned in: JT-4232`.    |

### mentions

```
mentions: <issue id>, <user>
```

Returns issues that contain either @mention for the specified user or issue IDs referenced in the description or a comment. User mentions and issue IDs in supplemental text fields aren't included in the search results.

| Values | Accepts an issue ID or user. |
| Example |    To find all issues that mention a user with the username valerie but do not contain mentions that reference your account, enter `mentions: valerie, -me`.     To find all issues that mention an issue with the issue ID JT-4232 in the description or comments, enter `mentions: JT-4232`.    |

### organization

```
organization: <organization name>
```

Returns issues that belong to the specified organization. This attribute can also be referenced as a single value.

| Values | Accepts an organization name. |
| Example | To find all issues that belong to the Test cluster organization that are assigned to the current user, enter `#my organization:{Test cluster}` or `#my #{Test cluster}`.             |

### project

```
project: <project name> | <project ID>
```

Returns issues that belong to the specified project. This attribute can also be referenced as a single value.

| Values | Accepts a project name or project ID. |
| Aliases | in |
| Example | To find all issues that belong to the ReSharper project that are assigned to current user, enter `#my #ReSharper #issues` or `#my #ReSharper`.             |

### reporter

```
reporter: <user> | <group>
```

Returns issues and tickets that were created by the specified user or a member of the specified group, including tickets created on behalf of the specified user. Use `me` to return issues that were created by the current user.

| Values | Accepts a user or group. |
| Aliases | by, created by, reported by |
| Example | To find all bugs reported by the user with the username yarko except for those with minor or normal priority, enter `#bug reporter: yarko -minor -normal` or `#bug by: yarko -minor -normal`.  |

### resolved date

```
resolved date: <date> | <period>
```

Returns issues that were resolved on a specific date or within a specified time frame.

| Values | Accepts a date, custom period, or [relative date parameter](#relative-date-parameters). |
| Example | To find all issues that are resolved in the MPS project this month, enter `#MPS resolved date: {this month}`. |

### saved search

```
saved search: <saved search name>
```

Returns issues that match the search criteria of a saved search. This attribute can also be referenced as a single value with the syntax `#<saved search name>` or `-<saved search name>`.

| Values | Accepts the name of a saved search. |
| Example | To find issues that match a search query that was saved as resharper this week, enter `saved search: {resharper this week}`.  |

### submitter

```
submitter: <user> | <group>
```

Returns issues that were submitted by the specified user or a member of the specified group on behalf of another user. Use `me` to return issues that were submitted by the current user.

| Values | Accepts a user or group. |
| Aliases | submitted by |
| Example | To find all tickets submitted by the agent with the username minnie.terry on behalf of other users, enter `submitter: minnie.terry` or `submitted by: minnie.terry`.  |

### summary

```
summary: <text>
```

Returns issues that contain word forms that match the specified word or words in the issue summary.

| Values | Accepts text. Values are parsed as described for [Text Search](full-text-search.html). |
| Example | To find issues with either scrum or board in the summary, enter `summary: {scrum board}`.       To find issues in the TS project that are assigned to the user john.johnson with the words Agile management in the summary (appearing in this order), enter `in: TS assigned to: john.johnson summary: "Agile management"`.     |

### tag

```
tag: <tag name>
```

Returns issues that match a specified tag. This attribute can also be referenced as a single value with the syntax `#<tag name>` or `-<tag name>`

| Values | Accepts the name of a tag. |
| Aliases | tagged as |
| Example | To find all issues with the priority Minor that have the myparser tag, enter `#minor tag: myparser` or `#minor #issues tagged as: myparser`.  |

### updated

```
updated: <date> | <period>
```

Returns issues where the most recent change occurred on a specific date or within a specified time frame.

| Values | Accepts a date, custom period, or [relative date parameter](#relative-date-parameters).     This attribute also accepts a user or group, but the unfiltered list of auto-completion options shows date-related values first. To see suggestions for users and groups, use the [updater](#updater) attribute.   |
| Example | To find all issues that are resolved in the MPS project where the most recent changes were applied this month, enter `#MPS updated: {this month} #resolved`. |

### updater

```
updater: <user> | <group>
```

Returns issues that were last updated by the specified user or a member of the specified group. Use `me` to return issues to which you applied the last update.

| Values | Accepts a user or group. |
| Aliases | updated by |
| Example | To find all major issues that you were the last person to update yesterday, enter `updater: me updated: yesterday priority: major` or `updater: me #yesterday #major`.  |

### vcs changes

```
vcs changes: <commit hash>
```

Returns issues that contain vcs changes that were applied in the commit object that is identified by the specified SHA-1 commit hash.

| Values | Accepts a full SHA-1 commit hash. The short version of the commit hash is not recognized. |
| Example | To find an issue that contains vcs changes for a specific commit, enter `vcs changes: f9b78079c40660c81f5df421b8ce7fc27497c4c2`.  |

### visible to

```
visible to: <user> | <group>
```

Returns issues that are visible to the specified user or a member of the specified group.

| Values | Accepts a user or group.     You can also use the keyword `{issue readers}`.   |
| Example | To find all major issues for which the visibility is restricted to members of the YouTrack Team, enter `priority: major visible to: {YouTrack Team}`.     To find issues for which the visibility is restricted to any set of users and groups, enter `visible to: -{issue readers}`.    |

### voter

```
voter: <user> | <group>
```

Returns issues that have votes from the specified user or a member of the specified group.

| Values | Accepts a user or group. |
| Aliases | voted by |
| Example | To find all major issues that have votes from members of the YouTrack Team, enter `priority: major voter: {YouTrack Team}`.  |

## Custom Fields

You can find issues that are assigned specific values in a custom field. As with other issue attributes, you use the syntax `attribute: value` or `attribute: -value`. In this case, the attribute is the name of the custom field. In most cases, you can reference values directly with the `#` or `-` symbols.

For custom fields that are assigned an empty value, you can reference this property as a value. For example, to search for issues that are not assigned to a specific user, enter `Assignee: Unassigned` or `#Unassigned`. If the field is not assigned an empty value, find issues that do not store a value in the field with the syntax `<field name>: {No <field name>}` or `has: -<field name>`.

This section lists the search attributes for default custom fields. Note that default fields and their values can be customized. The actual field names, values, and aliases may vary.

### Affected versions

```
Affected versions: <value>
```

Returns issues that were detected in a specific version of the product.

| Values | Accepts any of the values that are stored in the Affected versions field as well as the keywords `Released` and `Archived`. |
| Aliases | affects, affecting, that affect |
| Example | To find all issues that are assigned to the user John that were detected in version EAP3 of the product, enter `Affected versions: EAP3 assigned to: John`, or `#issues affecting: EAP3 assigned to: John`, or `#issues that affect: EAP3 assigned to: John`.  |

### Assignee

```
Assignee: <user> | <group>
```

Returns all issues that are assigned to the specified user or a member of the specified group.

| Values | Accepts a user or group. |
| Aliases | assigned to, for |
| Example | To find all issues with priority Show-stopper that are assigned to the user with the username John, enter `Priority: Show-stopper Assignee: John` or `#Show-stopper for: John`  |

### Fix versions

```
Fix versions: <value>
```

Returns issues that were fixed in a specific version of the product.

| Values | Accepts any of the values that are stored in the Fix versions field as well as the keywords `Released` and `Archived`. |
| Aliases | fix for, fixed in, version |
| Example | To find all issues that are assigned to the user John that were fixed in version EAP3 of the product, enter `for: John fixed in: EAP3`.  |

### Fixed in build

```
Fixed in build: <value>
```

Returns issues that were fixed in the specified build.

| Values | Accepts any of the values that are stored in the Fixed in build field as well as the keyword `Archived`. |
| Aliases | build, fix build, fix for, fixed in |
| Example | To find all issues that are assigned to the user John that were fixed in build number 36724, enter `for: John Fixed in build: 36724` or `for: John fixed in: 36724`.  |

### Priority

```
Priority: <value>
```

Returns issues that match the specified priority level.

| Values | Accepts any of the values that are stored in the Priority field as well as the keyword `Archived`. |
| Example | To find all unresolved issues with the priority Show-stopper that are assigned to the current user, enter `#my #unresolved #show-stoppers` or `#my state: unresolved priority: show-stopper`.  |

### State

```
State: <value> | Resolved | Unresolved
```

Returns issues that match the specified state.

The Resolved and Unresolved states cannot be assigned to an issue directly, as they are properties of specific values that are stored in the State field.

By default, Fixed, Won't fix, Duplicate, Incomplete, Obsolete, and Can't reproduce states are set as Resolved.

The Submitted, Open, In Progress, Reopened, and To be discussed states are set as Unresolved.

| Values | Accepts any of the values that are stored in the State field as well as the keywords `Resolved`, `Unresolved`, and `Archived`. |
| Example | To find all critical bugs that are assigned to the user with the username john that were closed with the state Won't fix, enter `#{won't fix} #critical #bug for: john` or `state: {won't fix} priority: critical #bug for: john`.  |

### Subsystem

```
Subsystem: <value>
```

Returns issues that are assigned to a specific subsystem within a project.

| Values | Accepts any of the values that are stored in the Subsystem field as well as the keyword `Archived`. |
| Aliases | in |
| Example | To find all issues that belong to the Smart UI subsystem, enter `subsystem: {smart ui}`. |

### Type

```
Type: <value>
```

Returns issues that match the specified issue type.

| Values | Accepts any of the values that are stored in the Type field as well as the keyword `Archived`. |
| Example | To find all issues that are assigned the Exception type and are assigned to the current user, enter `#exception assigned to: me`.  |

## Issue Links

You can search for issues based on the links that connect them to other issues. Search queries that reference a specific issue link type can be interpreted in two different ways:

* When specified as `<link type>: <issue ID>`, the query returns issues linked to the specified issue using this link type.

* Using `<link type>: (<sub-query>)`, the query returns issues linked to any issue that matches the specified sub-query using this link type.

When searching for linked issues, you can enter the outward name or inward name of any issue link type, then specify your search criteria.

This list contains search parameters for issue link types that are provided by default in YouTrack. The default issue link types can be customized, which means that the actual names may vary. You can also use this syntax to build search queries that refer to custom link types.

### links

```
links: <issue ID>
```

Returns issues that are linked to a target issue.

| Values | Accepts only an issue ID. |
| Example | To find all tasks that are linked to an issue with the ID JT-5072, enter `links: JT-5072`.  |

### aggregate

```
aggregate <aggregation link type>: <issue ID>
```

Returns issues that are indirectly linked to a target issue. Use this search term to find, for example, issues that are parent issues for a parent issue or subtasks of issues that are also subtasks of a target issue. The results include any issue that is linked to the target issue using the specified link type, whether directly or indirectly.

This search argument is only compatible with aggregation link types.

| Values | Accepts only an issue ID. |
| Example | To find all tasks that are linked as subtasks to issues that are also subtasks of an issue with the ID JT-5072, enter `aggregate Subtask of: JT-5072`.  |

### Depends on

```
Depends on: <issue ID> | (<sub-query>)
```

Returns issues that have depends on links to a target issue or any issue that matches the specified sub-query.

| Values | Accepts an issue ID or a sub-query. |
| Example | To find all tasks that are assigned to you that depend on the issue JT-5072, enter `for: me #task Depends on: JT-5072`.     To find any task assigned to you that depends on an unresolved issue, enter `for: me #task Depends on: (#Unresolved)`.    |

### Duplicates

```
Duplicates: <issue ID> | (<sub-query>)
```

Returns issues that have duplicates links to a target issue or any issue that matches the specified sub-query.

| Values | Accepts an issue ID or a sub-query. |
| Example | To find issues that duplicate the issue JT-5072, enter `Duplicates: JT-5072`.     To find any issue that duplicates an unresolved issue, enter `Duplicates: (#Unresolved)`.    |

### Is duplicated by

```
Is duplicated by: <issue ID> | (<sub-query>)
```

Returns issues that have is duplicated by links to a target issue or any issue that matches the specified sub-query.

| Values | Accepts an issue ID or a sub-query. |
| Example | To find issues that are duplicated by the issue JT-5072, enter `Is duplicated by: JT-5072`.     To find any issue that is duplicated by an issue that is currently in progress, enter `Is duplicated by: (State: {In Progress})`.    |

### Is required for

```
Is required for: <issue ID> | (<sub-query>)
```

Returns issues that have is required for links to a target issue or any issue that matches the specified sub-query.

| Values | Accepts an issue ID or a sub-query. |
| Example | To find issues that are assigned to you and are required for issue JT-5072, enter `for: me Is required for: JT-5072`.     To find all issues that are assigned to you and are required for any other unresolved issue, enter `for: me Is required for: (#Unresolved)`.    |

### Parent for

```
Parent for: <issue ID> | (<sub-query>)
```

Returns issues that have parent for links to a target issue or any issue that matches the specified sub-query.

| Values | Accepts an issue ID or a sub-query. |
| Example | To find the parent task for JT-5072, enter `Parent for: JT-5072`.     To find resolved issues that have unresolved subtasks, enter `#Resolved Parent for: (#Unresolved)`.    |

### Relates to

```
Relates to: <issue ID> | (<sub-query>)
```

Returns issues that have relates to links to a target issue or any issue that matches the specified sub-query.

| Values | Accepts an issue ID or a sub-query. |
| Example | To find issues that are assigned to you and are related to the issue with the ID JT-5072, enter `for: me Relates to: JT-5072`.     To find issues that are related to any other unresolved issue, enter `for: me Relates to: (#Unresolved)`.    |

### Subtask of

```
Subtask of: <issue ID> | (<sub-query>)
```

Returns issues that have subtask of links to a target issue or any issue that matches the specified sub-query.

| Values | Accepts an issue ID or a sub-query. |
| Example | To find issues that are assigned to you and are linked as subtasks to JT-5072, enter `for: me Subtask of: JT-5072`.     To find any unresolved issue where the value for the Product field in its parent issue is YouTrack, enter `#Unresolved Subtask of: (Product: YouTrack)`.    |

## Time Tracking

There is a dedicated set of search attributes that you can use to find issues that contain time tracking data. These attributes look for specific values that have been added as work items to an issue.

### work

```
work: <text>
```

Returns issues that contain word forms that match the specified word or phrase in a work item.

| Values | Accepts text. Values are parsed as described for [Text Search](full-text-search.html). |
| Example | To find issues with work items that include any form of the word "test", enter `work: test`.  |

### work author

```
work author: <user>
```

Returns issues that have work items that were added by the specified user.

| Values | Only accepts a user. |
| Example | To find all issues in the 'TST' project that have work items that were added by the current user, enter: `in: TST work author: me` |

### work type

```
work type: <value>
```

Returns issues that have work items that are assigned the specified work type. The query `work type: {No type}` returns issues that have work items that are not assigned a work item type.

| Values | Accepts a predefined work item type. |
| Example | To find all issues in the 'TST' project that have work items that are assigned the `Development` work item type, enter: `in: TST work type: Development` |

### work date

```
work date: <date> | <period>
```

Returns issues that have work items that are recorded for the specified date or within the specified time frame.

| Values | Accepts a date, custom period, or [relative date parameter](#relative-date-parameters). |
| Example | To find all issues in the 'TST' project that have work items that were added last week, enter: `in: TST work date: {Last week}` |

### custom work item attributes

```
work <attribute name>: <attribute value>
```

Returns issues that have work items that are assigned the specified value for a specific work item attribute.

| Values | Accepts an attribute name and value pair. |
| Example | To find all issues in the 'TST' project that have are assigned the value Non-billable for the Expenses attribute, enter: `in: TST work Expenses: Non-billable` |

## Sort Attributes

You can specify the sort order for the list of issues that are returned by the search query.

You can sort issues by any of the attributes on the following list. In the [Search Query Grammar](#search-query-grammar), these attributes represent the `<SortAttribute>` value.

### sort by

```
sort by: <value> <sort order>
```

Sorts issues that are returned by the query in the specified order.

| Values | You can sort issues by values from the following attributes: star, updated, updater, created, {resolved date}, project, reporter, {issue id}, votes, summary, comments, <custom field>, and {attachment size}.   |
| Sort Order | asc, desc |
| Aliases | order by |
| Example | To find all issues with the Fixed state that were either assigned to or reported by the current user, and sort them by the date of the last update in descending order, displaying the most recently updated issue first, enter `#my #fixed sort by: updated desc`.             |

When you perform a text search, the results can be sorted by relevance. You cannot specify relevance as a sort attribute. For more information, see [Sorting by Relevance](full-text-search.html#sort-by-relevance).

## Keywords

There are a number of values that can be substituted with a keyword. When you use a keyword in a search query, you do not specify an attribute. A keyword is preceded by the number sign (#) or the minus operator. In the YouTrack [Search Query Grammar](#search-query-grammar), these keywords correspond to a `<SingleValue>`.

### me

References the current user. This keyword can be used as a value for any attribute that accepts a user.

When used as a single value (`#me`) the search returns issues that are assigned to, reported by, or commented by the current user.

For example, to find unresolved issues that are assigned to, reported by, or contain comments from the current user, enter `#me -Resolved`.

The results also include issues that contain references to the current user in any custom field that stores values as users. For example, you have a custom field Reviewed by that stores a `user` type. The search query `#me -Resolved` also includes issues that reference the current user in this custom field.

### my

An alias for [me](#me).

### Resolved

This keyword references the Resolved issue property. This property is set based on the current value or combination of values for any custom field that stores a `state` type. In the default State field, the Resolved property is enabled for the values Fixed, Won't fix, Duplicate, Incomplete, Obsolete, and Can't reproduce.

For projects that use multiple state-type fields, the Resolved property is only true when all the state-type fields are assigned values that are considered to be resolved.

For example, to find all resolved issues that were updated today, enter `#Resolved updated: Today`.

### Unresolved

This keyword references the Unresolved issue property. This property is set based on the current value or combination of values for any custom field that stores a `state` type. In the default State field, the Resolved property is disabled for the values Submitted, Open, In Progress, Reopened, and To be discussed.

For projects that use multiple state-type fields, the Unresolved property is true when any state-type field is assigned a value that is not considered to be resolved.

For example, to find all unresolved issues that are assigned to the user john.doe in the Test project, enter `#Unresolved project: Test for: john.doe`.

### Released

This keyword references the Released property for values in a field that stores a `version` type. It can only be used together with the attribute name or alias for a version field. This means that it cannot be referenced as a single value.

With fields that store multiple values, the search query returns issues for which at least one of the versions that are stored in the field is marked as released.

For example, to find all issues in the Test project that are fixed in a version that has not yet been released, enter `in: Test fixed in: -Released`.

### Archived

This keyword references the Archived property for values in a field that stores a `version` type. It can only be used together with the attribute name or alias for a version field. This means that it cannot be referenced as a single value.

With fields that store multiple values, the search query only returns issues for which all the versions that are stored in the field are marked as archived.

For example, to find all issues in the Test project that are fixed in a version that has been archived, enter `in: Test fixed in: Archived`.

## Operators

The search query grammar applies default semantics to search queries that do not contain explicit logical operators.

* Searches that specify values for multiple attributes are treated as conjunctive. This means that the values are handled as if joined by an `AND` operator. For example, `State: {In Progress} Priority: Critical` returns issues that are assigned the specified state and priority. This extends to queries that look for the presence or absence of a value for a specific attribute (`has`) in combination with a reverence to a specific value for the same attribute. The presence or absence of a value and the value itself are considered as separate attributes in the issue. For example, `has: assignee Assignee: me` only returns issues where the assignee is set and that assignee is you.

* For text search, searches that include multiple words are treated as conjunctive. This means that the words are handled as if joined by an `AND` operator. For example, `State: Open context usage` returns issues that contain matching forms for both `context` and `usage`.

* Searches that include multiple values for a single attribute are treated as disjunctive. This means that the values are handled as if joined by an `OR` operator. For example, `State: {In Progress}, {To be discussed}` returns issues that are assigned either one or the other of these two states.

You can override the default semantics by applying explicit operators to the query.

> **Tip: For consistent results, use parentheses!**
> Any time you override the default semantics with explicit `AND` or `OR` operators, you should wrap all of your search arguments in parenthesis.
>
>
>
> In longer queries, it's easy to overlook multiple references to a single attribute, which are handled as if joined by an `OR` operator. As a result, the query returns more issues than expected. By wrapping each search argument in parentheses and joining them with specific operators, you ensure that the query returns the issues you want to work with.
>
>
>
> For details, see [Parentheses](#parentheses).

> **Note: Case Insensitivity**
> The logical operators that are supported in search queries are case-insensitive. It doesn't matter whether you write `AND`, `and`, `And`, or even `aNd`. Any differences between upper and lower case letters in these operators is ignored completely.

### and

The `AND` operator combines matches for multiple search attributes to narrow down the search results. When you join search arguments with the `AND` operator, the resulting issues must contain matches for all the specified attributes. Use this operator for issue fields that store `enum[*]` types and tags.

Search arguments that are joined with an `AND` operator are always processed as a group and have a higher priority than other arguments that are joined with an OR operator in the query.

Here are a few examples of search queries that contain `AND` operators:

* To find issues in the Ktor project that are tagged as both Next build and to be tested, enter: `in: Ktor and tag: {Next build} and tag: {to be tested}` The `AND` operator between the two tags ensures that the results only contain issues that have both tags.

* To find all issues that are set as Critical priority in the Ktor project or are set as Major priority and are assigned to you in the Kotlin project, enter: `in: Ktor #Critical or in: Kotlin #Major and for: me` If you were to remove the operators in this query, the references to the project and priority are parsed as disjunctive (`OR`) statements. The reference to the assignee (`me`) is then joined with a conjunctive (`AND`) statement. Instead of getting critical issues in the Ktor project plus a list of major-priority issues that you are assigned in Kotlin, you would only issues that are assigned to you that are either major or critical in either Ktor or Kotlin.

### or

The `OR` operator combines matches for multiple search attribute to broaden the search results.

This is very useful when searching for a term which has a synonym that might be used in an issue instead. For example, a search for `lesson OR tutorial` returns issues that contain matching forms for either "lesson" or "tutorial". If you remove the `OR` operator from the query, the search is performed conjunctively, which means the result would only include issues that contain matching forms for both words.

Here's another example of a search query that contains an `OR` operator:

* To find all issues in the Ktor project that are assigned to you or are tagged as to be tested in any project, enter: `in: Ktor for: me or tag: {to be tested}`

### Parentheses

Using parentheses `(` and `)` combines various search arguments to change the order in which the attributes and operators are processed. The part of a search query inside the parentheses has priority and is always processed as a single unit.

The most common use of parentheses is to enclose two search arguments that are separated by an `OR` operator and further restrict the search results by joining additional search arguments with `AND` operators.

Any time you use parentheses in a search query, you need to provide all the operators that join the parenthetical statement to neighboring search arguments. For example, the search query `in: Kotlin #Critical (in: Ktor and for:me)` cannot be processed. It must be written as `in: Kotlin #Critical or (in: Ktor and for:me)` instead.

Here's an example of a search query that uses parentheses:

* To find all issues that are assigned to you and are either assigned Critical priority in the Kotlin project or are assigned Major priority in the Ktor project, enter: `(in: Kotlin #Critical or in: Ktor #Major) and for: me`

## Symbols

The following symbols can be used to extend or refine a search query.

| Symbol | Description | Examples |
| --- | --- | --- |
| - | Excludes a subset from a set of search query results. When you use this symbol with a single value, do not use the number sign. | To find all unresolved issues except for issues with minor priority and sort the list of results by priority in ascending order, enter `#unresolved -minor sort by: priority asc`. |
| # | Indicates that the input represents a single value.  | To find all unresolved issues in the MRK project that were reported by, assigned to, or commented by the current user, enter `#my #unresolved in: MRK`.           |
| , | Separates a list of values for a single attribute. Can be used in combination with a range. | To find all issues assigned to, reported or commented by the current user, which were created today or yesterday, enter `#my created: Today, Yesterday`.           |
| .. | Defines a range of values. Insert this symbol between the values that define the upper and lower ranges. The search results include the upper and lower bounds. | To find all issues fixed in version 1.2.1 and in all versions from 1.3 to 1.5, enter `fixed in: 1.2.1, 1.3 .. 1.5`.       To find all issues created between March 10 and March 13, 2018, enter `created: 2018-03-10 .. 2018-03-13`.                |
| * | Wildcard character. Its behavior is context-dependent.       * When used with the `..` symbol, substitutes a value that determines the upper or lower bound in a range search. The search results are inclusive of the specified bound.    * When used in an attribute-based search, matches zero or more characters at the end of an attribute value. For more information, see [Wildcards in Attribute-based Search](attribute-based-search.html#Wildcards).    * When used in text search, matches zero or more characters in a string. For more information, see [Wildcards in Text Search](full-text-search.html#search-wildcards).   | To find all issues created on or before March 10, 2018, enter `created: * .. 2018-03-10`     To find issues that have tags that start with `refactoring`, enter `tag: refactoring*`.     To find unresolved issues that contain image attachments in PNG format, enter `#Unresolved attachments: *.png`.    |
| ? | Matches any single character in a string. You can only use this wildcard to search in attributes that store text. For more information, see [Wildcards in Text Search](full-text-search.html#search-wildcards). | To find issues that contain the words "prioritize" or "prioritise" in the issue description, enter `description: prioriti?e` |
| { } | Encloses attribute values that contain spaces. | To find all issues with the Fixed state that have the tag to be tested, enter `#Fixed tag: {to be tested}`.           |

## Date and Period Values

Several search attributes reference values that are stored as a date. You can search for dates as single values or use a range of values to define a period.

Specify dates in the format: `YYYY-MM-DD` or `YYYY-MM` or `MM-DD`. You also can specify a time in 24h format: `HH:MM:SS` or `HH:MM`. To specify both date and time, use the format: `YYYY-MM-DD}}T{{HH:MM:SS`. For example, the search query `created: 2010-01-01T12:00 .. 2010-01-01T15:00` returns all issues that were created on 1 January 2010 between 12:00 and 15:00.

### Predefined Relative Date Parameters

You can also use pre-defined relative parameters to search for date values. The values for these parameters are calculated relative to the current date according to the time zone of the current user. The actual value for each parameter is shown in the query assist panel.

!['Due Date' filter menu listing relative dates such as Today, Tomorrow, and This week.](https://resources.jetbrains.com/help/img/youtrack/2026.2/relative-date-values.png)

The following relative date parameters are supported:

| Parameter | Description |
| --- | --- |
| Now | The current instant. |
| Today | The current calendar day. |
| Tomorrow | The next calendar day. |
| Yesterday | The previous calendar day. |
| Sunday | The calendar Sunday for the current week. |
| Monday | The calendar Monday for the current week. |
| Tuesday | The calendar Tuesday for the current week. |
| Wednesday | The calendar Wednesday for the current week. |
| Thursday | The calendar Thursday for the current week. |
| Friday | The calendar Friday for the current week. |
| Saturday | The calendar Saturday for the current week. |
| {Last working day} | The most recent working day as defined by the Workdays that are configured in the settings on the Time Tracking page in YouTrack. |
| {This week} | The period from 00:00 Monday to 23:59 Sunday for the current week. |
| {Last week} | The period from 00:00 Monday to 23:59 Sunday for the previous week. |
| {Next week} | The period from 00:00 Monday to 23:59 Sunday for the next week. |
| {Two weeks ago} | The period from 00:00 Monday to 23:59 Sunday for the calendar week two weeks prior to the current date. |
| {Three weeks ago} | The period from 00:00 Monday to 23:59 Sunday for the calendar week three weeks prior to the current date. |
| {This month} | The period from the first day to the last day of the current calendar month. |
| {Last month} | The period from the first day to the last day of the previous calendar month. |
| {Next month} | The period from the first day to the last day of the next calendar month. |
| Older | The period from 1 January 1970 to the last day of the month two months prior to the current date. |

### Custom Date Parameters

If the predefined date parameters don't help you find issues that matter most to you, define your own date range in your search query. Here are a few examples of the queries you can write with custom date parameters:

* Find issues that have new comments added in the last seven days: ``` commented: {minus 7d} .. Today ```

* Find issues that were updated in the last two hours: ``` updated: {minus 2h} .. * ```

* Find unresolved issues that are at least one and a half years old: ``` created: * .. {minus 1y 6M} #Unresolved ```

* Find issues that are due in five days: ``` Due Date: {plus 5d} ```

To define a custom time frame in your search queries, use the following syntax:

* To specify dates or times in the past, use `minus`.

* To specify dates or times in the future, use `plus`.

* Specify the time frame as a series of whole numbers followed by a letter that represents the unit of time. Separate each unit of time with a space character. For example: ``` 2y 3M 1w 2d 12h ```

Queries that specify hours will filter for events that took place during the specified hour. For example, if it is currently 15:35, a query that is written as `created: {minus 48h}` returns issues that were created two days ago, at any time between 3 and 4 PM. Meanwhile, a query that is written as `created: {minus 2d}` returns all issues that were created two days ago at any time between midnight and 23:59.

This level of precision only applies to hours. A query that references the unit of time as `14d` returns exactly the same results as `2w`.

Search queries that specify units of time shorter than one hour (minutes, seconds) are not supported.

## Search Query Grammar

This page provides a BNF description of the YouTrack search query grammar.

```BNF
<SearchRequest> ::= <OrExpression>
<OrExpession> ::= <AndExpression> ('or' <AndExpression>)*
<AndExpression> ::= <AndOperand> ('and' <AndOperand>)*
<AndOperand> ::= '('<OrExpression>? ')' | Term
<Term> ::= <TermItem>*
<TermItem> ::= <QuotedText> | <NegativeText> | <PositiveSingleValue> | <NegativeSingleValue> | <Sort> | <Has> | <CategorizedFilter> | <Text>
<CategorizedFilter> ::= <Attribute> ':' <AttributeFilter> (',' <AttributeFilter>)*
<Attribute> ::= <name of issue field>
<AttributeFilter> ::= ('-'? <Value> ) | ('-'? <ValueRange>) | <LinkedIssuesQuery>
<LinkedIssuesQuery> ::= ( <OrExpression> )
<ValueRange> ::= <Value> '..' <Value>
<PositiveSingleValue> ::= '#'<SingleValue>
<NegativeSingleValue> ::= '-'<SingleValue>
<SingleValue> ::= <Value>
<Sort> ::= 'sort by:' <SortField> (',' <SortField>)*
<SortField> ::= <SortAttribute> ('asc' | 'desc')?
<Has> ::= 'has:' <Attribute> (',' <Attribute>)*
<QuotedText> ::= '"' <text without quotes> '"'
<NegativeText> ::= '-' <QuotedText>
<Text> ::= <text without parentheses>
<Value> ::= <ComplexValue> | <SimpleValue>
<SimpleValue> ::= <value without spaces>
<ComplexValue> ::= '{' <value (can have spaces)> '}'
```

Grammar is case-insensitive.

* For a complete list of search attributes, see [Issue Attributes](#issue-attributes).

* To see sample queries for common use cases, see [Sample Search Queries](sample-search-queries.html).



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/search-and-command-attributes.html](https://www.jetbrains.com/help/youtrack/cloud/search-and-command-attributes.html) · fetched 2026-09-22 08:34 Asia/Taipei*
