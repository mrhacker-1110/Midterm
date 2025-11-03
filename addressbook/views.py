from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm

# 2. FBV: Отображение списка контактов
def contact_list(request):
    contacts = Contact.objects.all().order_by('last_name')
    return render(request, 'addressbook/contact_list.html', {'contacts': contacts})

# 3. CBV: Отображение одного контакта
class ContactDetailView(DetailView):
    model = Contact
    template_name = 'addressbook/contact_detail.html'
    context_object_name = 'contact'

# 4. CBV: Добавление контакта
class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'addressbook/contact_form.html'
    success_url = reverse_lazy('contact_list')