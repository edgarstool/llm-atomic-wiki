---
title: "Security"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/security.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Security

YouTrack Cloud is a hosting platform that is designed and used by JetBrains to deliver YouTrack as a service. Each YouTrack Cloud instance is physically located on a server, hosted by Amazon Web Services (AWS).

The number of instances per server depends on several parameters, such as database size and number of online users. We permanently monitor each server load and activity to maintain well-balanced performance. When server activity reaches a certain level, we close this server for any new registrations.

* The JetBrains Operations team is responsible for provisioning, monitoring, and managing the servers that host YouTrack Cloud instances.

* The YouTrack Support team provides technical support to YouTrack Cloud subscribers.

We monitor these servers around the clock to ensure their availability and security. Even so, there are a number of things that you can do to protect your data. For more information, see [Secure Your Instance](secure-your-installation.html).

## Data Center Location

A new instance is created on the server with the lowest load and based on the customer preference of data center location:

| Region Name | Region |
| --- | --- |
| US West (Northern California) | us-west-1 |
| Europe (Frankfurt) | eu-central-1 |
| Europe (Ireland) | eu-west-1 |
| Asia Pacific (Singapore) | ap-southeast-1 |

The location of the data center is chosen by the instance owner when the instance is started for the first time.

The current data center location is displayed on the Global Settings page. To move your instance to a different data center, submit a request to [YouTrack Support](https://youtrack-support.jetbrains.com/hc/en-us/requests/new).

## Data Storage

We use [Amazon Web Services](https://aws.amazon.com/) (AWS) Cloud as the hosting provider. All data is stored on the [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/). Each Amazon EBS volume is automatically replicated within its Availability Zone to protect your data from component failure, offering high availability and durability. Amazon EBS volumes ensure consistent and low-latency performance.

Your application data is always processed within the corresponding AWS zone and is never transferred outside this geographic region without your explicit permission.

## Encryption of Data in Transit

All the instances that are hosted on the `*.youtrack.cloud` and `*.myjetbrains.com` domains use HTTPS connections to secure data in transit. For instances that use a custom domain, you have the option to use your own CA certificate. Otherwise, your instance is secured with a TLS certificate that is automatically generated and signed by [Let's Encrypt](https://letsencrypt.org/). Let's Encrypt certificates use the [SHA-2](https://en.wikipedia.org/wiki/SHA-2) cryptographic hash function to encrypt data in transit.

In 2017, JetBrains discontinued support for non-secure connections for YouTrack Cloud.

## Encryption of Data at Rest

The databases that store information for hosted instances are encrypted. This reduces the likelihood that your data is compromised even in situations where an attacker obtains unauthorized access.

YouTrack stores passwords in the database as salted hashes. Each user's password is hashed with a different, randomized salt. The salted passwords are hashed using the SHA-256 cryptographic hash function.

The database itself, including attachments, is encrypted with the [ChaCha20](https://en.wikipedia.org/wiki/Salsa20#ChaCha_variant) algorithm. There are several major implementations of ChaCha20, including Google's selection of ChaCha20 as a replacement for [RC4](https://en.wikipedia.org/wiki/RC4) in [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) and its inclusion in [OpenSSH](https://en.wikipedia.org/wiki/OpenSSH).

A unique encryption key is generated separately for each YouTrack Cloud instance. Access to these keys is restricted to the YouTrack Support and JetBrains Operations teams.

## Certification

We run our service in the AWS Cloud. Since we cannot physically control the servers, we rely on the [third-party certifications](https://aws.amazon.com/security/) that have been undertaken by AWS.

AWS has achieved ISO 27001 certification and has been validated as a Level 1 service provider under the Payment Card Industry (PCI) Data Security Standard (DSS). They undergo annual SOC1 audits and have been successfully evaluated at the Moderate level for Federal government systems as well as DIACAP Level 2 for DoD systems.

In addition:

* Both JetBrains and YouTrack undergo regular audits to ensure that we are acting in compliance with the General Data Protection Regulation (GDPR), which is a set of data protection and privacy regulations within the European Union (EU). This requires that we fulfill certain obligations, such as obtaining valid consent for data processing, implementing appropriate security measures to protect personal data, appointing a Data Protection Officer (DPO) in some cases, and providing individuals with rights to access, rectify, and delete their personal data.

* Starting from version 2023.2, YouTrack is Service Organization Control (SOC) 2 compliant. This means we subjected ourselves to an audit performed by an independent third-party who evaluated our systems and processes according to the SOC 2 framework. The audit covers areas such as data security, availability, processing integrity, confidentiality, and privacy.

* We have regular security audits conducted by both an in-house security team and an external independent audit company.

If you would like to obtain a copy of our most recent reports and certification documents, please contact [YouTrack Support](https://youtrack-support.jetbrains.com/hc/en-us/requests/new).

## Data Manager

The internal application that JetBrains uses to manage the data for YouTrack Cloud, Cloud Keeper, is only accessible to the YouTrack Support and JetBrains Operations teams. It is also possible to access and manage the data directly on the Amazon EC2 servers. Authentication is performed via individual SSL keys and the servers only accept incoming SSH connections from JetBrains and internal IP addresses.

## People and Access

Only the YouTrack Development and JetBrains Operations teams have access to YouTrack Cloud servers and the Cloud Keeper for maintenance and support purposes. These teams access Cloud Keeper and YouTrack Cloud data only for purposes of monitoring application health and performing system maintenance, or upon customer request.

YouTrack Cloud is designed to allow access to application data only with the appropriate credentials, so that no customer may access another customer's data without explicit knowledge of their account credentials. Customers are responsible for maintaining the security of their own login information.

The JetBrains Operations team monitors YouTrack Cloud servers 24x7. Our servers are hosted in different data centers in Europe, North America, and the Asia-Pacific region, according to the customer location and preference. For an overview of our availability, check the [YouTrack Cloud Service Status](https://www.jetbrains.com/youtrack/cloud/status/) page.

## Email Messages

Helpdesk projects and mailbox integrations can be configured to access and process email messages sent to a built-in email service that is hosted by JetBrains. We use the Amazon Simple Email Service to manage all email traffic in strict accordance with the guidelines recommended by [AWS](https://docs.aws.amazon.com/ses/latest/dg/data-protection.html). Email messages are stored in an encrypted state and deleted when no longer needed. We also encrypt data in transit to ensure that customer data is protected at all times.

A very limited number of JetBrains employees have access to email storage in the cloud and only do so when required to resolve customer support cases. JetBrains neither processes nor uses customer email data for any other purpose.

## Backups

The JetBrains Operations team is responsible for creating and storing backups. Backups are also stored on Amazon servers and are [encrypted in the same way as the database](#database-encryption). We re-sync backups daily, weekly, and monthly. You can create and export your own backups at any time from the Database Export page in YouTrack. For more information, see [Database Export](database.html).



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/security.html](https://www.jetbrains.com/help/youtrack/cloud/security.html) · fetched 2026-09-22 08:34 Asia/Taipei*
