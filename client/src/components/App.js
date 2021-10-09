import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from '../actions';


import Header from './Header';
import RegisterPage from './RegisterPage'
import LoginPage from './LoginPage';
import ListingGrid from './ListingGrid';
import ListingPage from './ListingPage'
import UserPage from './UserPage';

class App extends Component {  
  render() {
    return (
      <BrowserRouter>
        <Header />
        <div>
          <Switch>
            <Route path= '/' exact component={ListingGrid} />
            <Route path= '/register' exact component={RegisterPage} />
            <Route path='/login' exact component={LoginPage} />
            <Route path='/listing' exact component={ListingPage} />
            <Route path='/user' exact component={UserPage} />
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default connect(null, actions)(App)
