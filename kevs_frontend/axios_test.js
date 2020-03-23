var axios = require('axios')

/*
const options = {
  url: 'http://127.0.0.1:8000/api/login/',
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
  */
axios.post('http://127.0.0.1:8000/api/login/', {
  username: 'erica',
  password: 'baby2605'
  }
)
.then((response) => {
  console.log(response);
}, (error) => {
  console.log(error);
});

