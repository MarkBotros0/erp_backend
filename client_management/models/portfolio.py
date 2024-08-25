from django.db import models

from client_management.enums import PortfolioRenewalMethod, AccruedType, FundingType, PortfolioManagementType, \
    PortfolioWeightType
from common.enums.currency import Currency
from common.models import TimestampsAbstractModel


class Portfolio(TimestampsAbstractModel):
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    activation_date = models.DateField()
    renewal_duration = models.IntegerField()
    renewal_method = models.CharField(max_length=20, choices=PortfolioRenewalMethod.get_choices())
    currency = models.CharField(max_length=10, choices=Currency.get_choices())
    manager = models.CharField(max_length=255)
    investment_type = models.ForeignKey("InvestmentType", on_delete=models.PROTECT)
    profile_stock = models.ForeignKey("PortfolioStock", on_delete=models.PROTECT)
    accrued_type = models.CharField(max_length=50, choices=AccruedType.get_choices())
    base_value = models.DecimalField(max_digits=20, decimal_places=2)
    value_paid = models.DecimalField(max_digits=20, decimal_places=2)
    benchmark = models.CharField(max_length=255)
    frequency_closed = models.CharField(max_length=50)
    next_close_date = models.DateField()
    type_weight = models.CharField(max_length=50, choices=PortfolioWeightType.get_choices())
    fixed_fees_fist = models.BooleanField()
    avr_to_market = models.BooleanField()
    calc_daily_with_holiday = models.BooleanField()
    funding_type = models.CharField(max_length=50, choices=FundingType.get_choices())
    portfolio_management_type = models.CharField(max_length=50,
                                                 choices=PortfolioManagementType.get_choices())
    main_portfolio = models.ForeignKey("Portfolio", on_delete=models.SET_NULL, null=True, blank=True)
    included_in_main = models.BooleanField()
    notes = models.TextField(blank=True)
    bank_branch = models.ForeignKey("BankBranch", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.client}/{self.id}"
