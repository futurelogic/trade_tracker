#!/usr/local/bin/python3

import build
import datetime


# Ask the user for trade level / experience
def get_level():
    build.add_headspace()
    header = "Trading Level"
    border = "=" * len(header)
    print(header)
    print(border)
    level = None
    while level == None:
        print("What level are you trading at?\n")
        print("1. S1")
        print("2. S2")
        print("3. S3")
        print("4. RTP")
        print()
        level = str(input("")).strip()
        if level == "1":
            return "S1"
        elif level == "2":
            return "S2"
        elif level == "3":
            return "S3"
        elif level == "4":
            return "RTP"
        else:
            header = "* Input not recognized, please select [1], [2], [3], or [4] *"
            build.build_header(header)
            level = None


def tdo(type):
    build.add_headspace()
    header = "Calendar Date"
    border = "=" * len(header)
    print(header)
    print(border)
    date = None
    while date == None:
        try:
            date = input("What date did you {} the trade [YYYY-MM-DD]?\n".format(type)).strip()
            print()
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return date
        except ValueError:
            header = "* Incorrect data format, should be [YYYY-MM-DD] *"
            build.build_header(header)
            date = None


def get_trade_type():
    build.add_headspace()
    header = "Trade Type"
    border = "=" * len(header)
    print(header)
    print(border)
    trade_type = None
    while trade_type == None:
        trade_type = input("Is this a [c]all or [p]ut trade? ").strip().lower()
        if trade_type == "":
            header = "* Input was blank, please enter [c] or [p] *"
            build.build_header(header)
            trade_type = None
        elif trade_type == "c" or trade_type == "p":
            if trade_type == "c":
                return "call"
            elif trade_type == "p":
                return "put"
        else:
            header = "* Input not recognized, please enter [c] or [p] *"
            build.build_header(header)
            trade_type = None


def get_trade_details():
    build.add_headspace()
    open = tdo("open")
    close = None
    while close == None:
            close = input("Have you closed the trade yet, [Y] or [N]? ").strip().lower()
            print()
            if close == "":
                header = "* Input was blank, please enter [Y] or [N] *"
                build.build_header(header)
                close = None
            elif close == "y":
                close = tdo("close")
            elif close == "n":
                close = "still open"
            else:
                header = "* Your input was not recognized, please input [Y] or [N] *"
                build.build_header(header)
    return [open, close]


def get_other_details(type):
    if type == "symbol":
        print()
        date = input("What date did the symbol give SLI [YYYY-MM-DD]?\n").strip()
        print()
    elif type == "market":
        print()
        date = input("What date did the market give SLI [YYYY-MM-DD]?\n").strip()
        print()
    elif type == "current":
        print()
        date = input("What date does current earnings fall on [YYYY-MM-DD]?\n").strip()
        print()
    elif type == "previous":
        print()
        date = input("What date did previous earnings fall on [YYYY-MM-DD]?\n").strip()
        print()
    if type == "closed":
        print()
        date = input("What date did you close the trade [YYYY-MM-DD]?\n").strip()
        print()
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        header = "* Incorrect data format, should be [YYYY-MM-DD] *"
        build.build_header(header)
        date = None
    return date


# Function for Get Date
def get_date(type):
    date = None
    while date == None:
        if type == "trade":
            date = get_trade_details()
        else:
            date = get_other_details(type)
    return date


# Ask for trade open date and candle
def open_trade():
    date_type = "trade"
    trade_date = get_date(date_type)
    return trade_date


# Function for Get Candle
def get_candle(type):
    build.add_headspace()
    header = "Deciding Candle"
    border = "=" * len(header)
    print(header)
    print(border)
    candle = None
    while candle == None:
        if type == "market":
            candle = input("Which is the deciding candle on the {} ([1]st or [2]nd)? ".format(type)).strip()
            print()
        elif type == "symbol":
            candle = input("Which is the deciding candle on the {} ([1]st or [2]nd) ".format(type)).strip()
            print()

        if candle == "1":
            candle = "1st"
        elif candle == "2":
            candle = "2nd"
        else:
            header = "* Input not recognized, please input [1] or [2] *"
            build.build_header(header)
            candle = None

    return candle


def run_sli_check():
    build.add_headspace()
    header = "SLI Details"
    border = "=" * len(header)
    print(header)
    print(border)
    sli = ["Christmas Cross", "SRSI", "MACD", "Directional Movement"]
    count = 0
    check = {}
    while count < 4:
        user_input = input("Was the {} present [Y] or [N]? ".format(sli[count])).lower()
        if user_input == "y" or user_input == "n":
            check[sli[count]] = user_input
            count += 1
        else:
            build.add_headspace()
            header = "* Input not recognized, please select [Y] or [N] *"
            build.build_header(header)

    return check


# Which Market
def which_market():
    build.add_headspace()
    header = "Market Details"
    border = "=" * len(header)
    print(header)
    print(border)
    market = None
    while market == None:
        print("What market provided SLI:\n")
        print("1. $INDU")
        print("2. $COMPQ")
        print()
        market = str(input(""))

        if market == "1":
            market = "$INDU"
        elif market == "2":
            market = "$COMPQ"
        else:
            header = "* Input not recognized, please select [1] or [2] *"
            build.build_header(header)
            market = None
    return market


# Which Symbol
def which_symbol():
    build.add_headspace()
    header = "Symbol Details"
    border = "=" * len(header)
    print(header)
    print(border)
    symbol = None
    while symbol == None:
        symbol = input("Which symbol?\n").strip().capitalize()
        print()
        if symbol == "":
            header = "* Input was blank, please enter a symbol *"
            build.build_header(header)
            symbol = None
    return symbol


# Ask about earnings performance
def earnings_perf():
    perf = None
    while perf == None:
        perf = input("Did the current earnings beat the previous [Y] or [N]? ").strip().capitalize()
        print()
        if perf == "":
            header = "* Input was blank, please enter [Y] or [N] *"
            build.build_header(header)
            perf = None
        elif perf == "Y":
            return perf
        elif perf == "N":
            return perf
        else:
            header = "* Your input was not recognized, please enter [Y] or [N] *"
            build.build_header(header)
            perf = None


def get_weekly_candle():
    build.add_headspace()
    header = "Weekly Candle Call"
    border = "=" * len(header)
    print(header)
    print(border)
    weekly_candle = None
    while weekly_candle == None:
        weekly_candle = input("What color will the weekly be ([r]ed or [w]hite)? ").strip().lower()
        if weekly_candle == "":
            header = "* Input was blank, please enter [r]ed or [w]hite *"
            build.build_header(header)
            weekly_candle = None
        elif weekly_candle == "r":
            return "red"
        elif weekly_candle == "w":
            return "white"
        else:
            header = "* Your input was not recognized, please enter [r]ed or [w]hite *"
            build.build_header(header)
            weekly_candle = None

# Loop for considerations list
def get_consideration(counter, type):
    consideration_list = []
    consideration = None
    while consideration != "x":
        consideration = input("{}. ".format(counter))
        if consideration == "":
            header = "* Input was blank, please enter items for {} consideration list, or [x] to finish *".format(type)
            build.build_header(header)
            consideration = None
        else:
            consideration_list.append(consideration)
            counter += 1
    counter -= 1
    consideration_list.pop(-1)
    return [consideration_list, counter]


# Gather DEH data
def get_deh():
    build.add_headspace()
    header = "Dog, Elephant, Herd"
    border = "=" * len(header)
    print(header)
    print(border)
    deh_list = ["Dog", "Elephant", "Herd"]
    deh = {}
    counter = 0
    while counter < 3:
        data = input("Is the {} [u]p, [d]own, or [s]ideways? ".format(deh_list[0])).strip()
        if data == "":
            header = "* Input was blank, please enter [Y] or [N] *"
            build.build_header(header)
        elif data == "u":
            data = "up"
        elif data == "d":
            data = "down"
        elif data == "s":
            data = "sideways"
        if data == "up" or data == "down" or data == "sideways":
            deh[deh_list[0]] = data
            deh_list.pop(0)
            counter += 1
        else:
            header = "* Your input was not recognized, please enter [u]p, [d]own, or [s]ideways *"
            build.build_header(header)
    return deh


# Gather predictive paragraph
def get_pp():
    build.add_headspace()
    header = "Predictive Paragraph"
    border = "=" * len(header)
    print(header)
    print(border)
    counter = 0
    pp = []
    entry = None
    print("Build your predictive paragraph below. Write a sentence for each item / moving average line. "
          "Press [enter] to move to next sentence, [x] to finish predictive paragraph and move on.")
    print()
    while entry != "x":
        entry = input("{}. ".format(counter+1)).strip().lower()
        if entry == "":
            header = "* Input was blank, please enter an item for your predictive paragraph, or [x] to finish *"
            build.build_header(header)
            entry = None
        else:
            pp.append(entry)
            counter += 1
    pp.pop(-1)
    return pp


def get_leg():
    build.add_headspace()
    header = "Trading Leg Details"
    border = "=" * len(header)
    print(header)
    print(border)
    counter = 0
    entry = None
    leg_list = []
    print("Which legs are you doing the trade in ([x] to finish input of leg info)?\n")
    while entry != "x":
        entry = input("{}. ".format(counter+1))
        if entry == "":
            header = "* Input was blank, please enter name of trading leg (word 'leg' is added, " \
                     "only list account type like reward, trading, debt, etc.), or [x] to finish *"
            build.build_header(header)
            entry = None
        else:
            leg_list.append(entry)
            counter += 1
    leg_list.pop(-1)
    return leg_list


# Gather trade leg info
def get_acct_info():
    leg_info = None
    while leg_info == None:
        trade_info = input("Is this a [r]eal trade or [p]aper trade? ").strip().lower()
        if trade_info == "r":
            leg_info = get_leg()
            return leg_info
        if trade_info == "p":
            leg_info = "Paper"
            return leg_info
        else:
            build.add_headspace()
            header = "* Your input was not recognized... Please input 'r' for real or 'p' for paper *"
            build.build_header(header)
            leg_info = None


def get_which_support():
    user_input = None
    while user_input == None:
        user_input = str(input("Is your support coming from; [1]-377, [2]-Daily? ")).strip()
        if user_input == "":
            header = "Your input was blank, please select [1] for the 377 or [2] for the daily"
            build.build_header(header)
            user_input = None
        elif user_input == "1":
            return "377"
        elif user_input == "2":
            return "Daily"
        else:
            header = "* Your input was not recognized, please enter [1] for 377 or [2] for Daily *"
            build.build_header(header)
            user_input = None


def get_support_items(support_type):
    support_items = []
    user_input = None
    count = 1
    print("List the support items from the {} chart below ([x] to move on):\n".format(support_type))
    while user_input != "x":
        user_input = input("{}. ".format(count))
        if user_input == "":
            header = "Your input was blank, please enter a support item or type [x] to move on"
            build.build_header(header)
            user_input = None
        else:
            support_items.append("{}. {}".format(count, user_input))
            count += 1
    support_items.pop(-1)
    build.add_headspace()
    return support_items


def get_support():
    build.add_headspace()
    which_support = get_which_support()
    small_support = get_support_items(which_support)
    large_support = get_support_items("Weekly")
    return [small_support, large_support, which_support]

