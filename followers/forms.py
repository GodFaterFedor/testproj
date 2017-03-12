from django import forms

from .models import Man


class ManAdminForm(forms.ModelForm):
    class Meta:
        model = Man
        fields = ['id', 'name', 'follow_ids']

    id = forms.IntegerField(
        widget=forms.TextInput(attrs={'readonly':'readonly'}) 
    ) 
    follow_ids = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple, 
    	choices = Man.objects.get( id=503 ).following(), 
    )


#class ManAdminForm(forms.ModelForm):
#    class Meta:
#        model = Man
#
#    bars = forms.ModelMultipleChoiceField(queryset=Bar.objects.all())
#
#    def __init__(self, *args, **kwargs):
#        super(ManAdminForm, self).__init__(*args, **kwargs)
#        if self.instance:
#            self.fields['bars'].initial = self.instance.bar_set.all()
#
#    def save(self, *args, **kwargs):
        # FIXME: 'commit' argument is not handled
        # TODO: Wrap reassignments into transaction
        # NOTE: Previously assigned Foos are silently reset
#        instance = super(FooForm, self).save(commit=False)
#        self.fields['bars'].initial.update(foo=None)
#        self.cleaned_data['bars'].update(foo=instance)
#        return instance