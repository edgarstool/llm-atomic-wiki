---
title: "JavaScript Workflow Quick Start"
source_url: "https://www.jetbrains.com/help/youtrack/devportal/Quick-Start-Guide-Workflows-JS.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# JavaScript Workflow Quick Start Guide

This Quick Start Guide shows you how to create a pure workflow: a rule-only package that you author and manage with the workflow tools in YouTrack.

* If you want to skip the warm-up, you can [dive right into the API](Workflows-in-JavaScript.html).

* If you have never worked with workflows in YouTrack, start with the [workflow reference](youtrack-workflow-reference.html) for more background information.

* If you want to combine workflow rules with widgets, HTTP handlers, settings, or other app components, start with the [App Quick Start Guide](apps-quick-start-guide.html) instead.

* If you are not familiar with JavaScript, give the [Workflow Constructor](https://www.jetbrains.com/help/youtrack/cloud/workflow-constructor.html) a try instead. You can build workflows using the constructor without any programming knowledge.

## Permissions

Before you start, make sure you have permission to create and edit workflows. Users who have been granted the Update Project permission can create their own workflows and attach them to their projects.

The controls for creating workflows are available on the Workflows page, which is accessible from the Administration menu.

## Create a Workflow

The workflow itself is just a container. You can use a workflow to collect a set of rules that you want to apply in your project.

You build workflows to enforce specific business logic, so it's a good idea to sit down and map out your use case before you start.

For this guide, put yourself in the shoes of a project manager. You've just added a field to your project that you want to use to group issues so you can report your progress to your boss. You created a field with the name Phase and added the values Development , Testing , and Ready . Basically, your boss just needs to see how many issues you still have in development or testing to measure your progress against the roadmap.

Now you need to create a workflow that sets the values for this field based on other changes that are applied to the issues in the project. You want to set the values for this field automatically, so your project team doesn't have to worry about setting the value themselves.

Procedure: To create a workflow:

1. From the Administration menu, select Workflows .

2. Click the New workflow button, then select the JavaScript Editor option.

* The New Workflow dialog opens.

![New workflow dialog js](https://resources.jetbrains.com/help/img/youtrack/new-workflow-dialog-js.png)

3. In the New Workflow dialog, enter a name and an optional title. The workflow name follows the standard naming conventions for npm packages. For more information, see [https://docs.npmjs.com/files/package.json#name](https://docs.npmjs.com/files/package.json#name).

For this guide, use phase-management as the name and Phase Management as the title.

4. Click the Save button.

* Your workflow is added to the list.

## Add a Module to Your Workflow

So that was simple enough, but you're just getting started. You now have a container where you can store your scripts. You add scripts to your workflow in modules that can contain different types of rules or custom scripts.

The first action that you want to automate in this project is to clear the value of the Phase field when the team decides to postpone a task and move it to the product backlog. When the team postpones a task, they change the value of the Fix version field to Backlog .

This action takes place when a change is applied to an issue, so you want to add a module to the workflow that contains an on-change rule.

Procedure: To add a module to the workflow:

1. Select the empty phase-management workflow in the list.

![Workflow open rule](https://resources.jetbrains.com/help/img/youtrack/workflow-open-rule.png)

2. Click the On-change button.

* The New Module dialog opens.

3. Enter a name for the module, like `clear-phase-when-postponed`, then click the Save button.

* The new module is added to the workflow.

* The module name is displayed as a link.

* The template for an on-change rule loads in the editor.

![New module on change](https://resources.jetbrains.com/help/img/youtrack/new-module-on-change.png)

## Write Your First Rule

Now you're ready to write your first simple rule. The best way to proceed is to move from one `TODO` comment in the template to the next, updating the code line by line and removing any unnecessary comments as you go.

Procedure: To write your first rule:

1. Start with the first comment block in the template:

```JAVASCRIPT
/**
 * This is a template for an on-change rule. This rule defines what
 * happens when a change is applied to an issue.
 *
 * For details, read the Quick Start Guide:
 * https://www.jetbrains.com/help/youtrack/devportal/Quick-Start-Guide-Workflows-JS.html
 */
```

Aside from showing you how to add comment blocks to your modules, this comment tells you what type of rule is defined in this template and points you to this quick start guide. Since you're already here, and you know what this type of rule does, go ahead and delete the whole block.

2. Read the first line of code:

```JAVASCRIPT
const entities =
    require('@jetbrains/youtrack-scripting-api/entities');
```

This variable declaration references the `entities` module in the workflow API. This means that all the properties and methods contained in the `entities` module can be accessed in this rule.

If there are properties and methods that belong to other modules, for example, the `workflow` module, just add a `require` statement and point to the module you want to reference, like this:

```JAVASCRIPT
const workflow =
    require('@jetbrains/youtrack-scripting-api/workflow');
```

The most important point here is that you need to be familiar with the workflow API and know which modules contain the properties and methods that you need for your workflows. For this rule, you only want to update the value in a custom field. Issues and their custom fields are all accessible from the `entities` module, so you can keep the `require` statement that is built into the template.

3. Set the `exports.rule` property.

A script can export exactly one rule to this property. In the template, this property is set with the `entities.Issue.onChange` method. This method declares a rule that is triggered when a change is applied to an issue, so you're all set. You already determined that this script will be handled as an on-change rule when you loaded the template.

4. Set a value for the `title` property.

For an on-change rule, this property is optional. You can already see that the value you used for the module name has been copied to the title. You want the title to be user-friendly and help other users recognize what this rule does. For this example, change the title to `Clear Phase when Fix version is set to Backlog`.

After you set the title, remove the `TODO` on the line that precedes it.

5. Write a `guard` condition

This is where you actually start to code. With the `guard` property, you define the conditions that must be met for the rule to be applied.

The template has already declared the guard as a function that accepts a context as an argument:

```JAVASCRIPT
guard: (ctx) => {
```

This means the code defined for the `guard` property is treated as a function. For the action that follows to run, this function must return a value that evaluates to `true`.

You want this rule to apply an action only when a user changes the value of the Fix version field to Backlog . The following guard returns `true` when this change is applied to an issue:

```JAVASCRIPT
return ctx.issue.fields.becomes(ctx.FixVersion,
    ctx.FixVersion.Backlog);
```

You can paste this code over the guard condition in the template, then delete the `TODO` block inside the guard property.

6. Set an `action`.

With the `action` property, you define the changes that are applied when the guard condition is met.

You can see that the template has already declared the action as a function that accepts a context as an argument:

```JAVASCRIPT
action: (ctx) => {
```

It then declares a local variable `issue` and sets the value to reference an issue in context:

```JAVASCRIPT
const issue = ctx.issue;
```

or

```JAVASCRIPT
let issue = ctx.issue;
```

You'll want to use a variable declaration for complex rules that update multiple issue properties, but for a rule this simple, you don't need it. All you need to do is specify the action that you want to apply when the guard condition is met, which is to clear the value in the Phase field:

```JAVASCRIPT
=>ctx.issue.fields.Phase = null;
```

You can copy this block of code, paste it on top of the unnecessary variable declaration, then remove the next `TODO`.

You'll notice that the template closes the body of the function with a right brace and separates this block from the next property with a comma(`},`).

7. Add `requirements`.

The `requirements` property lists the components that this rule needs to run properly. This includes definitions for custom fields, issue link types, projects, saved searches, and so on. To learn more about requirements, see [requirements](requirements.html).

For your rule, you need to define the requirements for two custom fields: Fix version and Phase .

First, define that the Fix version field stores data as a `ProjectVersion` type, then specify that the field must include `Backlog` in the set of values.

```JAVASCRIPT
FixVersion: {
type: entities.ProjectVersion.fieldType,
name: "Fix version",
Backlog: {}
},
```

First, you'll notice that `FixVersion` is not the actual name of the custom field. This is an alias. Use an alias for custom names that contain spaces and other non-alpha characters, as it saves you from having to set these values in quotes and brackets. The actual name of the custom field is specified in the `name` property. The final property for the `FixVersion` specifies that the custom field must contain the value `Backlog`.

Then, set the requirements for the Phase field.

```JAVASCRIPT
Phase: {
type: entities.EnumField.fieldType,
}
```

Here, all you need to do is require that the field exists and stores an `EnumField`. You don't need to require any values for this field, as the rule sets the value to `null`.

Copy these blocks of code and paste them on top of the last `TODO` comment.

8. Click the Save button to store your changes.

9. Open the More actions menu in the workflow editor and select Reformat code . Your finished workflow should look like this:

```JAVASCRIPT
const entities = require('@jetbrains/youtrack-scripting-api/entities');

exports.rule = entities.Issue.onChange({
    title: 'Clear Phase when Fix version is set to Backlog',
    guard: (ctx) => {
        return ctx.issue.fields.becomes(ctx.FixVersion, ctx.FixVersion.Backlog);
    },
    action: (ctx) => {
        ctx.issue.fields.Phase = null;
    },
    requirements: {
        FixVersion: {
            type: entities.ProjectVersion.fieldType,
            name: "Fix version",
            Backlog: {}
        },
        Phase: {
            type: entities.EnumField.fieldType
        }
    }
});
```

## Then Write Another!

That was easy enough. Have another go at it. Remember what you learned from your first rule and add a second module to your workflow.

The next action that you want to automate is to set the value of the Phase field when a change is applied to the State field. This action also takes place when a change is applied to an issue, so you want to add another on-change rule.

Procedure: To add another module and define a second rule:

1. In the sidebar for your `phase-management` workflow, click the Add module icon and select On-change .

2. In the New Module dialog, enter `sync-phase-with-state`, then click the Save button.

* The template for a new on-change rule loads in the editor.

3. Delete the comment block.

4. Leave the `require` declaration for the `entities` variable as is.

5. Leave definition for the `exports.rule` property alone as well.

6. Set the value for the `title` property to `Set value for Phase when State changes` and remove the `TODO` that precedes it.

7. Replace the next `TODO` by adding a definition for the `guard` property. The following guard returns `true` when a user changes the value of the State field:

```JAVASCRIPT
guard: (ctx) => {
return ctx.issue.fields.isChanged(ctx.State);
},
```

8. Set the `action` property.

This time around, you'll keep the variable declaration. This helps you reference the properties and methods for the `issue` object in the `entities` module in context without having to use the explicit reference `entities.issue`. To learn more about context, see [context](context.html).

However, because this rule only needs to update a custom field, you can change the context variable declaration to reference the `fields` object:

```JAVASCRIPT
const issueFields = ctx.issue.fields;
```

Next, you'll do a little trick. For this rule, you want to change the value in the Phase field when a user updates the State field. You're going to have to set the phase separately for each update, but you can declare the function once. Just insert this function into the body of the `action` function:

```JAVASCRIPT
function setPhase(phase) {
    if ((ctx.issue.fields.Phase || {}).name !== phase.name) {
        ctx.issue.fields.Phase = phase;
    }
}
```

You now have a function named `setPhase` that you can use to assign a value to the Phase field.

Now write the conditions for changing the value of the Phase field. Frame the conditions and actions as a series of `if`s:

* If the State changes to Fixed , set the Phase to Testing .

* If the State changes to In Progress or Reopened , set the Phase to Development .

* If the State changes to Verified , set the Phase to Ready .

Enter the conditions and actions in a series of control flow statements. Compare the conditions that are listed above to see how they are translated into JavaScript:

```JAVASCRIPT
if (issueFields.becomes(ctx.State, ctx.State.Fixed)) {
setPhase(ctx.Phase.Testing);
} else if (issueFields.becomes(ctx.State, ctx.State.InProgress) ||
issueFields.becomes(ctx.State, ctx.State.Reopened)) {
setPhase(ctx.Phase.Development);
} else if (issueFields.becomes(ctx.State, ctx.State.Verified)) {
setPhase(ctx.Phase.Ready);
}
```

9. Add the `requirements` for this rule.

For this rule, you need to define the requirements for two custom fields: State and Phase .

First, define that the State field stores data as a `state` type, then specify which values must be included in the set of values for this field.

```JAVASCRIPT
State: {
type: entities.State.fieldType,
InProgress: {
name: "In Progress"
},
Fixed: {},
Verified: {},
Reopened: {}
},
```

Then do the same for the Phase field, except that this field stores data as an `enum` type.

```JAVASCRIPT
Phase: {
type: entities.EnumField.fieldType,
Development: {},
Testing: {},
Ready: {}
}
```

Paste these blocks of code over the last `TODO` comment.

10. Click the Save button.

11. Open the More actions menu in the workflow editor and select Reformat code . Your finished workflow should look like this:

```JAVASCRIPT
const entities = require('@jetbrains/youtrack-scripting-api/entities');

exports.rule = entities.Issue.onChange({
    title: 'Set value for Phase when State changes',
    guard: (ctx) => {
        return ctx.issue.fields.isChanged(ctx.State);
    },
    action: (ctx) => {
        const issueFields = ctx.issue.fields;

        function setPhase(phase) {
            if ((ctx.issue.fields.Phase || {}).name !== phase.name) {
                ctx.issue.fields.Phase = phase;
            }
        }

        if (issueFields.becomes(ctx.State, ctx.State.Fixed)) {
            setPhase(ctx.Phase.Testing);
        } else if (issueFields.becomes(ctx.State, ctx.State.InProgress) ||
                issueFields.becomes(ctx.State, ctx.State.Reopened)) {
            setPhase(ctx.Phase.Development);
        } else if (issueFields.becomes(ctx.State, ctx.State.Verified)) {
            setPhase(ctx.Phase.Ready);
        }
    },
    requirements: {
        State: {
            type: entities.State.fieldType,
            InProgress: {
                name: "In Progress"
            },
            Fixed: {},
            Verified: {},
            Reopened: {}
        },
        Phase: {
            type: entities.EnumField.fieldType,
            Development: {},
            Testing: {},
            Ready: {}
        }
    }
});
```

## So What's Next?

Now that you have a valid workflow stored in YouTrack, you have a few options. There's still a lot to learn and do.

Use this list to find your next hill to climb or mountain to conquer.

| Put your workflow to work! | To apply your business logic, you need to attach your workflow to one or more projects. For more information, see [Attach                         Workflows to Projects](https://www.jetbrains.com/help/youtrack/cloud/?Attach-Workflow-to-Projects).  |
| --- | --- |
| Know the rules | This guide introduced you to one rule type, but there are others to learn and master. Update issues on a set schedule or on demand with a command and manage transitions between values in a custom field. For more information, see [Workflow Rule Types](Workflow-Rules.html).  |
| Explore the possibilities | You won't be able to unlock the full power of workflows if you don't know what they are capable of. We've collected a set of common use cases to spark your imagination. For more information, see [Use Cases for Workflows](Workflow-Use-Cases.html).  |
| Shop around | There are tons of default workflows that are already available in YouTrack and waiting to be put to good use. While many default workflow are attached to projects automatically, most are optional. Check out the list of default workflows to see if there are automations that you want to use in your project, or adapt to match your business logic. For more information, see [Default Workflows](Default-Workflows.html).  |
| Dig deeper | You've only scratched the surface. The more you know about the workflow API and how to reference its properties and methods in JavaScript, the better you can customize your projects. For more information, see [JavaScript                         Workflow                         Reference](Workflows-in-JavaScript.html).  |
| Integrate | The REST client implementation in the workflow API lets you script push-style integrations with your favorite tools. For more information, see [Make Outbound HTTP Requests](JS-Workflow-REST-API.html).  |
| Go pro | You can export this rule for editing in an IDE that supports JavaScript, like [WebStorm](https://www.jetbrains.com/webstorm/). The export option also helps you write and test workflows in a test environment before you import them to your production server. You can also import scripts that were created in an external editor. For more information, see [Import and                         Export                         Workflows](https://www.jetbrains.com/help/youtrack/cloud/?Import-Export-Workflows).  |

### Test

So this is just text



---

*Source: [https://www.jetbrains.com/help/youtrack/devportal/Quick-Start-Guide-Workflows-JS.html](https://www.jetbrains.com/help/youtrack/devportal/Quick-Start-Guide-Workflows-JS.html) · fetched 2026-09-22 08:34 Asia/Taipei*
