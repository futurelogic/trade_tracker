import get_input
import output
import build
import storage
import sys
from os import system


def main():


    try:
        if sys.argv[1] == "-h":
            output.cls()
            build.build_big_space()
            system('more help.txt')
        elif sys.argv[1] == "-p":
            output.cls()
            system('more example.txt')
        elif sys.argv[1] == "-n":
            build.begin()
            level = get_input.get_level()
            market = build.build_sym_market("market")
            symbol = build.build_sym_market("symbol")
            support = get_input.get_support()
            print(support)
            earnings = build.build_earnings()
            trade_timing = get_input.open_trade()
            trade_type = get_input.get_trade_type()
            acct_info = get_input.get_acct_info()
            deh = build.build_deh()
            trade_filters = build.run_level_test(level, market, symbol)
            storage.write_results(level, market, symbol, support, earnings, trade_timing,
                                  trade_type, acct_info, deh, trade_filters)

    except:
        output.cls()
        system('cat no_flag.txt')
        build.add_headspace()
        build.add_headspace()
    '''

    if sys.argv[1] == "-h":
        output.cls()
        build.build_big_space()
        system('more help.txt')
    elif sys.argv[1] == "-e":
        output.cls()
        system('more example.txt')
    elif sys.argv[1] == "-n":
        build.begin()
        level = get_input.get_level()
        market = build.build_sym_market("market")
        symbol = build.build_sym_market("symbol")
        support = get_input.get_support()
        print(support)
        earnings = build.build_earnings()
        trade_timing = get_input.open_trade()
        trade_type = get_input.get_trade_type()
        acct_info = get_input.get_acct_info()
        deh = build.build_deh()
        trade_filters = build.run_level_test(level, market, symbol)
        storage.write_results(level, market, symbol, support, earnings, trade_timing,
                              trade_type, acct_info, deh, trade_filters)
    '''


if __name__ == "__main__":
    main()

