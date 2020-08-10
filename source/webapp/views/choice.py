from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ChoiceForm
from webapp.models import Choice, Poll


class ChoiceCreateView(CreateView):
    model = Choice
    form_class = ChoiceForm
    template_name = "choice/create.html"



    def form_valid(self, form):
        poll_pk = self.kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=poll_pk)
        poll.choices.create(**form.cleaned_data)
        return redirect('poll_view', pk=poll_pk)

    # def get_context_data(self, **kwargs):
    #     poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
    #     kwargs['poll'] = poll
    #     return super().get_context_data(**kwargs)
    #
    # def form_valid(self, form):
    #     poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
    #     form.instance.poll = poll
    #     return super().form_valid(form)
    #
    # def get_success_url(self):
    #     return reverse('poll_view', kwargs={'pk': self.kwargs.get('pk')})

    # def get_success_url(self):
    #     return reverse('poll_view', kwargs={'pk': self.object.pk})






class ChoiceUpdateView(UpdateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'choice/update.html'
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})



class ChoiceDeleteView(DeleteView):
    model = Choice
    context_object_name = 'choice'
    template_name = 'choice/delete.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})
