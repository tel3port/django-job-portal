from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.template.defaultfilters import slugify

STATUS = ((0, "Draft"), (1, "Publish"))

JOB_TYPE = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
    ('Freelance', 'Freelancer'),
)

CATEGORY = (
    ('Web Design', 'Web Design'),
    ('Graphic Design', 'Graphic Design'),
    ('Web Developing', 'Web Developing'),
    ('Software Engineering', 'Software Engineering'),
    ('HR', 'HR'),
    ('Administrative & Customer Support', 'Administrative & Customer Support,'),
    ('Architecture & Engineering', '       Architecture & Engineering,'),
    ('Community & Human Services', '       Community & Human Services,'),
    ('Construction & Extraction', '        Construction & Extraction,'),
    ('Education & Instruction', '          Education & Instruction,'),
    ('Finance & Accounting', '             Finance & Accounting,'),
    ('Flight Attendant', '                 Flight Attendant,'),
    ('Food & Beverage', '                  Food & Beverage,'),
    ('Healthcare', '                       Healthcare,'),
    ('Legal', '                            Legal,'),
    ('Marketing, Advertising & Public Relations', 'Marketing, Advertising & Public Relations'),
    ('Personal Services', '                Personal Services,'),
    ('Protective & Security', '            Protective & Security,'),
    ('Repair, Maintenance & Installation', 'Repair, Maintenance & Installation,'),
    ('Sales & Retail', '                   Sales & Retail,'),
    ('Technology', '                       Technology,'),
    ('Transportation', '                   Transportation,'),
    ('Travel, Attractions & Events', '     Travel, Attractions & Events,'),

)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Any', 'Any'),
)


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.first_name


class JobListing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, editable=False, blank=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    listing_kws = models.TextField(max_length=50000, default="job listing")
    company_name = models.CharField(max_length=200)
    employment_status = models.CharField(choices=JOB_TYPE, max_length=10)
    gender = models.CharField(choices=GENDER, max_length=30, null=True)
    category = models.CharField(choices=CATEGORY, max_length=30)
    description = models.TextField()
    responsibilities = models.TextField()
    experience = models.CharField(max_length=100)
    job_location = models.CharField(max_length=120)
    Salary = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='media', null=True)
    published_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:job-single", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(JobListing, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-published_on"]


class ApplyJob(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    file = models.FileField(null=True)

    def __str__(self):
        return self.name


class SiteMetaData(models.Model):
    meta_title = models.CharField(max_length=2000)
    tagline_1 = models.CharField(max_length=5000)
    tagline_2 = models.CharField(max_length=5000)
    review_1 = models.CharField(max_length=8000)
    review_2 = models.CharField(max_length=8000)
    review_3 = models.CharField(max_length=8000)
    review_4 = models.CharField(max_length=8000)
    service_1 = models.CharField(max_length=8000)
    service_2 = models.CharField(max_length=8000)
    service_3 = models.CharField(max_length=8000)
    service_4 = models.CharField(max_length=8000)
    service_5 = models.CharField(max_length=8000)
    service_6 = models.CharField(max_length=8000)
    location = models.CharField(max_length=5000)
    alt_kws = models.CharField(max_length=5000)
    about_site = models.CharField(max_length=15000)
    about_team_member_1 = models.CharField(max_length=5000)
    about_team_member_2 = models.CharField(max_length=5000)

    def __str__(self):
        return self.meta_title