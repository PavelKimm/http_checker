from django.db import models


class Website(models.Model):
    url = models.CharField(max_length=2048, unique=True)

    class Meta:
        ordering = ('url',)

    def __str__(self):
        return self.url


class WebsiteAvailability(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    response_status_code = models.SmallIntegerField(null=True)
    reason = models.TextField()
    ip_address = models.CharField(max_length=50, null=True)
    server = models.CharField(max_length=200, null=True)
    checked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('website__url', '-id')
        verbose_name_plural = "Website availabilities"

    def __str__(self):
        return f"{self.website.url} [id: {self.id}]"
