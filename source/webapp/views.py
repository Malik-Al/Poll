from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView

from webapp.forms import PollForm
from webapp.models import Poll





class PollIndexView(ListView):
    template_name = 'poll/index.html'
    model = Poll
    context_object_name = 'polls'
    ordering = ['-created_at']
    paginate_by = 2
    paginate_orphans = 1




class PollView(DetailView):
    model = Poll
    template_name = 'poll/poll.html'
    context_object_name = 'poll'



class PollCreateView(CreateView):
    template_name = 'poll/create.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self):
        return reverse('index')




class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/update.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('index')




class PollDeleteView(DeleteView):
    template_name = 'poll/delete.html'
    model = Poll
    context_key = 'poll'
    success_url = reverse_lazy('index')