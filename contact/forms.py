from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact


class ContactForm(forms.ModelForm):
    # 1ro metodo para alterar os dados de um campo do form
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nome',
                'class': 'add_qualquer_classe',
            },
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda',
    )

    # 2do metodo para alterar os dados de um campo do form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({'placeholder': 'Nome'})

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'categori',
            'picture',
        )

        # 3ro metodo para alterar os dados de um campo do form
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
        #     'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
        # }

    #
    # Usando par validar campos no formulario quando se deseja compara 2 campos
    def clean(self):
        cleaned_data = self.cleaned_data

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'O Primeiro nome não pode ser igual ao segundo',
                code='invalid',
            )

            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    #
    # Usando par validar campos no formulario quando validar apenas o campo em si
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Não digite "ABC" neste campo',
                    code='invalid',
                ),
            )

        return first_name


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(min_length=3, required=True)
    last_name = forms.CharField(min_length=3, required=True)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )
        unique_together = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Email já cadastrado', code='invalid'),
            )
