from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Email de Login',
        required=True,
        max_length= 100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "João_Silva@Alura.com",
            }
        )
    )
    Senha = forms.CharField(
        label='Senha',
        required=True,
        max_length= 70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
            }
        )
    )

class CadastroForms(forms.Form):
     nome_login = forms.CharField(
        label='Nome',
        required=True,
        max_length= 100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "João Silva",
            }
        )
    )
     email = forms.EmailField(
          label = 'Email Login',
          required= True,
          max_length= 100,
          widget=forms.EmailInput(
               attrs={
                     "class": "form-control",
                     "placeholder": "João_Silva@Alura.com",
               }
          )
     )
     Senha1 = forms.CharField(
        label='Senha',
        required=True,
        max_length= 70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
            }
        )
    )
     Senha2 = forms.CharField(
        label='Confirmação da Senha',
        required=True,
        max_length= 70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente",
            }
        )
    )