from django.shortcuts import render, redirect
from .models import Feedback

def feedback_view(request):
    if request.method == "POST":
        rating = int(request.POST.get("rating", 1))  # Get the rating from the form
        Feedback.objects.create(rating=rating)  # Save feedback to the database
        return render(request, "core/feedback.html", {"message": "Thank you for your feedback!", "rating": rating})
    return render(request, "core/feedback.html")
