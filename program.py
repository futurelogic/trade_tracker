import get_input
import output
import build
import storage
import help
import sys
from os import system


def main():
    try:
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
            earnings = build.build_earnings()
            trade_timing = get_input.open_trade()
            trade_type = get_input.get_trade_type()
            acct_info = get_input.get_acct_info()
            deh = build.build_deh()
            trade_filters = build.run_level_test(level, market, symbol)
            store = output.print_results(level, market, symbol, earnings, trade_timing, trade_type,
                                         acct_info, deh, trade_filters)
            storage.write_data(store)
    except:
        output.cls()
        print(help.no_flag)
        build.add_headspace()
        build.add_headspace()


if __name__ == "__main__":
    main()
