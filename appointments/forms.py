from django import forms
from django.core.exceptions import ValidationError
import re
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'phone', 'email', 'service', 'date', 'time', 'message']
        widgets = {
            'name':    forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше ім\'я'}),
            'phone':   forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+380 (XX) XXX-XX-XX'}),
            'email':   forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'service': forms.Select(attrs={'class': 'form-select'}),
            'date':    forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time':    forms.Select(attrs={'class': 'form-select'},
                                   choices=[('', 'Виберіть час')] + [
                                       (f'{h:02d}:{m:02d}', f'{h:02d}:{m:02d}')
                                       for h in range(9, 19) for m in (0, 30)
                                   ]),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,
                                             'placeholder': 'Додаткова інформація (необов\'язково)'}),
        }
        labels = {
            'name': 'Ваше ім\'я',
            'phone': 'Телефон',
            'email': 'Email',
            'service': 'Послуга',
            'date': 'Дата',
            'time': 'Час',
            'message': 'Коментар',
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        
        # Дозволені префікси: +380 (Україна), +43 (Австрія), +32 (Бельгія), 
        # +359 (Болгарія), +385 (Хорватія), +357 (Кіпр), +420 (Чехія),
        # +45 (Данія), +372 (Естонія), +358 (Фінляндія), +33 (Франція),
        # +49 (Німеччина), +30 (Греція), +36 (Угорщина), +353 (Ірландія),
        # +39 (Італія), +371 (Латвія), +370 (Литва), +352 (Люксембург),
        # +356 (Мальта), +31 (Нідерланди), +48 (Польща), +351 (Португалія),
        # +40 (Румунія), +421 (Словаччина), +386 (Словенія), +34 (Іспанія),
        # +46 (Швеція), +41 (Швейцарія)
        
        allowed_prefixes = [
            '+380',  # Україна
            '+43', '+32', '+359', '+385', '+357', '+420', '+45', '+372',
            '+358', '+33', '+49', '+30', '+36', '+353', '+39', '+371',
            '+370', '+352', '+356', '+31', '+48', '+351', '+40', '+421',
            '+386', '+34', '+46', '+41'  # Європа
        ]
        
        # Перевірка, чи номер починається з дозволеного префіксу
        if not any(phone.startswith(prefix) for prefix in allowed_prefixes):
            raise ValidationError(
                'Номер телефону повинен бути з України (+380) або Європи. '
                'Номери з Росії (+7) не прийматимуться.'
            )
        
        # Перевірка формату (має бути принаймні 10 цифр після +)
        digits_only = re.sub(r'\D', '', phone)
        if len(digits_only) < 10:
            raise ValidationError('Номер телефону має бути правильного формату.')
        
        return phone
