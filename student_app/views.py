import json
from django.http import JsonResponse

from .models import Students

def create_student(request):
    try:
        data = json.loads(request.body)
        if request.method == "POST":
            student = Students.objects.create(name=data.get('name'), roll_num=data.get('roll_num'))
            return JsonResponse({"data": {"id": student.id, "name": student.name, "roll_num": student.roll_num},
                                 "message": "Created",
                                 "status": 201}, status=201)
        return JsonResponse({"data": {}, "message": "Method not allowed", "status": 405}, status=405)

    except Exception as e:
        return JsonResponse({"data": {}, "message": str(e), "status": 400}, status=400)
