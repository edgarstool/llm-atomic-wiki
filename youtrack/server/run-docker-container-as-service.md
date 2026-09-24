---
title: "Run Docker as a Service"
source_url: "https://www.jetbrains.com/help/youtrack/server/run-docker-container-as-service.html"
fetched_at: "2026-09-22 08:35 Asia/Taipei"
product: YouTrack Server
---

# Run Docker Container as a Service

Docker recommends using their cross-platform built-in restart policy for running a container as a service. For this, [configure your Docker service to start on system boot](https://docs.docker.com/install/linux/linux-postinstall/#configure-docker-to-start-on-boot) and add the `--restart unless-stopped` parameter to the `docker run` command that starts YouTrack.

If you want to start multiple services one after the other, including YouTrack, the restart policy won't work well. In such cases, it's better to [use a process manager](https://docs.docker.com/config/containers/start-containers-automatically/#use-a-process-manager) instead.

Specific instructions for setting up a restart policy vary by operating system. To make sure you see information that is relevant to your installation, select the tab that corresponds with the operating system used in your host environment.

Linux (Bash):

Here's an example of how to run YouTrack container as a service on Linux with help of `systemd`.

Procedure: To run the YouTrack container as a service on Linux with systemd

1. Create a service descriptor file `/etc/systemd/system/docker.youtrack.service`:

```CONSOLE
[Unit]
Description=YouTrack Service
After=docker.service
Requires=docker.service

[Service]
TimeoutStartSec=0
Restart=always
ExecStartPre=-/usr/bin/docker exec %n stop
ExecStartPre=-/usr/bin/docker rm %n
ExecStartPre=/usr/bin/docker pull jetbrains/youtrack:<version>
ExecStart=/usr/bin/docker run --rm --name %n \
-v <path to data directory>:/opt/youtrack/data \
-v <path to conf directory>:/opt/youtrack/conf \
-v <path to logs directory>:/opt/youtrack/logs \
-v <path to backups directory>:/opt/youtrack/backups \
-p <port on host>:8080 \
--stop-timeout 60 \
jetbrains/youtrack:<version>
ExecStop=/usr/bin/docker exec %n stop

[Install]
WantedBy=default.target
```

2. Enable starting the service on system boot with the following command:

```CONSOLE
systemctl enable docker.youtrack
```

You can also stop and start the service manually at any moment with the following commands, respectively:

```CONSOLE
sudo service docker.youtrack stop
sudo service docker.youtrack start
```

Windows (PowerShell):

For Windows Server, you can run YouTrack with Docker Compose and rely on the container restart policy to start it automatically after the host restarts.

* Prepare the host to run Windows containers using a supported container runtime. For setup guidance, refer to the [installation instructions](youtrack-docker-installation.html#prepare-environment-docker) and the [official Windows documentation](https://learn.microsoft.com/en-us/virtualization/windowscontainers/quick-start/set-up-environment?tabs=dockerce#windows-server).

* Create a Docker Compose File. A Docker Compose file is typically a `.yml` that defines your containerized application and its configuration. In this case, your file contains the parameters you would typically use to run YouTrack. Here's an example you can use as a guide for writing your file: ```YAML version: "3" services: YouTrack: container_name: youtrack-server image: jetbrains/youtrack-windows:<version> user: "13001:13001" restart: unless-stopped ports: - "<port on host>:8080" volumes: - <path to data folder>:C:/opt/youtrack/data - <path to conf folder>:C:/opt/youtrack/conf - <path to logs folder>:C:/opt/youtrack/logs - <path to backups folder>:C:/opt/youtrack/backups ```

* Start the Compose application. Open a Command Prompt or PowerShell with administrative privileges. Navigate to the directory where your Docker Compose file is located and use the following command: ```CONSOLE docker compose -f docker-compose.yml up -d ``` This command starts YouTrack in detached mode and applies the restart policy declared in the Compose file.

You can then manage the YouTrack container using standard Docker Compose commands. For example:

* To stop the service, use: `docker compose -f docker-compose.yml down`

* To check the service status, use: `docker compose -f docker-compose.yml ps`

If the server shuts down for whatever reason, Docker will automatically restart the container on reboot.

In order for this to work, you must configure the container runtime and the Windows Server host to start automatically when the server boots up. For specific instructions, please refer to the documentation for your server operating system and container runtime.

> **Warning: Stopping YouTrack**
> When you shut down the server or host environment where the container is deployed, you need to make sure that YouTrack is given sufficient time to shut down as well.
>
>
>
> This means your system controllers should be sending instructions to stop the YouTrack service before shutting down the server.
>
>
>
> For specific instructions, see [Stop a Docker container](stop-and-start-youtrack.html#stop-docker-container).



---

*Source: [https://www.jetbrains.com/help/youtrack/server/run-docker-container-as-service.html](https://www.jetbrains.com/help/youtrack/server/run-docker-container-as-service.html) · fetched 2026-09-22 08:35 Asia/Taipei*
