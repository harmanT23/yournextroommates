import React, { Component } from 'react';
import { connect } from 'react-redux';
import { compose } from 'redux';
import { withRouter, Link } from 'react-router-dom';
import Carousel from 'react-material-ui-carousel'
import SizeMe from 'react-sizeme'
import Avatar from '@material-ui/core/Avatar';
import AcUnitIcon from '@material-ui/icons/AcUnit';
import BathtubIcon from '@material-ui/icons/Bathtub';
import Button from '@material-ui/core/Button';
import CircularProgress from '@material-ui/core/CircularProgress';
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
    }
  },
});

class ListingPage extends Component {
  componentDidMount() {
    this.props.fetchAuthUser();   
    this.props.fetchListing(this.props.match.params.slug);
  }

  getListingContent() {
    const listing = this.props.listingData;
    
    if (!checkEmpty(listing)) {
      return (
        <React.Fragment>
          <Typography
            gutterBottom
            variant='h2'
            align='center'
          >
            {listing.listing_title}
          </Typography>
          <div
            style={{ padding: '15px' }}
          >
            { listing.gallery_set && 
              <Carousel>
                {
                  listing.gallery_set[0].gallery_images.map((ele, idx) => (
                    <img
                      key= {idx}
                      onContextMenu={(e) => {
                        e.preventDefault();
                      }}
                      style={{ objectFit: 'cover', width: '100%', height: '680px', margin: 'auto' }}
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
            About this listing
          </Typography>
          <Divider />
          <Typography
            variant='body1'
            align='left'
            color='textPrimary'
            gutterBottom
            component='div'
          >
            {listing.room_desc}
          </Typography>
          <Typography
            variant='h5'
            align='left'
            color='textPrimary'
            gutterBottom
            style={{ padding: '10px 0px 0px 0px' }}
          >
            Where you'll sleep
          </Typography>
          <Divider />
          <Typography
            variant='body1'
            align='left'
            color='textPrimary'
            component='div'
            style={{
              display: 'flex',
              alignItems: 'center',
              flexWrap: 'wrap',
            }}
          >
            <SingleBedIcon/> 
            <span> &nbsp; </span>  
            {listing.room_type}
          </Typography>
          <Typography
            variant='h5'
            align='left'
            color='textPrimary'
            gutterBottom
            style={{ padding: '10px 0px 0px 0px' }}
          >
            Where you'll be located
          </Typography>
          <Divider />
          <Typography
            variant='body1'
            align='left'
            color='textPrimary'
            component='div'
          >
            { 
            (listing.address2 ? listing.address2 + ' - ':'') 
              + listing.address1 + ', ' + listing.city + ', ' 
              + listing.province
            }
          </Typography>
          <Typography
            variant='h5'
            align='left'
            color='textPrimary'
            gutterBottom
            style={{ padding: '10px 0px 0px 0px' }}
          >
            The Unit
          </Typography>
          <Divider />
          <Grid container spacing={2}>
            <Grid item xs={12} sm={6} md={4}>
              <List>
                {
                  listing.is_furnished && 
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
                  listing.is_furnished &&
                  <Divider variant='inset' component='li' />
                }
                {
                  listing.is_laundry_ensuite && 
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
                  listing.is_laundry_ensuite &&
                  <Divider variant='inset' component='li' />
                }
                {
                  listing.is_air_conditioned && 
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
                  listing.is_air_conditioned &&
                  <Divider variant='inset' component='li' />
                }
                {
                  listing.number_of_bathrooms > 0 && 
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
                              listing.number_of_bathrooms
                            }
                            {
                              listing.number_of_bathrooms > 1 ?
                                ' Bathrooms' : ' Bathroom'
                            }	
                          </Typography>
                        </React.Fragment>
                      }
                    />
                  </ListItem>
                }
                {
                  listing.number_of_bathrooms > 0 &&
                  <Divider variant='inset' component='li' />
                }
                {
                  listing.number_of_residents > 0 && 
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
                              listing.number_of_residents
                            }
                            {
                              listing.number_of_residents > 1 ?
                              ' Roommates' : ' Roommate'
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
            variant='h5'
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
                          <strong>
                            Earliest Move-In Date: {
                              listing.earliest_move_in_date
                            }
                          </strong>
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
                          <strong>
                            Monthly Rent: ${
                              listing.rent_per_month
                            }
                          </strong>
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
                          <strong>
                            Extra Monthly Expenses: ${
                              listing.extra_expenses_per_month
                            }
                          </strong>
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
            Roommate
          </Typography>
          <Divider />
          {
            listing.poster && 
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6} md={6}>
                <List 
                  sx={{ 
                    width: '100%', 
                    maxWidth: 360, 
                    bgcolor: 'background.paper' 
                  }}
                >
                  <ListItem alignItems='flex-start'>
                    <ListItemAvatar>
                      <Avatar 
                        alt= {
                          listing.poster.first_name + ' ' + 
                          listing.poster.last_name
                        }
                        src={listing.poster.profile_picture} />
                    </ListItemAvatar>
                    <ListItemText
                      primary={
                        listing.poster.first_name + ' ' +
                        listing.poster.last_name
                      }
                      secondary={
                        <React.Fragment>
                          <Typography
                            component='span'
                            variant='body2'
                            color='textPrimary'
                            style={{
                              display: 'flex',
                              alignItems: 'center',
                              flexWrap: 'nowrap',  
                            }}
                          >
                            {
                              listing.poster.university &&
                              <React.Fragment> 
                              <SchoolIcon /> <span> &nbsp; </span> 
                              {
                                listing.poster.university_major ? 
                                listing.poster.university_major + 
                                ' @ ' + listing.poster.university:
                                listing.poster.university
                              }
                              </React.Fragment>
                            }
                          </Typography>
                          <Typography
                            component='span'
                            variant='body2'
                            color='textPrimary'
                            style={{
                              display: 'flex',
                              alignItems: 'center',
                              flexWrap: 'nowrap',
                            }}
                          >
                            {
                              listing.poster.profession &&
                              <React.Fragment>
                                <WorkIcon /> <span> &nbsp; </span> 
                                {listing.poster.profession}
                              </React.Fragment> 
                            }
                          </Typography>
                          <div
                            style={{ padding: '5px 0px 0px 0px' }}
                          >
                            <Link
                              to= {{
                                pathname:'/user/',
                                state: { 
                                  userID: listing.poster.id 
                                }
                              }}
                            >
                              <Button 
                                size='small' 
                                color='secondary'
                                style={{ marginLeft: 'auto' }}
                              >
                                View
                              </Button>
                            </Link>
                            &nbsp;
                            <Link
                              to='#'
                              onClick={(e) => {
                                  window.location = 'mailto:' + listing.poster.email;
                                  e.preventDefault();
                              }}
                            >
                              <Button 
                                size='small' 
                                color='secondary'
                                style={{ marginLeft: 'auto' }}
                              >
                                Contact
                              </Button>
                            </Link>
                          </div>
                        </React.Fragment>
                      }
                  />
                  </ListItem>
                </List>
              </Grid>
            </Grid>
        }
        </React.Fragment>
      )} else {
        return (
          <React.Fragment>
            <Typography
              variant='h5'
              component='div'
            >
              Fetching listing... <CircularProgress />
            </Typography>
          </React.Fragment>
        );
      }
  }
  
  render() {
    return (
      <div
        style = {{width: '50%', margin: 'auto'}}
      >
        {this.getListingContent()}
      </div>
    );
  }
}

function mapStateToProps({ listingData }) {
  return { listingData };
}

export default compose(
  SizeMe(),
  withStyles(useStyles), 
  withRouter, 
  connect(mapStateToProps, actions)
)(ListingPage);
