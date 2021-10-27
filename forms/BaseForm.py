import wtforms as forms


class BaseForm(forms.Form):
    def get_form_data(self):
        feilds = self.__dict__.get('_fields')
        return {str(f): self[f].data for f in feilds}

    def get_errors(self):
        feilds = self.__dict__.get('_fields')
        return {str(f): self[f].errors for f in feilds if len(self[f].errors)}
