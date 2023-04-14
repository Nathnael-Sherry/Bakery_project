from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Client


def order_page(request):
    data = Client.objects.all()
    context = {"data": data}
    return render(request, "order.html", context)


def edit_page(request):
    return render(request, "edit.html")


def login_page(request):
    return render(request, "login.html")


def signup_page(request):
    return render(request, "signup.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        event = request.POST.get('event')
        caketype = request.POST.get('caketype')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        phone = request.POST.get('phone')
        orderdate = request.POST.get('orderdate')
        deliverydate = request.POST.get('deliverydate')

        query = Client(name=name, caketype=caketype, age=age, event=event, quantity=quantity, price=price, phone=phone, orderdate=orderdate, deliverydate=deliverydate)
        query.save()
        return redirect("/")

        return render(request, 'order.html')


def deleteData(request, id):
    d = Client.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "order.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        event = request.POST.get('event')
        caketype = request.POST.get('caketype')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        phone = request.POST.get('phone')
        orderdate = request.POST.get('orderdate')
        deliverydate = request.POST.get('deliverydate')

        update_info = Client.objects.get(id=id)
        update_info.name = name
        update_info.age = age
        update_info.event = event
        update_info.caketype = caketype
        update_info.quantity = quantity
        update_info.price = price
        update_info.phone = phone
        update_info.orderdate = orderdate
        update_info.deliverydate = deliverydate
        update_info.save()

        return redirect("/")

    d = Client.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)

def idx_page(request):
    return render(request, "idx.html")

# def clients_table(request):
#     return render(request, "table.html")