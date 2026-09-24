---
title: "Command Reference"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/command-reference.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Command Reference

Commands are basically a series of attribute and value pairs that apply changes to one or more issues at once. In many cases, you can skip the attribute and enter the value that you want to apply. YouTrack detects which attributes use the specified value and suggests valid options for the command.

The format you use to enter a command is similar to the syntax used in a [search query](search-and-command-attributes.html). However, the rules for using colons, braces, and number signs do not apply to commands. For example:

* To search for critical issues that are assigned to you and associated with the tag YouTrack Mobile, you enter the following search query: `for: me tag: {YouTrack Mobile} #critical`

* To apply a command that assigns the issues to yourself, adds the tag YouTrack Mobile, and elevates the priority to critical, you enter the following command: `for me tag YouTrack Mobile critical`

## Simple Commands

The following commands do not require any additional attributes or values. Simply select one or more issues and apply the command.

| Command | Description |
| --- | --- |
|  comment  | Adds a comment to the selected issues. Enter the comment text itself in the Comment input field. You can also select a group in the Visible for Group drop-down list to set the visibility of the comment. |
|  delete  | Deletes the selected issues. |
|  clone  | Creates a clone of the selected issues. You can also apply this action with the action clone command.  |

The following commands update specific issue attributes by adding or removing a specified value. You can either specify the attribute and value or simply enter the single value.

| Command | Description |
| --- | --- |
|  add  | Adds the specified value to the attribute. Use this command to add values to custom fields that store multiple values instead of changing the existing value. Additional usages of this command are described for each attribute that supports it.  |
|  remove  | Removes the specified value from the attribute. Use this command to remove single values from custom fields that store multiple values. Additional usages of this command are described for each attribute that supports it. |

## Projects

Use the following commands to move issues to another project.

| Command | Value | Description |
| --- | --- | --- |
| move to     project    | project name | Moves the selected issues to the specified project. |

You can also enter the <project name> as a single value.

## Custom Fields

You can use commands to set or change the values for [fields within the field panel of issues](custom-fields.html). Additional options for the Assignee field are described in the [Assignee](#assignee) section. The following options are supported for custom fields:

* Enter commands in the format field name value.

* Enter the value as a single value. The corresponding fields that use this value are shown in the auto-completion dialog.

* To update the value of a custom field that is managed by a state-machine rule in a workflow, enter the command in the format field name event.

* If the custom field can contain an empty value, enter the name of the empty value to clear the field.

For custom fields that store multiple values, you can reference this attribute with add and remove commands:

| Command | Description |
| --- | --- |
| add <field name> <value> | Adds the specified single value to the specified custom field. Unspecified values that are currently stored in the field are not affected. |
| remove <field name> <value> | Removes the specified single value from the specified custom field. Unspecified values that are currently stored in the field are not affected. |

For example, if the Fix versions field stores multiple values, you can enter `add Fix versions 2025.3` to add the 2025.3 version without affecting existing values. To remove that version from all selected issues, enter `remove Fix versions 2025.3`.

If you have the Update Project permission, you can add values to the custom field. This option is displayed in the Command Preview section of the dialog.

![Adding a value to a custom field directly in the Apply Command dialog.](https://resources.jetbrains.com/help/img/youtrack/2026.2/add-value-in-command-dialog.png)

The actual fields and values vary based on the custom fields that are used in your project. All custom fields support the field value command syntax. Other commands in this list use the aliases that are assigned to default custom fields.

| Command | Value | Description |
| --- | --- | --- |
|  <custom field>  | value name | Changes the value for the specified custom field.       * If you specify a value for a custom field that stores a string type, escape reserved characters with a slash. For example, to set the value of a field to Published assets for "Expressive Kotlin" webinar, you need to escape the quotation marks like this: ```GENERIC Published assets for \"Expressive Kotlin\" webinar ```    * If you reference a custom field that stores a date, you can replace specific dates with relative date parameters. For example: ```GENERIC Due Date Next month ``` For relative date parameters, the value is set to the first possible value in the date range.                          The only command that requires additional parameters is State Duplicates. Here, you must add the duplicates link type and specify the ID of the target issue.                     |
|    for     assigned to    | login | Sets the value for the Assignee field for the selected issues to the specified user. You can also assign issues to yourself with the command for me or assigned to me.     For additional options, see [Assignee](#assignee).   |
|  in  | value name | Changes the value for the Subsystem field. |
|    affects     that affect     affecting    | version | Changes the value for the Affected versions field. |
|    fix for     fixed in     version    | version | Changes the value for the Fix versions field. |
|  fixed in build  | build | Changes the value for the Fixed in build field. |

## Assignee

Assignee differs from other custom field types because it stores a user type. There are several aliases that you can use to set the value of this field.

* The aliases me and my reference the username of the current user. You can enter these aliases as single values to assign the selected issues to yourself.

* You can enter a username as a single value to assign the selected issues to a specific user.

* Use the name of the empty value (Unassigned) to clear the field.

* Use the syntax add <username> to assign an issue and remove <username> to unassign an issue.

You can also set the value of this field with the following commands:

| Command | Value | Description |
| --- | --- | --- |
|    for     assigned to    | username | Sets the value for the Assignee field for the selected issues to the specified user. You can also assign issues to yourself with the command for me or assigned to me. |

## Work Items

Use the work to add work items to one or more issues. Specify values for the work item in the following order: <work item type> <date> <time period> <description> Use the following parameters to set values for the work item:

| Parameter | Condition | Description |
| --- | --- | --- |
| work item type | Optional | Set the work item type. |
| date | Optional | Set the date with the format yyyy-mm-dd. If skipped, the current date is assigned to the work item. |
| time period | Mandatory | Enter the amount of time spent working on the issue. |
| description | Optional | Enter a description of the work performed. |

You can also use the syntax add work <work item>. The remove command is not supported.

## Link Types

You can use a command to add link types to one or more issues. To add a link type with a command, enter a link type and enter the issue ID of the target issue. You can also reference this attribute with add and remove commands:

| Command | Description |
| --- | --- |
| add <link type> <issue ID> | Adds the specified link type to the specified issue. |
| remove <link type> <issue ID> | Removes the specified link type from the specified issue. |

The following commands correspond to the outward names and inward names for default issue link types in YouTrack. Custom link types also use the outward names and inward names as commands.

| Command | Description |
| --- | --- |
|  depends on  | Adds a Depends on link to a target issue in the selected issues. Also adds an Is required for link to the selected issue in the target issue. |
|  duplicates  | Adds a Duplicates link to a target issue in the selected issues. Also adds an Is duplicated by link to the selected issue in the target issue. |
|  is duplicated by  | Adds an Is duplicated by link to a target issue in the selected issues. Also adds a Duplicates link to the selected issue in the target issue. |
|  is required for  | Adds an Is required for link to a target issue in the selected issues. Also adds a Depends on link to the selected issue in the target issue. |
|  parent for  | Adds a Parent for link to a target issue in the selected issues. Also adds a Subtask of link to the selected issue in the target issue. |
|  relates to  | Adds a Relates to link to a target issue in the selected issues. Also adds a Relates to link to the selected issue in the target issue. |
|  subtask of  | Adds a Subtask of link to a target issue in the selected issues. Also adds a Parent for link to the selected issue in the target issue. |

## Tags

You can use a command to add tags to an issue. You can also remove existing tags from an issue.

| Command | Value | Description |
| --- | --- | --- |
|  tag  | tag name | Adds the specified tag to the selected issues. If the specified tag does not exist, a new tag is created and added to the selected issues.     You can also use the syntax add tag <tag name> or simply enter the <tag name> as a single value.   |
|  untag  | tag name | Removes the specified tag from the selected issues.     You can also use the syntax remove tag <tag name>.   |

## Visibility

You can set or change the visibility setting for an issue with a command.

| Command | Value | Description |
| --- | --- | --- |
|  visible to  | group     username   | Sets the issue visibility to the specified user or group. |

You can also reference this attribute with add and remove commands:

| Command | Description |
| --- | --- |
| add visible to | Adds the specified user or group to the list of users and groups for whom the issue is visible. |
| remove visible to | Removes the specified user or group from the list of users and groups for whom the issue is visible. |

## Voters

The following commands manage votes for issues on behalf of the current user.

| Command | Description |
| --- | --- |
|    vote     +1    | Adds a vote to the selected issues. |
|  unvote  | Removes a vote from the selected issues. |

## Watchers

You can use a command to star or unstar an issue. To star and unstar issues with a command, enter the command and enter the username for whom the action applies.

| Command | Value | Description |
| --- | --- | --- |
|    star     watcher    | username | Adds the Star tag to the selected issues on behalf of the user with the specified username. This action adds the user to the list of watchers.     You can also use the syntax add <command> <username>.    |
|  unstar  | username | Removes the Star tag from the selected issues for the user with the specified username. This action removes the user from the list of watchers who subscribe to updates for issues with the Star tag. However, the user may remain on the list of watchers for other reasons. |

> **Note: Auto-completion Suggestions for User Accounts**
> These commands display usernames in the auto-completion list. The suggestions are filtered to show only users who have the Read Issue permission for the issue or issues to which the command will be applied.

## Boards

Use the following command to assign an issue to a sprint on an agile board.

| Command | Value | Description |
| --- | --- | --- |
|  Board <board name>  | sprint name | Assigns the issue to the sprint with the specified name on the specified agile board. You can substitute the sprint name with {current sprint} to assign issues to the current sprint. To learn how YouTrack identifies the current sprint, see [The Current Sprint](work-with-sprints.html#current-sprint).     For agile boards that use the Add new issues to sprint option, you can use Default as an alias for the name of the sprint that is selected in the board settings.   |

You can also reference this attribute with add and remove commands:

| Command | Description |
| --- | --- |
| add Board <board name> <sprint name> | Adds selected issues to the specified sprint for the specified agile board. |
| add Board <board name> | Adds selected issues to the specified agile board. If sprints are enabled for the board, the issues are added to the current sprint. |
| remove Board <board name> <sprint name> | Removes selected issues from the specified sprint for the specified agile board. |
| remove <board name> | Removes selected issues from any sprint for the specified agile board. For some board configurations, this command is handled differently.       * For boards with sprints enabled that use the Link sprints to custom field option, the issues cannot be removed from the board. Instead, the selected issues are assigned to the sprint that corresponds to the empty value for the linked custom field.    * For boards with sprints disabled that use the Filter cards to match a query option, this command is not valid. To remove the issue from the board, you need to update its fields so that the issue no longer matches the search query.    |

## Gantt Charts

Use the following command to assign an issue to a Gantt chart.

| Command | Value | Description |
| --- | --- | --- |
|  Gantt <chart name>  | chart name | Assigns the issue to the specified Gantt chart.   |

You can also reference this attribute with add and remove commands:

| Command | Description |
| --- | --- |
| add Gantt <chart name> | Adds selected issues to the specified Gantt chart. |
| remove Gantt <chart name> | Removes selected issues from the specified Gantt chart. |

## Command Grammar

This section provides a BNF description of the YouTrack command grammar.

```BNF
<CommandList> ::= <Command> ( <Command> )*
<Command> ::= <Comment> | <Value> | <LinkCommand> | <TagCommand> | <AttributeCommand> | <MultipleCommand>
<Comment> ::= 'comment'
<LinkCommand> ::= <LinkType> <IssueId>
<TagCommand> ::= 'tag' (<TagName> | <NewTagName>) | 'untag' <TagName>
<StarCommand> ::= ( 'unstar' | 'star' ) [ <Username> ]
<AttributeCommand> ::= <Attribute> <Value>
<MultipleCommand> ::= ('add' | 'remove') (<Value> | <LinkCommand> | <MultipleAttributeCommand> )
<MultipleAttributeCommand> ::= <MultipleAttribute> <Value>
```

Grammar is case-insensitive.



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/command-reference.html](https://www.jetbrains.com/help/youtrack/cloud/command-reference.html) · fetched 2026-09-22 08:34 Asia/Taipei*
