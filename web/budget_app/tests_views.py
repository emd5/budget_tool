from django.test import TestCase, Client
from ..budget_tools.factories import BudgetFactory, TransactionFactory, UserFactory


class TestCategoryViews(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.c = Client()

    def test_denied_if_no_login(self):
        res = self.c.get('/budget_app/budgets', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'class="login-form container"', res.content)

    def test_view_list_when_logged_in(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        category = BudgetFactory(user=self.user)
        res = self.c.get('/budget_app/budgets')

        self.assertIn(category.name.encode(), res.content)

    def test_lists_only_owned_budget(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        own_category = BudgetFactory(user=self.user)
        other_category = BudgetFactory()

        res = self.c.get('/budget_app/budgets')

        self.assertIn(own_category.name.encode(), res.content)
        self.assertNotIn(other_category.name.encode(), res.content)

    def test_cards_listed_in_view(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )
        category = BudgetFactory(user=self.user)
        transaction = TransactionFactory(category=category)
        res = self.c.get('/budget_app/budgets')

        self.assertIn(transaction.title.encode(), res.content)


class TestBudgetCreateViews(TestCase):
    """."""

    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('super_secret')
        self.user.save()
        self.c = Client()

    def test_new_budget_view(self):
        self.c.login(
            username=self.user.username,
            password='super_secret'
        )

        res = self.c.get('/budget_app/budgets/new')

        self.assertEqual(res.status_code, 200)
        self.assertIn(b'input type="submit"', res.content)
        self.assertIn(b'name="name"', res.content)
        self.assertIn(b'name="description"', res.content)

    def test_create_view_adds_new_budget(self):
        self.c.login(
            username=self.user.username,
            password='super_secret'
        )

        form_data = {
            'name': ' Budget thing',
            'description': 'this is budget description'
        }

        res = self.c.post('/budget_app/budgets/new', form_data, follow=True)

        self.assertIn(b'Name thing', res.content)
