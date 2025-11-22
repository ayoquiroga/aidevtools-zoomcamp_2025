from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TODO
from .forms import TODOForm

# Create your views here.

class TODOListView(ListView):
    model = TODO
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'

class TODOCreateView(CreateView):
    model = TODO
    template_name = 'todos/todo_form.html'
    form_class = TODOForm
    success_url = reverse_lazy('todo_list')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Excluir el campo resolved en la creación
        if 'resolved' in form.fields:
            del form.fields['resolved']
        return form

class TODOUpdateView(UpdateView):
    model = TODO
    template_name = 'todos/todo_form.html'
    form_class = TODOForm
    success_url = reverse_lazy('todo_list')

class TODODeleteView(DeleteView):
    model = TODO
    template_name = 'todos/todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')

def toggle_resolved(request, pk):
    todo = get_object_or_404(TODO, pk=pk)
    todo.resolved = not todo.resolved
    todo.save()
    return redirect('todo_list')
