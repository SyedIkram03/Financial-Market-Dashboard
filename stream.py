import streamlit as st
import yfinance as yf
from PIL import Image
from urllib.request import urlopen
import plotly.tools
from streamlit_option_menu import option_menu
from datetime import date, timedelta


st.set_page_config(page_title="Financial Market Dashboard", page_icon="chart", layout="wide", initial_sidebar_state="auto", menu_items=None)

col1, col2= st.columns(2)

with col1:
    st.title("Welcome to the World of Financial Analysis.")

with col2:
    
    # logo=Image.open(urlopen('https://cdn-icons-png.flaticon.com/512/2422/2422796.png'))
    # st.image(logo,width=150)

    st.image("https://img.freepik.com/free-vector/flat-design-stock-market-concept_23-2149180046.jpg?w=740&t=st=1667239754~exp=1667240354~hmac=1b765b9c33e8be507ecf02adaf6dbcd20a9b1e34df489d69c07a6192544b4780",width=200)




with st.sidebar:

	selected= option_menu(
	menu_title="Main Menu",
	options = ["Home","Indian Stock Market","USA Stock Market","Crypto Stock Market","NFT Collections Market","More..."],
	menu_icon="cast",
	
	)


if selected=="Home":
	col1, col2, col3 = st.columns(3)
	with col1:
	    st.write(' ')
	with col2:
		st.image("https://cdn-icons-png.flaticon.com/512/2163/2163350.png", caption="Home", width=60)
	    
	with col3:
		st.write(' ')
	    
	
	with st.spinner(text='Loading...'):

		st.title("Stock Market")
		stock=Image.open(urlopen('https://cdn-icons-png.flaticon.com/512/3606/3606247.png'))
		st.image(stock,width=250)

		st.write('''A stock market, equity market, or share market is the aggregation of buyers and sellers of stocks (also called shares), which represent ownership claims on businesses; these may include securities listed on a public stock exchange, as well as stock that is only traded privately, such as shares of private companies which are sold to investors through equity crowdfunding platforms. Investment is usually made with an investment strategy in mind.''')

		st.title("Cryptocurrency Market")
		logo=Image.open(urlopen('https://cdn-icons-png.flaticon.com/512/4340/4340800.png'))
		st.image(logo,width=250)

		st.write('''Cryptocurrency is decentralized digital money that is based on blockchain technology and secured by cryptography. To understand cryptocurrency, one needs to first understand three terminologies – blockchain, decentralization, and cryptography. 
		In simple words, blockchain in the context of cryptocurrency is a digital ledger whose access is distributed among authorized users. 
		This ledger records transactions related to a range of assets,like money, house, or even intellectual property. ''')

		st.title("NFT Collections")
		logo=Image.open(urlopen('https://cdn-icons-png.flaticon.com/512/7116/7116015.png'))
		st.image(logo,width=250)

		st.write("A non-fungible token (NFT) is a unique digital identifier that cannot be copied, substituted, or subdivided, that is recorded in a blockchain, and that is used to certify authenticity and ownership.The ownership of an NFT is recorded in the blockchain and can be transferred by the owner, allowing NFTs to be sold and traded. NFTs can be created by anybody, and require few or no coding skills to create.NFTs typically contain references to digital files such as photos, videos, and audio. Because NFTs are uniquely identifiable assets, they differ from cryptocurrencies, which are fungible.")

		
		st.snow()


elif selected=="Indian Stock Market":
	col1, col2, col3 = st.columns(3)

	with col1:
	    st.write(' ')

	with col2:
	    st.image("https://as1.ftcdn.net/v2/jpg/04/23/74/52/1000_F_423745269_5YH31rKdjWCcoLi843dOAPnK0JhCoKgk.jpg", caption="Indian Stock Market", width=100)

	with col3:
	    st.write(' ')

	
	col4, col5= st.columns(2)
	with col4:
	    # st.write("")
		company=st.text_input("Enter Name of the Company:")

	with col5:
		ti=st.text_input("Enter time frame:")
	    

	def compdata(comp,ti):
		try:
			comp=comp.upper()
			st.title(f"{comp}")
			st.image("https://cdn-icons-png.flaticon.com/512/2422/2422796.png",width=150)
    		
			Comphis=yf.Ticker(comp).history(period=f"{ti}")
			end =  date.today().strftime("%Y-%m-%d")
			# compdat=yf.download(Reliance,end)
			st.table(yf.download(comp,end))
			st.bar_chart(Comphis)
			st.line_chart(Comphis)
		except:
			st.error("Sorry some Error Occured!Try something like 'TATASTEEL.NS' time='2y' ")

	
	if st.button('Get Data'):
		compdata(company,ti)
	st.error("NOTE: Add '.NS' after the company code time can be 'max' or'1y','2m' year->y & month->m")
	
	
	#for reliance
	Reliance='RELIANCE.NS'
	RILhis=yf.Ticker(Reliance).history(period="max")
	start="2022-10-28"
	end =  date.today().strftime("%Y-%m-%d")
	RIL=yf.download(Reliance,start,end)
	st.title("Reliance Industries (RELIANCE.NS)")
	st.image("https://1000logos.net/wp-content/uploads/2021/08/Reliance-Industries-Limited-RIL-Logo-1966.png",width=300)
	st.table(RIL)
	st.bar_chart(RILhis)
	st.line_chart(RILhis)

	HDFC='HDFCBANK.NS'
	HDFChis=yf.Ticker(HDFC).history(period="5y")
	
	end =  date.today().strftime("%Y-%m-%d")
	HD=yf.download(HDFC,end)
	st.title("HDFC Industries (HDFC.NS)")
	st.image("https://www.hdfcbank.com/content/api/contentstream/723fb80a-2dde-42a3-9793-7ae1be57c87f/SEO/hdfc.png",width=300)
	st.table(HD)
	st.bar_chart(HDFChis)
	st.line_chart(HDFChis)


	TATA='TATASTEEL.NS'
	TATA_data=yf.Ticker(TATA)
	TATAhis=TATA_data.history(period="5y")
	end =  date.today().strftime("%Y-%m-%d")
	TATAd=yf.download(TATA,end)
	st.title("TATA Industries(TATASTEEL.NS)")
	st.image("https://assets.stickpng.com/images/5ec3e22d58550c000442773b.png")
	st.table(TATAd)
	st.bar_chart(TATAhis)
	st.line_chart(TATAhis)



elif selected=="USA Stock Market":
	col1, col2, col3 = st.columns(3)
	with col1:
	    st.write(' ')
	with col2:
		st.image("https://cdn-icons-png.flaticon.com/512/4256/4256900.png", caption=f"{selected}", width=60)
	    
	with col3:
		st.write(' ')
	# Apple (AAPL): 7.14%
	# Microsoft (MSFT): 6.1%
	# Amazon (AMZN): 3.8%
	# Tesla (TSLA): 2.5%
	# ALPHABET INC.	GOOG

	col4, col5= st.columns(2)
	with col4:
	    # st.write("")
		company=st.text_input("Enter Name of the US Stock:")

	with col5:
		ti=st.text_input("Enter time frame:")
	    

	def compdata(comp,ti):
		try:
			comp=comp.upper()
			st.title(f"{comp}")
			st.image("https://cdn-icons-png.flaticon.com/512/2422/2422796.png",width=150)
	   		
			Comphis=yf.Ticker(comp).history(period=f"{ti}")
			end =  date.today().strftime("%Y-%m-%d")
			# compdat=yf.download(Reliance,end)
			st.table(yf.download(comp,end))
			st.bar_chart(Comphis)
			st.line_chart(Comphis)
		except:
			st.error("Sorry some Error Occured!Try something like 'GOOG' time='max' ")

	
	if st.button('Get Data'):
		compdata(company,ti)
	st.error("NOTE: See company code on internet, time can be 'max' or'1y','2m' year->y & month->m")




	Apple='AAPL'
	AAPL_data=yf.Ticker(Apple)
	AAPLhis=AAPL_data.history(period="2y")
	
	end =  date.today().strftime("%Y-%m-%d")
	
	AAPL=yf.download(Apple,end)
	st.title("Apple")
	imgAAPL=Image.open(urlopen('https://cdn-icons-png.flaticon.com/512/831/831329.png'))
	st.image(imgAAPL,width=150)
	st.table(AAPL)
	st.bar_chart(AAPLhis)


	Amazon='AMZN'
	AMZN_data=yf.Ticker(Amazon)
	AMZNhis=AMZN_data.history(period="2y")
	# start="2022-08-28"
	end =  date.today().strftime("%Y-%m-%d")
	AMZN=yf.download(Amazon,end)
	st.title("Amazon  AMZN")
	imgAMZN=Image.open(urlopen('https://readersentertainment.com/wp-content/uploads/2022/05/a.png'))
	st.image(imgAMZN,width=150)
	st.table(AMZN)
	st.bar_chart(AMZNhis)

	Tesla='TSLA'
	TSLA_data=yf.Ticker(Tesla)
	TSLAhis=TSLA_data.history(period="5y")
	# start="2022-08-28"
	end =  date.today().strftime("%Y-%m-%d")
	TSLA=yf.download(Tesla,end)
	st.title("Tesla (TSLA)")
	
	st.image("https://cdn-icons-png.flaticon.com/512/305/305611.png",width=200)
	st.table(TSLA)
	st.bar_chart(TSLAhis)


	Microsoft='MSFT'
	MSFT_data=yf.Ticker(Microsoft)
	MSFThis=MSFT_data.history(period="2y")
	# start="2022-08-28"
	end =  date.today().strftime("%Y-%m-%d")
	MSFT=yf.download(Microsoft,end)
	
	st.title("Microsoft")
	imgMSFT=Image.open(urlopen('https://cdn-icons-png.flaticon.com/512/732/732221.png'))
	st.image(imgMSFT,width=150)
	st.table(MSFT)
	st.bar_chart(MSFThis)



elif selected=="Crypto Stock Market":


	col1, col2, col3 = st.columns(3)

	with col1:
	    st.write(' ')

	with col2:
	    st.image("https://cdn-icons-png.flaticon.com/512/7068/7068095.png", caption="Crypto Stock Market", width=90)

	with col3:
	    st.write(' ')

	
	col4, col5= st.columns(2)
	with col4:
	    # st.write("")
		company=st.text_input("Enter Name of the Cryptocurrency:")

	with col5:
		ti=st.text_input("Enter time frame:")
	    

	def compdata(comp,ti):
		try:
			comp=comp.upper()
			st.title(f"{comp}")
			st.image("https://cdn-icons-png.flaticon.com/512/2422/2422796.png",width=150)
	   		
			Comphis=yf.Ticker(comp).history(period=f"{ti}")
			end =  date.today().strftime("%Y-%m-%d")
			# compdat=yf.download(Reliance,end)
			st.table(yf.download(comp,end))
			st.bar_chart(Comphis)
			st.line_chart(Comphis)
		except:
			st.error("Sorry some Error Occured!Try something like 'SOL-USD' time='2m' ")

	
	if st.button('Get Data'):
		compdata(company,ti)
	st.error("Check crypto code on internet,time can be 'max' or'1y','2m' year->y & month->m")



	Bitcoin='BTC-USD'
	Ethereum='ETH-USD'
	Solana='SOL-USD'
	BinanceCoin='BNB-USD'

	BTC_data=yf.Ticker(Bitcoin)
	ETH_data=yf.Ticker(Ethereum)
	SOL_data=yf.Ticker(Solana)
	BNB_data=yf.Ticker(BinanceCoin)

	Btchis=BTC_data.history(period="3y")
	Ethhis=ETH_data.history(period="3y")
	SOLhis=SOL_data.history(period="3y")
	BNBhis=BNB_data.history(period="3y")

	start="2022-10-20"
	end =  date.today().strftime("%Y-%m-%d")
	BTC=yf.download(Bitcoin,end)
	# ETH=yf.download(Ethereum,start,end)
	# SOL=yf.download(Solana,start,end)
	# BNB=yf.download(BinanceCoin,start,end)
	ETH=yf.download(Ethereum,end)
	SOL=yf.download(Solana,end)
	BNB=yf.download(BinanceCoin,start,end)

	
	st.title("BITCOIN($)")
	imgBTC=Image.open(urlopen('https://cdn-icons-png.flaticon.com/512/1490/1490900.png'))
	st.image(imgBTC,width=150)
	st.table(BTC)
	st.bar_chart(Btchis)
	st.line_chart(Btchis)

	
	st.title("ETHEREUM(ETH)")
	imageETH=Image.open(urlopen('https://img.icons8.com/cotton/344/ethereum--v1.png'))
	st.image(imageETH,width=150)
	st.table(ETH)
	st.bar_chart(Ethhis)
	st.line_chart(Ethhis)

	
	st.title("Solana(S)")
	imageSOL=Image.open(urlopen('https://cdn-icons-png.flaticon.com/512/5987/5987962.png'))
	st.image(imageSOL,width=180)
	st.table(SOL)
	st.bar_chart(SOLhis)


	st.title("Binance Coin")
	imgBNB=Image.open(urlopen('https://cdn-icons-png.flaticon.com/512/6163/6163366.png'))
	st.image(imgBNB,width=200)
	st.table(BNB)
	st.bar_chart(BNBhis)




	Ripple='XRP-USD'
	XRP_data=yf.Ticker(Ripple)
	XRPhis=XRP_data.history(period="max")
	start="2022-10-28"
	end =  date.today().strftime("%Y-%m-%d")
	XRP=yf.download(Ripple,start,end)
	
	st.title("Ripple  XRP")
	imgXRP=Image.open(urlopen('https://cdn-icons-png.flaticon.com/512/2586/2586172.png'))
	st.image(imgXRP,width=200)
	st.table(XRP)
	st.bar_chart(XRPhis)
	st.write("GRAPH from MAX data available in yfin!!!")


	# Binance Coin (BNB)
	# XRP (XRP)

elif selected=="NFT Collections Market":

	col1, col2, col3 = st.columns(3)

	with col1:
	    st.write(' ')

	with col2:
	    st.image("https://cdn-icons-png.flaticon.com/512/8632/8632263.png", caption="NFT Collections Market", width=100)

	with col3:
	    st.write(' ')
	st.write('''Non-fungible tokens (NFTs) give you ownership of artwork, music, videos and other online collectibles. They exist on blockchains, the innovative technology that underlies cryptocurrencies like Bitcoin.

Here are some of the most popular and well-rated NFT marketplaces where you can buy and sell these digital assets.
An NFT marketplace is a digital platform for buying and selling NFTs. These platforms allow people to store and display their NFTs plus sell them to others for cryptocurrency or money. Some NFT marketplaces also allow users to mint their NFTs on the platform itself.''')    
	
	st.markdown('''OpenSea
OpenSea is ancient by NFT standards, having launched in 2017, and it’s also among the largest NFT marketplaces active today. It hosts many popular NFTs, including art, music, photography, trading cards and virtual worlds.     https://opensea.io/''')
	st.markdown('''Binance
Binance, one of the largest cryptocurrency exchanges, added an NFT marketplace in 2021. The international crypto exchange is one of many other industry players entering the NFT sector, like Crypto.com NFT, which describes itself as a highly-curated NFP marketplace.

Binance NFT offers the typical digital assets found on other major platforms: artwork, gaming items, and collectibles.   https://www.binance.com/en/nft/home''')


elif selected=="More...":
	st.title("Rock,Paper,Scissor!")
	import random
	
	col1, col2, col3 = st.columns(3)
	with col1:
	    st.image("https://cdn-icons-png.flaticon.com/512/630/630426.png", caption="Computer", width=110)
	with col2:
		st.image("https://cdn-icons-png.flaticon.com/512/6690/6690115.png", width=140)
	    
	with col3:
		st.image("https://cdn-icons-png.flaticon.com/512/149/149071.png", caption="You", width=110)

	item_list=["Rock", "Paper", "Scissor"]
	
	user_choice = st.selectbox('What would you like to select?',('Rock', 'Paper', 'Scissor'))
	comp_choice = random.choice(item_list)
	st.header(f"Robot selected:{comp_choice}       &       You selected: {user_choice}")
	
	

	if user_choice == comp_choice:
	    st.success("Match Tie")

	elif user_choice == "Rock":
	    if comp_choice == "Paper":
	        st.success("Paper covers Rock, Computer wins")
	    else:
	        st.success("Rock smashes Scissor, You won")

	elif user_choice == "Paper":
	    if comp_choice == "Scissor":
	        st.success("Scissor cuts Paper, Computer wins")
	    else:
	        st.success("Paper covers Rock, You won")

	elif user_choice == "Scissor":
	    if comp_choice == "Rock":
	        st.success("Rock smashes Scissor, Computer won")
	    else:
	        st.success("Scissor cuts Paper, You won")




st.date_input("Today's Date:")
st.error("In case of any error,Contact Syed Ikram!")
url = "https://forms.gle/xTun2Qon99RUgPK36"
st.write("Leave your Valuabe Feedback [Here](%s)" % url)










