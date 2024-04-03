from binance import Client, BinanceSocketManager
import numpy

import asyncio

import datetime

from datetime import datetime
from datetime import timedelta
import time
client = Client()

list_crypto = [

    '1INCH',
    'AAVE',
    'ACA',
    'ACH',
    'ACM',
    'ADA',
    'ADX',
    'AGLD',
    'AION',
    'AKRO',
    'ALCX',
    'ALGO',
    'ALICE',
    'ALPACA',
    'ALPHA',
    'ALPINE',
    'AMP',
    'ANC',
    'ANKT',
    'ANT',
    'APE',
    'API3',
    'ARPA',
    'AR',
    'ASTR',
    'ATA',
    'ATM',
    'ATOM',
    'AUCTION',
    'AUDIO',
    'AUD',
    'AUTO',
    'AVA',
    'AVAX',
    'AXS',
    'BADGER',
    'BAKE',
    'BAL',
    'BAND',
    'BAR',
    'BAT',
    'BCH',
    'BEAM',
    'BEL',
    'BETA',
    'BICO',
    'BIFI',
    'BLZ',
    'BNT',
    'BNX',
    'BOND',
    'BSW',
    'BTCST',
    'BTG',
    'BTS',
    'BTTC',
    'BURGER',
    'C98',
    'CAKE',
    'CELO',
    'CELR',
    'CFX',
    'CHESS',
    'CHR',
    'CHZ',
    'CITY',
    'CKB',
    'CLV',
    'COCOS',
    'COMP',
    'COS',
    'COTI',
    'CRV',
    'CTK',
    'CTSI',
    'CTXS',
    'CVC',
    'CVP',
    'CVX',
    'DAR',
    'DASH',
    'DATA',
    'DCR',
    'DEGO',
    'DENT',
    'DEXE',
    'DF',
    'DGB',
    'DIA',
    'DNT',
    'DOCK',
    'DODO',
    'DOGE',
    'DOT',
    'DREP',
    'DUSK',
    'DYDX',
    'EGLD',
    'ELF',
    'ENJ',
    'ENS',
    'EOS',
    'EPX',
    'ERN',
    'ETC',
    'EUR',
    'FARM',
    'FET',
    'FIDA',
    'FIL',
    'FIO',
    'FIRO',
    'FIS',
    'FLM',
    'FLOW',
    'FLUX',
    'FORTH',
    'FOR',
    'FRONT',
    'FTM',
    'FTT',
    'FUN',
    'FXS',
    'GALA',
    'GAL',
    'GBP',
    'GHST',
    'GLMR',
    'GMT',
    'GNO',
    'GRT',
    'GTC',
    'GTO',
    'HARD',
    'HBAR',
    'HIGH',
    'HIVE',
    'HNT',
    'HOT',
    'ICP',
    'ICS',
    'IDEX',
    'ILV',
    'IMX',
    'INJ',
    'IOST',
    'IOTA',
    'IOTX',
    'IRIS',
    'JASMY',
    'JOE',
    'JST',
    'JUV',
    'KAVA',
    'KDA',
    'KEY',
    'KLAY',
    'KMD',
    'KNS',
    'KP3R',
    'KSM',
    'LAZIO',
    'LDO',
    'LEVER',
    'LINA',
    'LINK',
    'LIT',
    'LOKA',
    'LPT',
    'LRC',
    'LSK',
    'LTC',
    'LTO',
    'LUNA',
    'MANA',
    'MASK',
    'MATIC',
    'MBL',
    'MBOX',
    'MC',
    'MDT',
    'MDX',
    'MFT',
    'MINA',
    'MIR',
    'MITH',
    'MKR',
    'MLN',
    'MOB',
    'MOVR',
    'MTL',
    'MULTI',
    'NBS',
    'NEAR',
    'NEO',
    'NEXO',
    'NKN',
    'NMR',
    'NULS',
    'OCEAN',
    'OGN',
    'OG',
    'OMG',
    'OM',
    'ONE',
    'ONG',
    'ONT',
    'OOKI',
    'OP',
    'ORN',
    'OXT',
    'PAXG',
    'PEOPLE',
    'PERL',
    'PERP',
    'PHA',
    'PLA',
    'PNT',
    'POLS',
    'POLY',
    'POND',
    'PORTO',
    'POWR',
    'PSG',
    'PUNDIX',
    'PYR',
    'QI',
    'QNT',
    'QTUM',
    'QUICK',
    'RAD',
    'RARE',
    'RAY',
    'REEF',
    'REI',
    'REN',
    'REP',
    'REQ',
    'RIF',
    'RLC',
    'RNDR',
    'ROSE',
    'RSR',
    'RUNE',
    'RVN',
    'SAND',
    'SANTOS',
    'SCRT',
    'SC',
    'SFP',
    'SHIB',
    'SKL',
    'SLP',
    'SNX',
    'SOL',
    'SPELL',
    'SRM',
    'STEEM',
    'STMX',
    'STORJ',
    'STPT',
    'STRAX',
    'STX',
    'SUN',
    'SUPER',
    'SUSHI',
    'SXP',
    'SYS',
    'TCT',
    'TFUEL',
    'THETA',
    'TKO',
    'TLM',
    'TOMO',
    'TORN',
    'TRB',
    'TRIBE',
    'TROY',
    'TRU',
    'TRX',
    'T',
    'TUSD',
    'TVK',
    'TWT',
    'UMA',
    'UNFI',
    'UNI',
    'USDC',
    'USDP',
    'UTK',
    'VET',
    'VGX',
    'VIDT',
    'VITE',
    'VOXEL',
    'VTHO',
    'WAN',
    'WAVES',
    'WAXP',
    'WING',
    'WIN',
    'WNXM',
    'WOO',
    'WRX',
    'WTC',
    'XEC',
    'XEM',
    'XLM',
    'XMR',
    'XNO',
    'XRP',
    'XTZ',
    'XVG',
    'XVS',
    'YFII',
    'YFI',
    'YGG',
    'ZEC',
    'ZEN',
    'ZIL',
    'ZRX',
]
converted_coins = ['BTC']
stable_coins = ['USDT']


class ArbiScaner:

    bal = 1000
    time_vol = 10
    fixed_profit = 0.01
    coin_to_stablecoin = {}
    list_profit = []
    i = 0
    infinity = 1
    bal_in_pull = 800
    list_crypto_random = []
    requests = 0
    requests_lim = 1200
    time_nows = ''
    time_thens = ''

    def set_ball_in_pull(self, bal_in_pull):
        self.bal_in_pull = bal_in_pull

    def get_bal_in_pull(self):
        return self.bal_in_pull

    def set_infinity(self, infinity):
        self.infinity = infinity

    def get_infinity(self):
        return self.infinity

    def set_bal(self, bal):
        self.bal = bal

    def get_bal(self):
        return self.bal

    def set_time_vol(self, time_vol):
        self.time_vol = time_vol

    def get_time_vol(self):
        return self.time_vol

    def set_fixed_profit(self, fixed_profit):
        self.fixed_profit = fixed_profit

    def get_fixed_profit(self):
        return self.fixed_profit


    def calculate_liquidity(self, coin1, coin2, t):
        symbol = '' + coin1 + coin2
        zero = 0

        time_now = datetime.now()
        time_then = (datetime.now() - timedelta(minutes=t))
        dt1 = datetime.timestamp(time_then)
        dt2 = datetime.timestamp(time_now)
        try:
            info = client.get_aggregate_trades(symbol=symbol, startTime=int(dt1 * 1000), endTime=int(dt2 * 1000))
        except:
            return zero, 'zero!'
        quantity = []
        val_usd = 0.0

        for i in info:
            quantity.append(float(i['q']))
        price_in_usd = self.swap_coins(coin1, 'USDT', 'asks')
        try:
            val_usd = sum(quantity) * float(price_in_usd)
        except:
            val_usd = 0.0
        val_usd = round(val_usd, 2)
        if len(quantity) > 0 and val_usd > self.bal_in_pull:
            print('liquidity of pair {0}/{1}: Val of orders = {2}; volume of {3} = {4} ~ {5}$ '.format(coin1, coin2,
                                                                                                len(quantity), coin1,
                                                                                                sum(quantity), val_usd))
            return len(quantity), 'liquidity of pair {0}/{1}: Val of orders = {2}; volume of {3} = {4} ~ {5}$ '.format(
                coin1, coin2, len(quantity), coin1, sum(quantity), val_usd) + '\n\n'
        else:
            return zero, 'zero!'

    def print_info(self, first_coin, second_coin, price, bal_after_swap):
        print('{0}/{1} price:'.format(first_coin, second_coin))
        print('{0:.10f}'.format(float(price)))
        print('Balance after swap = {0} {1}'.format(str(bal_after_swap), second_coin))

    def profit_percent(self, balence):
        tmp = balence - self.bal
        bal_percent = (tmp * 100) / self.bal
        if bal_percent > self.fixed_profit:
            return True
        else:
            False

    def swap_coins(self, coin1, coin2, str):
        symbol = '' + coin1 + coin2

        try:
            ticker = client.get_order_book(symbol=symbol)
        except:
            return 0
        if str == 'bids':
            try:
                return ticker['bids'][0][0]
            except:
                return 0

        elif str == 'asks':
            try:
                return ticker['asks'][0][0]
            except:
                return 0


    def get_volume(self, coin1, coin2, str):
        symbol = '' + coin1 + coin2

        try:
            ticker = client.get_order_book(symbol=symbol)
        except:
            return 0
        if str == 'bids':
            try:
                return ticker['bids'][0][1]
            except:
                return 0

        elif str == 'asks':
            try:
                return ticker['asks'][0][1]
            except:
                return 0

# named_tuple = time.localtime()  # get struct_time
# print("start work:", time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple))

    def print_prices(self, coin1, coin2, msg):
        symbol = '' + coin1 + coin2
        try:
            ticker = client.get_order_book(symbol=symbol)
        except:
            return 0

        price = ticker
        price_usd = float(self.swap_coins(coin1, 'USDT', 'bids'))

        volume = float(ticker['asks'][0][1])
        volume = volume * price_usd
        volume = str('{0:.2f}'.format(float(volume)))
        print('{0} price: {1}{2} = {3} | {4} Vol $'.format('asks', coin1, coin2, price['asks'][0][0], volume))
        msg = msg + '{0} price: {1}{2} = {3} | {4} Vol $'.format('asks', coin1, coin2, price['asks'][0][0], volume) + '\n'

        volume = float(ticker['bids'][0][1])
        volume = volume * price_usd
        volume = str('{0:.2f}'.format(float(volume)))
        print('{0} price: {1}{2} = {3} | {4} Vol $'.format('bids', coin1, coin2, price['bids'][0][0], volume))
        return msg + '{0} price: {1}{2} = {3} | {4} Vol $'.format('bids', coin1, coin2, price['bids'][0][0], volume) + '\n'

    def get_settings(self):
        return 'Scaner work with this parameters: \nperiod to calculate volume = {0} min;\nfixed profit > {1}%\nbalance in pull > {2}'.format(
            self.time_vol, self.fixed_profit, self.bal_in_pull) + '\n'

    def random_list(self):
        a = numpy.arange(len(list_crypto))
        numpy.random.shuffle(a)
        for i in a:
            self.list_crypto_random.append(list_crypto[a[i]])

    def start_work(self, bot, id, infinity):
        self.infinity = infinity
        self.requests = 0
        bot.send_message(id, self.get_settings())

        while self.infinity != 0:
            self.random_list()
            for coin in converted_coins:
                if self.infinity == 0:
                    break
                for stable_coin in stable_coins:
                    if self.infinity == 0:
                        break
                    price = self.swap_coins(coin, stable_coin, 'asks')

                    try:
                        val_of_swap = self.bal / float(price)
                    except:
                        val_of_swap = 0.0
                    for coin2 in self.list_crypto_random:
                        if self.infinity == 0:
                            break
                        price2 = self.swap_coins(coin2, coin, 'asks')
                        try:
                            val_of_swap2 = val_of_swap / float(price2)
                        except:
                            val_of_swap2 = 0
                        price3 = self.swap_coins(coin2, stable_coin, 'asks')
                        val_of_swap3 = val_of_swap2 * float(price3)

                        if self.profit_percent(val_of_swap3) == True:

                            nonzero1, info1 = self.calculate_liquidity(coin, stable_coin, self.time_vol)
                            nonzero2, info2 = self.calculate_liquidity(coin2, coin, self.time_vol)
                            nonzero3, info3 = self.calculate_liquidity(coin2, stable_coin, self.time_vol)

                            if nonzero1 and nonzero2 and nonzero3 != 0:
                                print('**************************************************************************')
                                msg = ''
                                named_tuple = time.localtime()  # get struct_time
                                print("time: ", time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple))
                                msg = msg + "time: " + time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple) + '\n\n'

                                msg = self.print_prices(coin, stable_coin, msg)
                                msg = msg + info1
                                # ii, msg = self.calculate_liquidity(coin, 'USDT', self.time_vol, msg)

                                msg = self.print_prices(coin2, coin, msg)
                                msg = msg + info2
                                # ii, msg = self.calculate_liquidity(coin, convert_coin, self.time_vol, msg)

                                msg = self.print_prices(coin2, stable_coin, msg)
                                msg = msg + info3
                                # ii, msg = self.calculate_liquidity(convert_coin, 'USDT', self.time_vol, msg)

                                print('Profit with bal 1000$ = {0}$'.format((val_of_swap3 - 1000)))
                                msg = msg + 'Profit with bal 1000$ = {0}$'.format((val_of_swap3 - 1000))

                                bot.send_message(id, msg)

                                print('**************************************************************************')
                                print()

                            self.list_profit.append(val_of_swap3 - self.bal)
                    print(self.i)
                    self.i = self.i + 1

        print("stopped!")





