---
title: "Migrate from Server to Cloud"
source_url: "https://www.jetbrains.com/help/youtrack/server/migrate-from-server-to-cloud.html"
fetched_at: "2026-09-22 08:35 Asia/Taipei"
product: YouTrack Server
---

# Migrate from Server to Cloud

This page provides instructions for migrating from a self-hosted YouTrack Server installation to a YouTrack Cloud instance hosted by JetBrains. When you perform this type of migration, we assume that:

* You want to migrate all data from your YouTrack Server installation to a YouTrack Cloud instance.

* You want to overwrite the YouTrack Cloud database with the data from your YouTrack Server installation.

* You plan to retire your Server installation and work exclusively with the YouTrack Cloud instance or use the Server installation for another purpose.

As YouTrack Cloud is hosted, supported, and maintained by JetBrains, users do not have access to the hosting machines and services. That is, you cannot perform the complete migration yourself. Instead, you must send a migration request to YouTrack support team and provide required data.

If you want to just import issues from your YouTrack Server installation to your YouTrack Cloud instance without overwriting existing data, see [Import from YouTrack](import-from-youtrack.html).

## Special Considerations for External Hub Installations

YouTrack Cloud uses a built-in Hub service for user authentication and access management. The option to connect to an external Hub service is not supported for YouTrack Cloud. That is: If your current YouTrack Server installation is connected to an external Hub service for authentication and authorization, you will need to prepare the Hub database for migration as well. This means that you will need to provide the most recent backup of the database for your external Hub installation as well.

## Requesting Migration from YouTrack Server to YouTrack Cloud

The YouTrack support team at JetBrains provides technical support for your YouTrack Cloud instance. When you migrate from YouTrack Server to YouTrack Cloud, the support team performs the migration for you.

> **Tip:**
> Requires permissions: Low-level Admin Write

Procedure: To prepare for the migration:

1. If you do not already have a registered instance, [sign up for YouTrack Cloud](https://www.jetbrains.com/youtrack/download/get_youtrack.html).

2. Make sure that your YouTrack Cloud instance has an active subscription. The number of users and storage limits supported by your YouTrack Cloud plan should be equal to or greater than your current license for YouTrack Server. Check your plan [here](https://www.jetbrains.com/youtrack/buy/).

3. Create a backup of your YouTrack Server database:

* Open the ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/settings.svg) `Administration > Server Settings > Database Backup` page.

* Click the Backup database now button.

* Click the link to download the backup file.

4. If you use an external Hub service, create and download a backup copy of your Hub database. For instructions, refer to the [Hub documentation](https://www.jetbrains.com/help/hub/Backing-up-and-restoring-data.html?origin=old_help).

5. [Send us a request](mailto:youtrack-support@jetbrains.com) to migrate the database to your YouTrack Cloud instance.

* Attach the backup of your YouTrack Server database.

* If applicable, attach the backup of your external Hub database.

* Provide the URL of your YouTrack Cloud instance.

For security purposes, the YouTrack support team asks you to confirm the email address that was used to register the YouTrack Cloud instance. If you used a different email address to request migration, send a confirmation email from the registration address.

When the support team receives the confirmation email, they migrate the data to your YouTrack Cloud instance and notify you when the operation is complete.



---

*Source: [https://www.jetbrains.com/help/youtrack/server/migrate-from-server-to-cloud.html](https://www.jetbrains.com/help/youtrack/server/migrate-from-server-to-cloud.html) · fetched 2026-09-22 08:35 Asia/Taipei*
