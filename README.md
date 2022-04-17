# Questionnaire

Building a web app for financial solutions where users will
answer a questionnaire and a business plan will be generated for them.
Task is to simulate this environment and build the APIs needed to
return the questions to the front-end and save the answers in the database

#### Tech stack
- Python
- Django
- DRF
- Postgres
- JWT

#### User Flow
- Create account from `{{base_url}}/auth/register/`
- Login `{{base_url}}/auth/login/`
- Create bussiness plan `{{base_url}}/questionnaire/plan`
- Get Question `{{base_url}}/questionnaire/question/`
- Click Save `{{base_url}}/questionnaire/save/`
- After complete your flow list your question `{{base_url}}/questionnaire/plan/questions`
- If you want to update your answer `{{base_url}}/questionnaire/answer/1` 


#### Postman
https://www.getpostman.com/collections/fb0d2d979ae72c04211b
