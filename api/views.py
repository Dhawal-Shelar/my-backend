from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

@api_view(["POST"])
def index(request):
    # Access query parameters using request.query_params
    email = request.query_params.get("email")
    feedback = request.query_params.get("feedback")
    
    print("Query Parameters from URL:", email, feedback)

    return Response({"data": "API is working", "email": email, "feedback": feedback})



@api_view(["GET"])
def get_feedbacks(request):
    # Fetch all feedback records from the database
    feedbacks = FeedbackModel.objects.all()

    # Serialize the data
    serializer = FeedbackSerializer(feedbacks, many=True)

    # Return the serialized data in the response
    return Response({"data": serializer.data}, status=200)


@api_view(["POST"])
def postFeedback(request):
  datas= request.data;
  email = datas.get('email')
  name = datas.get('name')
  feedback = datas.get('feedback')
  
  user = FeedbackModel.objects.create(email = email , name =name , feedback= feedback).save()
  
  return Response({"message": "feedback post succesful"})