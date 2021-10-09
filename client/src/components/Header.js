import React, { Fragment, Component } from 'react';
import { connect } from 'react-redux';
import { compose } from 'redux';
import { withRouter, Link } from 'react-router-dom';
import axiosInstance from '../api/axiosInstance';
import SizeMe from 'react-sizeme'

import AccountBoxIcon from '@material-ui/icons/AccountBox';
import AppBar from '@material-ui/core/AppBar'
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import SearchBar from './SearchBar'
import Toolbar from '@material-ui/core/Toolbar';
import Tooltip from '@material-ui/core/Tooltip';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';

import * as actions from '../actions';
import { checkEmpty }  from '../utilities/checkEmptyObj';
import Form from './Form';

const useStyles = (theme) => ({
  root: {
     flexGrow: 1,
  },
  mainButton: {
     textDecoration: 'none',
     color: '#00ADB5',
  },
  appBarRoot: {
    backgroundColor: '#393E46'
  },
  title: {
     flexGrow: 1,
     color: '#FFFFFF',
  },
  rightSideButtons: {
     textDecoration: 'none',
     color: '#FFFFFF',
  },
  leftAligned: {
     marginLeft: 'auto',
  },
  sellButton: {
    '&:hover': {
      backgroundColor: '#00ADB5',
      color: '#FFFFFF',
   },
  },
  dropdown: {
     '&:focus': {
        backgroundColor: theme.palette.primary.main,
        '& .MuiListItemIcon-root, & .MuiListItemText-primary': {
           color: theme.palette.common.white,
        },
     },
  },
  filterBtn: {
    marginLeft: '10px',
    marginRight: '10px',
    border: `1px solid `,
  },
});

class Header extends Component {
  state = {
    dropDownMenuElement: null,
    search: '',
    anchorEl: null,
  };

  handleAnchorClick = (e) => {
    this.setState({ anchorEl: e.currentTarget });
  };

  handleAnchorClose = () => {
    this.setState({ anchorEl: null });
  };


  doSearch = (e) => {
    this.props.history.push({
      pathname: 'search',
      search: '?search=' + this.state.search,
    });
    window.location.reload();
  };

  handleClick = (e) => {
    this.setState({ dropDownMenuElement: e.currentTarget });
  };

  handleClose = () => {
    this.setState({ dropDownMenuElement: null });
  };

  handleLogout = () => {
    this.handleClose();
    this.props.logoutUser().then(() =>{
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      axiosInstance.defaults.headers['Authorization'] = null;
    });

    this.props.history.push({
      pathname: '/',
    });
  };

  menuDropdown = () => {
    if (this.state.dropDownMenuElement) {
      return (
      <Menu
        id='account-dropdown'
        anchorEl={this.state.dropDownMenuElement}
        getContentAnchorEl={null}
        anchorOrigin={{
          vertical: 'bottom',
          horizontal: 'right',
        }}
        transformOrigin={{
          vertical: 'top',
          horizontal: 'right',
        }}
        elevation={0}
        keepMounted
        open={Boolean(this.state.dropDownMenuElement)}
        onClose={this.handleClose}
        border='1px solid #d3d4d5'
        visible={this.state.dropDownMenuElement}
      >
        <MenuItem className='dropdown' component={Link} to='/myprofile'>
          View Profile
        </MenuItem>
        <MenuItem className='dropdown' component={Link} to='/listing/new'>
          Post Listing
        </MenuItem>
        <MenuItem className='dropdown' onClick={this.handleLogout}>
          Logout
        </MenuItem>
      </Menu>
      );
  } else {
      return;
  }
  };

  getMenuItems(userData, classes, width) {
    if(!checkEmpty(userData)) {
      return (
        <Fragment>
          <Button
            aria-controls='account-dropdown'
            aria-haspopup='true'
            onClick={this.handleClick}
            className={classes.rightSideButtons}
          >
            <AccountBoxIcon 
              style={{ marginRight: '6px' }}
              color='inherit'
            />
            {width >= 500 && (
              <Typography
                variant='h6'
                className={classes.title}
              >
                {`${userData.first_name}`}
              </Typography>
            )}
          </Button>
          {this.menuDropdown()}
        </Fragment>
      );
    } else {
      return;
    }
  }

  getLoginButton(userData, classes) {
    if (checkEmpty(userData)) {
      return (
        <Link 
          to='/login' 
          className={classes.rightSideButtons}
        >
          <Button
            color='inherit'
          >
            <AccountBoxIcon 
              style={{ marginRight: '6px' }}
              color='inherit'
            />
            <Typography 
              variant='h5'
              className={classes.title}
            >
              Login
            </Typography>
          </Button>
        </Link>
      );
    } else {
      return;
    }
  }

  getLabelOrBoth(width, classes) {
    return (
      <Fragment>
        {width >= 500 && (
          <Typography
            style={{ marginLeft: '6px' }}
            variant='h5'
            className={classes.title}
          >
            YourNextRoommates
          </Typography>
        )}
      </Fragment>
    );
  }

  getAdvancedSearch(classes) {
    return (
      <Fragment>
        <Button
          aria-controls='simple-menu'
          aria-haspopup='true'
          onClick={this.handleAnchorClick}
          className={classes.filterBtn}
          color='inherit'
        >
          Advanced Search
        </Button>
        <Menu
          id='simple-menu'
          anchorEl={this.state.anchorEl}
          keepMounted
          open={Boolean(this.state.anchorEl)}
          onClose={this.handleAnchorClose}
        >
          <Form />
        </Menu>
      </ Fragment>
    );
  }

  // getSearchButton() {
  //   return (
  //     <Tooltip 
  //       title='Enter a Canadian city to find listings in.'
  //       aria-label='add'
  //     >
  //       <SearchBar
  //         placeholder={'Enter a City'}
  //         value={this.state.search}
  //         onChange={(query) => this.setState({ search: query })}
  //         onRequestSearch={() => this.doSearch(this.state.search)}
  //       />
  //     </ Tooltip>
  //   );
  // }

  render() {
    const {
      size: {width},
      classes
    } = this.props 

    return (
      <div
        className={classes.root}
      >
        <CssBaseline />
        <AppBar
          position='static'
          className={classes.appBarRoot}
        >
          <Toolbar>
            <Link
              to='/'
              className={classes.mainButton}
            >
              <Button
                color='inherit'
              >
                {this.getLabelOrBoth(width, classes)}
              </Button>
            </Link>
            <div
              className={classes.leftAligned}
            >
              {this.getAdvancedSearch(classes)}
              {this.getMenuItems(this.props.userData, classes, width)}
              {this.getLoginButton(this.props.userData, classes)}
            </div>
          </Toolbar>
        </AppBar>
      </div>
    );
  }
}

function mapStateToProps({ userData }) {
  return { userData };
}

export default compose(
  SizeMe(), 
  withStyles(useStyles),
  withRouter,  
  connect(mapStateToProps, actions)
)(Header);