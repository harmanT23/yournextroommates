import React, { Component } from 'react';
import { connect } from 'react-redux';
import { compose } from 'redux';
import { withRouter } from 'react-router-dom';
import axiosInstance from '../api/axiosInstance';

import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import CssBaseline from '@material-ui/core/CssBaseline';
import FormControl from '@material-ui/core/FormControl';
import Grid from '@material-ui/core/Grid';
import InputLabel from '@material-ui/core/InputLabel';
import IconButton from '@material-ui/core/InputLabel';
import { Link } from 'react-router-dom';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import MenuItem from '@material-ui/core/MenuItem';
import Select from '@material-ui/core/Select';
import Typography from '@material-ui/core/Typography';
import { ValidatorForm, TextValidator } from 'react-material-ui-form-validator';
import { withStyles } from '@material-ui/core/styles';

import * as actions from '../actions';

const useStyles = (theme) => ({
   paper: {
      marginTop: theme.spacing(8),
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
   },
   avatar: {
      margin: theme.spacing(1),
      backgroundColor: theme.palette.secondary.main,
   },
   form: {
      width: '100%',
      marginTop: theme.spacing(3),
   },
   submit: {
      margin: theme.spacing(3, 0, 2),
      '&:hover': {
        backgroundColor: '#00ADB5',
        color: '#FFFFFF',
       },
      primary: {
        main: '#393E46'
      }
   },
});

class RegisterPage extends Component {
  state = {
    email: '',
    password: '',
    first_name: '',
    last_name: '',
    date_of_birth: '',
    current_city: '',
    current_province: '',
    profile_picture: '',
    error: ''
  };

  componentDidMount() {
    //Ensure password length is at least 8 chars as required by backend
    ValidatorForm.addValidationRule('passwordLength', (value) => {
      if (value.length < 8) {
        return false;
      }
      return true;
    });

    ValidatorForm.addValidationRule('isLegalAge', (value) => {

      var today = new Date();
      var birthDate = new Date(value);
      var age = today.getFullYear() - birthDate.getFullYear();
      var m_diff = today.getMonth() - birthDate.getMonth();

      if (m_diff < 0 || 
         (m_diff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
      }

      if (age <= 18) {
        return false;
      }

      return true;

    });
    
  }

  componentWillUnmount() {
    // Remove validation checks when component unmounted
    ValidatorForm.removeValidationRule('passwordLength');
    ValidatorForm.removeValidationRule('isLegalAge');
  }

  handleChange = (e) => {
    this.setState({
      ...this.state,
      [e.target.name] : e.target.value,
      error: ''
    })
  };

  handleSubmit = () => {
    //Register then login the user.
    this.props.registerUser({
      username: this.state.username,
      password: this.state.password
    }).then((result) => {
      if (result) {
        this.props.loginUser({
          username: this.state.username,
          password: this.state.password
        }).then((loginResult) => {
          if (loginResult) {
            localStorage.setItem('access_token', loginResult.access);
            localStorage.setItem('refresh_token', loginResult.refresh);
            axiosInstance.defaults.headers['Authorization'] = 
            'JWT ' + localStorage.getItem('access_token');
            this.props.history.push({
              pathname: '/'
            });
          }
        });
      } 
    }).catch((err) => {
      alert('This username is already taken.');
    });
  };

  render() {
    const { classes } = this.props;
    return (
      <Container 
        component='main' 
        maxWidth='xs'
      >
        <CssBaseline />
        <div 
          className={classes.paper}
        >
          <Avatar 
            className={classes.avatar}
          >
            <LockOutlinedIcon />
          </Avatar>
          <Typography 
              component="h1" 
              variant="h5"
          >
              Register
          </Typography>
          <ValidatorForm 
            onSubmit={this.handleSubmit} 
            className={classes.form}
          >
            <Grid 
              container 
              spacing={2}
            >
              <Grid
                item
                xs={12}
              >
                <input
                accept='image/*'
                onChange={this.handleChange}
                id='contained-button-file'
                multiple
                type='file'
                />
                <label htmlFor='contained-button-file'>
                  <IconButton>
                    <Avatar 
                      src='https://source.unsplash.com/random/180x180/?person' 
                      style={{
                        margin: '10px',
                        width: '60px',
                        height: '60px',
                      }} 
                    />
                  </IconButton>
                </label>
              </ Grid>
              <Grid 
                item 
                xs={12}
              >
                <TextValidator
                  validators={['required', 'isEmail']}
                  variant='outlined'
                  fullWidth
                  id='email'
                  label='Email'
                  name='email'
                  autoComplete='your-email'
                  value={this.state.email}
                  onChange={this.handleChange}
                  errorMessages={[
                    'Please enter a email',
                    'Please enter a valid email'
                  ]}
                  error={this.state.error ? true : false}
                  helperText={this.state.error}
                />
              </Grid>
              <Grid 
                item 
                xs={12}
              >
                <TextValidator
                  validators={['required', 'passwordLength']}
                  variant='outlined'
                  fullWidth
                  id='password'
                  label='Password'
                  name='password'
                  autoComplete='create-password'
                  type={'password'}
                  value={this.state.password}
                  onChange={this.handleChange}
                  errorMessages={[
                    'Please enter a password',
                    'Password must be at least 8 characters in length'
                  ]}
                  error={this.state.error ? true : false}
                  helperText={this.state.error}
                />
              </Grid>
              <Grid 
                item 
                xs={12}
              >
                <TextValidator
                  validators={['required']}
                  variant='outlined'
                  fullWidth
                  id='first_name'
                  label='First Name'
                  name='first_name'
                  value={this.state.first_name}
                  onChange={this.handleChange}
                  errorMessages={[
                    'Please enter your first name'
                  ]}
                  error={this.state.error ? true : false}
                  helperText={this.state.error}
                />
              </Grid>
              <Grid 
                item 
                xs={12}
              >
                <TextValidator
                  validators={['required']}
                  variant='outlined'
                  fullWidth
                  id='last_name'
                  label='Last Name'
                  name='last_name'
                  autoComplete='your-first-name'
                  value={this.state.last_name}
                  onChange={this.handleChange}
                  errorMessages={[
                    'Please enter your last name'
                  ]}
                  error={this.state.error ? true : false}
                  helperText={this.state.error}
                />
              </Grid>
              <Grid 
                item 
                xs={12}
              >
                <TextValidator
                  validators={['required', 'isLegalAge']}
                  variant='outlined'
                  fullWidth
                  id='date_of_birth'
                  label='Date of Birth'
                  name='date_of_birth'
                  type={'date'}
                  value={this.state.date_of_birth}
                  onChange={this.handleChange}
                  errorMessages={[
                    'Please enter your date of birth.',
                    'Must be 18 years or older.'
                  ]}
                  error={this.state.error ? true : false}
                  helperText={this.state.error}
                />
              </Grid>
              <Grid 
                item 
                xs={12}
              >
                <TextValidator
                  validators={['required']}
                  variant='outlined'
                  fullWidth
                  id='current_city'
                  label='Current City'
                  name='current_city'
                  autoComplete='your-current-city'
                  value={this.state.current_city}
                  onChange={this.handleChange}
                  errorMessages={[
                    'Please enter a city',
                  ]}
                  error={this.state.error ? true : false}
                  helperText={this.state.error}
                />
              </Grid>
              <Grid 
                item 
                xs={12}
              >
                <FormControl className={classes.formControl}>
                  <InputLabel 
                    id="current_province"
                  >
                    Province
                  </InputLabel>
                  <Select
                    labelId="current_province"
                    id="current_province"
                    name="current_province"
                    onChange={this.handleChange}
                    defaultValue="" 
                  >
                    <MenuItem value=""></MenuItem>
                    <MenuItem value={'Newfoundland and Labrador'}>NL</MenuItem>
                    <MenuItem value={'Prince Edward Island'}>PE</MenuItem>
                    <MenuItem value={'Nova Scotia'}>NS</MenuItem>
                    <MenuItem value={'New Brunswick'}>NB</MenuItem>
                    <MenuItem value={'Quebec'}>QC</MenuItem>
                    <MenuItem value={'Ontario'}>ON</MenuItem>
                    <MenuItem value={'Manitoba'}>MB</MenuItem>
                    <MenuItem value={'Saskatchewan'}>SK</MenuItem>
                    <MenuItem value={'Alberta'}>AB</MenuItem>
                    <MenuItem value={'British Columbia'}>BC</MenuItem>
                    <MenuItem value={'Yukon'}>YT</MenuItem>
                    <MenuItem value={'Northwest Territories'}>NT</MenuItem>
                    <MenuItem value={'Nunavut'}>NU</MenuItem>
                  </Select>
                </FormControl>
              </Grid>
            </Grid>
            <Button
              type='submit'
              fullWidth
              variant='contained'
              color='primary'
              className={classes.submit}
            >
              Register
            </Button>
            <Link
              to='/login'
              variant='body2'
            >
              <Typography 
                component="h1" 
                variant="h5"
              >
                Already have an account? Login
              </Typography>
            </Link>
          </ValidatorForm>
        </div>
      </Container>
    );
  }
}

export default compose(
  withStyles(useStyles), 
  withRouter, 
  connect(null, actions)
)(RegisterPage)