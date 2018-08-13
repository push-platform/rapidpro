# Generated by Django 1.11.6 on 2018-04-11 16:55

from django.db import migrations

from temba.contacts.models import URN


def update_dart_hub9_ext_scheme_urns(apps, schema_editor):
    ContactURN = apps.get_model("contacts", "ContactURN")

    encrypted_urns = ContactURN.objects.filter(channel__channel_type__in=["DA", "H9"]).exclude(identity__icontains="+")
    for contact_urn in encrypted_urns:
        contact_urn.scheme = "ext"
        contact_urn.identity = URN.from_parts("ext", contact_urn.path)
        contact_urn.save()


class Migration(migrations.Migration):

    dependencies = [("contacts", "0075_create_modified_on_index")]

    operations = [migrations.RunPython(update_dart_hub9_ext_scheme_urns)]
