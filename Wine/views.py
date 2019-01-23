from django.views import generic
from django.views.generic import View
from .models import Winery
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm

# REST API imports required
from django.shortcuts import get_object_or_404
from .serializers import WineSerializer
from .models import Wine
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


# List all wines or create a new one
# wines/
class WineList(APIView):
    def get(self, request):
        wines = Wine.objects.all()
        serializer = WineSerializer(wines, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class IndexView(generic.ListView):
    template_name = 'Wine/index.html'
    context_object_name = 'all_wineries'

    def get_queryset(self):
        return Winery.objects.all()


class DetailView(generic.DetailView):
    model = Winery
    template_name = 'Wine/detail.html'


class WineryCreate(CreateView):
    model = Winery
    fields = ['winery_name', 'winery_location']


class WineryUpdate(UpdateView):
    model = Winery
    fields = ['winery_name', 'winery_location']

class WineryDelete(DeleteView):
    model = Winery
    success_url = reverse_lazy('Wine:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'Wine/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # creates an object from the form, but does
            # not save to database yet, i.e locally stored
            user = form.save(commit=False)
            # cleaned(normalized) data
            # used for sending info to database
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # properly saving the password as a hash
            # value, and increasing security
            user.set_password(password)
            user.save()

            # returns User objects uf credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                # if there is a user with the credentials from authenticate
                # we will see if the user is active and if so, log them in
                if user.is_active:
                    # sets the user to be available on all pages
                    login(request, user)
                    # request.user.username.profile() to show information

                    # send the puppy back to the homepage
                    return redirect('Wine:index')

        # if the login fails, we can send them back to the login page
        return render(request, self.template_name, {'form': form})













# from django.shortcuts import render, get_object_or_404
# from .models import Winery, Wine
#
#
# def index(request):
#     all_wineries = Winery.objects.all()
#     context = {'all_wineries': all_wineries}
#     return render(request, 'Wine/index.html', context)
#
#
# def detail(request, winery_id):
#     winery = get_object_or_404(Winery, id=winery_id)
#     return render(request, 'Wine/detail.html', {'winery': winery})
#
#
# def favorite(request, winery_id):
#     winery = get_object_or_404(Winery, id=winery_id)
#     try:
#         selected_wine = winery.wine_set.get(id=request.POST['wine'])
#     except (KeyError, Wine.DoesNotExist):
#         return render(request, 'Wine/detail.html', {
#             'winery': winery,
#             'error_message': "You did not select a valid wine",
#         })
#     else:
#         selected_wine.is_favorite = True
#         selected_wine.save()
#         return render(request, 'Wine/detail.html', {'winery': winery})










