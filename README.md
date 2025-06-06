<p align="center">
    <a href="https://github.com/UsergeTeam/Userge">
        <img src="https://telegra.ph/file/f3aed2f6f2d4a1ad7831d.png" alt="Userge">
    </a>
    <br>
    <b>Pluggable Telegram UserBot</b>
    <br>
    <a href="https://github.com/UsergeTeam/Userge#inspiration-">Inspiration</a>
    &nbsp•&nbsp
    <a href="https://github.com/UsergeTeam/Userge#documentation-">Documentation</a>
    &nbsp•&nbsp
    <a href="https://github.com/UsergeTeam/Userge#deployment-">Deployment</a>
    &nbsp•&nbsp
    <a href="#deploy-to-render-">Deploy to Render</a>
    &nbsp•&nbsp
    <a href="https://github.com/UsergeTeam/Userge#project-credits-">Project Credits</a>
    &nbsp•&nbsp
    <a href="https://github.com/UsergeTeam/Userge#copyright--license-">Copyright & License</a>
</p>

# Userge 🔥

[![Build Status](https://travis-ci.com/UsergeTeam/Userge.svg?branch=alpha)](https://travis-ci.com/UsergeTeam/Userge)
![Python Version](https://img.shields.io/badge/python-3.8/3.9-lightgrey)
![Release](https://img.shields.io/github/v/release/UsergeTeam/Userge)
![Stars](https://img.shields.io/github/stars/UsergeTeam/Userge)
![Forks](https://img.shields.io/github/forks/UsergeTeam/Userge)
![Issues Open](https://img.shields.io/github/issues/UsergeTeam/Userge)
![Issues Closed](https://img.shields.io/github/issues-closed/UsergeTeam/Userge)
![PRs Open](https://img.shields.io/github/issues-pr/UsergeTeam/Userge)
![PRs Closed](https://img.shields.io/github/issues-pr-closed/UsergeTeam/Userge)
![Contributors](https://img.shields.io/github/contributors/UsergeTeam/Userge)
![Repo Size](https://img.shields.io/github/repo-size/UsergeTeam/Userge)
![License](https://img.shields.io/github/license/UsergeTeam/Userge)
![Commit Activity](https://img.shields.io/github/commit-activity/m/UsergeTeam/Userge)
[![Plugins Repo!](https://img.shields.io/badge/Plugins%20Repo-!-orange)](https://github.com/UsergeTeam/Userge-Plugins)
[![Join Channel!](https://img.shields.io/badge/Join%20Channel-!-red)](https://t.me/theUserge)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/UsergeTeam/Userge/?ref=repository-badge)
[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/UsergeTeam/Userge)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

> **Userge** is a Powerful , _Pluggable_ Telegram UserBot written in _Python_ using [Pyrogram](https://github.com/pyrogram/pyrogram).

## Inspiration 😇

> This project is inspired by the following projects :)

* [tg_userbot](https://github.com/watzon/tg_userbot) ( heavily ) 🤗
* [PyroGramBot](https://github.com/SpEcHiDe/PyroGramBot)
* [Telegram-Paperplane](https://github.com/RaphielGang/Telegram-Paperplane)
* [UniBorg](https://github.com/SpEcHiDe/UniBorg)

> Special Thanks to all of you !!!.

## [Documentation](https://theuserge.github.io) 📘

## [Deployment](https://theuserge.github.io/deployment) 👷

## Deploy to Render 🚀

Userge can now be deployed directly to [Render.com](https://render.com), a modern cloud platform that makes it easy to deploy and scale your applications.

### One-Click Deployment

The easiest way to deploy Userge to Render is by clicking the "Deploy to Render" button above. This will:

1. Create a new Render account if you don't have one
2. Fork this repository to your GitHub account
3. Create a new Render Blueprint from your fork
4. Deploy both the Userge application and a MongoDB database

### Manual Deployment

If you prefer to deploy manually, follow these steps:

1. Fork this repository to your GitHub account
2. Create a new Render account or log in to your existing one
3. From the Render dashboard, click "New" and select "Blueprint"
4. Connect your GitHub account and select your forked repository
5. Render will automatically detect the `render.yaml` file and set up the services

### Required Environment Variables

You'll need to set the following environment variables in your Render dashboard:

| Variable | Description |
|----------|-------------|
| `API_ID` | Your Telegram API ID from [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | Your Telegram API Hash from [my.telegram.org](https://my.telegram.org) |
| `LOG_CHANNEL_ID` | Telegram Channel ID for logging |

Plus one of the following mode configurations:

**For USER Mode:**
- `SESSION_STRING` - Get this using [@genStr_Bot](https://t.me/genStr_Bot) or by running the `genStr` script

**For BOT Mode:**
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)
- `OWNER_ID` - Your Telegram User ID

### Optional Environment Variables

You can also set these optional variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `CMD_TRIGGER` | Command trigger character | `.` |
| `SUDO_TRIGGER` | Sudo command trigger | `!` |
| `WORKERS` | Number of workers | `4` |
| `DOWN_PATH` | Download path | `downloads/` |
| `FINISHED_PROGRESS_STR` | Finished progress character | `█` |
| `UNFINISHED_PROGRESS_STR` | Unfinished progress character | `░` |

### Troubleshooting

If you encounter any issues during deployment:

1. Check the Render logs for error messages
2. Ensure all required environment variables are set correctly
3. Verify your MongoDB connection string is valid
4. Make sure your Telegram API credentials are correct
5. For further assistance, join the [Discussion Group](https://t.me/usergeot)

## [Plugins](https://github.com/UsergeTeam/Userge-Plugins) 🔌

### Support & Discussions 👥

> Head over to the [Discussion Group](https://t.me/usergeot) and [Update Channel](https://t.me/theUserge)

### Project Credits 💆‍♂️

* [Specially to these projects](https://github.com/UsergeTeam/Userge#inspiration-) 🥰
* [Contributors](https://github.com/UsergeTeam/Userge/graphs/contributors) 👥

### Copyright & License 👮

* Copyright (C) 2020 - 2022 by [UsergeTeam](https://github.com/UsergeTeam) ❤️️
* Licensed under the terms of the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/UsergeTeam/Userge/blob/master/LICENSE)

