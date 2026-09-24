---
title: "Supported Environments"
source_url: "https://www.jetbrains.com/help/youtrack/server/youtrack-supported-environments.html"
fetched_at: "2026-09-22 08:35 Asia/Taipei"
product: YouTrack Server
---

# Supported Environments

This page describes the hardware and software requirements for YouTrack.

## Hardware Requirements

YouTrack Server does not have a specific set of hardware requirements. These requirements vary based on the size of your database and the average number of transactions that are processed on a regular basis. Use the following guidelines to estimate the requirements for your server.

| Storage | On average, YouTrack requires 1 GB of disk space to store approximately 5,000 issues. However, this is only a rough estimation. The exact amount of required space depends on the actual number and size of the files that are attached to issues in your installation. If, for example, you frequently attach large media files to each of your issues, your database will take up much more space per issue.     See, [Manage Your Database Size](manage-your-database-size.html) if you are running low on storage space or experiencing slow search queries.     > **Warning: NFS** > Your YouTrack database must use a storage solution that is directly attached to a single server or computer. Distributed file system protocols like NFS are not supported.    |
| CPU | For optimal performance, we recommend that you run YouTrack on a machine that has at least two available processors. For example, a machine with an Intel Core i3 processor or similar should be enough to start with. Larger installations with heavy traffic may require more processing power.     Starting from YouTrack version 2025.1, the Docker image for YouTrack has been made ARM-compatible. However, due to database compatibility limitations, YouTrack is not fully guaranteed to function properly in an ARM environment. We recommend opting for other deployment options if possible.    |
| Memory | YouTrack requires 1.5 GB minimum RAM.     There are minimum requirements for the amount of memory that is allocated to the Java virtual machine (JVM) that runs the YouTrack service:       * The maximum Metaspace memory must be at least 250m.    * The maximum Java heap size must be at least 1024m.                          These configuration parameters are applied to the JVM for all new installations by default.     > **Note: Smart Memory Management** > Whenever the application is restarted, it checks the current database size, excluding BLOBs (binary large objects, like attachments and large blocks of text). > > > > If the database exceeds the maximum Java heap size that is currently allocated to run the application, it automatically increases the allocation by 250 MB unless this number would be greater than 80% of the total memory available to the application. > > > > The application will continue to increase the maximum heap size until it covers the size of the existing database or reaches the 80% limit.    |

## Java

YouTrack is a web application that requires Java support. A compatible version of the JRE is bundled with the installation package, which means you don't need to install Java separately on the server that hosts the application.

You also do not need to install Java on client machines that access the application through the web interface.

## HTTP/2 and TLS

YouTrack is optimized to use the HTTP/2 protocol. Use of this protocol optimizes page load speed and helps to support live updates.

Even though the HTTP/2 standard does not require encryption, all major client implementations (Firefox, Chrome, Safari, Opera, IE, Edge) have stated that they will only support HTTP/2 over TLS. To ensure optimal performance, you need to set up an encrypted HTTPS connection with TLS(SSL) for your YouTrack Server installation.

* If your YouTrack installation uses [built-in TLS](secure-connection-for-youtrack-server.html), traffic between your server and clients uses HTTP/2 by default.

* If you install YouTrack behind a [reverse proxy server](reverse-proxy-configuration.html), we strongly recommend that you use TLS termination and configure the server to use HTTP/2 connections. To ensure that the configuration for your reverse proxy server is optimized to support your YouTrack installation, follow the [guidelines](reverse-proxy-configuration.html#Configure_Headers) that are specific to your server type.

## Operating Systems

We do our best to ensure the stability of YouTrack installations on platforms that are commonly used for public servers on the internet. However, we cannot guarantee that the application is compatible with all possible environments. For example, there are known incompatibilities with the Java Runtime Environment that is supported by the IBM z/OS operating system.

YouTrack is supported on 64-bit versions of Windows and macOS as well as most popular distributions of Linux, and other *nix environments. We regularly test and deploy on Fedora (Red Hat), Ubuntu, and Debian, but our [Docker container](youtrack-docker-installation.html) installation should work with any Linux distribution.

We do not support installations on versions of operating systems that have reached the end of their support lifecycle.

## Web Browsers

As a cloud-based application, YouTrack Server runs in a standard web browser. With the speed at which browsers are updated, it is not always possible to pre-certify every browser. We resolve functional issues in new releases of supported browsers as they arise.

YouTrack Server is supported in the two most recent stable versions of Chrome, Edge, Firefox. and Opera.

Since versioning for Safari works differently from other browsers, we support releases that meet [Baseline 2024](https://web.dev/baseline), the modern standard that defines a consistent set of web platform features supported across all major browsers. Currently, this means YouTrack supports Safari versions 17.4 or later.

To ensure the best performance and security, we recommend always running the latest available version of your browser.



---

*Source: [https://www.jetbrains.com/help/youtrack/server/youtrack-supported-environments.html](https://www.jetbrains.com/help/youtrack/server/youtrack-supported-environments.html) · fetched 2026-09-22 08:35 Asia/Taipei*
