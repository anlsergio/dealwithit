from django.shortcuts import render


products = [
    {
        'name': 'Product 1',
        'description': 'A great product',
        'seller': 'John Snow',
        'price': 120.90,
        'date_posted': 'August 27, 2018',
        'image': 'https://support.apple.com/library/content/dam/edam/applecare/images/en_US/il/ios12-product-lockup-callout.png'
    },
    {
        'name': 'Product 2',
        'description': 'Another great product',
        'seller': 'Daenerys Targerian',
        'price': 400.20,
        'date_posted': 'August 23, 2018',
        'image': 'https://support.apple.com/library/content/dam/edam/applecare/images/en_US/il/ios12-product-lockup-callout.png'
    },
    {
        'name': 'Product 3',
        'description': 'Not so good at all',
        'seller': 'Twin Lannister',
        'price': 99.50,
        'date_posted': 'February 12, 2019',
        'image': 'https://support.apple.com/library/content/dam/edam/applecare/images/en_US/il/ios12-product-lockup-callout.png'
    },
    {
        'name': 'Product 1',
        'description': 'A great product',
        'seller': 'John Snow',
        'price': 120.90,
        'date_posted': 'August 27, 2018',
        'image': 'https://support.apple.com/library/content/dam/edam/applecare/images/en_US/il/ios12-product-lockup-callout.png'
    },
    {
        'name': 'Product 2',
        'description': 'Another great product',
        'seller': 'Daenerys Targerian',
        'price': 400.20,
        'date_posted': 'August 23, 2018',
        'image': 'https://support.apple.com/library/content/dam/edam/applecare/images/en_US/il/ios12-product-lockup-callout.png'
    },
    {
        'name': 'Product 3',
        'description': 'Not so good at all',
        'seller': 'Twin Lannister',
        'price': 99.50,
        'date_posted': 'February 12, 2019',
        'image': 'https://support.apple.com/library/content/dam/edam/applecare/images/en_US/il/ios12-product-lockup-callout.png'
    }
]


# Create your views here.
def home(request):
    context = {
        'products': products
    }
    return render(request, 'store/home.html', context)

def about(request):
    return render(request, 'store/about.html', {'title': 'About'})