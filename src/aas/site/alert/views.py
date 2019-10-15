import json

from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView

from . import json_utils
from .forms import AlertJsonForm
from .models import Alert


def all_alerts_view(request):
    # json_result = json_utils.alert_hists_to_json(AlertHistory.objects.all())
    data = serializers.serialize("json", Alert.objects.all())
    json_result = json.dumps(json.loads(data), indent=4)
    return HttpResponse(json_result, content_type="application/json")


def all_alerts_from_source_view(request, source_id):
    data = serializers.serialize("json", AlertHistory.objects.filter(source=source_id))
    json_result = json.dumps(json.loads(data), indent=4)
    return HttpResponse(json_result, content_type="application/json")


class CreateAlertView(FormView):
    template_name = "alert/create_alert.html"
    form_class = AlertJsonForm

    def form_valid(self, form):
        """ TODO: temporarily disabled until JSON parsing has been implemented for the new data model
        json_string = form.cleaned_data["json"]
        alert_hist = json_utils.json_to_alert_hist(json_string)
        alert_hist.save()
        """
        # Redirect back to same form page
        return HttpResponseRedirect(self.request.path_info)
