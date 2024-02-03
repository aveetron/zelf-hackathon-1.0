# Zelf Hackathon 1.0

[![N|Solid](https://media.licdn.com/dms/image/C4E0BAQEwxC0Yo5NpNg/company-logo_200_200/0/1659401137386/hellozelf_logo?e=1715212800&v=beta&t=HEXMvOgSUz5kpsre98GXraNVTCWnD_H3FVyw2YZDZ1w)](https://hellozelf.com/)


Backend services designed and developed By Avee Chakraborty

### Proposed Architecture


Modular monolity 
why? We'll get benifits of monolith and benifits of microservice(in a small scale) in this project. 
*depending on the requirements, user load this architecture must need to improve more

### Proposed Solution (Serverless framework & AWS Focused)

[![N|Solid](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaq2iezevpTHCQTkETJ9b-8_OpHhzeeBM8u8wGRWERQw&s)](https://www.djangoproject.com/)
[![N|Solid](https://d1.awsstatic.com/logos/aws-logo-lockups/poweredbyaws/PB_AWS_logo_RGB_stacked_REV_SQ.91cd4af40773cbfbd15577a3c2b8a346fe3e8fa2.png)](https://aws.amazon.com)
[![N|Solid](https://miro.medium.com/v2/resize:fit:877/1*BdKEE3815BcMklgX9jTjIw.png)](https://www.serverless.com/)
[![N|Solid](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgjxDwlHSal7rkNZua5gkuT7iEwJ2yk1_V4RD3dGNTJw&s)](https://www.docker.com/)

- Core Django application will run by it's regular manner
- 3 philosophy of a good software is, the code base, media file 
    and database needs to be seperated. So, i'll use AWS RDS, SQS for Queuing purpose,
    s3 for asset purpose and ec2 or ecs for deployment purpose
- all the background works will be written in Serverless Framework
- Serverless framework is a one stop solution for Different services of AWS. But if we manually configure all those services then lot other manual works are involved for stopping ect
- "software becomes beautiful, when you use Docker" - Avee Chakraborty.  
- for loggin, i'll use discord logger so that if any error occurs can properly send the message immidiatly and kill my sweet sleep in the middle of the night

### Deployment

```sudo docker compose up --build```

### Deployment in detach mode 
``` sudo docker compose build ```
``` sudo docker compose up -d```
# zelf-hackathon-1.0
