from django.shortcuts import render, redirect
from note.models import carddet
from note.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import uuid
import hashlib


def index(request):
    notes = carddet.objects.all()
    return render(request, 'note/home.html', {'notes': notes})


def steps(request):
    return render(request, 'note/StepsRequired.html', {})


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def login(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            mycard = carddet.objects.filter(cardnum=request.POST['cardnum'])
            if len(mycard) == 1:
                mycard = mycard[0]
                if check_password(mycard.pin, request.POST['pin']):
                    print('auth success')
                    return redirect('seltype', mycard.cardnum)
                else:
                    print('auth failed')
                    return render(request, 'note/Login.html', {'form': login_form()})
            else:
                print('multiple objects reurned')
                return redirect('seltype')
        else:
            print('invalid form')
            return redirect('seltype')
    return render(request, 'note/Login.html', {'form': login_form()})


@csrf_exempt
def seltype(request, cardnum):
    return render(request, 'note/seltype.html', {'carddet': carddet.objects.filter(cardnum=cardnum)[0]})


def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def set(request):  # , cardnum):
    if request.method == 'POST':
        form = carddetForm(request.POST)
        if form.is_valid():
            if len(carddet.objects.filter(cardnum=request.POST['cardnum'])) == 0:
                card = form.save(commit=False)
                card.pin = hash_password(card.pin)
                card.save()
            else:
                messages.error(request, 'card with num: ' +
                               request.POST['cardnum'] + ' already exists')
                print('card with num: ' +
                      request.POST['cardnum'] + ' already exists')
            return redirect('index')
        else:
            messages.error(request, "Error")

    return render(request, 'note/mysettings.html', {'form': carddetForm()})


def transact(request, cardnum):
    return render(request, 'note/transact.html', {'carddet': carddet.objects.filter(cardnum=cardnum)[0]})


def withdraw(request, cardnum):
    t = carddet.objects.filter(cardnum=cardnum)[0]
    form = deposit_form(request.POST)
        
    if request.method == 'POST':
        if form.is_valid():
            t.balance = str(int(t.balance)-int(request.POST['balance']))
            print(t.balance)
            t.save()
            messages.success(request, 'SUCCESSFULLY WITHDRAWED')

    return render(request, 'note/withdraw.html', {'form': form,'carddet': t})


def enquire(request, cardnum):
    t = carddet.objects.filter(cardnum=cardnum)[0]
    return render(request, 'note/enquire.html', {'carddet': t})

def deposit(request, cardnum):
    t = carddet.objects.filter(cardnum=cardnum)[0]
    form = deposit_form(request.POST)
        
    if request.method == 'POST':
        if form.is_valid():
            t.balance = str(int(t.balance)+int(request.POST['balance']))
            print(t.balance)
            t.save()
            messages.success(request, 'SUCCESSFULLY DEPOSITED')

    return render(request, 'note/deposit.html', {'form': form, 'carddet': t})
