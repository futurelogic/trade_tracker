import build
from os import system


def print_level(level):
    p_level = "Trading level: {}".format(level)
    print(p_level)
    return p_level


def print_trade(trade_timing):
    p_trade = []
    p_trade.append("Trade opened: {}".format(trade_timing[0]))
    print(p_trade[0])
    if trade_timing[1] == "still open":
        p_trade.append(("Trade closed: Trade still open"))
        print(p_trade[1])
    else:
        p_trade.append("Trade closed: {}".format(trade_timing[1]))
        print(p_trade[1])
    return p_trade


def print_trade_type(trade_type):
    trade_type = "Trade type: {}".format(trade_type)
    print(trade_type)
    return trade_type


def print_legs(acct_info):
    legs = []
    build.add_headspace()
    count = 0
    legs.append("Legs you have this trade open in:")
    if acct_info == "Paper":
        legs.append("None, this is a paper trade.")
    else:
        for item in acct_info:
            legs.append("{}. {} leg".format(count+1, item))
            count += 1
    for line in legs:
        print(line)
    return legs


def print_sym_market(type):
    build.add_headspace()
    count = 0
    market = []
    market.append("The following indicators were present on {}'s {} 233 candle on {}:".format(type[0], type[2], type[1]))
    for item in type[3]:
        if type[3][item] == "n":
            count +=1
        elif type[3][item] == "y":
            market.append(item)
    if count > 3:
        market.append("None")
    for line in market:
        print(line)
    return market


def print_earnings(earnings):
    build.add_headspace()
    store_earnings = []
    store_earnings.append("Earnings")
    border = "=" * len(store_earnings[0])
    store_earnings.append(border)
    store_earnings.append("Previous earnings: {}".format(earnings[1]))
    store_earnings.append("Current earnings: {}".format(earnings[0]))
    if earnings[2] == "Y":
        store_earnings.append("Current earnings beat previous.")
    elif earnings[2] == "N":
        store_earnings.append("Current earnings did not beat previous.")
    for line in  store_earnings:
        print(line)
    return store_earnings



def print_cons(considerations, symbol_or_market, chart, count, cons_type):
    build.add_headspace()
    if symbol_or_market == "General":
        header = ("{}: ".format(symbol_or_market, chart))
    else:
        header = ("{} {}: ".format(symbol_or_market, chart))
    border = "=" * len(header)
    print(header)
    print(border)
    for item in considerations[cons_type]:
        print("{}. {}".format(count, item))
        count += 1
    return count


def print_considerations(considerations, symbol, market):
    build.add_headspace()
    count = 3

    count = print_cons(considerations, "General", "", count, "general")

    count = print_cons(considerations, symbol, "233", count, "symbol_233")
    count = print_cons(considerations, symbol, "Daily", count, "symbol_daily")
    count = print_cons(considerations, symbol, "Weekly", count, "symbol_weekly")
    count = print_cons(considerations, symbol, "Monthly", count, "symbol_monthly")
    count = print_cons(considerations, symbol, "Quarterly", count, "symbol_quarterly")

    count = print_cons(considerations, market, "233", count, "market_233")
    count = print_cons(considerations, market, "Daily", count, "market_daily")
    count = print_cons(considerations, market, "Weekly", count, "market_weekly")

    count = print_cons(considerations, "$VIX", "233", count, "vix_233")
    count = print_cons(considerations, "$VIX", "Daily", count, "vix_daily")
    count = print_cons(considerations, "$VIX", "Weekly", count, "vix_weekly")

    count = print_cons(considerations, "$VXN", "233", count, "vxn_233")
    count = print_cons(considerations, "$VXN", "Daily", count, "vxn_daily")
    count = print_cons(considerations, "$VXN", "Weekly", count, "vxn_weekly")

    count = print_cons(considerations, "$SPX", "233", count, "spx_233")
    count = print_cons(considerations, "$SPX", "Daily", count, "spx_daily")
    count = print_cons(considerations, "$SPX", "Weekly", count, "spx_weekly")

    count = print_cons(considerations, "$W5000", "233", count, "w5k_233")
    count = print_cons(considerations, "$W5000", "Daily", count, "w5k_daily")
    print_cons(considerations, "$W5000", "Weekly", count, "w5k_weekly")

    build.add_headspace()


def print_pp(pp):
    build.add_headspace()
    count = 0
    header = "Predictive paragraph"
    border = "=" * len(header)
    print(header)
    print(border)
    if not pp:
        print("None")
    else:
        for item in pp:
            print("{}. {}".format(count+1, item))
            count +=1


def print_deh(deh):
    build.add_headspace()
    header = "Dog, Elephant, Herd"
    border = "=" * len(header)
    print(header)
    print(border)

    count = 0
    for item in deh:
        print("{}. {} is {}".format(count+1, item, deh[item]))
        count += 1


def print_weekly_candle(weekly_candle):
    build.add_headspace()
    header = "Weekly Candle"
    border = "=" * len(header)

    print(header)
    print(border)
    print("The color of the weekly candle will be {}".format(weekly_candle))


def cls():
    system('clear')


def print_filters(level, trade_filters, symbol, market):
    if level == "S2" or level == "S3" or level == "RTP":
        print_weekly_candle(trade_filters[0])
    if level == "S3" or level == "RTP":
        print_pp(trade_filters[1])
    if level == "RTP":
        print_considerations(trade_filters[2], symbol[0], market[0])


def print_results(level, market, symbol, earnings, trade_timing, trade_type, acct_info, deh, trade_filters):
    cls()
    build.build_big_space()
    store_level = print_level(level)
    store_trade = print_trade(trade_timing)
    store_trade_type = print_trade_type(trade_type)
    store_legs = print_legs(acct_info)
    store_market = print_sym_market(market)
    store_symbol = print_sym_market(symbol)
    store_earnings = print_earnings(earnings)
    print_deh(deh)
    print_filters(level, trade_filters, symbol, market)
    build.add_headspace()
    build.add_headspace()

    return [store_level, store_trade, store_trade_type, store_legs, store_market, store_symbol,
            store_earnings]

