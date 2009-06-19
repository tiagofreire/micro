from django.contrib import admin
from models import *
from django.core.mail import EmailMessage, send_mail

class NewsletterAdmin(admin.ModelAdmin) :
    exclude = ('data_envio',)
    list_display = ('titulo', 'data_envio')
    ordering = ('data_envio',)
    
    def response_add(self, request, obj, post_url_continue = '../%s') :
        redirect = super(NewsletterAdmin, self).response_add(request, obj)
        obj.enviar()
        return redirect    

    def response_change(self, request, obj) :
        redirect = super(NewsletterAdmin, self).response_change(request, obj)
        obj.enviar()
        return redirect
       
class EmailAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data')
    exclude = ['data']
    actions_on_bottom = False   

admin.site.register(Email, EmailAdmin)
admin.site.register(Newsletter, NewsletterAdmin)

