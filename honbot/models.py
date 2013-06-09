from django.db import models


class Matches(models.Model):
    match_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    date = models.DateTimeField()
    replay_url = models.URLField(max_length=120, default="")
    realtime = models.CharField(max_length=10, default="")
    mode = models.CharField(max_length=10, default="")
    _map = models.CharField(max_length=10, default="")
    major = models.PositiveSmallIntegerField(default=0)
    minor = models.PositiveSmallIntegerField(default=0)
    revision = models.PositiveSmallIntegerField(default=0)
    build = models.PositiveSmallIntegerField(default=0)
    added = models.DateTimeField(auto_now_add=True, default=0)

    class Meta:
        ordering = ['-match_id']


class PlayerMatches(models.Model):
    player_id = models.PositiveIntegerField(default=0)
    match = models.ForeignKey(Matches)
    deaths = models.PositiveSmallIntegerField(default=0)
    win = models.BooleanField(default=False)
    apm = models.FloatField(default=0)
    cs = models.PositiveSmallIntegerField(default=0)
    smackdown = models.PositiveSmallIntegerField(default=0)
    secsdead = models.PositiveIntegerField(default=0)
    gpm = models.FloatField(default=0)
    bdmg = models.PositiveSmallIntegerField(default=0)
    herodmg = models.PositiveIntegerField(default=0)
    xpm = models.FloatField(default=0)
    kdr = models.FloatField(default=0)
    goldlost2death = models.PositiveSmallIntegerField(default=0)
    denies = models.PositiveSmallIntegerField(default=0)
    hero = models.PositiveSmallIntegerField(default=0)
    kills = models.PositiveSmallIntegerField(default=0)
    consumables = models.PositiveSmallIntegerField(default=0)
    assists = models.PositiveSmallIntegerField(default=0)
    nickname = models.TextField(max_length=25, default="")
    level = models.PositiveSmallIntegerField(default=0)
    wards = models.PositiveSmallIntegerField(default=0)
    team = models.PositiveSmallIntegerField(default=0)
    position = models.PositiveSmallIntegerField(default=0)


class PlayerIcon(models.Model):
    player_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    avatar = models.URLField(max_length=300, default="")
    updated = models.DateTimeField(auto_now=True, default=0)


class PlayerHistory(models.Model):
    player_id = models.PositiveIntegerField(default=0)
    history = models.TextField(default="")
    updated = models.DateTimeField(auto_now=True, default=0)
    mode = models.CharField(max_length=10, default="")


class PlayerStats(models.Model):
    player_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    username = models.CharField(max_length=30, default="")
    updated = models.DateTimeField(auto_now=True, default=0)
    ccalls = models.PositiveIntegerField(default=0)
    deaths = models.PositiveIntegerField(default=0)
    cc = models.PositiveIntegerField(default=0)
    assists = models.FloatField(default=0)
    TSR = models.FloatField(default=0)
    kdr = models.FloatField(default=0)
    adenies = models.FloatField(default=0)
    aconsumables = models.FloatField(default=0)
    kills = models.PositiveIntegerField(default=0)
    winpercent = models.CharField(max_length=4, default="")
    kadr = models.FloatField(default=0)
    akills = models.FloatField(default=0)
    kicked = models.PositiveIntegerField(default=0)
    agoldmin = models.PositiveIntegerField(default=0)
    matches = models.PositiveIntegerField(default=0)
    mmr = models.PositiveIntegerField(default=0)
    hours = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    awards = models.PositiveIntegerField(default=0)
    atime = models.PositiveIntegerField(default=0)
    aactionsmin = models.PositiveIntegerField(default=0)
    axpmin = models.PositiveIntegerField(default=0)
    adeaths = models.FloatField(default=0)
    acs = models.FloatField(default=0)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    left = models.PositiveIntegerField(default=0)
