# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TimelineEvent.tag'
        db.add_column('timelinejs_timelineevent', 'tag',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TimelineEvent.tag'
        db.delete_column('timelinejs_timelineevent', 'tag')


    models = {
        'timelinejs.timeline': {
            'Meta': {'object_name': 'Timeline'},
            'asset_caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'asset_credit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'asset_media': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '50'})
        },
        'timelinejs.timelineevent': {
            'Meta': {'object_name': 'TimelineEvent'},
            'asset_caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'asset_credit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'asset_media': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'timeline': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timelinejs.Timeline']"})
        },
        'timelinejs.timelineoptions': {
            'Meta': {'object_name': 'TimelineOptions'},
            'debug': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'embed_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'font': ('django.db.models.fields.CharField', [], {'default': "'Bevan-PotanoSans'", 'max_length': '50'}),
            'hash_bookmark': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "'600'", 'max_length': '10'}),
            'lang': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '6'}),
            'maptype': ('django.db.models.fields.CharField', [], {'default': "'watercolor'", 'max_length': '50'}),
            'start_at_end': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_at_slide': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'start_zoom_adjust': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'timeline': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['timelinejs.Timeline']", 'unique': 'True', 'primary_key': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "'100%'", 'max_length': '10'})
        }
    }

    complete_apps = ['timelinejs']