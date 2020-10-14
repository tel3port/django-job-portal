from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import *
from .models import *

meta_data_queryset = SiteMetaData.objects.all()


def home(request):
    meta_data_home = meta_data_queryset.get(id=1)
    md_title = meta_data_home.meta_title
    md_location = meta_data_home.location
    md_kws = meta_data_home.alt_kws
    md_tl_1 = meta_data_home.tagline_1
    md_t2_2 = meta_data_home.tagline_2
    md_rev1 = meta_data_home.review_1
    md_rev2 = meta_data_home.review_2
    md_rev3 = meta_data_home.review_3
    md_rev4 = meta_data_home.review_4

    qs = JobListing.objects.all()
    jobs = JobListing.objects.all().count()
    user = User.objects.all().count()
    company_name = JobListing.objects.filter(company_name__startswith='P').count()
    paginator = Paginator(qs, 10)  # Show 10 jobs per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'md_tl_1': md_tl_1,
        'md_tl_2': md_t2_2,
        'md_rev1': md_rev1,
        'md_rev2': md_rev2,
        'md_rev3': md_rev3,
        'md_rev4': md_rev4,
        'md_title': md_title,
        'md_location': md_location,
        'md_kws': md_kws,
        'query': qs,
        'job_qs': jobs,
        'company_name': company_name,
        'candidates': user
    }
    return render(request, "home.html", context)


def about_us(request):
    meta_data_about = meta_data_queryset.get(id=1)
    md_abt = meta_data_about.about_site
    md_team1 = meta_data_about.about_team_member_1
    md_team2 = meta_data_about.about_team_member_2
    md_kws = meta_data_about.alt_kws

    context = {
        'md_abt': md_abt,
        'md_team1': md_team1,
        'md_team2': md_team2,
        'md_kws': md_kws,
    }

    return render(request, "jobs/about_us.html", context)


def service(request):
    meta_data_service = meta_data_queryset.get(id=1)
    md_service1 = meta_data_service.service_1
    md_service2 = meta_data_service.service_2
    md_service3 = meta_data_service.service_3
    md_service4 = meta_data_service.service_4
    md_service5 = meta_data_service.service_5
    md_service6 = meta_data_service.service_6
    md_kws = meta_data_service.alt_kws

    context = {
        'md_service1': md_service1,
        'md_service2': md_service2,
        'md_service3': md_service3,
        'md_service4': md_service4,
        'md_service5': md_service5,
        'md_service6': md_service6,
        'md_kws': md_kws,
    }

    return render(request, "jobs/services.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, "jobs/contact.html", context)


def job_listing(request):
    query = JobListing.objects.all().count()

    qs = JobListing.objects.all().order_by('-published_on')
    paginator = Paginator(qs, 10)  # Show 10 jobs per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
        'job_qs': query

    }
    return render(request, "jobs/job_listing.html", context)


@login_required
def job_post(request):
    form = JobListingForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/jobs/job-listing/')
    context = {
        'form': form,

    }
    return render(request, "jobs/job_post.html", context)


def job_single(request, slug):
    job_query = get_object_or_404(JobListing, slug=slug)

    context = {
        'q': job_query,
    }
    return render(request, "jobs/job_single.html", context)


@login_required
def apply_job(request):
    form = JobApplyForm(request.POST or None, request.FILES)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/')
    context = {
        'form': form,

    }
    return render(request, "jobs/job_apply.html", context)


class SearchView(ListView):
    model = JobListing
    template_name = 'jobs/search.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.filter(title__contains=self.request.GET['title'],
                                         job_location__contains=self.request.GET['job_location'],
                                         employment_status__contains=self.request.GET['employment_status'])
