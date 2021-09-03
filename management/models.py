from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DateField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField


class Employee(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)


class Customer(models.Model):
    level = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    contract_people = models.CharField(max_length=100)
    contract_tel = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    pay_way = models.IntegerField(default=0)
    discount_package = models.IntegerField(default=0)
    responsable_person = ForeignKey(Employee, on_delete=CASCADE)
    recent_contract_time = DateField("最近联系")
    recent_deal_time = DateField("最近交易")
    comment = CharField("备注", max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    texture = models.CharField(max_length=50)
    size = models.CharField(max_length=200)
    price = models.IntegerField(default=0)


class Item(models.Model):
    number = IntegerField("序号")
    price_type = IntegerField()
    picture = CharField(max_length=200)
    project_type = CharField("项目类型", max_length=10)
    content = CharField(max_length=200)
    texture = CharField(max_length=100)
    width = IntegerField()
    high = IntegerField()
    requirment = CharField(max_length=200)
    count = IntegerField()
    unit = CharField(max_length=10)
    money = IntegerField()
    outside = BooleanField()
    need_install = BooleanField()
    need_deliver = BooleanField()
    need_design = BooleanField()
    area = FloatField()


class Order(models.Model):
    source = CharField(max_length=20)
    department = CharField(max_length=20)
    salesman = CharField(max_length=20)
    follow_man = CharField(max_length=20)
    install_requirement = CharField("安装要求", max_length=500)
    deliver_requirement = CharField("提货要求", max_length=500)
    deliver_date = DateField("交货日期")
    deliver_address = CharField("送货地址", max_length=500)
    total_fee = IntegerField("合计金额")
    tax_fee = IntegerField("税费", default=0)
    discount_fee = IntegerField("优惠金额", default=0)
    order_fee = IntegerField("订单金额")
    pre_pay_fee = IntegerField("预付款")
    pay_way = IntegerField("支付方式")
    input_account = IntegerField("收款账户")
    completed_time = DateField("结账日期")
    design_type = IntegerField("设计类型")
    design_person = CharField(max_length=20)
    order_type = IntegerField("单据类型")
    comment = CharField("备注", max_length=500)
    items = ManyToManyField(Item)
