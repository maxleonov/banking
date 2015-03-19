# coding=utf-8
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.shortcuts import render, redirect
from cashmachine.forms import CardForm, PinForm, GetCashForm
from cashmachine.models import Card, PIN_RETRIES_LIMIT, LogRecord,\
    Operation, GET_CASH, VIEW_BALANCE
from django.utils import timezone
from cashmachine.util import check_dict_keys


def logout(request):
    if 'card_id' in request.session:
        del(request.session['card_id'])
    if 'logged_in' in request.session:
        del(request.session['logged_in'])
    return redirect('cashmachine.views.card')


def card(request):
    if not request.POST.items():
        form = CardForm()
    else:
        form = CardForm(data=request.POST)
        if not form.is_valid():
            request.session['error'] = \
                'Please enter a valid card ID'
            return redirect('cashmachine.views.error')
        else:
            form.cleaned_data['card_id'] = \
                form.cleaned_data['card_id'].replace('-', '')
            try:
                card = Card.objects.get(id=form.cleaned_data['card_id'])
            except ObjectDoesNotExist:
                request.session['error'] = \
                    'There is no card with such ID'
                return redirect('cashmachine.views.error')
            else:
                if card.blocked:
                    request.session['error'] = 'This card is blocked'
                    return redirect('cashmachine.views.error')
                else:
                    request.session['card_id'] = card.id
                    request.session.set_expiry(300)
                    return redirect('cashmachine.views.pin')
    return render(request, 'cashmachine/card.html',
                  {'form': form})


def pin(request):
    try:
        check_dict_keys(['card_id'], request.session)
        card = Card.objects.get(id=request.session.get('card_id'))
    except (ObjectDoesNotExist, KeyError):
        return logout(request)

    if not request.POST.items():
        form = PinForm()
    else:
        form = PinForm(data=request.POST)
        if not form.is_valid():
            request.session['error'] = \
                'Please enter a valid PIN.'
            return redirect('cashmachine.views.error')
        elif Card.get_pin_hash(form.cleaned_data['pin']) != card.pin:
            card.pin_attempts_made += 1
            if card.pin_attempts_made > PIN_RETRIES_LIMIT:
                card.blocked = True
                card.save()
                del(request.session['card_id'])
                request.session['error'] = \
                    'Retries limit exceeded. This card is now blocked.'
                return redirect('cashmachine.views.error')
            else:
                card.save()
                request.session['error'] = 'PIN rejected'
                return redirect('cashmachine.views.error')
        else:
            if card.pin_attempts_made:
                card.pin_attempts_made = 0
                card.save()
            request.session['logged_in'] = True
            return redirect('cashmachine.views.operations')
    return render(request, 'cashmachine/pin.html',
                  {'form': form})


def operations(request):
    try:
        check_dict_keys(['card_id', 'logged_in'], request.session)
        Card.objects.get(id=request.session.get('card_id'))
    except (ObjectDoesNotExist, KeyError):
        return logout(request)

    return render(request, 'cashmachine/operations.html')


def balance(request):
    try:
        check_dict_keys(['card_id', 'logged_in'], request.session)
        card = Card.objects.get(id=request.session.get('card_id'))
    except (ObjectDoesNotExist, KeyError):
        return logout(request)

    log_record = LogRecord(
        card=card, created_at=timezone.now(),
        amount=0, balance_after_operation=card.balance,
        operation=Operation.objects.get_or_create(name=VIEW_BALANCE)[0])
    log_record.save()

    return redirect('report', operation=log_record.id)


def getcash(request):
    try:
        check_dict_keys(['card_id', 'logged_in'], request.session)
        card = Card.objects.get(id=request.session.get('card_id'))
    except (ObjectDoesNotExist, KeyError):
        return logout(request)

    if not request.POST.items():
        form = GetCashForm()
        return render(request, 'cashmachine/getcash.html',
                      {'form': form})
    else:
        form = GetCashForm(data=request.POST)
        if not form.is_valid():
            request.session['error'] = 'Please enter a valid amount'
            return redirect('cashmachine.views.error')
        elif card.balance >= form.cleaned_data['amount']:
            with transaction.atomic():
                card.balance -= form.cleaned_data['amount']
                card.save()

                log_record = LogRecord(
                    card=card, created_at=timezone.now(),
                    amount=form.cleaned_data['amount'],
                    balance_after_operation=card.balance,
                    operation=Operation.objects.get_or_create(name=GET_CASH)[0])
                log_record.save()

            return render(request, 'cashmachine/report.html',
                          {'log_record': log_record})
        else:
            request.session['error'] = 'Your credit card limit was reached'
            return redirect('cashmachine.views.error')


def report(request, operation):
    try:
        check_dict_keys(['card_id', 'logged_in'], request.session)
        log_record = LogRecord.objects.get(id=operation)
        if log_record.card_id != request.session.get('card_id'):
            raise ValueError
    except (ObjectDoesNotExist, KeyError, ValueError):
        return logout(request)

    return render(request, 'cashmachine/report.html',
                  {'log_record': log_record})


def error(request):
    try:
        check_dict_keys(['error'], request.session)
    except (ObjectDoesNotExist, KeyError):
        return logout(request)

    error = request.session['error']
    del(request.session['error'])

    return render(request, 'cashmachine/error.html',
                  {'error': error})
