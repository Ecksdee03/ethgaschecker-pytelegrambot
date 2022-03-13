## ethgascheckerbot

A simple telegram bot used to check live Ethereum prices and gas fees for different speeds on the Ethereum blockchain, using live data from [Etherscan.io](https://etherscan.io/). New features are planned to be added in the future, such as setting notifications for custom gas or ETH prices.

## Getting Started

This bot is built with pyTelegramBotAPI - A simple, but extensible Python implementation for the [Telegram Bot API](https://core.telegram.org/bots/api). This API is tested with Python 3.6-3.10 and Pypy 3. 

Download using:

`python -m pip install pyTelegramBotAPI`

Download these Python libraries too: flask, requests, telebot

## Prerequisites
It is presumed that you have already signed up for a Telegram account and obtained an [API token with @botfather](https://core.telegram.org/bots#botfather). We call this token `BOT_TOKEN`.

Save the API Token in an env file if sharing to the public. Install its library named python-dotenv using: `pip install python-dotenv` 

Then create an .env file in the same directory with `BOT_TOKEN` defined in it.

To prevent tracking in the Github repository, use the command `echo '.env' > .gitignore`

Also get an [API token from Etherscan](https://etherscan.io/apis) and we save this in the variable `ETH_TOKEN`

Furthermore, you should have basic knowledge of the Python programming language and more importantly the [Telegram Bot API](https://core.telegram.org/bots/api).

## Set up and deploy bot on replit
[Create new project](https://replit.com/~) using python or just clone this Git repository.

Run code and test your bot. Bot should welcome you to the room.

You can publish the repl, run it and close the tab and your bot will keep running in the background 24/7 for free!!