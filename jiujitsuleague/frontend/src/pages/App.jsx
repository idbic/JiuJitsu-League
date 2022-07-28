import { Component } from 'react';
import Navbar from '../components/navbar'
import './App.css';
import axios from 'axios'
import react from 'react'


export default function App() {

  state = {
    details: [],
  }

  componentDidMount() {

    let data;

    axios.get('http://localhost:8000/wel/')
      .then(res => {
        data = res.data;
        this.setState({
          details: data
        });
      })
      .catch(err => { })
  }

  return (
    <>

      <h1>React Front, Django rear </h1>

    </>



  );
}





