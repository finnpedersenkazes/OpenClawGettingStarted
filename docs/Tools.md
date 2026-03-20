# Tools

## Email

### Agent Mail

Go the [AgentMail.to](https://www.agentmail.to/) website and signup for a free account. You get three emails.

Setup an **inbox** and create an **API key**.

> Configure the Allow/Block lists

Tell OpenClaw that you have setup agentmail and give it its email address.

> I have created an Agent mail for you. This is your new email address: `<email address>@agentmail.to`
> Get the AgementMail skill from Clawhub.

It will ask you for the **API key**.

### Google Mail

I started with Gmail, but ran into issues with the token experiring and switched to Agent Mail.

However, you can consider investigating the `gog` skill.

## GitHub

On the GitHub account you want to use, go to Settings, Developer Settings, Personal access tokens.

Then press `Generate new token` and choose **Generate new token (Classic)**.

Give it just the access needed.

Do not close the page before you have a copy of the token.

Then give OpenClaw the url to the GitHub profile and it will ask for the token.

### Backup the Workspace

Instruct OpenClaw to make a backup of its Workspace to GitHub.

> This is important!

- It allows you to investigate the setup
- You can make changes to it
- Check the changes
