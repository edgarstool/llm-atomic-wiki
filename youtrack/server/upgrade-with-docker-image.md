---
title: "Upgrade with Docker"
source_url: "https://www.jetbrains.com/help/youtrack/server/upgrade-with-docker-image.html"
fetched_at: "2026-09-22 08:35 Asia/Taipei"
product: YouTrack Server
---

# Upgrade

This page describes various ways you can upgrade a YouTrack installation using a Docker image.

## Prerequisites

Before you upgrade, perform the following prerequisite tasks:

* [Create a backup of your current database](back-up-the-database.html). YouTrack Server does not provide forward database compatibility. Your database is migrated to the format that is compatible with the latest version during the upgrade procedure. This means that you cannot revert to a previous version and continue to use the database that was processed during the upgrade.

* Copy the backup of your current database to a secure location just in case you encounter problems with the upgrade and need to roll back to the previous version.

* Verify that your YouTrack license supports the upgrade. To view the license limitations, open the Administration menu and select `System Settings > Global Settings`, then select the License Details tab. If your free update period or subscription has expired, you need to [extend your subscription](https://www.jetbrains.com/youtrack/buy/#stand-alone).

* Mind the [recommended upgrade path](#upgrade-matrix).

### Recommended Upgrade Path

| Installation Version | Target Version |
| --- | --- |
| Any YouTrack installation earlier than 6.5 | YouTrack 6.5 |
| 6.5 | YouTrack 7.0 |
| 7.0 | 2017.1 |
| 2017.x | 2018.x |
| 2018.x | 2019.x |
| 2019.x | 2020.x |
| 2020.x | 2021.x |
| 2021.x | 2022.x |
| 2022.x | 2023.1 --> 2023.2 or 2023.3 |
| 2023.2 or 2023.3 | 2024.x |
| 2024.x | 2025.1 or 2025.2 --> 2025.3 |
| 2025.3 | 2026.x |

To locate the current version and build number for your YouTrack Server installation, open the Help menu in the main navigation.

![The current version number for a YouTrack Server installation.](https://resources.jetbrains.com/help/img/youtrack/2026.2/youtrack-server-current-version.png)

### Database Changes in YouTrack 2023.1

YouTrack version 2023.1 contains an incremental upgrade to the internal database used to store YouTrack data. To ensure that your data is migrated to the new database schema, we encourage you to upgrade from YouTrack versions released in 2022 to YouTrack 2023.1, then to 2023.2 or 2023.3 before proceeding with an upgrade to later versions.

### Dashboard Migrations Removed in YouTrack 2025.3

In YouTrack version 2024.3, we introduced support for apps. This update included a migration scheme that replaced existing dashboard widgets with widgets from the new apps. We also migrated from the Hub widget API to the new Host API for apps.

In YouTrack version 2025.3, we removed the migration code introduced in 2024.3. This means that direct upgrade from version 2024.2 and earlier to 2025.3 is not supported. To ensure that your dashboards are migrated properly, we recommend upgrading any YouTrack 2024 version to 2025.1 first, then upgrading to 2025.3.

## Upgrade a Docker Installation

If all you want to do is upgrade your YouTrack installation from one version to another without changing any environmental variables, you can simply apply the update and skip the web-based Configuration Wizard.

This is done by adding the following parameter to the configuration file the application reads on each new start.

```CONSOLE
-Ddisable.configuration.wizard.on.upgrade=true
```

This upgrade procedure is described below.

Procedure: To upgrade an existing Docker installation

1. [Create a backup](back-up-the-database.html) of the YouTrack database while your existing YouTrack installation is running.

2. Use the following command to [stop the Docker container](stop-and-start-youtrack.html#stop-docker-container):

```CONSOLE
docker exec <CONTAINER_ID> stop
```

If you don't know the ID of the YouTrack container, use the following command to get a list of the Docker containers for your server:

```CONSOLE
docker ps -a
```

3. Use the following command to remove the container with the previous version.

```CONSOLE
docker rm <CONTAINER_ID>
```

If you try to run the updated container without removing the previous version, the command will fail due to conflicts with duplicate container names.

4. Add the following parameter to your `youtrack.jvmoptions` file:

```CONSOLE
-Ddisable.configuration.wizard.on.upgrade=true
```

For specific instructions, see [Update JVM Options Manually](configure-jvm-options.html#set-jvm-options-manually).

> **Note:**
> You should only have to update this start parameter once. If you have already added this parameter to the startup configuration file for your YouTrack installation, continue from the next step.

5. Run the following command to pull and run an image for the target YouTrack version. All other attributes of the command (volumes and port mappings) must be the same as those that you used with the previous version of the YouTrack image:

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
jetbrains/youtrack:<new version>
```

Use the following information to customize this command as needed:

* `-it` is a command-line flag that attaches both the input and output of the container to your terminal. This lets you see the output produced by the container as if it were running directly in your terminal. When the container starts, you will see the log messages generated during the initialization process as well. Pressing `Ctrl` + `C` while the terminal is attached to a container's output sends an interrupt signal to the container's running process. This is similar to how you would stop a regular process in your terminal. This command causes the container to shut down, so be cautious when using `Ctrl` + `C` in this context. If you want to detach the terminal from the container output without interrupting the processes running in it, press `Ctrl` + `P` followed by `Ctrl` + `Q`. For more details, please refer to the [official docker documentation](https://docs.docker.com/engine/reference/commandline/attach/#extended-description).

* `--name youtrack-server-instance` is an arbitrary name for the container. By default, Docker generates random and sometimes cryptic names for containers. Use the `--name` option to give your container a more meaningful and human-readable name that makes it easier to identify and manage.

* `-v <path to <name> directory>:C:/opt/youtrack/<name>` specifies the location of the storage provisioned on the host machine and maps them to the corresponding `C:/opt/youtrack/<name>` directories inside the container.

* `-p <port on host>:8080` is a parameter that defines the port mapping. This tells the host machine to listen for traffic on the `<port on host>` port and propagate all traffic to port `8080` inside the container. The listen port must be accessible to end users or to the reverse proxy server, if one is in use. This may require explicitly opening access to this port through the firewall.

* `jetbrains/youtrack:<new version>` is a reference to the specific YouTrack version and build hosted in the [Docker Hub Repository](https://hub.docker.com/r/jetbrains/youtrack/).

Windows (PowerShell):

```POWERSHELL
docker run -it --name <youtrack-server-instance> `
-v <path to data directory>:C:/opt/youtrack/data `
-v <path to conf directory>:C:/opt/youtrack/conf `
-v <path to logs directory>:C:/opt/youtrack/logs `
-v <path to backups directory>:C:/opt/youtrack/backups `
-p <port on host>:8080 `
jetbrains/youtrack-windows:<new version>
```

Use the following information to customize this command as needed:

* `-it` is a command-line flag that attaches both the input and output of the container to your terminal. This lets you see the output produced by the container as if it were running directly in your terminal. When the container starts, you will see the log messages generated during the initialization process as well. Pressing `Ctrl` + `C` while the terminal is attached to a container's output sends an interrupt signal to the container's running process. This is similar to how you would stop a regular process in your terminal. This command causes the container to shut down, so be cautious when using `Ctrl` + `C` in this context. If you want to detach the terminal from the container output without interrupting the processes running in it, press `Ctrl` + `P` followed by `Ctrl` + `Q`. For more details, please refer to the [official docker documentation](https://docs.docker.com/engine/reference/commandline/attach/#extended-description).

* `--name youtrack-server-instance` is an arbitrary name for the container. By default, Docker generates random and sometimes cryptic names for containers. Use the `--name` option to give your container a more meaningful and human-readable name that makes it easier to identify and manage.

* `-v <path to <name> directory>:/opt/youtrack/<name>` specifies the location of the storage provisioned on the host machine and maps them to the corresponding `/opt/youtrack/<name>` directories inside the container.

* `-p <port on host>:8080` is a parameter that defines the port mapping. This tells the host machine to listen for traffic on the `<port on host>` port and propagate all traffic to port `8080` inside the container. The listen port must be accessible to end users or to the reverse proxy server, if one is in use. This may require explicitly opening access to this port through the firewall.

* `jetbrains/youtrack-windows:<new version>` is a reference to the specific YouTrack version and build hosted in the [Docker Hub Repository](https://hub.docker.com/r/jetbrains/youtrack-windows/).

There are several configuration parameters that can be updated during an upgrade installation. This includes:

* Switching from HTTP to HTTPS and vice versa.

* Changing the base URL or application listen port for your YouTrack installation.

If you want to apply one or more of these changes to the YouTrack environment, remove the configuration parameter that suppresses the Configuration Wizard, then modify the parameters that you want to update in the web-based Configuration Wizard.

## Upgrade an Existing Installation from a Database Backup using a Docker Image

You also have the ability to upgrade any installation type using a Docker image by downloading a backup copy of your YouTrack database and using the backup as the upgrade source in the configuration wizard during installation of the latest version.

This procedure can be used to upgrade any installation type (JAR, MSI, or ZIP). It can also be used to migrate an installation from one Docker container to another during the upgrade process, including migration from the Linux-based distribution to a Windows-native Docker image.

> **Note:**
> If the backup was exported from a YouTrack Cloud instance, follow the instructions in [Migrate from Cloud to Server](migrate-from-cloud-to-server.html) instead.
>
>
>
> That migration requires additional steps, including updating the Base URL and replacing the Cloud license with a YouTrack Server license.

Procedure:

1. [Create a backup](back-up-the-database.html) of the YouTrack database while your existing YouTrack installation is running.

2. [Stop the existing YouTrack service](stop-and-start-youtrack.html).

3. Pull an image for the target YouTrack version from the [Docker Hub Repository](https://hub.docker.com/r/jetbrains/):

Linux:

```CONSOLE
docker pull jetbrains/youtrack:<version>
```

Replace `<version>` with the complete version number and build. For a complete list of release versions, check [Docker Hub](https://hub.docker.com/r/jetbrains/youtrack/tags/).

Windows:

```CONSOLE
docker pull jetbrains/youtrack-windows:<version>
```

Replace `<version>` with the complete version number and build for a Windows Server host that is configured to run Windows containers. For a complete list of release versions, check [Docker Hub](https://hub.docker.com/r/jetbrains/youtrack-windows/tags/).

4. [Create and configure YouTrack-specific directories on the host machine.](youtrack-docker-installation.html#create-and-configure-directories)

5. Copy the backup file of the YouTrack database into the `backups` directory that you created in the previous step.

6. Run the following command to launch YouTrack in a container, mapping its data volumes and listen port:

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

Use the following information to customize this command as needed:

* `-it` is a command-line flag that attaches both the input and output of the container to your terminal. This lets you see the output produced by the container as if it were running directly in your terminal. When the container starts, you will see the log messages generated during the initialization process as well. Pressing `Ctrl` + `C` while the terminal is attached to a container's output sends an interrupt signal to the container's running process. This is similar to how you would stop a regular process in your terminal. This command causes the container to shut down, so be cautious when using `Ctrl` + `C` in this context. If you want to detach the terminal from the container output without interrupting the processes running in it, press `Ctrl` + `P` followed by `Ctrl` + `Q`. For more details, please refer to the [official docker documentation](https://docs.docker.com/engine/reference/commandline/attach/#extended-description).

* `--name youtrack-server-instance` is an arbitrary name for the container. By default, Docker generates random and sometimes cryptic names for containers. Use the `--name` option to give your container a more meaningful and human-readable name that makes it easier to identify and manage.

* `-v <path to <name> directory>:C:/opt/youtrack/<name>` specifies the location of the storage provisioned on the host machine and maps them to the corresponding `C:/opt/youtrack/<name>` directories inside the container.

* `-p <port on host>:8080` is a parameter that defines the port mapping. This tells the host machine to listen for traffic on the `<port on host>` port and propagate all traffic to port `8080` inside the container.

The YouTrack service starts on `{0.0.0.0:8080}` inside the Docker container, and port 8080 is mapped to the specified <port on host>. This way the service can be accessed from any machine that has network access to the <port on host> of your host machine. For instance, if the fully qualified domain name (FQDN) of the host machine is host.mydomain.com and the <port on host> is 7777, the service will be available at `http://host.mydomain.com:7777`.

> **Note: Picking the Right Port**
> Port 8080 is typically used for non-secure HTTP traffic. If you plan to run YouTrack behind a reverse proxy server, you can safely install the application using this port. Otherwise, we only recommend using this port for testing purposes.
>
>
>
> If you want to configure YouTrack to secure traffic using built-in TLS, choose port 8443 instead.

The YouTrack service starts with a web-based Configuration Wizard. The wizard is accessible from the web address where the service is hosted.

The Configuration Wizard is secured with a one-time access token, which you need to copy from the log output from Docker. For example:

`JetBrains YouTrack 2025.1 Configuration Wizard will listen inside container on {0.0.0.0:8080}/ after start and can be accessed by URL [http://<put-your-docker-HOST-name-here>:<put-host-port-mapped-to-container-port-8080-here>//?wizard_token=FOT8QIzHuktzvxtiT1Ax]`

Using the example from the previous section, the Configuration Wizard would be available from `http://host.mydomain.com:7777//?wizard_token=FOT8QIzHuktzvxtiT1Ax`

7. Open the URL for the Configuration Wizard in your web browser.

8. In the Configuration Wizard, click Upgrade.

![Configuration Wizard start page with Upgrade selected.](https://resources.jetbrains.com/help/img/youtrack/2026.2/upgrade-config-wizard-start.png)

9. On the Select Upgrade Source page, click the Select button and select the backup file as an upgrade source.

![Select Upgrade Source page with a backup archive selected in the Source field.](https://resources.jetbrains.com/help/img/youtrack/2026.2/docker-upgrade-source.png)

Click Next.

10. On the Confirm Settings page, confirm your system settings and the location of system directories.

![Confirm Settings page HTTP tab showing the Base URL and upgrade data locations.](https://resources.jetbrains.com/help/img/youtrack/2026.2/docker-upgrade-http-confirm.png)

11. Review your license. If required, you can also update your license on this page.

12. When done, click Upgrade.

* YouTrack Server launches its components. Do not close the page in the browser until the setup is complete. When the YouTrack Server server is ready, you are redirected to the login page.

13. Enter the credentials for the YouTrack Server administrator account and click the Log in button.

* YouTrack opens to the Dashboard page.

Your YouTrack Server installation is upgraded and ready to use.



---

*Source: [https://www.jetbrains.com/help/youtrack/server/upgrade-with-docker-image.html](https://www.jetbrains.com/help/youtrack/server/upgrade-with-docker-image.html) · fetched 2026-09-22 08:35 Asia/Taipei*
