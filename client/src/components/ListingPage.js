import React, { Component } from 'react';
import { connect } from 'react-redux';
import { compose } from 'redux';
import Carousel from 'react-material-ui-carousel'
import SizeMe from 'react-sizeme'
import Avatar from '@material-ui/core/Avatar';
import AcUnitIcon from '@material-ui/icons/AcUnit';
import BathtubIcon from '@material-ui/icons/Bathtub';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import Divider from '@material-ui/core/Divider';
import EventIcon from '@material-ui/icons/Event';
import EventSeatIcon from '@material-ui/icons/EventSeat';
import Grid from '@material-ui/core/Grid';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import LocalLaundryServiceIcon from '@material-ui/icons/LocalLaundryService';
import PeopleIcon from '@material-ui/icons/People';
import PaymentIcon from '@material-ui/icons/Payment';
import ReceiptIcon from '@material-ui/icons/Receipt';
import SchoolIcon from '@material-ui/icons/School';
import SingleBedIcon from '@material-ui/icons/SingleBed';
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

class ListingPage extends Component {
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
          {this.props.listing.listing_title}
        </Typography>
        <Divider />
        <Typography
          variant='h4'
          align='left'
          color='textPrimary'
          gutterBottom
        >
          About this listing
        </Typography>
        <Divider />
        <Typography
          variant='body1'
          align='left'
          color='textSecondary'
          gutterBottom
        >
          {this.props.listing.room_desc}
        </Typography>
        <Typography
          variant='h4'
          align='left'
          color='textPrimary'
          gutterBottom
        >
          Where you'll sleep
        </Typography>
        <Divider />
        <Typography
          variant='body1'
          align='left'
          color='textSecondary'
        >
        <SingleBedIcon/> 
        <span> &nbsp; </span>  
        {this.props.listing.room_type}
        </Typography>
        <Typography
          variant='h4'
          align='left'
          color='textPrimary'
          gutterBottom
        >
          Where you'll be located
        </Typography>
        <Divider />
        <Typography
          variant='body1'
          align='left'
          color='textSecondary'
        >
          { 
          (this.props.listing.address2 ? this.props.listing.address2 + ' - ':'') 
            + this.props.listing.address1 + ', ' + this.props.listing.city + ', ' 
            + this.props.listing.province
          }
        </Typography>
        <Typography
          variant='h4'
          align='left'
          color='textPrimary'
          gutterBottom
        >
          The Unit
        </Typography>
        <Divider />
        <Grid container spacing={2}>
          <Grid item xs={12} sm={6} md={4}>
            <List>
              {
                this.props.listing.is_furnished && 
                <ListItem>
                  <ListItemIcon>
                  <EventSeatIcon />
                  </ListItemIcon>
                  <ListItemText
                    primary= {
                      <React.Fragment>
                        <Typography
                          variant='body1'
                          align='left'
                          color='textSecondary'
								        >
                          Furnished
                        </Typography>
                      </React.Fragment>
                    }
                  />
                </ListItem>
              }
              {
                this.props.listing.is_furnished &&
                <Divider variant='inset' component='li' />
              }
              {
                this.props.listing.is_laundry_ensuite && 
                <ListItem>
                  <ListItemIcon>
                  <LocalLaundryServiceIcon />
                  </ListItemIcon>
                  <ListItemText
                    primary= {
                      <React.Fragment>
                        <Typography
                          variant='body1'
                          align='left'
                          color='textSecondary'
								        >
                          Ensuite Laundry 
                        </Typography>
                      </React.Fragment>
                    }
                  />
                </ListItem>
              }
              {
                this.props.listing.is_laundry_ensuite &&
                <Divider variant='inset' component='li' />
              }
              {
                this.props.listing.is_air_conditioned && 
                <ListItem>
                  <ListItemIcon>
                  <AcUnitIcon />
                  </ListItemIcon>
                  <ListItemText
                    primary= {
                      <React.Fragment>
                        <Typography
                          variant='body1'
                          align='left'
                          color='textSecondary'
								        >
                          Air Conditioning
                        </Typography>
                      </React.Fragment>
                    }
                  />
                </ListItem>
              }
              {
                this.props.listing.is_air_conditioned &&
                <Divider variant='inset' component='li' />
              }
              {
                this.props.listing.number_of_bathrooms > 0 && 
                <ListItem>
                  <ListItemIcon>
                  <BathtubIcon />
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
                            this.props.listing.number_of_bathrooms > 1 ?
                              'Bathrooms' : 'Bathroom'
                          }	
                        </Typography>
                      </React.Fragment>
                    }
                  />
                </ListItem>
              }
              {
                this.props.listing.number_of_bathrooms > 0 &&
                <Divider variant='inset' component='li' />
              }
              {
                this.props.listing.number_of_residents > 0 && 
                <ListItem>
                  <ListItemIcon>
                  <PeopleIcon />
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
                            this.props.listing.number_of_residents > 1 ?
                            'Roommates' : 'Roommate'
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
        <Typography
          variant='h4'
          align='left'
          color='textPrimary'
          gutterBottom
        >
          The Details
        </Typography>
        <Divider />
        <Grid container spacing={2}>
          <Grid item xs={12} sm={6} md={4}>
            <List>
              <ListItem>
                <ListItemIcon>
                  <EventIcon />
                </ListItemIcon>
                <ListItemText
                  primary= {
                    <React.Fragment>
                      <Typography
                        variant='body1'
                        align='left'
                        color='textSecondary'
                      >
                        Earliest Move-In Date: {
                          this.props.listing.earliest_move_in_date
                        }
                      </Typography>
                    </React.Fragment>
                  }
                />
              </ListItem>
              <ListItem>
                <ListItemIcon>
                  <PaymentIcon />
                </ListItemIcon>
                <ListItemText
                  primary= {
                    <React.Fragment>
                      <Typography
                        variant='body1'
                        align='left'
                        color='textSecondary'
                      >
                        Monthly Rent ${
                          this.props.listing.rent_per_month
                        }
                      </Typography>
                    </React.Fragment>
                  }
                />
              </ListItem>
              <ListItem>
                <ListItemIcon>
                  <ReceiptIcon />
                </ListItemIcon>
                <ListItemText
                  primary= {
                    <React.Fragment>
                      <Typography
                        variant='body1'
                        align='left'
                        color='textSecondary'
                      >
                        Extra Monthly Expenses ${
                          this.props.listing.extra_expenses_per_month
                        }
                      </Typography>
                    </React.Fragment>
                  }
                />
              </ListItem>
            </List>
          </Grid>
        </Grid>
        <Typography
          variant='h5'
          align='left'
          color='textPrimary'
          gutterBottom
        >
          Poster
        </Typography>
        <Grid container spacing={1}>
          <Grid item xs={12} sm={6} md={5}>
            <List sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
              <ListItem alignItems='flex-start'>
                <ListItemAvatar>
                  <Avatar 
                    alt= {
                      this.props.listing.poster.first_name + ' ' + 
                      this.props.listing.poster.last_name
                    }
                    src={this.props.listing.poster.profile_picture} />
                </ListItemAvatar>
                <ListItemText
                  primary={ this.props.listing.poster.first_name + ' ' + 
                            this.props.listing.poster.last_name
                  }
                  secondary={
                    <React.Fragment>
                      <Typography
                        sx={{ display: 'inline' }}
                        component='span'
                        variant='body2'
                        color='text.primary'
                      >
                        <SchoolIcon /> <span> &nbsp; </span> 
                        {
                          this.props.listing.poster.university_major ? 
                          this.props.listing.poster.university_major + 
                          ' @ ' + this.props.listing.poster.university: ''
                        }
                        <br/>
                        <WorkIcon /> <span> &nbsp; </span> 
                        {
                          this.props.listing.poster.profession ? 
                          this.props.listing.poster.profession: ''
                        }
                      </Typography>
                    </React.Fragment>
                  }
              />
              </ListItem>
            </List>
            <div>
              <Box component='span' m={0}>
                <Button size='small' variant='contained' color='primary'>
                  View
                </Button>
              </Box>
              <Box component='span' m={1}>
                <Button size='small' variant='contained' color='primary'>
                  Contact
                </Button>
              </Box>
            </div>
          </Grid>
        </Grid>
        <Carousel>
          {
            this.props.listing.gallery_set.map((image, idx) => (
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
)(ListingPage);
