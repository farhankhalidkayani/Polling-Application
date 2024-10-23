from django import forms
from main.models import Question, Option


# Form for the Question model
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["content"]  # Assuming 'content' is a field in the Question model
        widgets = {
            "content": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your question"}
            ),
        }
        labels = {
            "content": "Question",
        }


# Form for the Option model
class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ["content"]  # Assuming 'content' is a field in the Option model
        widgets = {
            "content": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter option text"}
            ),
        }
        labels = {
            "content": "Option",
        }
