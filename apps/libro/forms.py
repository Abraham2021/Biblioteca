from django import forms
from .models import Autor,Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']
        labels = {
            'nombre': 'Nombre del Autor',
            'apellidos': 'Apellido del Autor',
            'nacionalidad': 'Nacionalidad del Autor',
            'descripcion': 'Profesion del Autor',
        }
        widgets = {
            'nombre':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese Nombre',
                    'id':'nombre'
                }
            ),
            
            'apellidos':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese Apellido',
                    'id':'apellidos'
                }
            ),
            
            'nacionalidad':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese Nacionalidad',
                    'id':'nacionalidad'
                }
            ),
            
            'descripcion':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Descripcion',
                    'id':'descripcion'
                }
            )
            
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo','autor_id','fecha_publicacion')
        label = {
            'titulo':'Titulo del libro',
            'autor_id':'Autor(es) del Libro',
            'fecha_publicacion': 'Fecha de publicacion del libro'
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese titulo de libro'
                }    
            ),
            'autor_id': forms.SelectMultiple(
                attrs = {
                    'class':'form-control'
                }
            ),
            'fecha_publicacion': forms.SelectDateWidget(
                 attrs = {
                     'class':'form-control'
                 }
            )
            
        }
    
    
        
    
