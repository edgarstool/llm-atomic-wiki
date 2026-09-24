---
title: "Manage Permanent Tokens"
source_url: "https://www.jetbrains.com/help/youtrack/cloud/manage-permanent-token.html"
fetched_at: "2026-09-22 08:34 Asia/Taipei"
product: YouTrack
---

# Manage Permanent Tokens

In YouTrack Cloud, permanent tokens let developers access and perform operations securely using the REST API calls in their scripts and applications without having to implement OAuth 2.0 authentication flows. A permanent token allows access to a service with the permissions that are granted to the user account.

This page covers operations with permanent tokens that are performed in the user profile. For a sample of REST API calls using the permanent token, refer to the [Permanent Token Authorization](https://www.jetbrains.com/help/youtrack/devportal/authentication-with-permanent-token.html).

## Create a Permanent Token

To access a service programmatically with the permissions that are granted to your user account, create your own permanent token. The effective permissions for API requests made with this token cannot exceed the permissions that are granted to your account.

In addition to the permissions that are listed here, you need permission to read the service that you want to access with the token. Access to connected services is managed in Hub. If you work with YouTrack Cloud or a YouTrack Server installation that uses the built-in Hub service, all users have access to YouTrack services.

Procedure: To generate a new permanent token:

> **Tip:**
> Requires permissions: Update Self

1. From the main navigation menu, select your avatar, then select Profile.

2. Select the Account Security tab.

3. In the Tokens section of the page, click the New token button.

4. In the New Permanent Token dialog, specify a name for the new token and the access scope for it. The scope for the token is a list of services that you can access with this new token.

!['New Permanent Token' dialog with a name and scope selected.](https://resources.jetbrains.com/help/img/youtrack/2026.2/new-permanent-token-dialog.png)

Use the information in the following table to determine which scopes you want to assign the token.

| Scope | Description |
| --- | --- |
| YouTrack | Grants permission to work with issues, tags, commands, agile boards, dashboards, reports, and other basic operations in YouTrack.     This scope also gives you the ability to send REST API calls to the following endpoints:        * `/youtrack/rest/...`    * `/youtrack/api/...`    |
| YouTrack Administration | Grants permission to manage user access and update server settings.     This scope also gives you the ability to send REST API calls to the following endpoints:       * `/hub/api/...`    * `/hub/rest/...`   |
| Konnector | Grants permission to send information to messaging apps that are integrated with YouTrack's Konnector service. This includes the [YouTrack App for Slack](slack-app-integration.html) and the [YouTrack bot for Telegram](telegram-integration.html). |
| YouTrack Mobile | Grants permission to send push notifications to the YouTrack Mobile app. |

5. Click the Create token button.

* A dialog window with the new token is displayed.

![Generated permanent token with the 'Copy token' button.](https://resources.jetbrains.com/help/img/youtrack/2026.2/permanent-token-created.png)

6. Use either of these two actions to copy the token:

* Click the Copy token button.

* Select the token with your pointer and use the standard keyboard shortcut for your operating system to copy the current selection to the clipboard.

> **Warning:**
> You must copy the token at this point. As soon as you close the dialog, you can't access the token again. If you close the dialog accidentally, the only way to obtain a token is to repeat the procedure and create a new one.

7. After you copy the token, close the dialog.

* The new token is associated with your user account and is displayed in the Tokens list.

![Permanent Tokens list containing the newly created token.](https://resources.jetbrains.com/help/img/youtrack/2026.2/permanent-token-list.png)

## Delete a Permanent Token

A permanent token does not have an expiration date. If you suspect that an authenticated service has been compromised, you can explicitly delete this token in your profile.

Procedure: To delete a permanent token:

> **Tip:**
> Requires permissions: Update Self

1. From the main navigation menu, select your avatar, then select Profile.

2. Select the Account Security tab.

3. In the list of tokens, select the token that you want to revoke.

4. Click the Delete button.

* A confirmation dialog is displayed.

5. Click the Delete button to confirm the action.

![Confirmation dialog for deleting one permanent token.](https://resources.jetbrains.com/help/img/youtrack/2026.2/delete-token-confirm.png)

* The selected permanent token is deleted and removed from the list.



---

*Source: [https://www.jetbrains.com/help/youtrack/cloud/manage-permanent-token.html](https://www.jetbrains.com/help/youtrack/cloud/manage-permanent-token.html) · fetched 2026-09-22 08:34 Asia/Taipei*
