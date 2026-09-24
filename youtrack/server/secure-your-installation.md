---
title: "Safeguard Your Installation"
source_url: "https://www.jetbrains.com/help/youtrack/server/secure-your-installation.html"
fetched_at: "2026-09-22 08:35 Asia/Taipei"
product: YouTrack Server
---

# Safeguard Your Installation

YouTrack is developed with security in mind. We take great care to minimize exposures to different types of attacks. We work with third-parties who scan YouTrack for vulnerabilities and perform penetration tests. When a security issue is discovered, we strive to address the problem in the next major version or bug-fix release.

The recommendations on this page are intended to help you keep your YouTrack data secure. These best practices can help you avoid pitfalls that leave your data vulnerable to theft, damage, or loss.

## Document Your Setup

Documentation is an important part of your security plan. If your YouTrack administration changes hands, the new administrator shouldn't have to learn how the application is configured through trial and error. As you follow this guide to secure your YouTrack environment, make a note of each change and explain why you set it up the way you did. When done, collect your notes and add them to your information security policy documentation.

## Stay Up To Date

To ensure that your installation includes the most recent security enhancements, make sure you always use the latest version of YouTrack. To make sure you haven't missed an important update:

* Subscribe to updates on the [YouTrack blog](https://blog.jetbrains.com/youtrack/) or follow YouTrack on [Twitter](https://twitter.com/youtrack).

* Check for updates in the Update Info section of the [Global Settings](managing-global-settings.html) page.

To prevent accidental disclosure, we usually restrict the visibility to issues that are classified as a Security Problem to members of the JetBrains team. You may see issues in the Security Problem section of our release notes, but this is by no means a comprehensive list of security-related issues that have been fixed in any given release.

For this reason, we strongly recommend that you update your installation to the latest version as soon as possible.

## Create a Safe Environment

As a web-based application, registered users can connect to YouTrack from outside your network. Any server that is exposed to the Internet is vulnerable to hackers who can destroy data, encrypt data and hold it for ransom, or steal your secrets. We recommend that you install YouTrack in a trusted environment that is protected by a firewall. Your firewall rules should not allow traffic without any business justification.

Follow these guidelines to ensure the security of your installation:

* Restrict access to database files to prevent users or other processes from modifying or deleting your YouTrack data.

* Install security updates for the operating system as well as third-party software that is connected to your installation.

* Use firewall rules to allow traffic only through ports that are required for inbound network connections.

## Secure Your Connection

To secure communication over your network, you need to set up SSL encryption. All of your traffic is then encrypted using HTTPS (HTTP over SSL/TLS). YouTrack supports the following setups:

* Use built-in TLS for your YouTrack Server installation. For more information, see [Secure the Connections to Your YouTrack Server](secure-connection-for-youtrack-server.html).

* Use a third-party TLS-terminating reverse proxy server. For details, see [Reverse Proxy Configuration](reverse-proxy-configuration.html).

When users log in to YouTrack with an authentication module that does not support SSL/TLS encryption (for example, the Hub authentication module), the password is transmitted in plain text. If you don't use HTTPS, a packet sniffer can intercept and log this traffic and compromise your passwords. To protect your accounts, use a reverse proxy to secure all of your connections using HTTPS (HTTP over SSL/TLS).

> **Tip:**
> Secure connections to YouTrack Server installations must be configured to use TLS version 1.2 or later. Connections using older versions of the protocol are no longer supported.

## Use a Dedicated Service User Account

You should always use a dedicated user account to run YouTrack on your server. By default, the Docker container runs the application as the user defined in the Dockerfile of the image (using the `USER` directive). If no specific `USER` is defined, it typically runs as the `root` user inside the container.

To increase security, switch to a user account that was created specifically to run YouTrack. Limit the access rights that are available to this account at the operating system level to protect critical parts of the system. This should be a non-privileged user that only has access to the YouTrack installation and home directories.

## Encrypt your Data

YouTrack stores passwords in the database as salted hashes. Each user's password is hashed with a different, randomized salt. The salted passwords are hashed using the SHA-256 cryptographic hash function.

The database for your YouTrack Server installation, however, is not encrypted. To ensure that your data is secure, we recommend that you apply filesystem-level or full disc encryption to the server that runs YouTrack.

## Restrict Cross-origin Requests

If you have integrations or web services that request data from outside your YouTrack domain, you can restrict access to specific origins. YouTrack supports cross-origin resource sharing, or CORS.

To protect your data from malicious attacks, create a fixed list of trusted origins that are allowed access. You can manage this list in the Resource Sharing section of the Global Settings page. For more information, see [Resource Sharing](server-configuration-settings.html#resource-sharing-settings).

## Use Digital Certificates

You should not only secure access to YouTrack over HTTPS, but secure the data that is exchanged between YouTrack and the web services that are connected to it. Obtain an SSL certificate for each external service and import the certificates into YouTrack.

* You should import trusted SSL certificates for any external application that is integrated with YouTrack. For more information, see [SSL Certificates](ssl-certificates.html).

* You should also have an SSL keystore that identifies YouTrack as a client when it tries to connect to a third party. For more information, see [SSL Keys](ssl-key-stores.html).

The following integrations can be configured to establish a secure connection using SSL:

* [Imports](imports.html)

* [Mailbox Integration](mailbox-integration.html)

* [TeamCity Integration](integration-with-teamcity.html)

* [VCS Integration](integration-with-version-control-systems.html)

* [Zendesk Integration](integration-with-zendesk.html)

* [LDAP Auth Module](ldap-authentication-module.html)

* [Atlassian Jira Auth Module](atlassian-jira-auth-module.html)

You should also use a digital certificate to secure the connection to the SMTP server that sends email notifications from YouTrack.

## Require Two-factor Authentication

YouTrack supports two-factor authentication (2FA). Many of the third-party authentication modules that are supported in YouTrack also support 2FA. YouTrack lets you require 2FA for every member of your organization. Users can choose to protect their accounts with app-based or token-based 2FA.

* With app-based 2FA, users must use an external app to generate an authentication code, which they must then enter when they log in with their password. This adds an extra layer of security. Even if a password is compromised, the malicious user cannot access the application without the authentication code from the external app.

* With token-based 2FA, users pair their Hub account with a hardware device. Users must have this hardware device in their possession when they log in.

When you require 2FA for one or more groups, the information that is accessible to members of these groups is subject to an additional layer of protection. To learn how to enable this feature, see [Require Two-factor Authentication](require-two-factor-authentication.html).

## Enforce a Password Policy

If you're using third-party services for authentication and don't require 2FA, you can't guarantee that every user sets it up. Or uses a strong password.

Here's what you do know:

* Many users don't create unique passwords for each of their accounts.

* Most passwords are extremely weak and easy to crack.

* An attacker only has to guess one weak password to gain access to your system.

The Hub authentication module lets you ensure that users create passwords that keep your data safe. If you use this module to manage logins, we recommend that you set the Password Strength to Good or Very Strong. For more information, see [Set a Password Policy](set-a-password-policy.html).

## Require Email Verification

Asking users to verify their email addresses ensures that your users confirm ownership of their accounts. This is especially important when you let users register their own accounts.

For installations that create user accounts from incoming email messages with the [Mailbox Integration](mailbox-integration.html) or tickets that are imported with the [Zendesk Integration](integration-with-zendesk.html), the option to require email verification prevents users from registering accounts that can be used to gain unauthorized access to YouTrack and other applications in your business environment.

The option to require email verification is located on the `Auth Modules > Common Settings` page in YouTrack. For more information, see [Common Settings for Auth Modules](auth-module-common-settings.html).

## Banish Bots

The Hub authentication module lets users register their own accounts in YouTrack. If you allow self-registration and your installation is accessible from outside your network, you should protect your installation from registration bots. These bots can consume resources and claim licenses that are intended for use by humans.

To block registration bots, enable reCAPTCHA in the Hub authentication module. For more information, see [Hub Auth Module](hub-auth-module.html).

## Throttle Failed Login Attempts

Throttling or rate limitation helps protect the application from brute-force attacks. The Hub authentication module has settings that let you apply rate limits to logins and requests to verify credentials. Rate limits are applied per IP address. Rate limits help slow down brute-force attacks by blocking new login requests for a short time following a series of consecutive login failures, so they keep your passwords safe.

These rate limits are applied all logins from any active authentication module. For more information, see [Throttling by Login Settings](auth-module-common-settings.html#throttling-settings).

## Grant Permissions with Care

Many operations in YouTrack are managed by a permission scheme. Permissions are assigned to a collection of roles, which are then granted to users and groups for a specific project. Users only have permission to perform the operations that are allowed for the role that they are assigned in each project.

If you are overly-generous with granting permissions, you expose your system to high risk from insider threats. It also gives external hackers access to sensitive data as soon as any of your accounts is compromised.

We recommend that you follow the principle of least privilege and only grant access to the information and resources that are absolutely necessary to perform the operations that are required for each user. Start small, then go bigger — but only with good reason. Follow these guidelines to prevent unnecessary access to sensitive data:

* Grant as little access as necessary to new accounts, then add permissions if necessary.

* Revoke access when it is no longer required.

* Delete or ban unnecessary user accounts.

* Avoid the auto-join groups option if user registration is enabled in the Hub authentication module.

* Limit the permissions that are available to the Guest user account.

* Grant roles with very limited permissions to the All Users and Registered Users groups.

* Limit the number of users who are assigned roles in the Global project.

* Use as few accounts with System Admin roles as possible and monitor their activity.

### Restrict Access to User Profiles

In YouTrack installations created with version 2026.1 or later, the Registered Users group is assigned the default Observer role in the Global project. This role includes the Read User Details permission, which lets every registered user view additional profile details for other registered users. These details include email addresses and authorization data, such as role assignments and group memberships. The permission does not grant access to account security details, such as credentials and authentication tokens.

Consider whether this level of access is appropriate for your installation, especially when you allow open user registration or provide access to external users through helpdesk projects.

To restrict access to user profile details:

1. [Create a custom role](create-and-edit-roles.html#create-role) that contains the Read User Basic and Update Self permissions.

2. [Revoke](configure-access-for-a-user-group.html#revoke-role-group) the Observer role from the Registered Users group in the Global project.

3. [Assign](configure-access-for-a-user-group.html#grant-role-to-group) the custom role to the Registered Users group in the Global project.

This configuration lets registered users view the basic information required to interact with other users and update their own profiles without exposing full user profile details.

## Back up Your Data

To protect your installation against ransomware and recover from hardware or software failure, make sure your YouTrack database is included in your backup plan.

* Enable regular backup of your YouTrack database and set up notifications should the backup fail. For more information, see [Database Backup](back-up-the-database.html).

* Test backups by restoring your system to make sure the process works. For more information, see [Restore a YouTrack Installation](restore-docker-image-installation.html).

* Keep copies of recent backups off premises.

* Make sure your backups are secure and encrypted.

## Secure the Default Administrator Account

You set the username and password for the default administrator account when you install YouTrack Server on your server. This account has permission to perform any operation in YouTrack.

One of the most common problems detected by risk and security audits is an administrator account that is not tied to a specific individual. You might be tempted to create a simple username and password combination and share the default administrator account with more than one administrator. Don't.

* Shared accounts are often used to gain uncontrolled access to systems.

* Audit events and logs are rendered useless when you cannot associate a change with a specific individual.

* Administrator accounts have unlimited access and should use the strongest possible passwords.

Follow these guidelines to secure your default administrator account:

* After initial setup, create personal user accounts for each administrator and grant them the required level of access. Administrators should use their own accounts to perform administrative tasks.

* Limit the number of accounts with administrative access rights to the users who require this level of access.

* Require that users with administrator privileges use strong passwords and change them periodically.

* Revoke administrative access as soon as it is no longer required.

* Manage ownership of the default administrator account carefully. If the user who is responsible for this account leaves your organization or is no longer responsible for the application, select another user to assume ownership and transfer this responsibility. If the previous administrator no longer requires access to YouTrack: * Use the Merge User operation to combine these two user accounts. For more information, see [Merge User Accounts](merge-user-accounts.html). * Remove the credentials for the previous administrator from the merged user account. If the previous administrator still requires access to YouTrack in a non-administrative role: * Create a new user account for the previous administrator and grant the appropriate level of access to the account. * Use the Merge User operation as described above to transfer ownership of the default administrator account to the new administrator.

## Browse Audit Events and Check Security Logs

YouTrack provides tools that let you monitor your application for suspicious activity.

* The Audit Events page provides a list of events, targets, and authors for every event that is logged in YouTrack. These events are recorded every time an operation is applied to a target entity that is managed by the built-in Hub service. This includes changes that are applied to users, groups, projects, roles, auth modules, services, and resources, among others. You can filter the list to search for specific types of activity or download the events as a JSON file for further investigation.

* Events that are considered to be security-related are printed to a dedicated `security.log` file. This file contains a wider range of events and target entities.

* Login events are printed to a dedicated `hub-login.log` file.

You can browse the audit events and security logs to detect unusual activity or for troubleshooting. However, if your organization uses security information and event management software, a much better solution is to include your YouTrack log files as a data source. These solutions let you scan and analyze aggregated log files and generate alerts when a suspicious pattern of activity is detected.

Follow these guidelines to secure your log files:

* Ensure that only individuals who have a job-related need have access to the data directory where you store your YouTrack log files.

* Create backup copies of your YouTrack log files on a centralized log server.

## Limit Access to Sensitive Information

If you store sensitive information in your issues, take extra efforts to make sure this data is secure.

* Use dedicated projects to store issues that contain information that can be used to identify a person.

* Make sure the users who have access to issues in this project understand the sensitivity of this information.

* Restrict project access to the users who need to view and use this information.

* Restrict the visibility of issues and comments to the group of users who have access to the project.

For issues that contain sensitive or confidential information, don't leave anything to chance. If you rely on users to set the visibility manually, someone is bound to forget.

Use workflows to set the visibility for issues and comments according to your security scheme. You can create and attach workflows that support the following common use cases:

* Set issue visibility automatically when it is created in a project that is used to manage sensitive information.

* Change visibility when an issue is assigned a specific type or subsystem.

* Warn users who set the visibility for a comment that is different from the issue visibility.

* Block users from changing the visibility setting for an issue or comment.

For more information, see [Workflows](workflow-guide.html).

## Restrict Anonymous Access

By default, all YouTrack installations include a dedicated user account for guests. This user is granted the default Observer role in the Global project. If your installation is accessible from outside your network, anyone who knows your server address can use the guest account to browse issues in your projects without having to log in.

If you wish to limit or block anonymous access, you have the following options:

* You can revoke the role that is assigned to the guest account in the Global project. You can then choose whether you want to grant the guest account an Observer role in the projects that you want to make available to the public. We generally discourage granting roles with update permissions to the guest account, as these actions cannot be associated with an individual.

* You can ban the guest account. All users are required to log in to view issues with a registered account. Access to issues in each project is determined by the roles that are assigned on a per-user or per-group basis.

For more information, see [Manage the Guest User Account](managing-guest-users.html).



---

*Source: [https://www.jetbrains.com/help/youtrack/server/secure-your-installation.html](https://www.jetbrains.com/help/youtrack/server/secure-your-installation.html) · fetched 2026-09-22 08:35 Asia/Taipei*
