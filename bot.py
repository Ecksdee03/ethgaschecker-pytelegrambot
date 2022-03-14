import telebot, os, requests
from dotenv import load_dotenv
from telebot import types
from telebot.types import ReplyKeyboardMarkup as rkm
from keep_alive import app
import threading

#fetch api keys and initialise bot object
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(token=TOKEN, parse_mode = "HTML")
ethscan_token = os.getenv('ETH_TOKEN')
print("Bot is running now!")

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
<b>ETH Address:</b> 0x08BD6b1c3834bd578fcfe53fbCB35f9b516c5372
<b>BTC Address:</b> bc1q92pz4ut6460yyu5umjq5jmpn2klqd5lgfey8vn
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

#conversion of gas price unit gwei to usd
def gweitousd(gwei):
	ethprice = round(ethdata['ethereum']['usd'], 2)
	usdp = gwei * ethprice * 1.00E-9 * 21000
	return usdp

#configure functions run by user msg commands
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

#opens server in the background
threading.Thread(target=lambda: app.run(host='0.0.0.0')).start()
#bot continuously polls for new msgs from user
bot.polling()
