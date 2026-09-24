---
title: "YouTrack Cloud Database Backups"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/youtrack-cloud-database-backups.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# YouTrack Cloud Database Backups

Like the self-hosted version, YouTrack Cloud uses its own in-process database.

With a hosted instance, you cannot change the database location or restore your instance from a backup file. These operations are performed by the JetBrains YouTrack team. In the unlikely event that you need to restore your database from a backup, [contact YouTrack support](mailto:youtrack-support@jetbrains.com).

For each YouTrack Cloud instance, we automatically create and store the following database backups:

| Type | Quantity | Description |
| --- | --- | --- |
| Daily | 7 | Stores a snapshot of the database for a specific day. When a new backup is created, the backup that is more than one week old is deleted. |
| Weekly | 3 | One of the daily snapshots that was taken towards the end of the calendar week. When a new backup is created at the end of the week, the oldest weekly backup in the set is deleted. |
| Monthly | 11 | One of the daily snapshots that was taken towards the end of the calendar month. When a new backup is added to this set at the end of the month, the oldest monthly backup in the set is deleted. |

Backups are created for each instance separately. This is an automated process that creates a backup for one instance then moves on to the next. As such, these instances are not backed up at a fixed time each day. If you find yourself in a situation where you want to restore your instance from a backup, the YouTrack support team can tell you which points in time can be restored to.

## Database Export

In addition to an automatic backup, which is configured and maintained by the YouTrack team, you can create a backup copy of your database and download the archive to your local machine. Use this option when you want to import the data to a self-hosted YouTrack installation or for troubleshooting.

For more information, see [Database Export](database.html).

## Backup Policy for Inactive Instances

When your YouTrack license or subscription expires, your instance is considered inactive. Inactive instances are scheduled for deletion after a predefined period of time. For details, see [Automatic Deletion of Inactive Instances](instance-cancellation.html#automatic-deletion).

When an instance is deleted automatically, we retain a backup copy of the database for up to six months. During this time, we can restore the data to another active instance or send a copy of the latest backup files upon request. After six months, we delete the backup. It is no longer possible to restore the instance using our copy of the database.



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/youtrack-cloud-database-backups.html](https://www.jetbrains.com/help/youtrack/cloud/youtrack-cloud-database-backups.html) · fetched 2026-09-22 08:34 Asia/Taipei*
