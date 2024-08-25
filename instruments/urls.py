from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    stock_views, bond_views, deposit_views, treasury_bill_views,
    call_account_views, premium_views, fund_views
)

router = DefaultRouter()

# Stock routes
router.register(r'sectors', stock_views.SectorViewSet)
router.register(r'subsectors', stock_views.SubSectorViewSet)
router.register(r'stock-exchanges', stock_views.StockExchangeViewSet)
router.register(r'stocks', stock_views.StockViewSet)
router.register(r'stock-issues', stock_views.StockIssueViewSet)
router.register(r'stock-trades', stock_views.StockTradeViewSet)

# Bond routes
router.register(r'bond-types', bond_views.BondTypeViewSet)
router.register(r'bonds', bond_views.BondViewSet)
router.register(r'bond-coupons', bond_views.BondCouponViewSet)
router.register(r'bond-trades', bond_views.BondTradeViewSet)

# Deposit routes
router.register(r'deposits', deposit_views.DepositViewSet)
router.register(r'deposit-transactions', deposit_views.DepositTransactionViewSet)

# Treasury Bill routes
router.register(r'treasury-bills', treasury_bill_views.TreasuryBillViewSet)
router.register(r'treasury-bill-trades', treasury_bill_views.TreasuryBillTradeViewSet)

# Call Account routes
router.register(r'call-accounts', call_account_views.CallAccountViewSet)
router.register(r'call-account-transactions', call_account_views.CallAccountTransactionViewSet)

# Premium routes
router.register(r'premiums', premium_views.PremiumViewSet)
router.register(r'premium-transactions', premium_views.PremiumTransactionViewSet)

# Fund routes
router.register(r'fund-types', fund_views.FundTypeViewSet)
router.register(r'funds', fund_views.FundViewSet)
router.register(r'fund-transactions', fund_views.FundTransactionViewSet)
router.register(r'fund-dividends', fund_views.FundDividendViewSet)

urlpatterns = [
    path('', include(router.urls)),
]