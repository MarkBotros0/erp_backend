import pandas as pd
from .models import Client, ClientTitle, ClientType, ClientNature

def handle_uploaded_file(file):
    df = pd.read_excel(file)
    errors = []

    for index, row in df.iterrows():
        try:
            title, _ = ClientTitle.objects.get_or_create(title=row['title'], defaults={'title_ar': row['title_ar']})
            
            client_type, created = ClientType.objects.get_or_create(name=row['client_type'], defaults={'code': f"CT{index}"})
            if created:
                print(f"Created new client type: {client_type.name} with code {client_type.code}")
                
            client_nature, created = ClientNature.objects.get_or_create(name=row['client_nature'], defaults={'code': f"CN{index}"})
            if created:
                print(f"Created new client nature: {client_nature.name} with code {client_nature.code}")

            Client.objects.create(
                title=title,
                first_name=row['first_name'],
                first_name_ar=row['first_name_ar'],
                family_name=row['family_name'],
                family_name_ar=row['family_name_ar'],
                gender=row['gender'],
                client_type=client_type,
                client_nature=client_nature,
                unique_code=row['unique_code'],
                country=row['country'],
                city=row['city'],
                nationality=row['nationality']
            )
        except Exception as e:
            errors.append(f"Error processing row {index}: {str(e)}")

    if errors:
        for error in errors:
            print(error)
