from django import forms


class AddProjectForm(forms.Form):
    name = forms.CharField(max_length=255,
                           label="Название проекта",
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Введите имя проекта"}))
    platform = forms.CharField(max_length=255,
                               label="Платформа, на которой будет разрабатываться проект",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Выберите платформу"}))
    price = forms.FloatField(label="Ваш бюджет на разработку приложения ",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Укажите бюджет (в гривнах)", 'type': 'number'}),)
    terms = forms.IntegerField(label="Желаемые сроки реализации приложения",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Укажите сроки (в днях) ", 'type': 'number'}))
