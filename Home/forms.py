from django import forms

class SignupForm(forms.Form):
    fname = forms.CharField(
        label='First Name',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'})
    )
    lname = forms.CharField(
        label='Last Name',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'})
    )
    username = forms.CharField(
        label='Username (Email or Phone)',
        max_length=11,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter email'})
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter email'})
    )
    phone = forms.CharField(
        label='Phone number',
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Phone number'})
    )
    program = forms.CharField(
        label='Program',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Program'})
    )
    department = forms.CharField(
        label='Department',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Department'})
    )
    batch = forms.CharField(
        label='Batch',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Batch'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'})
    )
    cpassword = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter Password'})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        # Add your username validation logic here
        if not is_valid_username(username):
            raise forms.ValidationError("Invalid username format. It should be four digits, three alphabets, and four digits.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        # Add your email validation logic here
        if not is_valid_email(email):
            raise forms.ValidationError("Email should end with '@iiitkottayam.ac.in'")
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        # Add your phone number validation logic here
        if not is_valid_phone(phone):
            raise forms.ValidationError("Phone number should contain 10 digits.")
        return phone

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        cpassword = cleaned_data.get('cpassword')
        # Add your password matching validation logic here
        if password and cpassword and password != cpassword:
            raise forms.ValidationError("Password and Confirm Password do not match.")
