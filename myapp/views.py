from django.shortcuts import render
from django.http import HttpResponse
from .models import Item,FeatureFlag
from .models import AuditLog
import time
# Create your views here.
def index(request):
    item_list=Item.objects.all()
    return render(request, 'mysite/index.html', {'item_list':item_list})

def detail(request,pk):
    item_detail=Item.objects.get(pk=pk)
    context={
        'item':item_detail
    }
    return render(request, 'mysite/detail.html', context)

# views.py
from django.shortcuts import render, redirect
from .models import Item

def create_item(request):
    if request.method == "POST":
        start = time.time()

        try:
            connection.ensure_connection()
            db_status = "OK"
        except Exception:
            db_status = "DOWN"
        name = request.POST.get('item_name')
        price = request.POST.get('item_price')
        desc = request.POST.get('item_decs')

        item = Item.objects.create(
            item_name=name,
            item_price=price,
            item_decs=desc
        )
        end = time.time()

        return JsonResponse({
            "status": "OK" if db_status == "OK" else "FAIL",
            "database": db_status,
            "response_time": f"{round((end - start)*1000, 2)} ms"
        })

        AuditLog.objects.create(
            user=request.user if request.user.is_authenticated else None,
            action="item.created",
            ip_address=request.META.get('REMOTE_ADDR'),
            extra_data={
                "item_name": item.item_name,
                "item_price": item.item_price
            }
        )

        return redirect('create_item')

    return render(request, 'mysite/create_item.html')


last_call = 0
LIMIT_SEC = 5

def APIrateLimit(request):
    item_list=Item.objects.all()
    global last_call
    now = time.time()
    if now - last_call < LIMIT_SEC:
        wait = LIMIT_SEC - (now - last_call)
        return HttpResponse(f"Out of limit wait for {wait} sec")
    last_call = now

    return render(request, 'mysite/index.html', {'item_list':item_list})
    
def feature_enabled(name):
    try:
        return FeatureFlag.objects.get(name=name).is_enabled
    except FeatureFlag.DoesNotExist:
        return False

def feature_flag_view(request):
    if feature_enabled("new_feature2"):
        return HttpResponse("New Feature")
    else:
        return HttpResponse(f"Old Feature")



def audit_log_view(request):
    logs = AuditLog.objects.all().order_by('-timestamp')

    return render(request, 'mysite/audit_logs.html', {
        'logs': logs
    })


from django.db import connection
from django.http import JsonResponse



def health_check(request):
    start = time.time()

    try:
        connection.ensure_connection()
        db_status = "OK"
    except Exception:
        db_status = "DOWN"

    end = time.time()

    return JsonResponse({
        "status": "OK" if db_status == "OK" else "FAIL",
        "database": db_status,
        "response_time": f"{round((end - start)*1000, 2)} ms"
    })


# views.py
from django.utils import timezone
from datetime import timedelta
from .models import ScheduledJob

def create_job(request):
    run_time = timezone.now() + timedelta(seconds=5)

    ScheduledJob.objects.create(
        name="Test Job",
        run_at=run_time
    )

    return HttpResponse("Job scheduled")



from django.utils import timezone
from datetime import timedelta
from .models import EmailTask

# Example 1: A Delayed Job (Send in 1 hour)
def schedule_delayed_email(request):
    execution_time = timezone.now() + timedelta(hours=1)
    
    EmailTask.objects.create(
        subject="Delayed Reminder",
        recipient="user@example.com",
        message="This was scheduled 1 hour ago!",
        run_at=execution_time
    )
    return HttpResponse("Job scheduled for 1 hour from now.")