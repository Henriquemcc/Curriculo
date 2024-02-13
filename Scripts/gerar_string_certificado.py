import datetime

from certificate import Certificate

bh = "Belo Horizonte, Minas Gerais, Brasil"
online = "Online"

certificados = []

# AWS Certified Cloud Practitioner
certificados.append(Certificate(name="AWS Certified Cloud Practitioner", url="https://www.credly.com/badges/7623bc5f-4a7a-49d9-9504-26b399105745/linked_in_profile", date=datetime.date(2024, 1, 31), location=bh))

# B2 First – Score 172
certificados.append(Certificate(name="B2 First – Score 172 - Cambridge University Press & Assessment English", url="https://drive.google.com/file/d/1XlpfYXp5Veeiyn8zAHABk8SSAO36QncZ/view?usp=sharing", date=datetime.date(2022, 9, 9), location=bh))

# Networking Basics
certificados.append(Certificate(name="Networking Basics - Cisco", url="https://www.credly.com/badges/c9830260-5298-434e-8955-4eb876480ba6/linked_in_profile", date=datetime.date(2022, 9, 8), location=online))

# Introduction to Cybersecurity
certificados.append(Certificate(name="Introduction to Cybersecurity - Cisco", url="https://www.credly.com/badges/4676e79d-3e11-4856-afc7-38b96e1edc95/linked_in_profile", date=datetime.date(2022, 8, 9), location=online))

# Cursos da Alura
certificados.append(Certificate(name="Cursos da Alura", url="https://cursos.alura.com.br/user/henriquemcc/fullCertificate/ebc4dcd6245bdf46e4d6ffd89a1e3ec2", beginning_date=datetime.datetime(2020, 7, 26), end_date=datetime.datetime(2023, 12, 25), location=online))

# B2 First – Score 166
certificados.append(Certificate(name="B2 First – Score 166 - Cambridge University Press & Assessment English", url="https://drive.google.com/file/d/1_a7pPVYLn72of6atRhqDsAnVPhztZAF9/view?usp=drive_link", location=bh, date=datetime.date(2019, 2, 1), ))


# Ordenando
certificados.sort(key=lambda x: x.date, reverse=True)


# Gerando string
string = ""
for c in certificados:
    string += c.to_latex()
    string += "\n\n"

print(string)