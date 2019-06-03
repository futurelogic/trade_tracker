import get_input
import datetime
import os
import getpass
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove


def cls():
    os.system('clear')


# Add space header
def add_headspace():
    print()
    print()


# Add error header
def add_error(size):
    header = "-" * size
    return header


def build_first_head():
    header = "Stock Market Trading Document Builder"
    border = "=" * len(header)
    return [header, border]


def begin():
    cls()
    header = build_first_head()
    print(header[0])
    print(header[1])
    add_headspace()

def build_header(header):
    add_headspace()
    error_border = add_error(len(header))
    print(error_border)
    print(header)
    print(error_border)
    add_headspace()


def build_big_space():
    count = 0
    while count < 100:
        add_headspace()
        count += 1


# Ask for market
def build_sym_market(type):
    if type == "market":
        return_data = get_input.which_market()
    elif type == "symbol":
        return_data = get_input.which_symbol()
    return_date = get_input.get_date(type)
    return_candle = get_input.get_candle(type)
    return_sli = get_input.run_sli_check()
    return [return_data, return_date, return_candle, return_sli]


# Ask for next earnings date
def build_earnings():
    add_headspace()
    header = "Earnings"
    border = "=" * len(header)
    print(header)
    print(border)
    type = "current"
    current_earnings = get_input.get_date(type)
    type = "previous"
    previous_earnings = get_input.get_date(type)
    perf_data = get_input.earnings_perf()
    return [current_earnings, previous_earnings, perf_data]


def build_func(counter, matrix, type, chart, sym_or_market):
    add_headspace()
    if type == "general":
        print("List {} considerations below, or type [X] to move on".format(type))
        data_type = get_input.get_consideration(counter, type)
        matrix[type] = data_type[0]
        counter = data_type[1]
    else:
        print("List considerations for {}'s {} below, or type [X] to move on".format(sym_or_market, chart))
        data_type = get_input.get_consideration(counter, type)
        matrix[type] = data_type[0]
        counter = data_type[1]

    return [counter, matrix]


def build_deh():
    deh = get_input.get_deh()
    return deh


# Build considerations list
def build_considerations(symbol, market, count):
    matrix = {}
    general = build_func(count, matrix, "general", "", "")
    sym_233 = build_func(general[0], general[1], "symbol_233", "233", symbol)
    sym_daily = build_func(sym_233[0], sym_233[1], "symbol_daily", "Daily", symbol)
    sym_weekly = build_func(sym_daily[0], sym_daily[1], "symbol_weekly", "Weekly", symbol)
    sym_monthly = build_func(sym_weekly[0], sym_weekly[1], "symbol_monthly", "Monthly", symbol)
    sym_quarterly = build_func(sym_monthly[0], sym_monthly[1], "symbol_quarterly", "Quarterly", symbol)

    market_233 = build_func(sym_quarterly[0], sym_quarterly[1], "market_233", "233", market)
    market_daily = build_func(market_233[0], market_233[1], "market_daily", "Daily", market)
    market_weekly = build_func(market_daily[0], market_daily[1], "market_weekly", "Weekly", market)

    vix_233 = build_func(market_weekly[0], market_weekly[1], "vix_233", "233", "$VIX")
    vix_daily = build_func(vix_233[0], vix_233[1], "vix_daily", "Daily", "$VIX")
    vix_weekly = build_func(vix_daily[0], vix_daily[1], "vix_weekly", "Weekly", "$VIX")

    vxn_233 = build_func(vix_weekly[0], vix_weekly[1], "vxn_233", "233", "$VXN")
    vxn_daily = build_func(vxn_233[0], vxn_233[1], "vxn_daily", "Daily", "$VXN")
    vxn_weekly = build_func(vxn_daily[0], vxn_daily[1], "vxn_weekly", "Weekly", "$VXN")

    spx_233 = build_func(vxn_weekly[0], vxn_weekly[1], "spx_233", "233", "$SPX")
    spx_daily = build_func(spx_233[0], spx_233[1], "spx_daily", "Daily", "$SPX")
    spx_weekly = build_func(spx_daily[0], spx_daily[1], "spx_weekly", "Weekly", "$SPX")

    w5k_233 = build_func(spx_weekly[0], spx_weekly[1], "w5k_233", "233", "$W5000")
    w5k_daily = build_func(w5k_233[0], w5k_233[1], "w5k_daily", "Daily", "$W5000")
    w5k_weekly = build_func(w5k_daily[0], w5k_daily[1], "w5k_weekly", "Weekly", "$W5000")

    return w5k_weekly[1]


def run_level_test(level, market, symbol):
    if level == "S1":
        weekly_candle = None
        pp = None
        considerations = None
        return [weekly_candle, pp, considerations]
    elif level == "S2":
        weekly_candle = get_input.get_weekly_candle()
        pp = None
        considerations = None
        return [weekly_candle, pp, considerations]
    elif level == "S3":
        weekly_candle = get_input.get_weekly_candle()
        pp = get_input.get_pp()
        considerations = None
        return [weekly_candle, pp, considerations]
    elif level == "RTP":
        count = 1
        weekly_candle = get_input.get_weekly_candle()
        pp = get_input.get_pp()
        considerations = build_considerations(symbol[0], market[0], count)
        return [weekly_candle, pp, considerations]


def get_user():
    user = getpass.getuser()
    return user


def get_date():
    date = datetime.datetime.now()
    return date


def file_path(user, date):
    path = "/Users/"
    file = "_trade_doc.txt"
    file = str(date)+"_"+file
    complete = os.path.join(path, user, file)
    return complete


def date_sort(date):
    year = date.year
    if date.month < 10:
        month = "0{}".format(date.month)
    else:
        month = date.month
    if date.day < 10:
        day = "0{}".format(date.day)
    else:
        day = date.day
    if date.hour < 10:
        hour = "0{}".format(date.hour)
    else:
        hour = date.hour
    if date.minute < 10:
        minute = "0{}".format(date.minute)
    else:
        minute = date.minute
    return [year, month, day, hour, minute]

def build_path(user, date):
    path = file_path(user, str(date))
    return path


def build_edit_path(file, home):
    path = os.path.join(home, file)
    return path


def build_date():
    date = get_date()
    date = date_sort(date)
    date = "{}-{}-{}_{}:{}".format(date[0], date[1], date[2], date[3], date[4])
    return date


def replace(path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    #Search for string, replace
    with fdopen(fh,'w') as new_file:
        with open(path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Remove original file
    remove(path)
    #Store modified contents
    move(abs_path, path)
    #Print new output
    os.system('more {}'.format(path))
