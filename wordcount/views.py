from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):

    return render(request, 'home.html', {'hithere': 'This is the Admin', 'bythere': 'This is the laxman'})


def count(request):
    full_text = request.GET['fulltext']

    word_count = {}

    for text in full_text.split(' '):
        word_count[text] = word_count.get(text, 0) + 1

    sortedwords = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)

    print(word_count)

    return render(request, 'count.html', {'words':sortedwords})


def about(request):

    return render(request, 'about.html')
