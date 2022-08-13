from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from .mixins import LoginRequiredMixin
from .models import Message
from .forms import MessageForm


class ContactUsView(LoginRequiredMixin, FormView):
    template_name = "contact_us/contact.html"
    form_class = MessageForm
    success_url = reverse_lazy("home:main")

    def form_valid(self, form):
        form_data = form.cleaned_data
        Message.objects.create(**form_data)
        return super().form_valid(form)


# class MessageView(CreateView):
#     model = Message
#     fields = ('name', 'email', 'subject', 'message',  'date')
#     success_url = reverse_lazy("home:main")
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["messages"] = Message.objects.all()
#         return context
#
#     def form_valid(self, form):
#         instance = form.save(commit=False)
#         instance.email = self.request.user.email
#         instance.save()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return super(MessageView, self).get_success_url()
