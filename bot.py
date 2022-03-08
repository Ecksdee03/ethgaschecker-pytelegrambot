import telebot, os, requests
from dotenv import load_dotenv
from telebot import types
from telebot.types import ReplyKeyboardMarkup as rkm
# from time import sleep
from flask import Flask, request
import logging

#initialise bot objects
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(token=TOKEN, parse_mode = "HTML")
ethscan_token = os.getenv('ETHERSCAN_TOKEN')

print("Bot started successfully! Running now..")
print(TOKEN)

#Fetching data with Python request library
gasurl = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={}".format(ethscan_token)
ethurl = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd%2Cbtc&include_market_cap=true&include_24hr_change=true"
ethdata = requests.get(ethurl).json()
gasdata = requests.get(gasurl).json()

welcome_msg = ''' Howdy, I am the ETH Gas Checker Bot, how are you doing?

Type /gas to check the live Ethereum gas fees in GWEI
Type /price to check the live Ethereum price
Type /donate to support future development of this Bot
Made by @Jhw0ng
'''

donate = '''Any amount of donation to my developer will be much appreciated!＼(＾▽＾)／
They will be used to support more features for me!
<b>ETH Address:</b>
<b>BTC Address:</b>
<b>LUNA Address:</b>
<b>FTM Address:</b>
<b>DOGE Address:</b>
<b>MATIC Address:</b>
'''


def ethprice():
	price = round(ethdata['ethereum']['usd'], 2)
	mcap = round(ethdata['ethereum']['usd_market_cap'], 2)
	pchange = round(ethdata['ethereum']['usd_24h_change'], 2)
	btcprice = round(ethdata['ethereum']['btc'], 5)
	mcap = format(int(mcap), ",")

	ethinfo = f"""<strong><ins>Ethereum | $ETH</ins></strong>
	<b>USD:</b> ${price}
	<b>24h change:</b> {pchange}%
	<b>Market Cap:</b> ${mcap}
	<b>BTC:</b> ฿{btcprice}
	"""

	return ethinfo

def gasfees():
	low = int(gasdata["result"]["SafeGasPrice"])
	avg = int(gasdata["result"]["ProposeGasPrice"])
	high = int(gasdata["result"]["FastGasPrice"])

	lowp = round(gweitousd(low),2)
	avgp = round(gweitousd(avg),2)
	highp = round(gweitousd(high),2)

	gasinfo = f"""<strong><ins>Ethereum Live Gas Fees:</ins></strong>
	<b>Low</b>: {low} GWEI | ${lowp} (1min)
	<b>Average</b>: {avg} GWEI | ${avgp} (3min)
	<b>High/Fast</b>: {high} GWEI | ${highp} (10min)
    
	Powered by <a href=\"etherscan.io/gastracker\">EtherScan</a>."""

	return gasinfo

def gweitousd(gwei):
	ethprice = round(ethdata['ethereum']['usd'], 2)
	usdp = gwei * ethprice * 1.00E-9 * 21000
	return usdp

#configure msg commands
#note: handlers are tested in the order declared
@bot.message_handler(commands=['start', 'cmds'])
def send_welcome(msg):
	bot.send_message(msg.chat.id, welcome_msg)
	chatid = str(msg.chat.id)
	markup = rkm(row_width = 2)
	gasbtn = types.KeyboardButton('/gas')
	ethbtn = types.KeyboardButton('/price')
	donatebtn = types.KeyboardButton('/donate')
	markup.add(gasbtn, ethbtn, donatebtn)
	bot.send_message(msg.chat.id, 'Choose an option', reply_markup = markup)


@bot.message_handler(commands = ['gas'])
def gas_fees(msg):
	bot.send_message(msg.chat.id, gasfees(), disable_web_page_preview=True)

@bot.message_handler(commands = ['price'])
def eth_price(msg):
	bot.send_message(msg.chat.id, ethprice())

@bot.message_handler(commands = ['donate'])
def helpme(msg):
	bot.send_message(msg.chat.id, donate)

# while True:
# 	try:
# 		bot.infinity_polling(skip_pending=True)
# 		telebot.apihelper.SESSION_TIME_TO_LIVE = 2000
# 	except:
# 		sleep(1)

Setting up of webhooks for hosting on Heroku server
See if the environment variable Heroku (how to add it, see below)
if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)
    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200
    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://glacial-bayou-22780.herokuapp.com/") # this url must be replaced with the url of your Heroku app
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
else:
    # if the environment variable HEROKU no, it means run your dev machine.
	# Delete webhook just in case, and start with the usual polling.
    bot.remove_webhook()
    bot.polling(none_stop=True)