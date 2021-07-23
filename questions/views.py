from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Question, Result

# Create your views here.

class HomeView(TemplateView):
    template_name = 'questions/questions.html'
    model = Question

    def get_context_data(self, **kwargs):
        """Add section data in context."""
        context = super(HomeView, self).get_context_data(**kwargs)
        context['questions'] = Question.objects.all()
        return context

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        ip_address = self.get_client_ip(request)
        post_data = dict(request.POST)
        total = 0
        for i in range(len(post_data['questions'])):
            pk=int(post_data['questions'][i])
            ques = Question.objects.get(pk=pk)
            ans = int(post_data['question_' + str(i+1)][0])
            marks = ques.relevance_marks * ans
            total += marks
            result = Result(Question=ques, answer=ans, marks=marks, ip_address=ip_address)
            result.save()
        context = {"result": total}
        request.session['result'] = total
        return redirect('/result')


def result(request):
    context = {}
    result = request.session.get('result', 0)
    context['result'] = result
    if result <= 50:
        color = "red"
    if (result > 50) and (result <=70):
        color = "orange"
    if result > 70:
        color = "green"
    context['color'] = color
    return render(request, "questions/results.html", context)
