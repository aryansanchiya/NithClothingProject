from .models import Products,Admin_Details,Admin_Drop_Link,User, Order, TrackingDetails
# from attr import attrs,fields
from django import forms

Choices = [
    ('top','Top'),
    ('croptop','CropTop'),
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('ProductName','Catgories','Price','TypeOfStock','BustOrWaist','Condition','Details','Image1','Image2','Image3','Image4','Image5','FreeSize','Size22','Size23','Size24','Size25','Size26','Size27','Size28','Size29','Size30','Size31','Size32','Size33','Size34','Size35','Size36','Size37','Size38','Size39','Size40','Size41','Size42')
        # Catgories = forms.ChoiceField(choices=Choices)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Admin_Details
        fields = ('AdminName','AdminEmail','AdminPassword')
        widgets = {
        'AdminPassword': forms.PasswordInput()
         }
        
class DropForm(forms.ModelForm):
    class Meta:
        model = Admin_Drop_Link
        fields = ('DropName','DropNum')

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('FullName','MobileNo','Emailid','Password','ConfirmPassword')

class AdminTrackingDetails(forms.ModelForm):
    class Meta:
        model = TrackingDetails
        fields = ('order','trackingno','trackinglink')