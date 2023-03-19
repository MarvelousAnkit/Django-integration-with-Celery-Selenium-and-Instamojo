# Django-integration-with-Celery-Selenium-and-Instamojo
Hello there! I am pleased to inform you that I have started a small startup at Amity University Patna that provides printout services to students.



 To use our service, students can visit printf.in, upload their document, and let our Python automation take care of the rest.

I have integrated Django with Selenium and Celery to automate the backend process. As soon as someone uploads their document, the Selenium code runs, opens WhatsApp Web, and sends me the document along with the user's details. This process follows the principle of "first in, first out" because of Celery framework. 

The best part is that Selenium and Celery will work in parallel with the view function, resulting in multitasking capabilities



In addition to the aforementioned services, our website also offers a unique feature that converts normal text to handwritten text. This innovative feature will assist students in completing their assignments with ease. To accept payment, I have used the Instamojo payment gateway.



Visit Now - printf.in

Some usefull command To Run celery 
To run celery
celery -A Website worker --pool=solo -l info

To delete all pending Task
celery -A Website purge
