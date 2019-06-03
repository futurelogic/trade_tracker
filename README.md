# Trade Tracker

Welcome to the trade document builder. This app will help you build your trade documents when evaluating trades. This app is built with Python 3, as such having Python 3 installed is a prerequisite.

To run the app, execute program.py

Ex:

cd ~/trade_tracker
python3 program.py -n

When initializing the app, you must use a flag to specify what you would like to do...

-n:  Create a new trade doc
-h: Print this help file to screen
-p: Print example trade to the screen
-e: Edit Trade (used to add the date the trade was closed)

This app is built for all skill levels, S1 all the way to RTP. The app will adjust it's questions based on the level you pick in the beginning.

If you pick S1, you will be asked:

- The level you trade at
- The market you are working off
- The date for market's SLI
- The deciding candle for the market
- Indicators for the market's SLI
- The symbol you are trading
- The date for symbol's SLI
- The deciding candle for the symbol
- Indicators for symbol's SLI
- The date the next earnings falls on
- The date the previous earnings falls on
- Did the current earnings out perform the previous
- The date you are opening the trade
- Has the trade been closed yet (for historic study)
- Is this a call or a put
- Is this a real or a paper trade
- If real, what legs are you opening the trade in
- What are the dog, elephant, and herd doing


If you pick S2, this adds calling the weekly candle


If you pick S3, this adds the predictive paragraph


If you pick RTP, this adds the following considerations:

- General

- Symbol 233
- Symbol Daily
- Symbol Weekly
- Symbol Monthly
- Symbol Quarterly

- Market 233
- Market Daily
- Market Weekly

- $VIX 233
- $VIX Daily
- $VIX Weekly

- $VXN 233
- $VXN Daily
- $VXN Weekly

- $SPX 233
- $SPX Daily
- $SPX Weekly

- $W5000 233
- $W5000 Daily
- $W5000 Weekly
