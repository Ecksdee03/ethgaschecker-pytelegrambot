## @EthGasCheckerBot

A simple telegram bot used to check live Ethereum prices and gas fees for different speeds on the Ethereum blockchain, using live data from [Etherscan.io](https://etherscan.io/).

## Getting Started

This bot is built with [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) - A simple, but extensible Python implementation for the [Telegram Bot API](https://core.telegram.org/bots/api). It is hosted on a replit web server using Flask. This API is tested with Python 3.6-3.10 and Pypy 3. 

Download using:

`pip install pyTelegramBotAPI`

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

Run code by using `python bot.py` and configuring it to the native run command on replit and test your bot. 

Add your API keys `BOT_TOKEN` and `ETH_TOKEN` to the environment variables page on replit

You can publish the repl, run it and close the tab and your bot will keep running in the background 24/7 for free!!

To check if the bot is running in background, you can make an account on [Uptime Robot](https://uptimerobot.com/) and put a monitor on your repl url. It should stay up.

Once that is done, you should be able to access the Telegram bot at @EthGasCheckerBot on Telegram and access its commands.

![Screenshot (444)](https://user-images.githubusercontent.com/77221369/158120895-b6694392-9e9a-4605-a57d-770719c0812b.png)
![Screenshot (445)](https://user-images.githubusercontent.com/77221369/158120904-d9905412-8e93-4582-abda-ef97c8b1341d.png)
