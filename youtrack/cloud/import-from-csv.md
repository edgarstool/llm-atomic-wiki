---
title: "Import from CSV"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/import-from-csv.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Import from CSV

You can import data from a CSV file to YouTrack with a Google spreadsheet acting as an intermediary.

Upload your CSV file to a Google spreadsheet first, and then import data from Google to YouTrack.

## Import Details

If the spreadsheet contains references to entities that do not yet exist in YouTrack, they are created.

The YouTrack user account you use to run the import should have enough permissions to create all imported entities. We recommend using an account with a System Admin role or the Low-level Admin Write permission to run the import.

> **Note: Basic and Advanced Modes**
> Starting from version 2023.1, YouTrack supports two modes for importing data from Google Sheets: basic and advanced.
>
>
>
> Basic mode only supports importing issues, while advanced mode lets you import comments, links, and attachments.
>
>
>
> The mode depends on the way you format the data in the spreadsheet. Some instructions in this article differ for different modes. Select the corresponding tab to view the instructions and other details for the mode you plan to use.

### Imported Entities

Basic Mode:

* YouTrack creates an issue for each row in the spreadsheet.

* Columns are processed as custom fields and their values. For more details on processing custom fields, see [Importing Custom Fields](#importing-custom-fields).

* Values in columns with the type set to `user` are processed as users. YouTrack finds an existing user account or creates a new one for each user value. For details on setting a column type, see [Custom field types](#processing-field-types).

Advanced Mode:

* For each row in the spreadsheet, YouTrack creates one of the following entities: * an issue * a comment * a link between two issues * an attachment The value in the `$type$` column determines the type of the imported entity. For more details, see [Format the Data](#format-data).

* Columns are processed as entity attributes and their values. When importing issues, YouTrack processes columns as custom fields. For details on processing custom fields, see [Importing Custom Fields](#importing-custom-fields).

* Values in columns with the type set to `user` are processed as users. YouTrack finds an existing user account or creates a new one for each user value. For details on setting a column type, see [Format the Data](#format-data).

### Importing Custom Fields

YouTrack processes each column as an entity attribute or a custom field. When importing custom fields, the column header is processed as the custom field name.

Here is the list of rules that YouTrack follows when importing custom fields:

* If a column contains numeric data, YouTrack imports it into values of a `float` custom field.

* If a column contains data that can be converted into dates, YouTrack imports it into values of a `date and time` custom field. For more details about processing date values, see [Dates](#processing-dates).

* YouTrack recognizes explicitly set custom field types. You can set the field type for a column by adding the type to the column name in parentheses. For field type mapping between the spreadsheet and YouTrack, see [Custom Field Mapping](#field-mapping).

* When you import a column with its type explicitly set to `user` (for example, a column named `Assignee (user)`), YouTrack finds an existing user account or creates a new one for each value. New user accounts that exceed the license number are banned.

* YouTrack doesn't import any data from columns with names matching standard issue attributes like `updated`. For the full list of reserved field names, see [Columns with names matching standard YouTrack issue attributes](#reserved-fields).

* When YouTrack doesn't associate data from a column with any data type, it imports that column as a `string` custom field.

For details on how to prepare the data in your spreadsheet for the import, see [Format the Data](#format-data).

### Custom Field Mapping

You can set the field type for a column by adding the type to the column name in parentheses.

Currently, the import supports only a subset of custom field types available in YouTrack. This means that in some cases, even if you set a particular field type for a column, YouTrack will convert data from this column into another data type.

Here is the mapping for custom field types between the spreadsheet and YouTrack:

| Spreadsheet field type | YouTrack field type | Details |
| --- | --- | --- |
| `string` | `string` |  |
| `text` | `string` |  |
| `float` | `float` |  |
| `integer` | `float` |  |
| `state` | `state` |  |
| `enum` | `enum` |  |
| `version` | `enum` |  |
| `enum multi` | `enum (multi)` | YouTrack imports this field as multi-value enum-type field. |
| `build` | `enum (multi)` | Build-type fields are imported as multi-value `enum` custom fields. |
| `ownedField` | `string` | The import doesn't support `ownedField` field type yet. |
| `user` | `user` |    YouTrack finds an existing user account or creates a new one for each value. New user accounts that exceed the license number are banned.     To import a user account as banned, include an exclamation point before the login. Example: `!jane.doe`.    |
| `group` | `string` | The import doesn't support `group` field type yet. |
| `date and time` | `date and time` | See [Dates](#processing-dates) for supported date value formats. |
| `date` | `date and time` | See [Dates](#processing-dates) for supported date value formats. |
| `period` | `period` | Converts a value in milliseconds to a YouTrack field displaying the value in weeks, days, hours, and minutes. |

When YouTrack doesn't associate data from a column with any data type, it imports that column as a `string` custom field.

## Spreadsheet Setup

Before setting up import in YouTrack, you need to import your CSV file to a Google spreadsheet, configure the sharing settings of the spreadsheet, and preformat the data.

### Import the CSV file to Google Sheets

Procedure: To import a CSV file to Google Sheets:

1. In Google Sheets, open or create a spreadsheet.

2. From the File menu, select Import.

3. Switch to the Upload tab and upload the CSV file from your computer.

4. Select the import location and the separator type.

5. Click Import data.

* Your CSV file is imported to a Google spreadsheet.

For more details on importing data to Google Sheets, refer to the [Google documentation](https://support.google.com/docs/answer/40608).

### Configure Sharing Settings

Make sure your Google spreadsheet is shared publicly. Otherwise, YouTrack will not be able to access the data and the import won't start.

In the sharing settings of your spreadsheet, select the Anyone with the link option and set the level of access to Viewer or higher.

![Google Sheets Get link dialog with Anyone with the link set to Viewer.](https://resources.jetbrains.com/help/img/youtrack/2026.2/google-spreadsheet-sharing-settings.png)

### Format the Data

To make sure that YouTrack handles the data from your spreadsheet accurately, preformat the column names and the values as follows.

When processing column names, YouTrack is case-insensitive.

Basic Mode:

| Column or Data Type | Required |
| --- | --- |
| [Summary](#summary) | ✓ |
| [Description](#description) |  |
| [Dates](#processing-dates) |  |
| [Columns with names matching standard YouTrack issue attributes](#reserved-fields) |  |
| [Custom field types](#processing-field-types) |  |

Summary (required)
: Each imported sheet must contain a column named Summary. Data from the Summary column is converted into issue summaries.

Description
: Add a column named Description to import data from this column into issue descriptions.

Dates
: To import data values, make sure that these values match one of the supported date formats.
:
:
:
: The default import script supports the following date formats:
:
:
:
: * `dd.MM.yy`
:
: * `dd.MM.yy HH:mm`
:
: * `dd.MM.yyyy HH.mm`
:
: * `dd/MMM/yy`
:
: * `dd/MMM/yy HH:mm`
:
: * `dd MMM yyyy`
:
: * `yyyy-MM-dd`
:
: * `yyyy-MM-dd HH:mm`
:
: * `yyyy-MM-ddTHH:mmX`
:
: * `yyyy-MM-ddTHH:mm:ssX`
:
: * `yyyy-MM-ddTHH:mm:ss.SSSX`
:
:
:
: To customize the list of recognized date formats, edit the import script.

Columns with names matching standard YouTrack issue attributes
: If your spreadsheet has columns with names matching those of standard issue attributes in YouTrack, data from these columns will not be imported. If you need to import these columns, edit their names so that they do not match any of the standard issue attributes.
:
:
:
: Here is the list of the names reserved for the standard issue attributes:
:
:
:
: * `tags`
:
: * `links`
:
: * `attachments`
:
: * `comments`
:
: * `watchers`
:
: * `created`
:
: * `updated`
:
: * `author`
:
: * `voters`
:
:
:
: The name parser is case-insensitive.

Custom field types
: Define the field type for a column explicitly by adding the type to the column name in parentheses. This will ensure that YouTrack creates a custom field with the right type during the import. Example: `State (state)`.
:
:
:
: When YouTrack doesn't associate data from a column with any data type, it imports that column as a `string` custom field.
:
:
:
: For the full list of field types supported by the import, see [Custom Field Mapping](#field-mapping).

Advanced Mode:

| Column or Data Type | Required |
| --- | --- |
| [$type$](#type) | ✓ |
| [ID](#id) | ✓ |
| [Author](#author) |  |
| [Created](#created) |  |
| [Summary](#summary-advanced) | ✓ |
| [Description](#description-advanced) |  |
| [Dates](#processing-dates-advanced) |  |
| [Columns with names matching standard YouTrack issue                                 attributes](#reserved-fields-advanced)  |  |
| [Custom field types](#processing-field-types-advanced) |  |

$type$ (required)
: Define the type of the imported entity in this column. YouTrack can process four types of entities:
:
:
:
: | Entity Type | Description |
: | --- | --- |
: | `issue` | YouTrack imports this entry as an issue. |
: | `link` |    YouTrack imports this entry as a link from one issue to another.     The row representing a link must be placed below a row representing an issue. The link will connect the issue above to the issue which ID is set in the `ID` column.     ![Google spreadsheet row identifying the linked issue ID and link type.](https://resources.jetbrains.com/help/img/youtrack/2026.2/google-sheets-import-links.png)  |
: | `comment` |    YouTrack imports this entry as a comment to an issue.     The row representing a comment must be placed below a row representing an issue. The comment will be added to the issue above.     ![Google spreadsheet rows identifying issue comments and their authors.](https://resources.jetbrains.com/help/img/youtrack/2026.2/google-sheets-import-comment.png)  |
: | `attachment` |    YouTrack imports this entry as an attachment to an issue.     The row representing an attachment must be placed below a row representing an issue. The attachment will be added to the issue above.     ![Google spreadsheet row identifying an issue attachment URL.](https://resources.jetbrains.com/help/img/youtrack/2026.2/google-sheets-import-attachment.png)                             |
:
:
:
: > **Note: Basic Import Option**
: > You have the option to omit the `$type$` column and proceed with the [basic import](#basic-advanced-modes) of issues from a Google Sheets spreadsheet.
: >
: >
: >
: > If you don't include the `$type$` column in your spreadsheet, YouTrack will process all rows of the spreadsheet as issues.

ID (required)
: Each entry must have an ID value.
:
:
:
: For issues and links, the ID is the reference attribute that helps link issues together. For more details about linking issues using IDs, see [link type](#link).
:
:
:
: For comments and attachments, the ID is their unique attribute within their issue. IDs must be unique within the collection of comments or attachments, but not unique to both collections. If you have several comments or several attachments with the same ID within an issue, the import only imports the latest one and ignores all others.

Author
: In this optional attribute, you can define the author for the issue, comment, or attachment.
:
:
:
: YouTrack finds an existing user account or creates a new one for each value. New user accounts that exceed the license number are banned.
:
:
:
: To import a user account as banned, include an exclamation point before the login. Example: `!jane.doe`.
:
:
:
: If the `Author` value is not set, YouTrack imports entities as created by the `admin` user.

Created
: Optionally, set the date when an issue, comment, or an attachment was created.
:
:
:
: If the `Created` value is not set, YouTrack imports entities as created at the moment of the import.
:
:
:
: For the full list of recognized date formats, see [Dates](#processing-dates-advanced).

Summary (required)
: Each imported sheet must contain a column named Summary. Each data row must have a value in this column. If a value is missing, the import fails.
:
:
:
: Depending on the entity type, data from the Summary column is processed as follows:
:
:
:
: | Entity type set in the `$type$` column | How `Summary` column is processed |
: | --- | --- |
: | `issue` | YouTrack converts the Summary column contents into the issue summary. |
: | `link` |    YouTrack converts the Summary column contents into the name of the link type. A link of this type will connect the issue above to the issue which ID is set in the `ID` column.     If YouTrack doesn't find an issue link type with this name, it creates a new undirected link type and connects issues with this link type.    |
: | `comment` | YouTrack converts the Summary column contents into the text of the comment. This comment will be added to the issue above. |
: | `attachment` | In the Summary column, YouTrack expects a link to a file. This file will be added to the issue above as an attachment. |

Description
: Add a column named Description to import data from this column into issue descriptions.

Dates
: To import date values, make sure that these values match one of the supported date formats.
:
:
:
: The default import script supports the following date formats:
:
:
:
: * `dd.MM.yy`
:
: * `dd.MM.yy HH:mm`
:
: * `dd.MM.yyyy HH.mm`
:
: * `dd/MMM/yy`
:
: * `dd/MMM/yy HH:mm`
:
: * `dd MMM yyyy`
:
: * `yyyy-MM-dd`
:
: * `yyyy-MM-dd HH:mm`
:
: * `yyyy-MM-ddTHH:mmX`
:
: * `yyyy-MM-ddTHH:mm:ssX`
:
: * `yyyy-MM-ddTHH:mm:ss.SSSX`
:
:
:
: To customize the list of recognized date formats, edit the import script.

Columns with names matching standard YouTrack issue attributes
: If your spreadsheet has columns with names matching those of standard issue attributes in YouTrack, data from these columns will not be imported. If you need to import these columns, edit their names so that they do not match any of the standard issue attributes.
:
:
:
: Here is the list of the names reserved for the standard issue attributes:
:
:
:
: * `tags`
:
: * `links`
:
: * `attachments`
:
: * `comments`
:
: * `watchers`
:
: * `updated`
:
: * `voters`
:
:
:
: The name parser is case-insensitive.

Custom field types
: Define the field type for a column explicitly by adding the type to the column name in parentheses. This will ensure that YouTrack creates a custom field with the right type during the import. Example: `State (state)`.
:
:
:
: When YouTrack doesn't associate data from a column with any data type, it imports that column as a `string` custom field.
:
:
:
: For the full list of field types supported by the import, see [Custom Field Mapping](#field-mapping).

For details on how YouTrack import processes columns into custom fields, see [Importing Custom Fields](#importing-custom-fields).

Here is an example of a spreadsheet with columns prepared for the import:

Basic Mode:

![Google spreadsheet with basic issue fields prepared for import.](https://resources.jetbrains.com/help/img/youtrack/2026.2/spreadsheet-example-basic.png)

Advanced Mode:

![Google spreadsheet with issue links, comments, and attachments prepared for import.](https://resources.jetbrains.com/help/img/youtrack/2026.2/spreadsheet-example.png)

## Set up an Import from Google Sheets

Before you add a new import configuration, you need to create an API key associated with a project in Google. After that, you'll be able to set up an import in YouTrack.

### Create an API Key in Google

Due to Google policies, the YouTrack import script can only use the Google API if the requests are linked to a project in Google. To set up an import of data from Google Sheets, you need to create an API key associated with your Google account and a project in Google.

Procedure: To create an API key in Google:

1. Open [Google Cloud Console](https://console.cloud.google.com/).

2. Log in using your Google account.

3. Create a new project or select an existing one.

4. From the Navigation menu on the left, select `APIs and services > Enabled APIs and services`.

5. Click Enable APIs and services, find the Google Sheets API, and enable it for your project.

![Google Cloud Google Sheets API page with the Enable button.](https://resources.jetbrains.com/help/img/youtrack/2026.2/enable-google-sheets-api.png)

6. Go back to the Enabled APIs and services page.

7. Click Enable APIs and services, find the Google Drive API, and enable it for your project.

![Google Cloud Google Drive API page with the Enable button.](https://resources.jetbrains.com/help/img/youtrack/2026.2/enable-google-drive-api.png)

8. From the Credentials section, click Create credentials and select API key.

* You have created an API key associated with your Google account and a project in Google.

![Google Cloud API key created dialog with the generated key displayed.](https://resources.jetbrains.com/help/img/youtrack/2026.2/google-api-key.png)

9. Copy the API key to enter it in the import setup wizard.

For more information on API keys in Google, refer to the [Google documentation](https://cloud.google.com/docs/authentication/api-keys).

### Configure an Import from Google Sheets in YouTrack

The setup wizard guides you through the setup process.

Procedure: To configure an import from Google Sheets:

> **Tip:**
> Requires permissions: Low-level Admin Write

1. From the main navigation menu, select ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/settings.svg) `Administration > Integrations > Imports`.

2. Click New import to open the setup dialog.

![New Import dialog listing supported source services.](https://resources.jetbrains.com/help/img/youtrack/2026.2/new-import-dialog.png)

3. Select CSV.

* The import dialog for a new import from CSV opens. From here, you'll be redirected to set up import from Google Sheets.

![New Import from CSV page explaining the Google Sheets upload step.](https://resources.jetbrains.com/help/img/youtrack/2026.2/new-csv-import-dialog.png)

Alternatively, select the Google Sheets option right away without selecting CSV first.

4. Click Next.

* The import dialog for a new import from Google Sheets opens.

5. Configure the import settings:

![New Import from Google Sheets step with spreadsheet URL and API key fields.](https://resources.jetbrains.com/help/img/youtrack/2026.2/google-sheets-new-import-settings.png)

| Setting | Description |
| --- | --- |
| Spreadsheet URL |    The public link of the spreadsheet in Google Sheets. Configure the sharing settings for the spreadsheet to allow anyone with the link to view the file.    |
| API key | The [API key](#api-key) that you have generated in your Google account to access the target spreadsheet.  |

When done, click Next.

6. Review the settings that you have provided.

Select the sheets and the target YouTrack projects for the import. For more details about the project mapping configuration, see [Project Mapping](#project-mapping).

![Import confirmation step with project mappings and the Start import button.](https://resources.jetbrains.com/help/img/youtrack/2026.2/google-sheets-import-settings-confirm.png)

7. When done, click Start import.

* YouTrack will create a project of the same name as the target sheet in the Google spreadsheet and import issues, custom fields, and users. If you have configured a project mapping, YouTrack will create new projects and import data to the existing ones according to the mapping.

When you have set up an import, it appears in the Imports list. To view configuration and import details, select the import configuration from the list.

![Import details showing status and imported item counts.](https://resources.jetbrains.com/help/img/youtrack/2026.2/google-sheets-import-result.png)

In the details sidebar, YouTrack shows import status and details on the data that was imported. Click the ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/refresh.svg) Resume button in the toolbar to explicitly start polling for changes and importing updates from the selected sheets in the Google spreadsheet.

* The content of issues is updated when the `Updated` field in the import has a more recent date/time than the `Updated` field in the corresponding YouTrack issues.

* If the `Updated` field in the import is empty, the corresponding issues in YouTrack will be updated.

* Only new comments are added during an update. Edited comments are not modified.

You can also download the import log file to study and investigate when needed.

## Project Mapping

On the final step of the import setup, you can select those sheets in the Google spreadsheet that you want to import to YouTrack. You can also choose whether to create a new project for the import or import data into an existing project in YouTrack.

YouTrack recognizes when a web address has already mapped a source project by a previous import. Imported source projects that have already been mapped in YouTrack aren't selectable. You can create multiple import jobs from the same source without importing duplicate data.

![Project Mapping step pairing source projects with YouTrack projects.](https://resources.jetbrains.com/help/img/youtrack/2026.2/google-sheets-import-settings-confirm.png)

Procedure: To configure project mapping:

1. From the main navigation menu, select ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/settings.svg) `Administration > Integrations > Imports`.

2. Locate those sheets that you want to import.

Use the filter bar on the right to filter the sheets by name.

3. Select the sheets that you want to import. Select the option at the top of the list to import all available sheets.

4. Select a target YouTrack project for each sheet.

* When loading the list of sheets for mapping, YouTrack checks for existing YouTrack projects with corresponding names. If it finds a YouTrack project with the same name as the sheet in the Google spreadsheet, YouTrack suggests it as the target project.

* If there is no existing YouTrack project with the corresponding name, YouTrack suggests creating a new one.

5. If you want to change a target project, select another option from the corresponding dropdown on the list.

6. Click Next to start import.

* Import starts.

## Import Options

After the initial import, the following controls are available in the sidebar:

![Import details with Resume, Edit, and Delete actions.](https://resources.jetbrains.com/help/img/youtrack/2026.2/google-sheets-import-options.png)

| Control | Description |
| --- | --- |
| Disable/Enable | Disable or enable the import. This lets you keep the settings for an import even if you aren't using it. |
| Resume | Immediately imports any changes made in the selected sheets in the Google spreadsheet after the previous import. |
| Edit | Opens the integration settings page in edit mode. Use this option to connect to a different Google spreadsheet, update the API key, or update project mapping. |
| Delete | Deletes the current import settings. Imported content remains unless you choose to permanently delete affected projects. For details, see [Delete an Import](delete-import.html). |
| Download import log | Downloads the import log. Use this option to view and investigate errors that occurred during import. |



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/import-from-csv.html](https://www.jetbrains.com/help/youtrack/cloud/import-from-csv.html) · fetched 2026-09-22 08:34 Asia/Taipei*
