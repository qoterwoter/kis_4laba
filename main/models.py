from django.db import models
from django.contrib.auth.models import User
STATUS_CHOICE = (
    ('Привелигированный','Привелигированный'),
    ('Обычный','Обычный'),
    ('VIP','VIP')
)
NUMBERS_CHOICE = (
    ('Стандарт','Стандарт'),
    ('Делюкс','Делюкс'),
)
EAT_CHOICE = (
    ('RO','RO'),
    ('EP','EP'),
    ('BB','BB'),
    ('H','H'),
)
SEX_CHOICE = (
    ('м',"Мужской"),
    ('ж',"Женский")
)
POSITION_CHOICE = (
    ('Бухгалтер','Бухгалтер'),
    ('Администратор','Администратор'),
    ('Менеджер','Менеджер')
)
HOTEL_CHOICE = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('a','Апартаменты'),
)

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField('Страна',max_length=255)
    class Meta:
        verbose_name = ('Страна')
        verbose_name_plural = ('Страны')
    def __str__(self):
        return(self.country)
    
class City(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField('Город',max_length=255)
    country = models.ForeignKey(Country, related_name='countryes', on_delete=models.CASCADE)
    class Meta:
        verbose_name = ('Город')
        verbose_name_plural = ('Города')
    def __str__(self):
        return(self.city)

class Organisation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Имя организации',max_length=255)
    city = models.ForeignKey(City, related_name='cities', on_delete=models.CASCADE)
    class Meta:
        verbose_name = ('Организация')
        verbose_name_plural = ('Организации')
    def __str__(self):
        return(self.name)   
class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Имя сотрудника",max_length=255)
    full_name = models.CharField('ФИО',max_length=255)
    sex = models.CharField('Пол',max_length=1,choices=SEX_CHOICE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    position = models.CharField('Должность',max_length=20,choices=POSITION_CHOICE)
    photo = models.CharField('Фотография',max_length=255)
    birthday = models.DateField(("Дата рождения"), auto_now=False, auto_now_add=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("Сотрудник")
        verbose_name_plural = ("Сотрудники")
    def __str__(self):
        return(self.name)
    
class Agents(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Имя',max_length=255)
    full_name = models.CharField('ФИО',max_length=255)
    organisation = models.ForeignKey(Organisation, related_name='organisations', on_delete=models.CASCADE)
    class Meta:
        verbose_name = ('Агент')
        verbose_name_plural = ('Агенты')
    def __str__(self):
        return(self.name)   
    
class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Название договора',max_length=255)
    participants = models.IntegerField('Участники поездки')
    date = models.DateField(("Дата"), auto_now=False, auto_now_add=False)
    total = models.FloatField('Сумма(в валюте)')
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    class Meta:
        verbose_name = ('Договор')
        verbose_name_plural = ('Договоры')
    def __str__(self):
        return(self.title)   
    
class PaymentOfTheContract(models.Model):
    id = models.AutoField(primary_key=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    date = models.DateField('Дата',auto_now=False,auto_now_add=False)
    total = models.FloatField('Сумма(в валюте)')
    class Meta:
        verbose_name = ('Оплата договора')
        verbose_name_plural = ('Оплата договоров')
    def __str__(self):
        return(str(self.id))
    
class Report(models.Model):
    id = models.AutoField(primary_key=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    date = models.DateField('Дата')
    currency = models.CharField('Валюта',max_length=100)
    total_currency = models.FloatField('Сумма(в валюте)')
    total_rubles = models.FloatField('Сумма(в рублях)')
    class Meta:
        verbose_name = ('Отчет')
        verbose_name_plural = ('Отчеты')
    def __str__(self):
        return(str(self.id))
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Имя',max_length=255)
    full_name = models.CharField('ФИО',max_length=255)
    sex = models.CharField('Пол',max_length=1,choices=SEX_CHOICE)
    photo = models.CharField('Фотография',max_length=255)
    birthday = models.DateField(("Дата рождения"), auto_now=False, auto_now_add=False)
    birthplace = models.CharField('Место рождения',max_length=255)
    passport_series = models.IntegerField('Серия паспорта')
    passport_number = models.IntegerField('Номер паспорта')
    passport_date = models.DateField('Дата выдачи', auto_now=False, auto_now_add=False)
    passport_date_end = models.DateField('Дата окончания действия', auto_now=False, auto_now_add=False)
    agency = models.CharField('Орган выдавший документ',max_length=255)
    status = models.CharField(max_length=25,choices=STATUS_CHOICE)
    class Meta:
        verbose_name = ('Клиент')
        verbose_name_plural = ('Клиенты')
    def __str__(self):
        return(self.name)
class Agreement(models.Model):
    id = models.AutoField(primary_key=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agents,on_delete=models.CASCADE)
    countryes = models.ManyToManyField(Country)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    date = models.DateField('Дата соглашения', auto_now=False, auto_now_add=False)
    date_begin = models.DateField('Дата начала поездки', auto_now=False, auto_now_add=False)
    date_end = models.DateField('Дата окончания поездки', auto_now=False, auto_now_add=False)
    class Meta:
        verbose_name = ('Соглашение')
        verbose_name_plural = ('Соглашения')
    def __str__(self):
        return(str(self.id)) 
    
class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    name = models.CharField('Название отеля',max_length=255)
    category = models.CharField(max_length=1,choices=HOTEL_CHOICE)
    adress = models.CharField('Адрес',max_length=255)
    class Meta:
        verbose_name = ('Отель')
        verbose_name_plural = ('Отели')
    def __str__(self):
        return(self.name)
    
class Route(models.Model):
    id = models.AutoField(primary_key=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    class Meta:
        verbose_name = ('Маршрут поездки')
        verbose_name_plural = ('Маршруты поездок')
    def __str__(self):
        return(str(self.contract))

class Voucher(models.Model):
    id = models.AutoField(primary_key=True)
    transport=models.CharField('Вид транспорта',max_length=255)
    class Meta:
        verbose_name = ('Ваучер')
        verbose_name_plural = ('Ваучеры')
    def __str__(self):
        return(self.transport)

class Tour(models.Model):
    id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher,on_delete=models.CASCADE)
    route = models.ForeignKey(Route,on_delete=models.CASCADE)
    type_of_number = models.CharField('Тип номера',max_length=15,choices=NUMBERS_CHOICE)
    type_of_eat = models.CharField('Тип питания',max_length=15,choices=EAT_CHOICE)
    class Meta:
        verbose_name = ('Тур')
        verbose_name_plural = ('Туры')
    def __str__(self):
        return(str(self.id))
class ParticipantsOfTheTrip(models.Model):
    id = models.AutoField(primary_key=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    name = models.CharField('Имя',max_length=255)
    full_name = models.CharField('ФИО',max_length=255)
    birthday = models.DateField(("Дата рождения"), auto_now=False, auto_now_add=False)
    class Meta:
        verbose_name = ('Участники поездки')
        verbose_name_plural = ('Участники поездок')
    def __str__(self):
        return(str(self.id))
    
class Transfer(models.Model):
    id = models.AutoField(primary_key=True)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    arrival = models.TimeField('Дата прибытия', auto_now=False, auto_now_add=False)
    departure = models.TimeField('Дата отправления', auto_now=False, auto_now_add=False)
    car_model = models.CharField('Модель машины',max_length=100)
    class Meta:
        verbose_name = ('Модель машины')
        verbose_name_plural = ('Модели машин')
    def __str__(self):
        return(self.car_model)