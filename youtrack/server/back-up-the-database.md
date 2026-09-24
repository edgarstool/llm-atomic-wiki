---
title: "Database Backup"
source_url: "https://www.jetbrains.com/help/youtrack/server/back-up-the-database.html"
fetched_at: "2026-09-22 08:35 Asia/Taipei"
product: YouTrack Server
---

# Database Backup

YouTrack uses its own in-process database, no dedicated database server is required.

> **Note: Database Accessibility**
> Please ensure that database files are accessible from within YouTrack!
>
>
>
> * The user account that runs the YouTrack service should always have permission to create, modify, and read database files.
>
> * Access to database files over the network is prohibited because YouTrack cannot guarantee the durability of your data when accessed in this way. Specifically, you must not use NFS to store the YouTrack database.

Each backup file contains a snapshot of your database, including all the attachments that were stored on your server at the time the file was created.

A collection of valid backup files can come in handy if you need to restore your installation after an outage or attack. We strongly recommend that you enable regular backup of your YouTrack database and set up notifications should the backup fail.

> **Note: About the Backup Archive**
> The backup archive is intended for supported backup, restore, and migration scenarios.
>
>
>
> We don't document the internal structure of the archived database or recommend modifying records directly in the database. If you need to update your data, use the supported features in YouTrack, the REST API, workflows, or import tools instead.

To protect your installation against ransomware and recover from hardware or software failure, you should back up your YouTrack database on a regular basis. You should always have at least one recent, valid backup copy of your database that you can use to restore your installation.

To access your database management settings, open the ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/settings.svg)  Administration menu and select `Server Settings > Database Backup`.

![YouTrack interface showing database backup.](https://resources.jetbrains.com/help/img/youtrack/2026.2/database-backup.png)

You can back up YouTrack database right away or use a cron expression to back up the database on a set schedule (see [cron expression syntax](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) for reference).

> **Note: Cron Expression Format**
> YouTrack evaluates cron expressions using the Quartz Job Scheduling Library. To ensure that your cron expressions are interpreted correctly:
>
>
>
> * Specify values for six fields (second, minute, hour, day of the month, month, day of the week), not five.
>
> * Specify the day of the week as a value between 1 and 7, where 1 represents Sunday. It also accepts three-letter abbreviations for SUN-SAT. Expressions that use values between 0 and 7 where both 0 and 7 represent Sunday will not be parsed as expected.

There are several things to take note of regarding YouTrack database settings and controls:

* If YouTrack uses a built-in Hub service, YouTrack automatically switches the Hub database to read-only mode when you start the database backup. This preserves the synchronization between the YouTrack and Hub databases. Users can continue working with issues in YouTrack while the backup runs, but most settings on administrative pages are read only until the backup is complete. For best results, schedule backups outside of working hours.

* You can't cancel the database backup once it has started.

* Notifications about the status of the database backup can only be configured for YouTrack application administrators.

## Configure Backup Settings

You can modify the default settings of your database backup configuration.

Procedure: To configure database backup settings:

> **Tip:**
> Requires permissions: Low-level Admin Write

1. From the main navigation menu, select ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/settings.svg) `Administration > Server Settings > Database Backup`.

2. In the Backup Location field, set the location of the backup folder for your server.

3. Set the Archive Format to determine whether the backup files are created as a TAR.GZ or ZIP archive.

The maximum size of the ZIP backup file is 2Gb. For larger databases, use TAR.GZ archives.

4. In the Notify about Failures drop-down list, select the users who receive notification messages about the database backups.

To receive notifications for database backup, the user must also have the Low-level Admin Write permission.

5. To configure automated backups, select the Enable regular backup check box. When you enable regular backup, the following settings are displayed:

* Backup Interval — Set the schedule for automatic backups. Select one of the pre-configured intervals or use a cron expression to set up a custom interval (for additional instructions, see [cron expression syntax](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html)).

* Backup Files Rotation — Specify a number of the database backup files to keep. This parameter lets you create a rotation of database backups. Only the specified number of the backups files is kept on your server. To disable the automatic backup rotation, set the number to '0' (zero). In this case, all backups files are kept and must be deleted manually. To delete a backup file manually, select the file in the list and click the trash button.

## Restore Your Installation

One of the primary reasons for storing backups is to keep a valid copy of your data that you can use to recover from hardware or software failure. To keep your data safe, we strongly recommend that you enable regular backup of your database and test the process of restoring your installation.

For additional information and instructions, see [Restore a YouTrack Installation](restore-docker-image-installation.html).



---

*Source: [https://www.jetbrains.com/help/youtrack/server/back-up-the-database.html](https://www.jetbrains.com/help/youtrack/server/back-up-the-database.html) · fetched 2026-09-22 08:35 Asia/Taipei*
