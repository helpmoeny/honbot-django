# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'HeroData.cli_name'
        db.alter_column(u'honbot_herodata', 'cli_name', self.gf('django.db.models.fields.CharField')(max_length=120))
        # Adding index on 'HeroData', fields ['cli_name']
        db.create_index(u'honbot_herodata', ['cli_name'])


    def backwards(self, orm):
        # Removing index on 'HeroData', fields ['cli_name']
        db.delete_index(u'honbot_herodata', ['cli_name'])


        # Changing field 'HeroData.cli_name'
        db.alter_column(u'honbot_herodata', 'cli_name', self.gf('django.db.models.fields.TextField')())

    models = {
        u'honbot.apicount': {
            'Meta': {'object_name': 'APICount'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'unique': 'True', 'primary_key': 'True', 'db_index': 'True'})
        },
        u'honbot.builds': {
            'Meta': {'object_name': 'Builds'},
            'hero': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lvl1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl10': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl11': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl12': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl13': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl14': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl15': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl16': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl17': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl18': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl19': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl20': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl21': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl22': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl23': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl24': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl25': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl3': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl4': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl5': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl6': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl7': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl8': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl9': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'match_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'mmr': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'win': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'honbot.chat': {
            'Meta': {'object_name': 'Chat'},
            'json': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'match_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_index': 'True'})
        },
        u'honbot.herodata': {
            'Meta': {'object_name': 'HeroData'},
            'ability1': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'ability2': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'ability3': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'ability4': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'aggrorange': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'agility': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'agilityperlevel': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'armor': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'attackactiontime': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'attackcooldown': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'attackdamagemax': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'attackdamagemin': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'attackduration': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'attacknumanims': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'attackrange': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'attackspeedpersec': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'attacktype': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'calcattackspeed': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'carryrating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'category': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'cli_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '120', 'db_index': 'True'}),
            'difficulty': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'disp_name': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'effectivearmor': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'gankerating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'health': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'healthregen': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'hero_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_index': 'True'}),
            'initiatorrating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'intelligence': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'junglerating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'magicarmor': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'mana': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'manaregen': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'maxhealth': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'meleerating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'movespeed': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'primaryattribute': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'pusherrating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'rangedrating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'sightrangeday': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sightrangenight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'solorating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'strength': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'strengthperlevel': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'supportrating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'turnrate': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'wanderrange': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'honbot.heroes': {
            'Meta': {'object_name': 'Heroes'},
            'attacktype': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'disp_name': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'hero_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_index': 'True'}),
            'primaryattribute': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'team': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'honbot.herouse': {
            'Meta': {'object_name': 'HeroUse'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'hero_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'popularity': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'usage': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'honbot.matchcount': {
            'Meta': {'object_name': 'MatchCount'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'unique': 'True', 'primary_key': 'True', 'db_index': 'True'})
        },
        u'honbot.matches': {
            'Meta': {'ordering': "['-match_id']", 'object_name': 'Matches'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now_add': 'True', 'blank': 'True'}),
            'build': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'major': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'map_used': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'match_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_index': 'True'}),
            'minor': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'db_index': 'True'}),
            'realtime': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'replay_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '120', 'null': 'True'}),
            'revision': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'honbot.playercount': {
            'Meta': {'object_name': 'PlayerCount'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'unique': 'True', 'primary_key': 'True', 'db_index': 'True'})
        },
        u'honbot.playerherostats': {
            'Meta': {'object_name': 'PlayerHeroStats'},
            'data': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'hero_id': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "'rnk'", 'max_length': '10'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'})
        },
        u'honbot.playerhistory': {
            'Meta': {'object_name': 'PlayerHistory'},
            'history': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'db_index': 'True'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'})
        },
        u'honbot.playericon': {
            'Meta': {'object_name': 'PlayerIcon'},
            'avatar': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '300'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'})
        },
        u'honbot.playermatchcount': {
            'Meta': {'object_name': 'PlayerMatchCount'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'unique': 'True', 'primary_key': 'True', 'db_index': 'True'})
        },
        u'honbot.playermatches': {
            'Meta': {'object_name': 'PlayerMatches'},
            'annihilation': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'apm': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'assists': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'bdmg': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'bgold': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'bloodlust': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'buybacks': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'consumables': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'cs': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'deaths': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'denies': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'doublekill': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'exp_denied': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'gold_spent': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'goldlost2death': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'gpm': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'hero': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'herodmg': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'kdr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kills': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['honbot.Matches']"}),
            'mmr_change': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'db_index': 'True'}),
            'nickname': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '25'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'quadkill': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'razed': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'secsdead': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'smackdown': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'triplekill': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'wards': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'win': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'xpm': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'honbot.playerstats': {
            'Meta': {'object_name': 'PlayerStats'},
            'TSR': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'aactionsmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'aassists': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'aconsumables': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'acs': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'adeaths': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'adenies': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'agoldmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'akills': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'annihilation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'assists': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'atime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'awards': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'axpmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'bloodlust': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cc': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cccalls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'deaths': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'doublekill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'hours': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'humiliation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kadr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kdr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kicked': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kills': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks10': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks15': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks3': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks4': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks5': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks6': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks7': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks8': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks9': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'left': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'level_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'losses': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'matches': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'max_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'min_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'mmr': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'nemesis': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'db_index': 'True'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_index': 'True'}),
            'quadkill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'razed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'retribution': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'smackdown': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'triplekill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'}),
            'winpercent': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4'}),
            'wins': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'honbot.playerstatscasual': {
            'Meta': {'object_name': 'PlayerStatsCasual'},
            'TSR': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'aactionsmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'aassists': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'aconsumables': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'acs': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'adeaths': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'adenies': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'agoldmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'akills': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'annihilation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'assists': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'atime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'awards': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'axpmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'bloodlust': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cc': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cccalls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'deaths': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'doublekill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'hours': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'humiliation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kadr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kdr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kicked': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kills': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks10': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'ks15': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'ks3': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks4': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks5': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks6': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks7': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks8': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks9': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'left': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'level_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'losses': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'matches': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'max_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'min_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'mmr': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nemesis': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'quadkill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'razed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'retribution': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'smackdown': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'triplekill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'}),
            'winpercent': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4'}),
            'wins': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'honbot.playerstatspublic': {
            'Meta': {'object_name': 'PlayerStatsPublic'},
            'TSR': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'aactionsmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'aassists': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'aconsumables': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'acs': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'adeaths': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'adenies': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'agoldmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'akills': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'annihilation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'assists': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'atime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'awards': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'axpmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'bloodlust': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cc': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cccalls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'deaths': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'doublekill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'hours': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'humiliation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kadr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kdr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kicked': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kills': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks10': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'ks15': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'ks3': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks4': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks5': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks6': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks7': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks8': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks9': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'left': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'level_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'losses': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'matches': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'max_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'min_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'mmr': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nemesis': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'quadkill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'razed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'retribution': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'smackdown': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'triplekill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'}),
            'winpercent': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4'}),
            'wins': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['honbot']