import datetime

from certificate import Certificate

bh = "Belo Horizonte, Minas Gerais, Brazil"
online = "Online"

certificados = []

# Formação Kotlin e Spring Boot
certificados.append(Certificate(name="Kotlin and Spring Boot Course - Alura", url="https://cursos.alura.com.br/degree/certificate/09cbf228-4894-4225-bf0e-6be933822ffe?lang", github="https://github.com/Henriquemcc/Forum_-_Formacao_Kotlin_e_Spring_Boot_-_Alura", location=online, date=datetime.date(2025, 3, 21)))

# React: comece seu projeto full stack
certificados.append(Certificate(name="React: Start your full stack project - Alura", url="https://cursos.alura.com.br/certificate/b4f48602-24d3-4fce-928f-0038f178004a?lang", github="https://github.com/Henriquemcc/Alura_Books_-_Formacao_Full_stack_JavaScript_-_Alura", date=datetime.date(2025, 1, 16), location=online))

# Endpoint Security
certificados.append(Certificate(name="Endpoint Security - Cisco", url="https://www.credly.com/badges/dd945a87-ba32-4732-9ea5-88198208599f/linked_in_profile", date=datetime.date(2024, 3, 24), location=online))

# AWS Certified Cloud Practitioner
certificados.append(Certificate(name="AWS Certified Cloud Practitioner", url="https://www.credly.com/badges/7623bc5f-4a7a-49d9-9504-26b399105745/linked_in_profile", date=datetime.date(2024, 1, 31), location=bh))

# Cursos da Alura
certificados.append(Certificate(name="Alura's Courses", url="https://cursos.alura.com.br/user/henriquemcc/fullCertificate/ebc4dcd6245bdf46e4d6ffd89a1e3ec2", beginning_date=datetime.date(2020, 7, 26), end_date=datetime.date(2023, 12, 25), location=online))

# B2 First – Score 172
certificados.append(Certificate(name="B2 First – Score 172 - Cambridge University Press & Assessment English", url="https://drive.google.com/file/d/1XlpfYXp5Veeiyn8zAHABk8SSAO36QncZ/view?usp=sharing", date=datetime.date(2022, 9, 9), location=bh))

# Networking Basics
certificados.append(Certificate(name="Networking Basics - Cisco", url="https://www.credly.com/badges/c9830260-5298-434e-8955-4eb876480ba6/linked_in_profile", date=datetime.date(2022, 9, 8), location=online))

# Introduction to Cybersecurity
certificados.append(Certificate(name="Introduction to Cybersecurity - Cisco", url="https://www.credly.com/badges/4676e79d-3e11-4856-afc7-38b96e1edc95/linked_in_profile", date=datetime.date(2022, 8, 9), location=online))

# Formação Linguagem Kotlin - Alura
certificados.append(Certificate(name="Kotlin Language Course - Alura", url="https://cursos.alura.com.br/degree/certificate/18f608ec-a511-43b4-8586-04c87b079a4c?lang", date=datetime.date(2021, 7, 7), location=online))

# Formação Python - Alura
certificados.append(Certificate(name="Python Course - Alura", url="https://cursos.alura.com.br/degree/certificate/b96bda48-dc02-4105-9ca5-ae64c2e135e3?lang", date=datetime.date(2020, 8, 14), location=online))


# Ordenando
certificados.sort(key=lambda x: x.date, reverse=True)


# Gerando string
string = ""
for c in certificados:
    string += c.to_latex()
    string += "\n\n"

print(string)