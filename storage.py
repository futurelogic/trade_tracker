import build
import output
from pathlib import Path
from os import system

def write(path, data):
    with open(path, "a") as fout:
        fout.write(str(data)+"\n")

def get_path():
    user = build.get_user()
    date = build.build_date()
    path = build.build_path(user, date)
    Path(path).touch()
    return path


def write_header(path):
    header = "Stock Market Trading Document Builder"
    border = "=" * len(header)
    write(path, header)
    write(path, border)
    write_space(path)


def write_space(path):
    write(path, "")


def write_level(level, path):
    w_level = "Trading level: {}".format(level)
    write(path, w_level)


def write_trade(trade_timing, path):
    w_trade = []
    w_trade.append("Trade opened: {}".format(trade_timing[0]))
    write(path, w_trade[0])
    if trade_timing[1] == "still open":
        w_trade.append(("Trade closed: Trade still open"))
        write(path, w_trade[1])
    else:
        w_trade.append("Trade closed: {}".format(trade_timing[1]))
        write(path, w_trade[1])


def write_trade_type(trade_type, path):
    trade_type = "Trade type: {}".format(trade_type)
    write(path, trade_type)
    write_space(path)
    write_space(path)


def write_support(support, path):
    header = "{} support items".format(support[2])
    border = "=" * len(header)
    write(path, header)
    write(path, border)
    for line in support[0]:
        write(path, line)
    write_space(path)
    write_space(path)
    header = "Weekly support items"
    border = "=" * len(header)
    write(path, header)
    write(path, border)
    for line in support[1]:
        write(path, line)
    write_space(path)
    write_space(path)


def write_legs(acct_info, path):
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
        write(path, line)
    write_space(path)
    write_space(path)


def write_sym_market(type, path):
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
        write(path, line)
    write_space(path)
    write_space(path)


def write_earnings(earnings, path):
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
        write(path, line)
    write_space(path)
    write_space(path)


def write_deh(deh, path):
    build.add_headspace()
    header = "Dog, Elephant, Herd"
    border = "=" * len(header)
    write(path, header)
    write(path, border)
    count = 1
    for item in deh:
        write(path, ("{}. {} is {}".format(count, item, deh[item])))
        count += 1
    write_space(path)
    write_space(path)


def write_weekly_candle(weekly_candle, path):
    build.add_headspace()
    header = "Weekly Candle"
    border = "=" * len(header)

    write(path, header)
    write(path, border)
    write(path, ("The color of the weekly candle will be {}".format(weekly_candle)))
    write_space(path)
    write_space(path)


def write_pp(pp, path):
    build.add_headspace()
    count = 1
    header = "Predictive paragraph"
    border = "=" * len(header)
    write(path, header)
    write(path, border)
    if not pp:
        write(path, "None")
    else:
        for item in pp:
            write(path, "{}. {}".format(count, item))
            count +=1
    write_space(path)
    write_space(path)


def write_cons(considerations, symbol_or_market, chart, cons_type, count, path):
    build.add_headspace()
    if symbol_or_market == "General":
        header = ("{}: ".format(symbol_or_market, chart))
    else:
        header = ("{} {}: ".format(symbol_or_market, chart))
    border = "=" * len(header)
    write(path, header)
    write(path, border)
    for item in considerations[cons_type]:
        write(path, "{}. {}".format(count, item))
        count += 1
    write_space(path)
    write_space(path)
    return count


def write_considerations(considerations, symbol, market, path):
    count = 1
    count = write_cons(considerations, "General", "", "general", count, path)

    count = write_cons(considerations, symbol, "233", "symbol_233", count, path)
    count = write_cons(considerations, symbol, "Daily", "symbol_daily", count, path)
    count = write_cons(considerations, symbol, "Weekly", "symbol_weekly", count, path)
    count = write_cons(considerations, symbol, "Monthly", "symbol_monthly", count, path)
    count = write_cons(considerations, symbol, "Quarterly", "symbol_quarterly", count, path)

    count = write_cons(considerations, market, "233", "market_233", count, path)
    count = write_cons(considerations, market, "Daily", "market_daily", count, path)
    count = write_cons(considerations, market, "Weekly", "market_weekly", count, path)

    count = write_cons(considerations, "$VIX", "233", "vix_233", count, path)
    count = write_cons(considerations, "$VIX", "Daily", "vix_daily", count, path)
    count = write_cons(considerations, "$VIX", "Weekly", "vix_weekly", count, path)

    count = write_cons(considerations, "$VXN", "233", "vxn_233", count, path)
    count = write_cons(considerations, "$VXN", "Daily", "vxn_daily", count, path)
    count = write_cons(considerations, "$VXN", "Weekly", "vxn_weekly", count, path)

    count = write_cons(considerations, "$SPX", "233", "spx_233", count, path)
    count = write_cons(considerations, "$SPX", "Daily", "spx_daily", count, path)
    count = write_cons(considerations, "$SPX", "Weekly", "spx_weekly", count, path)

    count = write_cons(considerations, "$W5000", "233", "w5k_233", count, path)
    count = write_cons(considerations, "$W5000", "Daily", "w5k_daily", count, path)
    write_cons(considerations, "$W5000", "Weekly", "w5k_weekly", count, path)



def write_filters(level, trade_filters, symbol, market, path):
    filters = []
    if level == "S2" or level == "S3" or level == "RTP":
        write_weekly_candle(trade_filters[0], path)
        filters.append(trade_filters[0])
    if level == "S3" or level == "RTP":
        write_pp(trade_filters[1], path)
        filters.append(trade_filters[1])
    if level == "RTP":
        write_considerations(trade_filters[2], symbol[0], market[0], path)
        filters.append(trade_filters[2])
    write_space(path)
    write_space(path)


def print_pre_output(path):
    pre_output = '''
    * The results are listed below *
    * The results have been stored in the following file *
    * {} *
    * Press the <SPACE BAR> to scroll through the trade *
    * Press <ENTER> to continue *
    '''.format(path)
    user_input = None
    while user_input == None:
        print(pre_output)
        user_input = input("")
    print(pre_output)


def print_file(path):
    system('more {}'.format(path))



def write_results(level, market, symbol, support, earnings, trade_timing, trade_type, acct_info, deh, trade_filters):
    path = get_path()
    write_header(path)
    write_space(path)
    write_level(level, path)
    write_trade(trade_timing, path)
    write_trade_type(trade_type, path)
    write_sym_market(market, path)
    write_sym_market(symbol, path)
    write_support(support, path)
    write_earnings(earnings, path)
    write_deh(deh, path)
    write_legs(acct_info, path)
    write_filters(level, trade_filters, symbol, market, path)
    output.cls()
    build.build_big_space()
    print_pre_output(path)
    print_file(path)

