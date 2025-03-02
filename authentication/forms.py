from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(widget = forms.TextInput(attrs={
                                                             'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                               'required':'required'}))

    password = forms.CharField(widget= forms.PasswordInput(attrs={
                                                               'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                               'required':'required'}))