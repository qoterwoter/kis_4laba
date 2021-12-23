from django.contrib import admin
from .models import *
from django.db.models.functions import Lower
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

@admin.register(Staff)
class StaffAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","name","full_name","sex",'position',"photo","birthday")
      search_fields = ['name','full_name']
      list_filter = ['sex','position']
      pass
      def get_ordering(self,request):
            return [Lower('id')]

@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","country")
      search_fields = ['country']
      pass
      def get_ordering(self,request):
            return [Lower('id')]
    
@admin.register(City)
class CityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","country","city")
      search_fields = ['country__country','city']
      list_filter = ['country']
      pass
      def get_ordering(self,request):
            return [Lower('id')]
      
@admin.register(Organisation)
class OrganisationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","name","city")
      search_fields = ['name','city']
      list_filter = ['city']
      pass
      def get_ordering(self,request):
            return [Lower('id')]
      
@admin.register(Agents)
class AgentsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","name","full_name",'organisation')
      search_fields = ['name','full_name','organisation__name']
      list_filter = ['organisation__name']
      pass
      def get_ordering(self,request):
            return [Lower('id')]
      
@admin.register(Contract)
class ContractAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","participants",'organisation','date','total')
      search_fields = ['name','organisation','total']
      list_filter = ['organisation']
      pass
      def get_ordering(self,request):
            return [Lower('id')]

@admin.register(PaymentOfTheContract)
class PaymentOfTheContractAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","contract","staff",'date','total')
      search_fields = ['staff__name','total']
      list_filter = ['staff']
      pass
      def get_ordering(self,request):
            return [Lower('id')]
      
@admin.register(Report)
class ReportAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","contract","staff",'date','total_currency','total_rubles')
      search_fields = ['staff__name','total_currency','total_rubles']
      list_filter = ['staff']
      pass
      def get_ordering(self,request):
            return [Lower('id')]

@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","name","full_name","sex",'passport_series','passport_number','status')
      search_fields = ['name','full_name']
      list_filter = ['sex','status']
      pass
      def get_ordering(self,request):
            return [Lower('id')]
      
@admin.register(Agreement)
class AgreementAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","get_organisation","get_agent",'get_client','get_staff','date','date_begin','date_end')
      search_fields = ['organisation__name','agent__name','countryes__country']
      list_filter = ['staff__name','agent__name','organisation__name','countryes__country']
      pass
      def get_ordering(self,request):
            return [Lower('id')]
      def get_staff(self,obj):
            return obj.staff.name
      get_staff.admin_order_field = 'Сотрудник'
      get_staff.short_description= 'Сотрудник'
      def get_agent(self,obj):
            return obj.agent.name
      get_agent.admin_order_field = 'Агент'
      get_agent.short_description= 'Агент'
      def get_client(self,obj):
            return obj.client.name
      get_client.admin_order_field = 'Клиент'
      get_client.short_description= 'Клиент'
      def get_organisation(self,obj):
            return obj.organisation.name
      get_organisation.admin_order_field = 'Организация'
      get_organisation.short_description= 'Организация'
      
@admin.register(Hotels)
class HotelsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","city",'name','category','adress')
      search_fields = ['name']
      list_filter = ['city__city']
      pass
      def get_ordering(self,request):
            return [Lower('id')]
      
@admin.register(Route)
class RouteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","contract")
      pass
      def get_ordering(self,request):
            return [Lower('id')]
      
@admin.register(Voucher)
class VoucherAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","transport")
      search_fields=['transport']
      pass
      def get_ordering(self,request):
            return [Lower('id')]
      
@admin.register(Tour)
class TourAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","get_hotel",'get_transport','get_route','type_of_number','type_of_eat')
      search_fields=['hotel__name','type_of_number','type_of_eat']
      list_filter = ['type_of_number','type_of_eat','hotel__name']
      pass
      def get_ordering(self,request):
            return [Lower('id')]
      def get_hotel(self,obj):
            return obj.hotel.name
      def get_route(self,obj):
            return obj.route.id
      def get_transport(self,obj):
            return obj.voucher.transport
      get_transport.admin_order_field = 'Транспорт'
      get_transport.short_description= 'Транспорт из ваучера'
      get_route.admin_order_field = 'Машрут'
      get_route.short_description= 'Номер маршрута'
      get_hotel.short_description = 'Отель'
      
@admin.register(ParticipantsOfTheTrip)
class ParticipantsOfTheTripAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","contract",'voucher','name','full_name','birthday')
      search_fields = ['name','full_name']
      list_filter=['voucher__id']
      pass
      def get_ordering(self,request):
            return [Lower('id')]
      
@admin.register(Transfer)
class TransferAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ("id","voucher",'arrival','departure','car_model')
      search_fields=['car_model']
      list_filter=['voucher__id']
      pass
      def get_ordering(self,request):
            return [Lower('id')]