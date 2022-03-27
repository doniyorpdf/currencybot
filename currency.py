import requests
from pprint import pprint as print
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5180966191:AAH_lVdkuDs9o-HolPcs92wvujlfDtzDv6k'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Valyutalar kursi botiga xush kelibsiz.\n"
                        "O'zingizga kerakli valyutaning qisqartmasini yozing.\n"
                        "Agarda ularni bilmasangi /currency ni jo'nating")

@dp.message_handler(commands=['currency'])
async def send_welcome(message: types.Message):
    await message.reply("Albania Lek	ALL	Lek\n"
                        "Afghanistan Afghani	AFN ؋\n"
                        "Argentina Peso	ARS	$\n"
                        "Aruba Guilder	AWG	ƒ\n"
                        "Australia Dollar	AUD	$\n"
                        "Azerbaijan Manat	AZN	₼\n"
                        "Bahamas Dollar	BSD	$\n"
                        "Barbados Dollar	BBD	$\n"
                        "Belarus Ruble	BYN	Br\n"
                        "Belize Dollar	BZD	BZ$\n"
                        "Bermuda Dollar	BMD	$\n"
                        "Bolivia Bolíviano	BOB	$b\n"
                        "Bosnia and Herzegovina Convertible Mark	BAM	KM\n"
                        "Botswana Pula	BWP	P\n"
                        "Bulgaria Lev	BGN	лв\n"
                        "Brazil Real	BRL	R$\n"
                        "Brunei Darussalam Dollar	BND	$\n"
                        "Cambodia Riel	KHR	៛\n"
                        "Canada Dollar	CAD	$\n"
                        "Cayman Islands Dollar	KYD	$\n"
                        "Chile Peso	CLP	$\n"
                        "China Yuan Renminbi	CNY	¥\n"
                        "Colombia Peso	COP	$\n"
                        "Costa Rica Colon	CRC	₡\n"
                        "Croatia Kuna	HRK	kn\n"
                        "Cuba Peso	CUP	₱\n"
                        "Czech Republic Koruna	CZK	Kč\n"
                        "Denmark Krone	DKK	kr\n"
                        "Dominican Republic Peso	DOP	RD$\n"
                        "East Caribbean Dollar	XCD	$\n"
                        "Egypt Pound	EGP	£\n"
                        "El Salvador Colon	SVC	$\n"
                        "Euro Member Countries	EUR	€\n"
                        "Falkland Islands (Malvinas) Pound	FKP	£\n"
                        "Fiji Dollar	FJD	$\n"
                        "Ghana Cedi	GHS	¢\n"
                        "Gibraltar Pound	GIP	£\n"
                        "Guatemala Quetzal	GTQ	Q\n"
                        "Guernsey Pound	GGP	£\n"
                        "Guyana Dollar	GYD	$\n"
                        "Honduras Lempira	HNL	L\n"
                        "Hong Kong Dollar	HKD	$\n"
                        "Hungary Forint	HUF	Ft\n"
                        "Iceland Krona	ISK	kr\n"
                        "India Rupee	INR	₹\n"
                        "Indonesia Rupiah	IDR	Rp\n"
                        "Iran Rial	IRR  ﷼  \n"
                        "Isle of Man Pound	IMP	£\n"
                        "Israel Shekel	ILS	₪\n"
                        "Jamaica Dollar	JMD	J$\n"
                        "Japan Yen	JPY	¥\n"
                        "Jersey Pound	JEP	£\n"
                        "Kazakhstan Tenge	KZT	лв\n"
                        "Korea (North) Won	KPW	₩\n"
                        "Korea (South) Won	KRW	₩\n"
                        "Kyrgyzstan Som	KGS	лв\n"
                        "Laos Kip	LAK	₭\n"
                        "Lebanon Pound	LBP	£\n"
                        "Liberia Dollar	LRD	$\n"
                        "Macedonia Denar	MKD	ден\n"
                        "Malaysia Ringgit	MYR	RM\n"
                        "Mauritius Rupee	MUR	₨\n"
                        "Mexico Peso	MXN	$\n"
                        "Mongolia Tughrik	MNT	₮\n"
                        "Moroccan-dirham	MNT د.إ\n"
                        "Mozambique Metical	MZN	MT\n"
                        "Namibia Dollar	NAD	$\n"
                        "Nepal Rupee	NPR	₨\n"
                        "Netherlands Antilles Guilder	ANG	ƒ\n"
                        "New Zealand Dollar	NZD	$\n"
                        "Nicaragua Cordoba	NIO	C$\n"
                        "Nigeria Naira	NGN	₦\n"
                        "Norway Krone	NOK	kr\n"
                        "Oman Rial	OMR  ﷼ \n"
                        "Pakistan Rupee	PKR	₨\n"
                        "Panama Balboa	PAB	B/.\n"
                        "Paraguay Guarani	PYG	Gs\n"
                        "Peru Sol	PEN	S/.\n"
                        "Philippines Peso	PHP	₱\n"
                        "Poland Zloty	PLN	zł\n"
                        "Qatar Riyal	QAR  ﷼	\n"
                        "Romania Leu	RON	lei\n"
                        "Russia Ruble	RUB	₽\n"
                        "Saint Helena Pound	SHP	£\n"
                        "Saudi Arabia Riyal	SAR  ﷼	\n"
                        "Serbia Dinar	RSD	Дин.\n"
                        "Seychelles Rupee	SCR	₨\n"
                        "Singapore Dollar	SGD	$\n"
                        "Solomon Islands Dollar	SBD	$\n"
                        "Somalia Shilling	SOS	S\n"
                        "South Korean Won	KRW	₩\n"
                        "South Africa Rand	ZAR	R\n"
                        "Sri Lanka Rupee	LKR	₨\n"
                        "Sweden Krona	SEK	kr\n"
                        "Switzerland Franc	CHF	CHF\n"
                        "Suriname Dollar	SRD	$\n"
                        "Syria Pound	SYP	£\n"
                        "Taiwan New Dollar	TWD	NT$\n"
                        "Thailand Baht	THB	฿\n"
                        "Trinidad and Tobago Dollar	TTD	TT$\n"
                        "Turkey Lira	TRY	₺\n"
                        "Tuvalu Dollar	TVD	$\n"
                        "Ukraine Hryvnia	UAH	₴\n"
                        "UAE-Dirham	AED د.إ\n"
                        "United Kingdom Pound	GBP	£\n"
                        "United States Dollar	USD	$\n"
                        "Uruguay Peso	UYU	  $ U\n"
                        "Uzbekistan So\'m	UZS\n"
                        "Venezuela Bolívar	VEF	Bs\n"
                        "Viet Nam Dong	VND	₫\n"
                        "Yemen Rial	YER  ﷼ 	\n")

@dp.message_handler()
async def sendcurrency(message: types.Message):
    try:
        API_KEY = '2c80f973601e508384cc8bcc'

        currency = message.text
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

        response = requests.get(url)
        jsondata = response.json()
        kurs = response.json()['conversion_rate']
        respond = f"{jsondata['time_last_update_utc']} dagi kurs: 1 {currency.upper()} = {kurs} so'm"
        await message.answer(respond)
    except:
        await message.answer("Kechirasiz, bu turdagi valyuta topilmadi")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)