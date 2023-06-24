from django.views.generic import TemplateView

from fruitipedia_app.profile_app.models import ProfileModel


def get_user_profile():
    try:
        return ProfileModel.objects.first()
    except ProfileModel.DoesNotExist:
        return None


class DisableFields:
    disabled_fields = ()
    fields = {}

    def _disable_fields(self):
        if self.disabled_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields

        for field in fields:
            if field in self.fields:
                field = self.fields[field]
                field.widget.attrs['disabled'] = 'disabled'
                field.required = False
