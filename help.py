help = '''
Trade Document Builder Help
===========================

Welcome to the trade document builder. This app will help you build your trade documents when evaluating trades and \
deciding whether to enter.

This app is built for all skill levels, S1 all the way to RTP. The app will adjust it's questions based on the level \
you pick in the beginning.

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

'''


no_flag = '''
You have called the program without a flag...

Please run with one of the following flags:

-n = New file, start a new trade doc
-h = Print help file to screen
-e = Example trade (Gary's example from FB)

Example:

python3 program.py -n

or 

python3 program.py -h'''