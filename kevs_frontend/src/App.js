import React, { Component } from 'react';
import Nav from './components/Nav';
import LoginForm from './components/LoginForm';
import SignupForm from './components/SignupForm';
import axios from 'axios'



class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading",
      url: 'http://localhost:8000'
    };
  }

  componentDidMount() {
    axios
      .post("/api/card", this.state.url)
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          }
        })
      })
  }

  render(){
    return (
    <ul>
      {this.state.data.map(card => {
        return (
          <li key={card.id}>
            {card.name} - {card.price}
          </li>
        );
      })}
    </ul>
  )
}
}


export default App;
