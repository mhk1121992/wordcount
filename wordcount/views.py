from django.http import HttpResponse
from django.shortcuts import render
import operator


def index(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()

    worddictionary = {}
    for word in word_list:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add to dictionary
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext,
                                          'text_count': len(word_list),
                                          'sortedwords': sortedwords})

def about(request):
    return render(request, 'about.html')