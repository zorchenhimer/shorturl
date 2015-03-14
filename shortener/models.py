from django.db import models

class Link(models.Model):
    create_time = models.DateTimeField(auto_now_add = True)
    last_visit = models.DateTimeField(auto_now = True)
    destination = models.CharField(max_length=2000)
    times_visited = models.IntegerField()

    # Alpha-numeric case sensitive identifiers gives 8.39x10^17 combinations
    # with ten characters.
    short_name = models.CharField(max_length=10)

    def __str__(self):
        return '[{s}] {d}'.format(s=self.short_name, d=self.destination)
