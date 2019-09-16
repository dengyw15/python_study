import datetime


def wriete_file(fileoutpath, content, encode='utf-8'):
    with open(fileoutpath, 'a', encoding=encode) as targetfile:
        targetfile.seek(0, 2)
        targetfile.write(content)

# 生成路透股票测试报文
def gen_single_stk_baowen(symbol, offclcode, dsplynmll, dsplyname):
    single = '''
                <ric data_quality="Real_time">
                    <fid id="REC_STATUS">18</fid>
                    <fid id="MSG_TYPE">9</fid>
                    <fid id="RDN_EXCHD2">SHH</fid>
                    <fid id="SALTIM_MS">22192280</fid>
                    <fid id="ACVOL_UNS">53642755</fid>
                    <fid id="TRNOVR_UNS">722968119</fid>
                    <fid id="SYMBOL">''' + symbol + '''</fid>
                    <fid id="DSPLY_NAME">''' + dsplyname + '''</fid>
                    <fid id="NEWS_TIME">*</fid>
                    <fid id="PRCTCK">↓</fid>
                    <fid id="TRDPRC_1">6.490</fid>
                    <fid id="NETCHNG_1">0.080</fid>
                    <fid id="OPEN_PRC">6.390</fid>
                    <fid id="HIGH_1"> 6.500</fid>
                    <fid id="LOW_1">6.370</fid>
                    <fid id="HST_CLOSE">6.410</fid>
                    <fid id="OFFCL_CODE">''' + offclcode + '''</fid>
                    <fid id="PCTCHNG">+0.07</fid>
                    <fid id="DSPLY_NMLL">''' + dsplynmll + '''</fid>
                    <fid id="BIDSIZE">123886</fid>
                    <fid id="ASKSIZE">66400</fid>
                    <fid id="TRADE_DATE">31AUG17</fid>
                    <fid id="CURRENCY">CNY</fid>
                    <fid id="HSTCLSDATE">18JUL17</fid>
                    <fid id="BID">13.440</fid>
                    <fid id="ASK">13.450</fid>
                </ric>'''
    return single

# 生成路透债券测试报文
def gen_single_bond_baowen(symbol, offclcode, dsplynmll, dsplyname):
    single = '''
                <ric data_quality="Real_time">
                    <fid id="REC_STATUS">18</fid>
                    <fid id="MSG_TYPE">9</fid>
                    <fid id="SALTIM_MS">21207940</fid>
                    <fid id="ACVOL_UNS">626220</fid>
                    <fid id="OFFCL_CODE">''' + offclcode + '''</fid>
                    <fid id="DSPLY_NAME">''' + dsplyname + '''</fid>
                    <fid id="COUPN_RATE">4.26</fid>
                    <fid id="MATUR_DATE">31JUL21</fid>
                    <fid id="BID">102.16</fid>
                    <fid id="ASK">102.17</fid>
                    <fid id="BIDSIZE">500</fid>
                    <fid id="ASKSIZE">5032</fid>
                    <fid id="PRCTCK">↓</fid>
                    <fid id="TRDPRC_1">102.150</fid>
                    <fid id="TRDVOL_1">5</fid>
                    <fid id="HST_CLOSE">6.410</fid>
                    <fid id="HSTCLSDATE">12JUL17</fid>
                    <fid id="DSPLY_NMLL">''' + dsplynmll + '''</fid>
                    <fid id="RDN_EXCHD2">SHH</fid>
                    <fid id="CURRENCY">CNY</fid>
                    <fid id="TRADE_DATE">31AUG17</fid>
                    <fid id="PCTCHNG">+0.11</fid>
                    <fid id="OPEN_PRC">102.060</fid>
                    <fid id="HIGH_1">102.170</fid>
                    <fid id="LOW_1">102.040</fid>
                    <fid id="SYMBOL">''' + symbol + '''</fid>
                </ric>'''
    return single

def gen_stk_baowen():
    filepath = 'h:/tmp/python/gentestdata/stk_tmp.dat'
    fileoutpath = 'h:/tmp/python/gentestdata/reutersstkdata.xml'
    xmlhead = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <QuoteTemplate>
    		<ric data_quality="Real_time">
    			<fid id="REC_STATUS">0</fid>
    			<fid id="MSG_TYPE">0</fid>
    			<fid id="SYMBOL">0#ASHARES.SSh</fid>
    			<fid id="DSPLY_NAME">SSE - A SHARES</fid>
    			<fid id="DSPLY_NMLL">上海交易所A股</fid>
    			<fid id="RDN_EXCHD2">SSH</fid>
    			<fid id="CURRENCY">CNY</fid>
    		</ric>'''
    with open(filepath, 'r+') as sourcefile:
        wriete_file(fileoutpath, xmlhead)
        lines = sourcefile.readlines()
        for line in lines:
            arr = line.split('|')
            symbol = arr[0].replace('SS', 'SSh')
            offclcode = arr[1]
            dsplynmll = arr[2]
            dsplyname = arr[3]
            wriete_file(fileoutpath, gen_single_stk_baowen(symbol, offclcode, dsplynmll, dsplyname))

def gen_bond_baowen():
    filepath = 'h:/tmp/python/gentestdata/bond_tmp.dat'
    fileoutpath = 'h:/tmp/python/gentestdata/reutersbonddata.xml'
    xmlhead = '''<?xml version="1.0" encoding="UTF-8"?>
    <QuoteTemplate>
		<ric data_quality="Real_time">
			<fid id="REC_STATUS">0</fid>
			<fid id="MSG_TYPE">0</fid>
			<fid id="SYMBOL">0#CNTSY=SSh</fid>
			<fid id="DSPLY_NAME">SSE TSY BOND</fid>
			<fid id="DSPLY_NMLL">SHH</fid>
			<fid id="RDN_EXCHD2">SSH</fid>
			<fid id="CURRENCY">CNY</fid>
		</ric>'''
    with open(filepath, 'r+') as sourcefile:
        wriete_file(fileoutpath, xmlhead)
        lines = sourcefile.readlines()
        for line in lines:
            arr = line.split('|')
            symbol = arr[0].replace('SS', 'SSh')
            offclcode = arr[1]
            dsplynmll = arr[2]
            dsplyname = ''
            wriete_file(fileoutpath, gen_single_bond_baowen(symbol, offclcode, dsplynmll, dsplyname))


def getdate(days=0):
    return datetime.date.today() + datetime.timedelta(days)


def gen_frx_his_data():
    filepath = 'h:/tmp/python/gentestdata/frx_his.dat'
    with open(filepath, 'r+', encoding='utf-8') as sourcefile:
        content = sourcefile.read()
        for i in range(0, 30):
            date = str(getdate(i))
            replacedate = content.split('|')[2]
            content = content.replace(replacedate, date)
            wriete_file(filepath, content)


if __name__ == '__main__':
    # gen_bond_baowen()
    # gen_stk_baowen()
    gen_frx_his_data()


