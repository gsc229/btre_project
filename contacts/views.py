from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail


def contact(request):
  print(request.POST)
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    # Check to see if the user has made an inquiry alread
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have alread made an inquiry for this listing')
        return redirect('/listings/'+listing_id)

  contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )
  contact.save()

  #Send Email
  send_mail(
    'Property Listing Inquiry',
    'There has been an inquiry for ' + listing + ' from '+ email +'. Sign into the admin panel for more info',
     email,
    [realtor_email, 'gsc229dev@gmail.com'],
    fail_silently=False

  )

  messages.success(request, 'Your request has been submitted, a realtor will get bak to you soon')
  return redirect('/listings/'+listing_id)
  