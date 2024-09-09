from email.policy import default

from django import forms


class PublicKeyForm(forms.Form):
    key = forms.CharField(max_length=50)    # поле для ввода публичной ссылки
    path = forms.CharField(initial='/') # поле, указывающее путь к файлу (по умолчанию - /)
    path.widget = path.hidden_widget()  # данное поле скрыто


class TypeForm(forms.Form):
    ALL = [
        'audio', 'backup', 'book',
        'compressed', 'data',
        'development', 'diskimage',
        'document', 'encoded',
        'executable', 'flash',
        'font', 'image', 'settings',
        'spreadsheet', 'text',
        'unknown', 'video', 'web'
           ]
    TYPE = [
        (ALL, 'все'),
        ('document', 'документы'),
        ('image', 'изображения')
    ]
    type = forms.ChoiceField(choices=TYPE)