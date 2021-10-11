import React, { Component } from 'react';
import { connect } from 'react-redux';
import { compose } from 'redux';
import { withRouter, Link } from 'react-router-dom';
import Carousel from 'react-material-ui-carousel'
import SizeMe from 'react-sizeme'
import Button from '@material-ui/core/Button';
import CircularProgress from '@material-ui/core/CircularProgress';
import Divider from '@material-ui/core/Divider';
import Grid from '@material-ui/core/Grid';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import RoomIcon from '@material-ui/icons/Room';
import SchoolIcon from '@material-ui/icons/School';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';
import WorkIcon from '@material-ui/icons/Work';

import * as actions from '../actions';
import { checkEmpty }  from '../utilities/checkEmptyObj';


const useStyles = (theme) => ({
  rightSideButtons: {
     marginLeft: 'auto',
     textDecoration: 'none',
     '&:hover': {
        backgroundColor: '#00ADB5',
        color: '#FFFFFF',
     },
     primary: {
      main: '#393E46'
    },
  },
});


class UserPage extends Component {
  componentDidMount() {
    this.props.fetchAuthUser();   
    this.props.fetchUser(this.props.location.state.userID);
  }

  state = {
    error: false,
  };

  getUserData() {
    const poster = this.props.sUserData;
    if (!checkEmpty(poster)) {
      return (
      <React.Fragment> 
        <Typography
          gutterBottom
          variant='h2'
          align='center'
        >
          {
            poster.first_name +
            ' ' + poster.last_name
          }
        </Typography>
        <div
          style={{ padding: '5px' }}
        >
          { poster.gallery_set && 
            <Carousel>
              {
                poster.gallery_set[0].gallery_images.map((ele, idx)  => (
                  <img
                    key={idx} 
                    onContextMenu={(e) => {
                      e.preventDefault();
                    }}
                    style={{ width: '100%', height: 'auto', margin: 'auto' }}
                    src={ele.image}
                    alt={'Unavailable'}
                  />
                ))
              }
            </Carousel>
          }
        </div>
        <Typography
          variant='h5'
          align='left'
          color='textPrimary'
          gutterBottom
        >
          About Me
        </Typography>
        <Divider />
        <Typography
          variant='body1'
          align='left'
          color='textPrimary'
          gutterBottom
          style={{ padding: '0px 0px 0px 2px' }}
        >
          {poster.about_me}
        </Typography>
        <Divider />
        <Grid container spacing={2}>
          <Grid item xs={12} sm={6} md={4}>
            <List>
              {
                poster.university && 
                <ListItem>
                  <ListItemIcon>
                  <SchoolIcon />
                  </ListItemIcon>
                  <ListItemText
                    primary= {
                      <React.Fragment>
                        <Typography
                          variant='body1'
                          align='left'
                          color='textSecondary'
                        >
                          {
                            poster.university_major ? 
                            poster.university_major + 
                            ' @ ' + poster.university:
                            poster.university
                          }
                        </Typography>
                      </React.Fragment>
                    }
                  />
                </ListItem>
              }
              {
                poster.university &&
                <Divider variant='inset' component='li' />
              }
              {
                poster.profession && 
                <ListItem>
                  <ListItemIcon>
                  <WorkIcon />
                  </ListItemIcon>
                  <ListItemText
                    primary= {
                      <React.Fragment>
                        <Typography
                          variant='body1'
                          align='left'
                          color='textSecondary'
                        >
                          {
                            poster.profession
                          }
                        </Typography>
                      </React.Fragment>
                    }
                  />
                </ListItem>
              }
              {
                poster.profession &&
                <Divider variant='inset' component='li' />
              }
              {
                poster.city && 
                poster.province &&
                <ListItem>
                  <ListItemIcon>
                  <RoomIcon />
                  </ListItemIcon>
                  <ListItemText
                    primary= {
                      <React.Fragment>
                        <Typography
                          variant='body1'
                          align='left'
                          color='textSecondary'
                        >
                          {
                            poster.city + ', ' +
                            poster.province
                          }
                        </Typography>
                      </React.Fragment>
                    }
                  />
                </ListItem>
              }
              {
                poster.city && 
                poster.province &&
                <Divider variant='inset' component='li' />
              }
            </List>
          </Grid>
        </Grid>
        <div>
          <Link
            to='#'
            onClick={(e) => {
                window.location = 'mailto:' + poster.email;
                e.preventDefault();
            }}
          >
            <Button 
              size='medium' 
              color='secondary'
              style={{ marginLeft: 'auto' }}
            >
              Contact
            </Button>
          </Link>
        </div>
      </React.Fragment>
      ); 
    } else {
      return (
        <React.Fragment>
          <Typography
            variant='h5'
            component='div'
          >
            Fetching user... <CircularProgress />
          </Typography>
        </React.Fragment>
      );
    }
  }

  render() {
    return (
      <div>
        {this.getUserData()}
      </div>
    );
  }
}

function mapStateToProps({ sUserData }) {
  return { sUserData };
}


export default compose(
  SizeMe(),
  withStyles(useStyles), 
  withRouter, 
  connect(mapStateToProps, actions)
)(UserPage);
