from django.http import HttpResponse
from django.template import loader
from .models import Users,Roles

def home(request):
     
    usersapp = Users.objects.raw('select u.*,r.access_level,r.menu from userapp_users u Left Join userapp_roles r ON u.roles_id_id = r.roles_id')
    template = loader.get_template('home.html')
    context = {
        'users': usersapp,
    }
    return HttpResponse(template.render(context, request))

