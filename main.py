{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red113\green184\blue255;\red23\green23\blue23;\red202\green202\blue202;
\red183\green111\blue179;\red89\green156\blue62;\red194\green126\blue101;\red212\green212\blue212;\red212\green214\blue154;
\red70\green137\blue204;\red140\green211\blue254;\red67\green192\blue160;\red167\green197\blue152;}
{\*\expandedcolortbl;;\cssrgb\c50980\c77647\c100000;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c77255\c52549\c75294;\cssrgb\c41569\c66275\c30980;\cssrgb\c80784\c56863\c47059;\cssrgb\c86275\c86275\c86275;\cssrgb\c86275\c86275\c66667;
\cssrgb\c33725\c61176\c83922;\cssrgb\c61176\c86275\c99608;\cssrgb\c30588\c78824\c69020;\cssrgb\c70980\c80784\c65882;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 !\cf4 \strokec4 pip install requests\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 import\cf4 \strokec4  requests\cb1 \
\cf5 \cb3 \strokec5 from\cf4 \strokec4  bs4 \cf5 \strokec5 import\cf4 \strokec4  BeautifulSoup\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  smtplib\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  pickle\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # Define the product URLs\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 crocs_product_url = \cf7 \strokec7 "https://www.crocs.ca/classic-clog/10001,en_CA,pd.html?cgid=classic-clogs&cid=5BN"\cf4 \cb1 \strokec4 \
\cb3 jd_product_url = \cf7 \strokec7 "https://jdsports.ca/products/crocs-classic-clog-atmosphere"\cf4 \cb1 \strokec4 \
\cb3 sportchek_product_url = \cf7 \strokec7 "https://www.sportchek.ca/en/pdp/crocs-men-s-classic-rotating-back-strap-clogs-water-resistant-11736707f.330932435.html#store=389"\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # Define headers\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 headers = \cf8 \strokec8 \{\cf4 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 "user-agent"\cf8 \strokec8 :\cf4 \strokec4  \cf7 \strokec7 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 \}\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # Data fetching for the crocs website\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 page = requests.get\cf8 \strokec8 (\cf4 \strokec4 url=crocs_product_url\cf8 \strokec8 ,\cf4 \strokec4  headers=headers\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\cb3 soup = BeautifulSoup\cf8 \strokec8 (\cf4 \strokec4 page.content\cf8 \strokec8 ,\cf4 \strokec4  \cf7 \strokec7 'lxml'\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 print\cf8 \strokec8 (\cf4 \strokec4 soup.prettify\cf8 \strokec8 ())\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 tag = soup.find\cf8 \strokec8 (\cf7 \strokec7 'span'\cf8 \strokec8 ,\cf4 \strokec4  class_=\cf7 \strokec7 'price'\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  tag\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     crocs_product_price = tag.get_text\cf8 \strokec8 ()\cf4 \strokec4 .strip\cf8 \strokec8 ()\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 else\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     crocs_product_price = \cf7 \strokec7 "Price not found"\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # Data fetching for JD website\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 page = requests.get\cf8 \strokec8 (\cf4 \strokec4 url=jd_product_url\cf8 \strokec8 ,\cf4 \strokec4  headers=headers\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\cb3 soup = BeautifulSoup\cf8 \strokec8 (\cf4 \strokec4 page.content\cf8 \strokec8 ,\cf4 \strokec4  \cf7 \strokec7 'lxml'\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 print\cf8 \strokec8 (\cf4 \strokec4 soup.prettify\cf8 \strokec8 ())\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 tag = soup.find\cf8 \strokec8 (\cf7 \strokec7 'span'\cf8 \strokec8 ,\cf4 \strokec4  class_=\cf7 \strokec7 'price'\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  tag\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     jd_product_price = tag.get_text\cf8 \strokec8 ()\cf4 \strokec4 .strip\cf8 \strokec8 ()\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 else\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     jd_product_price = \cf7 \strokec7 "Price not found"\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # Data fetching for Sportchek\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 page = requests.get\cf8 \strokec8 (\cf4 \strokec4 url=sportchek_product_url\cf8 \strokec8 ,\cf4 \strokec4  headers=headers\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\cb3 soup = BeautifulSoup\cf8 \strokec8 (\cf4 \strokec4 page.content\cf8 \strokec8 ,\cf4 \strokec4  \cf7 \strokec7 'lxml'\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 print\cf8 \strokec8 (\cf4 \strokec4 soup.prettify\cf8 \strokec8 ())\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 tag = soup.find\cf8 \strokec8 (\cf7 \strokec7 'span'\cf8 \strokec8 ,\cf4 \strokec4  class_=\cf7 \strokec7 'price'\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  tag\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     sportchek_product_price = tag.get_text\cf8 \strokec8 ()\cf4 \strokec4 .strip\cf8 \strokec8 ()\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 else\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     sportchek_product_price = \cf7 \strokec7 "Price not found"\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # Storing data\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 def\cf4 \strokec4  \cf9 \strokec9 store_data\cf4 \strokec4 ()\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     data = \cf8 \strokec8 \{\cf4 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 'crocs'\cf8 \strokec8 :\cf4 \strokec4  \cf8 \strokec8 \{\cf7 \strokec7 'product_name'\cf8 \strokec8 :\cf4 \strokec4  \cf7 \strokec7 'Classic Crocs'\cf8 \strokec8 ,\cf4 \strokec4  \cf7 \strokec7 'price'\cf8 \strokec8 :\cf4 \strokec4  crocs_product_price\cf8 \strokec8 \},\cf4 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 'jdsports'\cf8 \strokec8 :\cf4 \strokec4  \cf8 \strokec8 \{\cf7 \strokec7 'product_name'\cf8 \strokec8 :\cf4 \strokec4  \cf7 \strokec7 'Classic Crocs'\cf8 \strokec8 ,\cf4 \strokec4  \cf7 \strokec7 'price'\cf8 \strokec8 :\cf4 \strokec4  jd_product_price\cf8 \strokec8 \},\cf4 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 'sportchek'\cf8 \strokec8 :\cf4 \strokec4  \cf8 \strokec8 \{\cf7 \strokec7 'product_name'\cf8 \strokec8 :\cf4 \strokec4  \cf7 \strokec7 'Classic Crocs'\cf8 \strokec8 ,\cf4 \strokec4  \cf7 \strokec7 'price'\cf8 \strokec8 :\cf4 \strokec4  sportchek_product_price\cf8 \strokec8 \}\cf4 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 \}\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 with\cf4 \strokec4  \cf9 \strokec9 open\cf8 \strokec8 (\cf7 \strokec7 'price_data.pkl'\cf8 \strokec8 ,\cf4 \strokec4  \cf7 \strokec7 'wb'\cf8 \strokec8 )\cf4 \strokec4  \cf5 \strokec5 as\cf4 \strokec4  \cf11 \strokec11 file\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\cb3         pickle.dump\cf8 \strokec8 (\cf4 \strokec4 data\cf8 \strokec8 ,\cf4 \strokec4  \cf11 \strokec11 file\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # Loading Stored Data\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 def\cf4 \strokec4  \cf9 \strokec9 read_data\cf4 \strokec4 ()\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 with\cf4 \strokec4  \cf9 \strokec9 open\cf8 \strokec8 (\cf7 \strokec7 'price_data.pkl'\cf8 \strokec8 ,\cf4 \strokec4  \cf7 \strokec7 'rb'\cf8 \strokec8 )\cf4 \strokec4  \cf5 \strokec5 as\cf4 \strokec4  \cf11 \strokec11 file\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\cb3         data = pickle.load\cf8 \strokec8 (\cf11 \strokec11 file\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\cb3         \cf5 \strokec5 for\cf4 \strokec4  key\cf8 \strokec8 ,\cf4 \strokec4  value \cf2 \strokec2 in\cf4 \strokec4  data.items\cf8 \strokec8 ():\cf4 \cb1 \strokec4 \
\cb3             \cf9 \strokec9 print\cf8 \strokec8 (\cf4 \strokec4 key\cf8 \strokec8 ,\cf4 \strokec4  \cf7 \strokec7 '::'\cf8 \strokec8 ,\cf4 \strokec4  value\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # Compare prices\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 try\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     crocs_product_price = \cf12 \strokec12 float\cf8 \strokec8 (\cf4 \strokec4 crocs_product_price\cf8 \strokec8 [\cf13 \strokec13 1\cf8 \strokec8 :])\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 except\cf4 \strokec4  ValueError\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     crocs_product_price = \cf12 \strokec12 float\cf8 \strokec8 (\cf7 \strokec7 'inf'\cf8 \strokec8 )\cf4 \strokec4  \cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 try\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     jd_product_price = \cf12 \strokec12 float\cf8 \strokec8 (\cf4 \strokec4 jd_product_price\cf8 \strokec8 [\cf13 \strokec13 1\cf8 \strokec8 :])\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 except\cf4 \strokec4  ValueError\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     jd_product_price = \cf12 \strokec12 float\cf8 \strokec8 (\cf7 \strokec7 'inf'\cf8 \strokec8 )\cf4 \strokec4  \cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 try\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     sportchek_product_price = \cf12 \strokec12 float\cf8 \strokec8 (\cf4 \strokec4 sportchek_product_price\cf8 \strokec8 [\cf13 \strokec13 1\cf8 \strokec8 :])\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 except\cf4 \strokec4  ValueError\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     sportchek_product_price = \cf12 \strokec12 float\cf8 \strokec8 (\cf7 \strokec7 'inf'\cf8 \strokec8 )\cf4 \strokec4  \cb1 \
\
\cb3 min_price = \cf9 \strokec9 min\cf8 \strokec8 (\cf4 \strokec4 crocs_product_price\cf8 \strokec8 ,\cf4 \strokec4  jd_product_price\cf8 \strokec8 ,\cf4 \strokec4  sportchek_product_price\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  min_price == crocs_product_price\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     company = \cf7 \strokec7 'Crocs'\cf4 \cb1 \strokec4 \
\cb3     url = crocs_product_url\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 elif\cf4 \strokec4  min_price == jd_product_price\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     company = \cf7 \strokec7 'JdSports'\cf4 \cb1 \strokec4 \
\cb3     url = jd_product_url\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 elif\cf4 \strokec4  min_price == sportchek_product_price\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     company = \cf7 \strokec7 'Sportchek'\cf4 \cb1 \strokec4 \
\cb3     url = sportchek_product_url\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # Data visualization\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 def\cf4 \strokec4  \cf9 \strokec9 notifications\cf4 \strokec4 ()\cf8 \strokec8 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     server = smtplib.SMTP\cf8 \strokec8 (\cf7 \strokec7 "smtp.gmail.com"\cf8 \strokec8 ,\cf4 \strokec4  \cf13 \strokec13 587\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\cb3     server.ehlo\cf8 \strokec8 ()\cf4 \cb1 \strokec4 \
\cb3     server.starttls\cf8 \strokec8 ()\cf4 \cb1 \strokec4 \
\cb3     server.ehlo\cf8 \strokec8 ()\cf4 \cb1 \strokec4 \
\cb3     server.login\cf8 \strokec8 (\cf7 \strokec7 "username"\cf8 \strokec8 ,\cf4 \strokec4  \cf7 \strokec7 "password"\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\cb3     subject = \cf7 \strokec7 "Prices Fell Down"\cf4 \cb1 \strokec4 \
\cb3     body = \cf10 \strokec10 f\cf7 \strokec7 "Please check \cf8 \strokec8 \{\cf4 \strokec4 company\cf8 \strokec8 \}\cf7 \strokec7 , click here \cf8 \strokec8 \{\cf4 \strokec4 url\cf8 \strokec8 \}\cf7 \strokec7 "\cf4 \cb1 \strokec4 \
\cb3     msg = \cf10 \strokec10 f\cf7 \strokec7 "Subject: \cf8 \strokec8 \{\cf4 \strokec4 subject\cf8 \strokec8 \}\cf7 \strokec7 \\n\\n\cf8 \strokec8 \{\cf4 \strokec4 body\cf8 \strokec8 \}\cf7 \strokec7 "\cf4 \cb1 \strokec4 \
\cb3     server.sendmail\cf8 \strokec8 (\cf7 \strokec7 "receivermailid"\cf8 \strokec8 ,\cf4 \strokec4  \cf7 \strokec7 "receivermailid"\cf8 \strokec8 ,\cf4 \strokec4  msg\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\cb3     \cf9 \strokec9 print\cf8 \strokec8 (\cf7 \strokec7 "Mail sent"\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\cb3     server.\cf9 \strokec9 quit\cf8 \strokec8 ()\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # Call the functions\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 store_data\cf8 \strokec8 ()\cf4 \cb1 \strokec4 \
\cb3 read_data\cf8 \strokec8 ()\cf4 \cb1 \strokec4 \
\cb3 notifications\cf8 \strokec8 ()\cf4 \cb1 \strokec4 \
}