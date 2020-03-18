var axios = require('axios')

const options = {
  url: 'http://127.0.0.1:8000/api/token/',
  method: 'POST',
  data: {
    'username': 'kevin',
    'password': 'SN8PyP$qJs3T'
  }
};

axios(options)
  .then(response => {
    console.log(response.data);
  });

