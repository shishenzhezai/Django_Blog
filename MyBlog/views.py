# Create your views here.
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
