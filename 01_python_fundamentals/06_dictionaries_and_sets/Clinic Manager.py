clinic_info = {"name": "life care clinic", "city": "Lahore"}

Today_patients = ["ali","sara","ali", "zain", "hassan", "sara"]

remove_duplicates =set(Today_patients)
remove_duplicates.add("umer")
total_unique_patients = len(remove_duplicates)

fees = 500
tax = 10

Total = (total_unique_patients*fees)*1.1

print(f"ClinicName:{clinic_info['name'].title()}\n Location Name:{clinic_info['city'].upper()}\n total_unique_patients:{total_unique_patients}\n Final total{Total}")