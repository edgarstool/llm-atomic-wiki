---
title: "Restore Docker Installation"
source_url: "https://www.jetbrains.com/help/youtrack/server/restore-docker-image-installation.html"
fetched_at: "2026-09-22 08:35 Asia/Taipei"
product: YouTrack Server
---

# Restore a YouTrack Installation

> **Note: Note**
> To restore your database from a backup successfully, the version of the backup file should be the same or earlier than the version of YouTrack to which you restore this database.

Before you begin, make sure you have a backup copy of the database that you want to restore. Note the location of the backup copy so you are sure to select the correct file during this procedure.

* If you're rolling back to the previous installation version after an unsuccessful upgrade, use the backup that you created prior to installation. If you ignored this prerequisite, locate a backup file that corresponds with the version of your previous installation.

* If you're attempting to restore the current installation, locate an archived backup file in the directory that is set as the Backup location that corresponds with the current version of your installation.

## Restore an Installation from a Backup Copy of Your Database

To restore your database to the current or previous version, you need to reinstall YouTrack and use the backup as the Upgrade Source during installation.

When you restore to a previous version of YouTrack, use a backup that corresponds to the version of the product that you want to restore.

Procedure: To restore your database from a backup:

> **Tip:**
> Requires permissions: Low-level Admin Write

1. Stop the YouTrack service. For detailed instructions, see [Stop
Docker Container](stop-and-start-youtrack.html#stop-docker-container).

2. Clean the contents of the `data` and `conf` directories. You need to clean the content of these two YouTrack-specific directories on the host machine. For more details, see [Create and Configure Directories](youtrack-docker-installation.html#create-and-configure-directories) chapter of the installation instructions.

3. Make sure that the backup file that you wish to restore is located in the `backups` YouTrack directory on the host machine. The backup file must also be accessible to the user `13001:13001` that runs YouTrack service inside the container. For instance, on a Linux host machine, you can use the following commands to ensure the access:

```CONSOLE
chmod 750 <path to the backup file on the host machine>
chown 13001:13001 <path to the backup file on the host machine>
```

When you run the docker image, you need to map this directory to the corresponding directory inside the container (`/opt/youtrack/backups`).

4. Execute the following command to run a container with YouTrack server:

> **Note:**
> To make sure you see information that is relevant to your installation, select the tab that corresponds with the operating system used in your host environment.

Linux (Bash):

```CONSOLE
docker run -it --name <youtrack-server-instance> \
-v <path to data directory>:/opt/youtrack/data \
-v <path to conf directory>:/opt/youtrack/conf \
-v <path to logs directory>:/opt/youtrack/logs \
-v <path to backups directory>:/opt/youtrack/backups \
-p <port on host>:8080 \
jetbrains/youtrack:<version>
```

Windows (PowerShell):

```POWERSHELL
docker run -it --name <youtrack-server-instance> `
-v <path to data directory>:C:/opt/youtrack/data `
-v <path to conf directory>:C:/opt/youtrack/conf `
-v <path to logs directory>:C:/opt/youtrack/logs `
-v <path to backups directory>:C:/opt/youtrack/backups `
-p <port on host>:8080 `
jetbrains/youtrack-windows:<version>
```

For more details about running YouTrack container and command parameters, see [Run the Docker Container](youtrack-docker-installation.html#run-youtrack-service).

* YouTrack image starts the web-based Configuration Wizard. In a browser, open the URL of the Configuration Wizard displayed in the console output.

5. In the Configuration Wizard, select the Upgrade option.

![Configuration Wizard start page with Upgrade selected for restoring a backup.](https://resources.jetbrains.com/help/img/youtrack/2026.2/upgrade-config-wizard-start.png)

6. On the Select Upgrade Source page, select your backup as the Upgrade Source and click the Next button.

![Select Upgrade Source page with the backup archive selected in the Source field.](https://resources.jetbrains.com/help/img/youtrack/2026.2/docker-upgrade-source.png)

7. Review the locations where YouTrack stores product data. When done, click the Upgrade  button.

![Confirm Settings page showing the data locations used to restore the backup.](https://resources.jetbrains.com/help/img/youtrack/2026.2/docker-upgrade-http-confirm.png)

* YouTrack service starts with the data from the backup file.



---

*Source: [https://www.jetbrains.com/help/youtrack/server/restore-docker-image-installation.html](https://www.jetbrains.com/help/youtrack/server/restore-docker-image-installation.html) · fetched 2026-09-22 08:35 Asia/Taipei*
