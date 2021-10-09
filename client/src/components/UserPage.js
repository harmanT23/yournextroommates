import React, { Component } from 'react';
import { connect } from 'react-redux';
import { compose } from 'redux';
import Carousel from 'react-material-ui-carousel'
import SizeMe from 'react-sizeme'
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import Divider from '@material-ui/core/Divider';
import Grid from '@material-ui/core/Grid';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import SchoolIcon from '@material-ui/icons/School';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';
import WorkIcon from '@material-ui/icons/Work';

import * as actions from '../actions';


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
  state = {
    error: false,
  };

  render() {
    return (
      <div>
        <Typography
          gutterBottom
          variant='h2'
          align='center'
        >
          {
            this.props.userData.first_name +
            ' ' + this.props.userData.last_name
          }
        </Typography>
        <Divider />
        <Typography
          variant='h4'
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
          color='textSecondary'
          gutterBottom
        >
          {this.props.userData.about_me}
        </Typography>
        <Divider />
        <Grid container spacing={2}>
          <Grid item xs={12} sm={6} md={4}>
            <List>
              {
                this.props.userData.university && 
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
                            this.props.userData.university + 
                            ', ' + this.props.userData.university_major
                          }
                        </Typography>
                      </React.Fragment>
                    }
                  />
                </ListItem>
              }
              {
                this.props.userData.university &&
                <Divider variant='inset' component='li' />
              }
              {
                this.props.userData.profession && 
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
                            this.props.userData.profession
                          }
                        </Typography>
                      </React.Fragment>
                    }
                  />
                </ListItem>
              }
            </List>
          </Grid>
        </Grid>
        <div>
          <Box component='span' m={0}>
            <Button size='small' variant='contained' color='primary'>
              Contact
            </Button>
          </Box>
        </div>
        <Carousel>
          {
            this.props.userData.gallery_set.map((image, idx) => (
              <img 
                onContextMenu={(e) => {
                  e.preventDefault();
                }}
                style={{ width: '100%', height: 'auto', margin: 'auto' }}
                src={image.image_url}
                alt={'Unavailable'}
              />
            ))
          }
        </Carousel> 
      </div>
    );
  }
}


export default compose(
  SizeMe(),
  withStyles(useStyles), 
  connect(null, actions)
)(UserPage);
