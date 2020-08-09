from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from webapp.forms import PollForm
from webapp.models import Poll





class PollIndexView(ListView):
    template_name = 'poll/index.html'
    model = Poll
    context_object_name = 'polls'
    ordering = ['-created_at']







class PollView(TemplateView):
    template_name = 'poll/poll.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll_pk = kwargs.get('pk')
        context['poll'] = get_object_or_404(Poll, pk=poll_pk)
        return context




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