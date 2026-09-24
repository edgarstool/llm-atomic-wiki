---
title: "Advanced Search"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/attribute-based-search.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Advanced Search

YouTrack supports two options for searching issues: Simple and Advanced. Advanced search lets you build search queries that locate issues using attribute and value pairs.

Not all search queries have to be attribute-based. You can also perform a [text search](full-text-search.html). In fact, you can specify search criteria that include both types of search syntax. Learning when and how to use these search syntaxes helps you find exactly the issues you're looking for every time.

Procedure: To activate advanced search:

1. From the main navigation menu, select ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/issues.svg) Issues.

2. Click the ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/filters.svg) Settings button to the right of the search box.

3. For the Search setting, select Advanced.

![The option to use advanced search for the list of issues.](https://resources.jetbrains.com/help/img/youtrack/2026.2/issue-list-settings-advanced-search.png)

## Syntax for Advanced Search

Each issue has a number of attributes, such as project, state, issue ID, and assignee. In turn, each attribute has a value. When you search, you specify the attribute that you want to check and the value currently assigned to the issues that you want to find.

Use the following guidelines to compose an attribute-based search query:

| Guideline | Example |
| --- | --- |
| Separate the attribute from the value with a colon and a space. | To find all the issues in the IDEADEV project, enter:   `project: IDEADEV` |
| List multiple values for a single attribute, separated by commas. | To find issues in the IDEADEV project that are assigned to fix versions 2018.1 and 2018.2, enter: `project: IDEADEV Fix versions: 2018.1 , 2018.2` |
| To search for specific values without referencing the attribute by name, replace the attribute name with the number sign and enter the value directly. Use the minus sign to exclude a value.     To learn more, see [Single Value Search](#single-value-search).   | To find open issues that are not normal priority, enter:   `#Open -Normal` |
| Find issues that match a range of values by entering the values that represent the upper and lower bounds, separated by two periods.     To learn more, see [Searching for a Range of Values](#search-queries-ranges).   | To find issues in the IDEADEV project that were fixed in builds from 41238 to 43006, enter: `project: IDEADEV Fixed in builds: 41238 .. 43006` |
| Replace the value that represents the upper or lower bound in a range with an asterisk to search for an open range.     To learn more, see [Searching for a Range of Values](#search-queries-ranges).   | To find unresolved issues in the IDEADEV project that have greater than 50 votes, enter: `project: IDEADEV votes: 50 .. * #Unresolved` |
| Enclose values that contain spaces with braces. | To find issues that are assigned the Support Request type, enter:   `Type: {Support Request}` |
| Enter the minus sign before a value to exclude the value from the search results. | To exclude issues that are assigned the Open and In Progress states, enter:   `State: -Open , -{In Progress}` |
| Combine multiple attribute-value pairs to refine your search. You can enter these search parameters in any order. | To find support requests in the IDEADEV project that include comments from John Davis and are not assigned the Fixed state, enter:   `project: IDEADEV State: -Fixed commenter: John Davis Type: {Support Request}`   Unlike the previous example, you don't have to set the user's full name in braces. Users' full names are resolved as usernames, which do not contain spaces.   |
| Use operators and symbols to formulate complex search criteria. Operators and symbols let you exclude or combine multiple search attributes, change the processing order, define a range of values, and more. For details, see [Operators](search-and-command-attributes.html#Operators) and [Symbols](search-and-command-attributes.html#Symbols). | To find issues in the IDEADEV project that are either support requests or include comments from John Davis and are not assigned the Fixed state, enter:   `project: IDEADEV and (Type: {Support Request} or commenter: John Davis) and State: -Fixed` |

The key to mastering attribute-based search is knowing which attributes contain the values that are relevant to the issues you want to find. For a complete list of issue attributes that are supported in search queries, see [Search Query Reference](search-and-command-attributes.html).

## Smart Search Suggestions

When you search for a value only used in a specific set of projects, the values suggested for subsequent attributes are restricted to the sets of values used in these projects as well. Values that would be inappropriate to suggest in this context are still available but appear lower in the list.

For example, if you search for items that are assigned the `State: On hold`, suggestions for additional attributes in the query will prioritize values for fields in projects that also use the On hold state. In this case, the suggested values for the `Assignee` attribute will de-prioritize users who are not in the list of possible assignees for projects that use the On hold state. You can still choose an assignee who doesn't belong to the suggested set, but the query won't return any matches.

## Search Suggestions for User Accounts

Search attributes that reference users display usernames in the auto-completion list. The following example shows how user data is displayed in auto-completion dialogs.

![Auto-completion for user accounts.](https://resources.jetbrains.com/help/img/youtrack/2026.2/search-suggestions-user-accounts-lite.png)

These suggestions are only offered when you are granted the Read User Basic permission in at least one project. If you have not been granted this permission, the only user suggested is your own account.

## Wildcards in Attribute-based Search

You can use the `*` character as a wildcard in search attributes that reference values in many custom fields and sprints. This wildcard matches zero or more characters in the search request. You can only add a wildcard to the end of an attribute value.

* You can use the `*` wildcard to find values in custom fields that store an `enum`, `state`, `ownedField`, `version`, `build`, or `string`. You can also use this wildcard for sprint names, project names, and tags.

* Wildcards are not supported for fields that store a `user`, `date`, `period`, `float`, or `integer`.

* The `?` wildcard is not supported in attribute-based search queries, even for custom fields that store a `string` type.

## Single Value Search

You can search for specific values without referencing the attribute that stores the value. YouTrack returns issues that contain the specified value in any issue attribute that does not store text.

* To search for single values, substitute the attribute with a number sign and enter the value directly. Use the minus sign to exclude a value. To find issues that are in progress that are not support requests, enter: `#{In Progress} -{Support Request}`

* To search for negative values, enter the negative number with a minus sign inside braces. To find issues with pricing values between -100 and -500, enter: `Pricing: {-100} .. {-500}`

* Use keywords to reference specific issue properties. For a complete list of keywords, see [Keywords](search-and-command-attributes.html#Keywords). To find a list of issues that you reported, are assigned, or added a comment to that are unresolved, enter: `#me -Resolved`

> **Warning: References to Values Used in Multiple Fields or Projects**
> Searching for single values is fast and easy to use, but if the value you're looking for is used in various contexts, your search results may contain unwanted matches. You may encounter this problem when:
>
>
>
> * You reference a value used in more than one field. For example, there is one project that uses Android as a value for the Subsystem field and another project that stores this value in the Platform field.
>
> * You can also have a value used for a custom field in one project that another team is using to label issues as a tag.
>
> * You reference a username as a single value. There are several issue attributes that reference user accounts, not just the Assignee. Searching for a username as a single value returns any issue where the user created the issue, applied the most recent update, added a comment, a vote, and much, much more.
>
>
>
> If you experience unpredictable behavior with a query that contains references to a single value, editing the query to include the attribute that stores the value should solve the problem.

## Searching for a Range of Values

You can search for issues that contain a value inside a range of values for a specified attribute.

Procedure: To search for a range:

1. Enter the name of the attribute, followed by a colon (`:`).

2. Enter the value that defines the upper or lower bound of the range, followed by two periods (`..`).

3. Enter the value that closes the range. To search for an open range, use the `*` character as a wildcard.

4. Execute the search query.

YouTrack applies the following logic to search queries that specify a range of values:

* The search results are always inclusive. This means that the query returns issues that contain the values that define the upper and lower bounds and every value in between. To exclude specific values, use the format `-<value>`.

* For attributes that store simple data types, YouTrack uses a basic mathematical comparison to exclude values that are less than the lower bound and greater than the upper bound. This logic applies to attributes that store a `date`, `date and time`, `period`, `integer`, and `float` type. Range search is not supported for attributes that store data as a `string` type.

* For attributes that store enumerated types, each value in the set is assigned an index number. Values with index numbers less than the lower bound and greater than the upper bound are excluded from the search results. These index numbers are assigned to each value based on the sort order that is applied to the set of values. Values can be sorted manually, by name, version, build, or by an additional property like release date or assemble date. This sort order can vary on a per-project basis. To get predictable results when you use a range of values to find issues in multiple projects, each project should use the same sort order for values in the specified field. For more information, see [Sort Values in a Set](manage-custom-fields-per-project.html#sort-values-in-set-per-project). This logic applies to attributes that store `enum`, `ownedField`, `state`, `version`, and `build` types. Range search is not supported for projects or attributes that store an enumerated type as a `user` or `group`.

The following examples show how to search for ranges of values in attributes that store different types of data. These examples show different formulations for queries that use open and closed ranges.

| Query | Range | Description |
| --- | --- | --- |
| `Spent time: 1h .. 2h` | closed | Returns issues in which the amount of spent time is at least one hour but not greater than two hours. |
| `Spent time: 8h1m .. *` | open | Returns issues in which the amount of spent time is greater than one day. This could also be written as: `Spent time: 8h .. * , - 8h` |
| `Created: 2018-03-10 .. 2018-03-13` | closed | Returns issues created from March 10 to March 13, 2018. |
| `Created: * .. 2018-03-10` | open | Returns issues created on or before March 10, 2018. |
| `Actual start: 2025-03-25T09:00 ..  2025-03-25T18:00` | closed | Returns issues started on March 25, 2025 between 09:00 and 18:00. |
| `Actual start: 2025-03-25T014:00 .. *` | open | Returns issues started on or after March 25, 2025 at 14:00. |
| `Story Points: 1 .. 5` | closed | Returns issues that are assigned at least one story point but not more than five story points. |
| `Story Points: 10 .. *` | open | Returns issues that are assigned 10 story points and higher. |
| `Price: {-100} .. {-500}` | closed | Returns issues that have a price value between -100 and -500. |
| `Price: {-500} .. *` | open | Returns issues have a price value of -500 or higher. |
| `votes: 30 .. * #Unresolved` | open | Returns unresolved issues that have 30 or more votes. |
| `Priority: * .. Major #Unresolved` | open | Returns unresolved issues that are assigned major priority or higher.     Notice how the wildcard replaces the lower bound for the range of values. In the default Priority field, the set of values is sorted manually. The values Show-stopper and Critical have index numbers that are lower than Major.   |
| `Type: Bug #Resolved Fixed in builds: 41238 .. 43006` | closed | Returns resolved issues that are categorized as bugs that are fixed in builds from 41238 to 43006. |
| `Type: Bug #Resolved Fixed in builds: 41238 .. *` | open | Returns resolved issues that are categorized as bugs that are fixed in builds 41238 and higher. |

## Searching in Attributes that Store Text

For attributes like the issue summary, description, or comments, the values are stored as text. When you specify one of these attributes in your search query, YouTrack understands that you want to check the specified attribute for one or more words. Instead of attempting to match the value of the attribute exactly, YouTrack searches inside the attribute for matches to the specified text.

The syntax for text search is slightly different from the standard used for an attribute-based search. Instead of setting multiple words in braces, you can enter as many words as you want, in any order. For example, `project: IDEADEV commenter: John Davis description: customer support` returns all issues in the IDEADEV project that include comments from John Davis and contain forms of the words "customer" and "support" in the description.

You can also search for multiple words as a phrase by setting the words in quotation marks that contain one or more words in the summary, description, or comments. For example, `project: IDEADEV commenter: John Davis description: "customer support"` returns all issues in the IDEADEV project that include comments from John Davis and contain forms of the words "customer" and "support" in the description as a phrase. For a complete description, see [Text Search](full-text-search.html).

## Query Completion

The Search box supports query completion. Query completion suggests possible attributes and values that are based on your current input. When you start typing an empty search query, YouTrack suggests attributes and values for keywords that match the current input. You can select an item from the list using your mouse or keyboard.

* If you select an attribute, the query completion suggests possible values for the selected attribute.

* If you select a single value, the value is added to the query.

![Query completion in the search box.](https://resources.jetbrains.com/help/img/youtrack/2026.2/query-completion.png)

## Visual Indicators

When you enter a query in the search box, YouTrack applies visual indicators to the query. This formatting tells you that your query has been parsed as a structured search.

![Search query with syntax elements identified and an unknown-value error displayed.](https://resources.jetbrains.com/help/img/youtrack/2026.2/search-query-highlight-lite.png)

1. Issue attributes are shown as normal text without formatting.

2. Attribute values are shown in blue text.

3. Words or phrases that are parsed as a text search are shown in gold.

4. Invalid parameters are underlined in red.



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/attribute-based-search.html](https://www.jetbrains.com/help/youtrack/cloud/attribute-based-search.html) · fetched 2026-09-22 08:34 Asia/Taipei*
