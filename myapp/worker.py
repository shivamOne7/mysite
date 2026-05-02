

# import os
# import django
# import time
# from datetime import timedelta

# # 🔹 Setup Django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# django.setup()

# from django.utils import timezone
# from django.db import models
# from myapp.models import EmailTask

# def process_email_tasks():
#     now = timezone.now()
    
#     # Feature 1: Delayed Scheduler (only get tasks where run_at <= now)
#     tasks = EmailTask.objects.filter(
#         run_at__lte=now,
#         is_done=False,
#         attempts__lt=models.F('max_retries')
#     )

#     for task in tasks:
#         try:
#             print(f"[{now}] Processing: {task.subject} for {task.recipient}")
            
#             # Simulate Email Logic
#             # if random.choice([True, False]): raise Exception("Connection Timeout")
            
#             task.is_done = True
#             task.status = 'success'
#             task.save()
#             print(f"✅ Successfully sent email to {task.recipient}")

#         except Exception as e:
#             # Feature 2: Retry System + Exponential Backoff
#             task.attempts += 1
            
#             if task.attempts >= task.max_retries:
#                 task.is_done = True
#                 task.status = 'failed'
#                 print(f"❌ Max retries reached for {task.id}. Giving up.")
#             else:
#                 # Math: Wait 2, 4, 8, 16 minutes... based on attempts
#                 wait_time = 2 ** task.attempts 
#                 task.run_at = timezone.now() + timedelta(minutes=wait_time)
#                 print(f"⚠️ Failed. Scheduled retry #{task.attempts} in {wait_time}m")
            
#             task.save()

# if __name__ == "__main__":
#     print("🚀 Worker started. Monitoring for delayed and retry tasks...")
#     while True:
#         process_email_tasks()
#         time.sleep(10) # Check every 10 seconds




import os
import django
import time
import sys


sys.path.append(os.getcwd())
# 🔹 Setup Django (VERY IMPORTANT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# 🔹 Now imports will work
from django.utils import timezone
from myapp.models import ScheduledJob 

def run_jobs():
    now = timezone.now()

    jobs = ScheduledJob.objects.filter(
        run_at__lte=now,
        is_done=False
    )

    for job in jobs:
        print(f"Running job: {job.name}")

        # 🔥 Your task logic here
        

        job.is_done = True
        job.save()

# 🔁 Loop
while True:
    print("Checking jobs...")
    run_jobs()
    time.sleep(10)

