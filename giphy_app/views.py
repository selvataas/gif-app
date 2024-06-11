from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import datetime
from .models import Image
from .forms import UploadImageForm


class IndexView(View):
  def get(self, request):
    images = Image.objects.order_by("uploaded_date")
    return render(
      request,
      "giphy_app/index.html",
      {
        "images": images,
      },
    )


class SignUpView(View):
  def get(self, request):
    return render(
      request,
      "giphy_app/signup.html",
      {
        "form": UserCreationForm(),
      },
    )

  def post(self, request):
    form = UserCreationForm(request.POST)

    if form.is_valid():
      form.save()
      username = form.data["username"]
      password = form.data["password1"]
      user = authenticate(
        request,
        username=username,
        password=password,
      )
      if user:
        login(request, user)
      return redirect("/")

    return render(
      request,
      "giphy_app/signup.html",
      {
        "form": form,
      },
    )


class UploadImageView(LoginRequiredMixin, View):
  login_url = "/login/"

  def get(self, request):
    return render(
      request,
      "giphy_app/upload.html",
      {
        "form": UploadImageForm(),
      },
    )

  def post(self, request):
    user = request.user
    if not user.is_authenticated:
      raise Exception("User is not authenticated")

    form = UploadImageForm(request.POST, request.FILES)

    if form.is_valid():
      img = Image(
        title=form.data["title"],
        image=form.files["image"],
        uploaded_date=datetime.now(),
        uploaded_by=user,
      )

      img.save()

      return redirect("/")

    return render(
      request,
      "giphy_app/upload.html",
      {
        "form": form,
      },
    )
  







# from datetime import datetime
# from django.shortcuts import render, redirect
# from django.views import View

# from .forms import UploadImageForm
# from .models import Image
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.mixins import LoginRequiredMixin


# class IndexView(View):
#     def get(self, request):
#         images = Image.objects.order_by("uploaded_date")
#         return render (request, "giphy_app/index.html",
#                       {
#                         "images": images,
#                       },
#         ) 

# class SignUpView(View):
#     def get(self, request):
#         return render(request, "giphy_app/signup.html",
#                       {
#                         "form": UserCreationForm(),
#                       },
#         )

#     def post(self, request):
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             username = form.data["username"]
#             password = form.data["password1"]

#             user = authenticate(request, username=username, password=password,)

#             if user:
#                 login(request, user)
#             return redirect("/")
            
#         return render(request, "giphy_app/signup.html",
#                         {
#                             "form": form,
#                         },
#         )
    
# class UploadImageView(LoginRequiredMixin, View):
#   login_url = "/login/"

#   def get(self, request):
#     return render(
#       request,
#       "giphy_app/upload.html",
#       {
#         "form": UploadImageForm(),
#       },
#     )

#   def post(self, request):
#     user = request.user
#     if not user.is_authenticated:
#       raise Exception("User is not authenticated")

#     form = UploadImageForm(request.POST, request.FILES)

#     if form.is_valid():
#       img = Image(
#         title=form.data["title"],
#         image=form.files["image"],
#         uploaded_date=datetime.now(),
#         uploaded_by=user,
#       )

#       img.save()
#       return redirect("/")

#     return render(
#       request,
#       "giphy_app/upload.html",
#       {
#         "form": form,
#       },
#     )





