from django import forms

class ReportForm(forms.Form):
    search=forms.CharField(label="Search", widget=forms.Textarea(attrs={'cols':'80', 'rows':'2', 'placeholder':'検索ワードを入力'}))

class PageForm(forms.Form):
    pages=forms.CharField(label="Page", required=False, disabled=False, widget=forms.TextInput(attrs={'cols':'80', 'rows':'2', 'pattern':'^[0-9]+$', 'placeholder':'ページ数を入力'}))