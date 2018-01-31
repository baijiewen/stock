from django.shortcuts import render
import tushare as ts
import pandas
import numpy as np
# Create your views here.

def get_average_price(stock, date):
    pass

def get_volume_most(stock, date):
    pass


class StockCrawler(object):
    '''
    爬取股票信息，价格，均线，成交量等
    '''
    aa = ts.get_hist_data('601880')
    np.array(aa)


class PricePredicted(object):
    '''
    根据历史数据做数据建模，对不同行业不同周期提取模型，
    建立线性模型，分析某只股票是否符合线性关系
    '''

class CollectorStockMsg(object):
    '''
    收集股票有关新闻消息，对新闻提取词语打标记，
    有监督学习，加权算对股票价格影响
    '''

class ChooseStock(object):
    '''
    条件选股
    '''


class TradingStraegy(object):
    '''
    交易策略，低频交易策略，中度频率策略，高频交易策略
    大资金交易策略，小资金交易策略
    '''
    pass

class User(object):
    '''
    用户名，资金量，风险偏好（制定相应投资策略），持有周期，等等
    '''

    def __init__(self, name, money, risk, holding):
        self.name = name
        self.money = money
        self.risk = risk
        self.holding_time = holding
