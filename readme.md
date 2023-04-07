# linkedn-get-job

- add .env to main dir. Fill like this

      api-key='<api-key>'
      linkedn_email='<email>'
      linkedn_password='<password>'
      
- While reqesting add X-Access-Token: '<api-key>' header.

- Currently only job description can be parsed. Send get request to / with below body payload.

      {
          "id": "124132412" 
      }