from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Budget, Transaction
from .forms import BudgetForm, TransactionForm


class BudgetListView(LoginRequiredMixin, ListView):
    """List all available budgets owned by current user"""
    template_name = 'budgets/budget_list.html'
    model = Budget
    context_object_name = 'budgets'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Budget.objects.filter(user__username=self.request.user.username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(budget__user__username=self.request.user.username)
        return context


class BudgetDetailView(LoginRequiredMixin, DetailView):
    """List all available transactions within the selected budget"""
    template_name = 'budgets/budget_detail.html'
    model =Transaction
    context_object_name = 'transaction'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Transaction.objects.filter(budget__name__username=self.request.user.username)


class BudgetCreateView(LoginRequiredMixin, CreateView):
    """Class based Budget create view for test"""
    template_name = 'budgets/budget_create.html'
    model = Budget
    form_class = BudgetForm
    success_url = reverse_lazy('budget_view')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        """Create a user for form validation testing"""
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionDetailView(LoginRequiredMixin, DetailView):
    """Class based Transaction Detail View"""
    template_name = 'budgets/transaction_detail.html'
    context_object_name = 'transaction'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Transaction.objects.filter(
            budget__user__username=self.request.user.username)


class TransactionCreateView(LoginRequiredMixin, CreateView):
    """Class based Transaction create view for test"""
    template_name = 'budgets/transaction_create.html'
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('budget_view')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        """ Attatch a user
        """
        form.instance.user = self.request.user
        return super().form_valid(form)
