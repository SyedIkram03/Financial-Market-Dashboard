import streamlit as st
import yfinance as yf
from PIL import Image
from urllib.request import urlopen
import plotly.tools
from streamlit_option_menu import option_menu
st.set_page_config(page_title="My Dashboard", page_icon="graph", layout="wide", initial_sidebar_state="auto", menu_items=None)
logo=Image.open(urlopen('https://img.icons8.com/dusk/344/stocks.png'))
st.image(logo,width=400)
st.date_input("Today's Date:")
st.title("Welcome to the World of Financial Analysis. ")
# imageC=Image.open(urlopen('https://img.icons8.com/fluency/2x/bitcoin-cryptocurrency.png'))
# st.image(imageC)

with st.sidebar:
	selected= option_menu(
	menu_title="Main Menu",
	options = ["Home","Indian Stock Market","USA Stock Market","Crypto Stock Market"],
	icons = ["House door","Currency rupee", "Currency dollar","Currency bitcoin"],
	menu_icon="cast",
	
	)



if selected=="Home":
	st.write(f"You have selected {selected}")



	st.title("stock market")
	stock=Image.open(urlopen('https://www.financialexpress.com/wp-content/uploads/2022/08/3-6.jpg'))
	st.image(stock,width=400)

	st.write('''A stock market, equity market, or share market is the aggregation of buyers and sellers of stocks (also called shares), which represent ownership claims on businesses; these may include securities listed on a public stock exchange, as well as stock that is only traded privately, such as shares of private companies which are sold to investors through equity crowdfunding platforms. Investment is usually made with an investment strategy in mind.''')


	st.title("Cryptocurrency market")
	logo=Image.open(urlopen('https://www.marketsmedia.com/wp-content/uploads/2019/01/iStock-977691792-1024x683.jpg'))
	st.image(logo,width=400)

	st.write('''Cryptocurrency is decentralized digital money that is based on blockchain technology and secured by cryptography. To understand cryptocurrency, one needs to first understand three terminologies – blockchain, decentralization, and cryptography. 

	In simple words, blockchain in the context of cryptocurrency is a digital ledger 
	whose access is distributed among authorized users. 
	This ledger records transactions related to a range of assets,
	 like money, house, or even intellectual property. ''')


	st.balloons()

	



elif selected=="Indian Stock Market":
	st.title(f"You have selected {selected}")

	#for reliance
	Reliance='RELIANCE.NS'
	RIL_data=yf.Ticker(Reliance)
	RILhis=RIL_data.history(period="max")
	start="2022-08-28"
	end="2022-09-01"
	RIL=yf.download(Reliance,start,end)
	
	st.title("RELIANCE(RIL)")
	imgRIL=Image.open(urlopen('https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/b2lye57ekzo1ovhlsscn'))
	st.image(imgRIL)
	st.table(RIL)
	st.bar_chart(RILhis)
	st.line_chart(RILhis)


	SENSEX='SENSEX.NS'
	SENSEX_data=yf.Ticker(SENSEX)
	SENSEXhis=RIL_data.history(period="max")
	start="2022-08-28"
	end="2022-09-01"
	SENSEXd=yf.download(SENSEX,start,end)
	
	st.title("SENSEX(RIL)")
	imgSENSEX=Image.open(urlopen('https://blog.ipleaders.in/wp-content/uploads/2020/10/MT5-bombay-stock-exchange-bse.png'))
	st.image(imgSENSEX)
	st.table(SENSEXd)
	st.bar_chart(SENSEXhis)
	st.line_chart(SENSEXhis)



	st.balloons()






elif selected=="USA Stock Market":
	st.title(f"You have selected {selected}")
	# Apple (AAPL): 7.14%
	# Microsoft (MSFT): 6.1%
	# Amazon (AMZN): 3.8%
	# Tesla (TSLA): 2.5%
	# ALPHABET INC.	GOOG

	Apple='AAPL-USD'
	AAPL_data=yf.Ticker(Apple)
	AAPLhis=AAPL_data.history(period="max")
	start="2022-08-28"
	end="2022-09-01"
	AAPL=yf.download(Apple,start,end)
	st.title("Apple")
	imgAAPL=Image.open(urlopen('https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png?202208222229'))
	st.image(imgAAPL,width=200)
	st.table(AAPL)
	st.bar_chart(AAPLhis)

	Microsoft='MSFT-USD'
	MSFT_data=yf.Ticker(Microsoft)
	MSFThis=MSFT_data.history(period="max")
	start="2022-08-28"
	end="2022-09-01"
	MSFT=yf.download(Microsoft,start,end)
	
	st.title("Microsoft")
	imgMSFT=Image.open(urlopen('https://www.gartner.com/imagesrv/peer-insights/vendors/logos/microsoft.jpg'))
	st.image(imgMSFT,width=200)
	st.table(MSFT)
	st.bar_chart(MSFThis)

	st.balloons()


elif selected=="Crypto Stock Market":
	st.title(f"You have selected {selected}")
	Bitcoin='BTC-USD'
	Ethereum='ETH-USD'
	Solana='SOL-USD'
	BinanceCoin='BNB-USD'

	BTC_data=yf.Ticker(Bitcoin)
	ETH_data=yf.Ticker(Ethereum)
	SOL_data=yf.Ticker(Solana)
	BNB_data=yf.Ticker(BinanceCoin)

	Btchis=BTC_data.history(period="max")
	Ethhis=ETH_data.history(period="max")
	SOLhis=SOL_data.history(period="max")
	BNBhis=BNB_data.history(period="max")

	start="2022-08-28"
	end="2022-09-01"
	BTC=yf.download(Bitcoin,start,end)
	ETH=yf.download(Ethereum,start,end)
	SOL=yf.download(Solana,start,end)
	BNB=yf.download(BinanceCoin,start,end)

	
	st.title("BITCOIN($)")
	imgBTC=Image.open(urlopen('https://img.icons8.com/color/2x/bitcoin.png'))
	st.image(imgBTC,width=200)
	st.table(BTC)
	st.bar_chart(Btchis)

	
	st.title("ETHEREUM(ETH)")
	imageETH=Image.open(urlopen('https://img.icons8.com/cotton/344/ethereum--v1.png'))
	st.image(imageETH,width=200)
	st.table(ETH)
	st.bar_chart(Ethhis)

	
	st.title("Solana(S)")
	imageSOL=Image.open(urlopen('https://thumbor.forbes.com/thumbor/fit-in/900x510/https://www.forbes.com/advisor/wp-content/uploads/2022/06/solana_logo.jpeg.jpg'))
	st.image(imageSOL,width=200)
	st.table(SOL)
	st.bar_chart(SOLhis)


	st.title("Binance Coin")
	imgBNB=Image.open(urlopen('https://blog.bitnovo.com/wp-content/uploads/2021/03/Que%CC%81-es-Binance-Coin-BNB-1.jpg'))
	st.image(imgBNB,width=200)
	st.table(BNB)
	st.bar_chart(BNBhis)


	# Binance Coin (BNB)
	# XRP (XRP)
	st.balloons()



st.error("In case of any error, Please Contact the Administrator!")
st.success("Thanks For Visiting the Website!")
st.warning("Like and Follow us for More.")







