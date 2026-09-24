---
title: "About YouTrack Cloud"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/about-youtrack-cloud.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# About YouTrack Cloud

YouTrack Cloud is a cloud-based web application hosted by JetBrains. YouTrack Cloud lets you take full advantage of the issue tracking and project management tool without the need to install or maintain the server. The YouTrack team performs all maintenance and upgrades for you.

Here's what you get with YouTrack Cloud:

* A full-featured YouTrack instance according to [your subscription plan](https://www.jetbrains.com/youtrack/buy/?section=cloud).

* [Regular automatic updates](youtrack-cloud-maintenance-calendar.html).

* [Daily backups](youtrack-cloud-database-backups.html).

* Import from other issue tracking and project management tools using [predefined import scripts](imports.html).

* No-effort [migration to YouTrack Server](migrate-from-cloud-to-server.html) using a backup copy of the data from your hosted instance, and [vice versa](migrate-from-server-to-cloud.html).

* A robust [REST API](https://www.jetbrains.com/help/youtrack/devportal/youtrack-rest-api-reference.html) for building integrations with third-party tools.

## Cloud Domains

The default domain for the new YouTrack Cloud instances registered on November 2, 2021, or later is `youtrack.cloud`. Newly registered instances are available at `instancename.youtrack.cloud`.

YouTrack Cloud instances registered before November 2, 2021, remain accessible at the `myjetbrains.com` domain. Once an instance is upgraded to version 2021.4, it may migrate to `youtrack.cloud`. The migration requires the administrator to reconfigure the domain settings and the settings of some third-party auth modules.

Your instance name is automatically reserved on both domains, `myjetbrains.com` and `youtrack.cloud`, so you can migrate to the new domain at any time.

### Migrate to the New Domain

All YouTrack Cloud instances registered before November 2, 2021, are hosted on `instancename.myjetbrains.com` by default. When your instance is upgraded from an older version to version 2021.4, the instance administrator gets the opportunity to migrate to `instancename.youtrack.cloud`.

#### Update Auth Modules

Before updating the domain settings, you need to update the settings of the auth modules based on OAuth 2.0 or OpenID. If you don't have any OAuth 2.0 or OpenID auth modules, skip this part and proceed to update the [domain settings](#update-domain-settings).

Auth modules that require no reconfiguration: Hub, Active Directory, Atlassian Jira, LDAP, Open LDAP, SAML 2.0.

Auth modules that require reconfiguration: Amazon, AOL, Azure AD 2.0, Bitbucket Cloud, Facebook, GitHub, GitLab, Google, JetBrains Account, Microsoft Live, OAuth 2.0, OpenID 2.0, PayPal, Yahoo!, Yandex Passport.

Procedure: To update auth modules:

1. On the side of the IdP, proceed to update the Authorized redirect URI field or its analogue.

2. For each redirect URI on the list starting with `https://instancename.myjetbrains.com/youtrack`, add one more URI starting with `https://instancename.youtrack.cloud`.

Don't remove any URIs from the list, as they may come in handy if you decide to roll the base URL back.

3. Apply your changes.

4. In your browser, navigate to `https://instancename.youtrack.cloud` and try to log in with the updated auth module.

5. Repeat the procedure for all auth modules that require reconfiguration.

#### Update Domain Settings

When the auth modules are reconfigured, change the base URL of your YouTrack to migrate it to the new domain.

Procedure: To update the domain settings:

1. From the ![](https://resources.jetbrains.com/help/img/youtrack/2026.2/settings.svg) Administration menu in YouTrack, select `Server Settings > Global Settings`.

2. On the Server Configuration tab, scroll down to the Domain Settings section.

3. In the Base URL field, enter `https://instancename.youtrack.cloud`, where `instancename` corresponds to the name of your YouTrack Cloud instance.

4. Click Save to save the new value and apply changes.

* Your YouTrack is migrated to the new base URL.

* For the full list of changes after the migration, see [Changes for the Instances Migrated to the New Domain](#changes-to-migrated-instances).

#### Changes for the Instances Migrated to the New Domain

Here is the list of changes that happen to a YouTrack Cloud instance after migrating to the new `youtrack.cloud`:

| Change Area | Details |
| --- | --- |
| Default Domain |      * The instance becomes available at `instancename.youtrack.cloud`.    * The old address at `instancename.myjetbrains.com` remains fully functional for backward compatibility.    |
| Default email address |    If you're using the default mail server for notifications, its address changes to `service@youtrack.cloud`.    |
| Links to Issues from Notifications and Widgets | All links to YouTrack issues from notifications and dashboard widgets will lead to the new domain at `youtrack.cloud`. |
| Third-Party Auth Modules | If you haven't yet reconfigured auth modules that redirect to `myjetbrains.com`, they may require reconfiguration. For instructions, refer to [Update Auth Modules](#update-auth-modules). |



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/about-youtrack-cloud.html](https://www.jetbrains.com/help/youtrack/cloud/about-youtrack-cloud.html) · fetched 2026-09-22 08:34 Asia/Taipei*
