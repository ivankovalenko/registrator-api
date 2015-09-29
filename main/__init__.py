# coding: utf-8
from django.db.models import signals
from django.contrib.auth import get_user_model
from tastypie.models import create_api_key
import main.signals_receivers
import main.api
import main.admin_user

signals.post_save.connect(create_api_key, sender=get_user_model())
