---
title: "Migrate from Cloud to Server"
source_url: "https://www.jetbrains.com/help/youtrack/server/migrate-from-cloud-to-server.html"
fetched_at: "2026-09-22 08:35 Asia/Taipei"
product: YouTrack Server
---

# Migrate from Cloud to Server

This page provides instructions for migrating from a YouTrack Cloud instance that is hosted by JetBrains to a self-hosted YouTrack Server installation. When you perform this type of migration, we assume that:

* Your YouTrack Server installation is either empty or can be overwritten.

* You plan to retire your YouTrack Cloud instance and work exclusively with the Server installation or use the YouTrack Cloud instance for another purpose.

* You have already purchased a license for YouTrack Server that meets or exceeds the number of active users in your hosted instance. You need to enter the License User Name and License Key during the migration, so keep these values handy. If you currently use the free plan and are not migrating to a commercial Server license, you can use the value for the free version of YouTrack Server as shown here: | Field | Value | | --- | --- | | License username | YouTrack Default | | License key | `42bd2ce4dbaf8554bf082946a1c039d4384e81a99ed53fb75215c1b6ace8d34cf66889fdeee418cbe93d54f38f6e94a8a05a0108234b1955582d566283e3d084b23a0b8b52b016b0e610abcbbe7573fa3ff8fb3cdc9346dc94ef5f596f5b12719abcb02e6fae23d98f53f22a01788066aac7298b7fe79cc3dcd6f8df2fb41ab4` |

If you simply want to import issues from a YouTrack Cloud instance to an existing YouTrack Server installation, see [Import from YouTrack](import-from-youtrack.html).

Many administrators install and test YouTrack Server before they migrate data from an YouTrack Cloud instance and make it available to other users. In this case, the installation only contains test data that can be deleted.

If you set up a YouTrack Server installation for testing purposes, we recommend that you uninstall the test installation and migrate the data from your YouTrack Cloud instance to a clean installation of YouTrack Server.

## Export Your YouTrack Cloud Database

The first step is to export a backup copy of your YouTrack Cloud database.

The backup file contains the data from your YouTrack Cloud instance, including the issues, articles, and attachments that are stored in the database.

Procedure: To export your YouTrack Cloud database:

> **Tip:**
> Requires permissions: Low-level Admin Write

1. In YouTrack Cloud, from the main navigation menu, select ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/settings.svg) `Administration > Server Settings > Database Export`.

2. On the Database Export page, click the Create export file button. If an export file already exists, click Update export file instead.

3. When the export file has finished updating, click the Download link.

* The backup file is saved to your local directory.

## Install YouTrack Server

The next step is to install YouTrack Server with the data from your YouTrack Cloud instance. If you follow the instructions for an upgrade installation, you are given the change the data source. Use this option to install the application using the backup of your YouTrack Cloud data.

Note that the backup of your YouTrack Cloud database contains the base URL and license for your YouTrack Cloud instance. Follow the instructions in this guide to update these properties and properly configure your YouTrack Server installation.

Procedure: To install YouTrack Server using a backup from YouTrack Cloud:

1. Download and install YouTrack Server. Follow the standard installation guide up to the step where the web-based Configuration Wizard opens in your default browser.

For the complete installation guide, see [Installation](youtrack-docker-installation.html).

2. In the Configuration Wizard, click Upgrade.

3. On the Select Upgrade Source page, select the database backup that you exported from your YouTrack Cloud instance in the previous procedure.

4. Click the Next button.

* The Confirm Settings page opens.

* The Base URL displays the URL of your YouTrack Cloud instance.

5. Change the Base URL setting to the URL of your YouTrack Server installation.

6. Click the Upgrade button.

* The configuration is applied to your YouTrack Server installation.

* The YouTrack service starts using the license that is associated with your YouTrack Cloud instance. You are notified that the license can only be used for YouTrack Cloud.

7. Click the link to access the Global Settings page.

8. Enter the License User Name and License Key for YouTrack Server.

9. Click the Save button.

* Your YouTrack server runs using the updated license.

* The data from your YouTrack Cloud instance is available for use on your YouTrack Server installation.

## Migrate Notification Services

By default, YouTrack Cloud instances use an email service hosted by JetBrains to deliver notifications. After you migrate to a YouTrack Server installation, this service is no longer available. If you're not already using your own notification service, you need to set it up and connect it to your YouTrack Server installation.

To learn more, see [Connect YouTrack to an Email Service](enable-email-notifications.html).

## Migrate Mailbox Integration

If you used the Mailbox integration with a [default mailbox configuration](https://www.jetbrains.com/help/youtrack/cloud/Mailbox-Integration.html#default-mailbox-configuration) in your YouTrack Cloud instance, it would stop functioning after the migration. The default mailbox configuration is only available for YouTrack Cloud instances.

To migrate the mailbox integration from YouTrack Cloud to YouTrack Server, choose one of the two options:

| Option | Result |
| --- | --- |
| Delete the mailbox configuration |    The default mailbox configuration migrated from the YouTrack Cloud is removed along with the mailbox rules.     The issues, comments, attachments, and users created from emails remain in YouTrack. However, the references to the original emails are lost. This means that if you add a new mailbox integration, connect it to the same mailbox and try to process the same emails again, it will create duplicate entities in YouTrack.    |
| Reconfigure the mailbox connection settings to match the new environment |    The mailbox rules do not require any updates, so you can simply use the same rules with the new mailbox.     Even though the default cloud mailbox is no longer accessible, you can use the same setup with a changed support email. In this case, the threads in the mailbox and in comments will not be interrupted and just continue with the new support address.    |



---

*Source: [https://www.jetbrains.com/help/youtrack/server/migrate-from-cloud-to-server.html](https://www.jetbrains.com/help/youtrack/server/migrate-from-cloud-to-server.html) · fetched 2026-09-22 08:35 Asia/Taipei*
