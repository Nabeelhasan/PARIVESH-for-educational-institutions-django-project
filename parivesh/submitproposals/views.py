from django.shortcuts import render
from django.views import View
from .forms import ProposalForm
from .models import Proposal

class HomeView(View):
    def get(self, request):
        form = ProposalForm()
        proposals = Proposal.objects.all()
        return render(request, 'submitproposals/home.html', {'form': form, 'proposals': proposals})

    def post(self, request):
        form = ProposalForm(request.POST, request.FILES)
        form.save()
        return render(request, 'submitproposals/message.html')

class ProposalView(View):
    # pk is short for a primary key, which is a unique identifier for each record in a database
    def get(self, request, pk):
        proposal = Proposal.objects.get(pk=pk)
        return render(request, 'submitproposals/proposal.html', {'proposal': proposal})

class MessageView(View):
    def get(self, request):
        return render(request, 'submitproposals/message.html')