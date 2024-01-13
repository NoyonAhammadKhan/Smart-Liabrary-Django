from .models import Transaction
from .forms import DepositForm
from django.urls import reverse_lazy
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .constants import TRANSACTION_TYPE, DEPOSIT, BOOK_RETURN, BOOK_ISSUE
from django.template.loader import render_to_string


def send_transaction_email(user, amount, subject, template):
    message = render_to_string(template, {
        'user': user,
        'amount': amount,
    })
    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()


class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transaction_app/deposit_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })

        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })
        return context


class DepositView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'
    # template_name = 'transaction_app/deposit_form.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields=['balance']
        )

        user = self.request.user
        subject = "Deposit Money"
        send_transaction_email(user, amount, subject,
                               'transaction_app/deposit_email.html')
        return super().form_valid(form)
