from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import date, timedelta
from .models import TODO


class TODOModelTest(TestCase):
    """Pruebas para el modelo TODO"""
    
    def setUp(self):
        self.todo = TODO.objects.create(
            title="Test TODO",
            description="Test description",
            due_date=date.today() + timedelta(days=7)
        )
    
    def test_todo_creation(self):
        """Verificar que un TODO se crea correctamente"""
        self.assertEqual(self.todo.title, "Test TODO")
        self.assertEqual(self.todo.description, "Test description")
        self.assertFalse(self.todo.resolved)
        self.assertIsNotNone(self.todo.created_at)
    
    def test_todo_str_method(self):
        """Verificar el método __str__"""
        self.assertEqual(str(self.todo), "Test TODO")
    
    def test_todo_default_resolved_is_false(self):
        """Verificar que resolved es False por defecto"""
        new_todo = TODO.objects.create(title="Another TODO")
        self.assertFalse(new_todo.resolved)
    
    def test_todo_ordering(self):
        """Verificar que los TODOs se ordenan por fecha de creación (más recientes primero)"""
        todo1 = TODO.objects.create(title="First TODO")
        todo2 = TODO.objects.create(title="Second TODO")
        todos = TODO.objects.all()
        self.assertEqual(todos[0], todo2)  # El más reciente primero
        self.assertEqual(todos[1], todo1)


class TODOViewTest(TestCase):
    """Pruebas para las vistas de TODO"""
    
    def setUp(self):
        self.client = Client()
        self.todo = TODO.objects.create(
            title="Test TODO",
            description="Test description",
            due_date=date.today() + timedelta(days=7)
        )
    
    def test_todo_list_view(self):
        """Verificar que la vista de lista funciona"""
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test TODO")
        self.assertTemplateUsed(response, 'todos/todo_list.html')
    
    def test_todo_create_view_get(self):
        """Verificar que se muestra el formulario de creación"""
        response = self.client.get(reverse('todo_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/todo_form.html')
    
    def test_todo_create_view_post(self):
        """Verificar que se puede crear un TODO mediante POST"""
        data = {
            'title': 'New TODO',
            'description': 'New description',
            'due_date': date.today() + timedelta(days=3)
        }
        response = self.client.post(reverse('todo_create'), data)
        self.assertEqual(response.status_code, 302)  # Redirect después de crear
        self.assertTrue(TODO.objects.filter(title='New TODO').exists())
    
    def test_todo_create_view_requires_title(self):
        """Verificar que el título es requerido"""
        data = {
            'description': 'Description without title',
        }
        response = self.client.post(reverse('todo_create'), data)
        self.assertEqual(response.status_code, 200)  # Se queda en el formulario
        self.assertFalse(TODO.objects.filter(description='Description without title').exists())
    
    def test_todo_update_view_get(self):
        """Verificar que se muestra el formulario de edición"""
        response = self.client.get(reverse('todo_edit', kwargs={'pk': self.todo.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test TODO")
        self.assertTemplateUsed(response, 'todos/todo_form.html')
    
    def test_todo_update_view_post(self):
        """Verificar que se puede actualizar un TODO"""
        data = {
            'title': 'Updated TODO',
            'description': 'Updated description',
            'due_date': date.today() + timedelta(days=5),
            'resolved': True
        }
        response = self.client.post(reverse('todo_edit', kwargs={'pk': self.todo.pk}), data)
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated TODO')
        self.assertTrue(self.todo.resolved)
    
    def test_todo_delete_view_get(self):
        """Verificar que se muestra la confirmación de eliminación"""
        response = self.client.get(reverse('todo_delete', kwargs={'pk': self.todo.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/todo_confirm_delete.html')
    
    def test_todo_delete_view_post(self):
        """Verificar que se puede eliminar un TODO"""
        todo_pk = self.todo.pk
        response = self.client.post(reverse('todo_delete', kwargs={'pk': todo_pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(TODO.objects.filter(pk=todo_pk).exists())
    
    def test_toggle_resolved(self):
        """Verificar que se puede cambiar el estado de resuelto"""
        self.assertFalse(self.todo.resolved)
        response = self.client.get(reverse('todo_toggle', kwargs={'pk': self.todo.pk}))
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.resolved)
        
        # Toggle de nuevo
        response = self.client.get(reverse('todo_toggle', kwargs={'pk': self.todo.pk}))
        self.todo.refresh_from_db()
        self.assertFalse(self.todo.resolved)
    
    def test_empty_todo_list(self):
        """Verificar que se muestra mensaje cuando no hay TODOs"""
        TODO.objects.all().delete()
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay TODOs")


class TODOIntegrationTest(TestCase):
    """Pruebas de integración para flujos completos"""
    
    def setUp(self):
        self.client = Client()
    
    def test_complete_todo_workflow(self):
        """Probar el flujo completo: crear, editar, resolver y eliminar"""
        # 1. Crear un TODO
        data = {
            'title': 'Complete workflow TODO',
            'description': 'Testing complete workflow',
            'due_date': date.today() + timedelta(days=7)
        }
        response = self.client.post(reverse('todo_create'), data)
        self.assertEqual(response.status_code, 302)
        
        # 2. Verificar que existe
        todo = TODO.objects.get(title='Complete workflow TODO')
        self.assertIsNotNone(todo)
        self.assertFalse(todo.resolved)
        
        # 3. Editar el TODO
        data['title'] = 'Updated workflow TODO'
        data['resolved'] = False
        response = self.client.post(reverse('todo_edit', kwargs={'pk': todo.pk}), data)
        todo.refresh_from_db()
        self.assertEqual(todo.title, 'Updated workflow TODO')
        
        # 4. Marcar como resuelto
        response = self.client.get(reverse('todo_toggle', kwargs={'pk': todo.pk}))
        todo.refresh_from_db()
        self.assertTrue(todo.resolved)
        
        # 5. Eliminar
        response = self.client.post(reverse('todo_delete', kwargs={'pk': todo.pk}))
        self.assertFalse(TODO.objects.filter(pk=todo.pk).exists())
