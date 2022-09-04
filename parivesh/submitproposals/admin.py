from django.contrib import admin
from .models import Proposal

@admin.register(Proposal)
class ProposalModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'enrollment_no', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'locations', 'proposer_img', 'attachment']