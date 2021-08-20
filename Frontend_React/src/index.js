import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {
  Route,
  BrowserRouter as Router,
  Switch
} from 'react-router-dom';
import App from './App';
import Header from './components/Header';
import Footer from './components/Footer';
import Register from './components/Register';
import Login from './components/Login'
import Logout from './components/Logout'
import SingleListing from './components/SingleListing'

const routing = (
    <Router>
      <React.StrictMode>
        <Header />
        <Switch>
          <Route exact path="/" component={App} />
          <Route path="/register" component={Register} />
          <Route path="/login" component={Login} />
          <Route path="/logout" component={Logout} />
          <Route path="/listings/:slug" component={SingleListing} />
        </Switch>
        <Footer />
      </React.StrictMode>
    </Router>
);

ReactDOM.render(routing, document.getElementById('root'));
