# Generated by Django 2.2.2 on 2019-09-13 23:53

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gaugeaction', '0001_initial'),
        ('fermionaction', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GaugeConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.TextField(editable=False)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(blank=True, help_text='(Optional) Char(20): User defined tag for easy searches', max_length=20, null=True)),
                ('misc', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text="(Optional) JSON: {'anything': 'you want'}", null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nf211',
            fields=[
                ('gaugeconfig_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gaugeconfig.GaugeConfig')),
                ('short_tag', models.TextField(blank=True, help_text="(Optional) Text: Short name for gaugeconfig (e.g. 'a15m310')", null=True)),
                ('stream', models.TextField(help_text='Text: Stream tag for Monte Carlo')),
                ('config', models.PositiveSmallIntegerField(help_text='PositiveSmallInt: Configuration number')),
                ('nx', models.PositiveSmallIntegerField(help_text='PositiveSmallInt: Spatial length in lattice units')),
                ('ny', models.PositiveSmallIntegerField(help_text='PositiveSmallInt: Spatial length in lattice units')),
                ('nz', models.PositiveSmallIntegerField(help_text='PositiveSmallInt: Spatial length in lattice units')),
                ('nt', models.PositiveSmallIntegerField(help_text='PositiveSmallInt: Temporal length in lattice units')),
                ('mpi', models.DecimalField(decimal_places=6, help_text='(Optional) Decimal(10,6): Pion mass in MeV', max_digits=10, null=True)),
                ('charm', models.ForeignKey(help_text='ForeignKey pointing to lattice fermion action', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='fermionaction.FermionAction')),
                ('gaugeaction', models.ForeignKey(help_text='ForeignKey pointing to lattice gauge action', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='gaugeaction.GaugeAction')),
                ('light', models.ForeignKey(help_text='ForeignKey pointing to lattice fermion action', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='fermionaction.FermionAction')),
                ('strange', models.ForeignKey(help_text='ForeignKey pointing to lattice fermion action', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='fermionaction.FermionAction')),
            ],
            bases=('gaugeconfig.gaugeconfig',),
        ),
        migrations.AddConstraint(
            model_name='nf211',
            constraint=models.UniqueConstraint(fields=('stream', 'config', 'gaugeaction', 'nx', 'ny', 'nz', 'nt', 'light', 'strange', 'charm'), name='unique_gaugeconfig_nf211'),
        ),
    ]
