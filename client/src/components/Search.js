import React, { Component } from 'react';
import { connect } from 'react-redux';
import { compose } from 'redux';
import { withRouter, Link } from 'react-router-dom';
import SizeMe from 'react-sizeme';
import StackGrid from 'react-stack-grid';
import axiosInstance from '../api/axiosInstance';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardHeader from '@material-ui/core/CardHeader';
import Checkbox from '@material-ui/core/Checkbox';
import Container from '@material-ui/core/Container';
import CssBaseline from '@material-ui/core/CssBaseline';
import IconButton from '@material-ui/core/IconButton';
import { red } from '@material-ui/core/colors';
import ShareIcon from '@material-ui/icons/Share';
import Typography from '@material-ui/core/Typography';

import * as actions from '../actions';
import { checkEmpty }  from '../utilities/checkEmptyObj';

class Search extends Component {
  state = {
    search: '',
    listings: [],
  }

  componentDidMount() {
    this.props.fetchAuthUser();

    axiosInstance.get('/listings/' + window.location.search).then((res) => {
      this.setState({listings: res.data});
      this.setState({search: window.location.search});
    })
  }

  getCityTitle() {
    const listings = this.state.listings;
    if (!checkEmpty(listings)) {
      return (
        <div>
          <Container maxWidth="sm">
            <Typography 
              component="h1" 
              variant="h2" 
              align="center" 
              color="textPrimary" 
              gutterBottom
            >
              Listings in {listings[0].city + ', ' + listings[0].province}
            </Typography>
          </Container>
        </div>
      );
    }
  }

  getLoadingDisplay() {
    const listings = this.state.listings;
    if (checkEmpty(listings)) {
      return (
        <React.Fragment>
          <Typography
            variant='h5'
            component='div'
          >
            No listings found that meet your search criteria
          </Typography>
        </React.Fragment>
      );
    } else return;
  }

  getlistings() {
    const listings = Array.from(this.state.listings);
    if (!checkEmpty(listings))  {
      return listings.map((listing, idx) => (
        <div 
         key={idx}
        >
         <figure
           style = {{ margin: 10 }}
         >
           <Card>
            <CardHeader
              title={listing.listing_title}
              titleTypographyProps={{
                variant:'h6', 
                fontSize:'fontSize', 
                fontWeight:'fontWeightLight',
              }}
              style={{ textAlign: 'center' }}
              subheader= {'Listed by ' + listing.poster.first_name}
              avatar={
                <Avatar 
                  alt={
                    listing.poster.first_name + ' ' + listing.poster.last_name
                  }
                  src={listing.poster.profile_picture}
                  style={{ backgroundColor: red[500] }}
                >
                </Avatar>
              }
            />
             <img 
               onContextMenu={(e) => {
                 e.preventDefault();
               }}
               style={{ width: '100%', height: 'auto', margin: 'auto' }}
               src={listing.gallery_set[0].gallery_images[0].image}
               alt={'None'}
             />{' '}
            <div
              style={{ padding: '5px' }}
            >
              <CardContent 
                style ={{ flexGrow: 1 }}
              >
                <Typography 
                  gutterBottom 
                  variant='h5' 
                  component='h2'
                >
                  { 
                    (listing.address2 ? listing.address2 + ' - ':'') + 
                      listing.address1 + ', ' + listing.city + ', ' + 
                      listing.province 
                  }
                </Typography>
                <Typography
                  component='' 
                  variant='body1' 
                  align='left'
                 >
                  <strong> { '$' + listing.rent_per_month } </strong> per month
                 </Typography>
                 <Typography
                    component='' 
                    variant='body2' 
                    align='left'
                 >
                   {listing.room_type}
                 </Typography>
                 <Typography
                  component='' 
                  variant='body2' 
                  align='left'
                 >
                  Earliest move-in date: 
                  <strong> {listing.earliest_move_in_date} </strong>
                 </Typography>
                 <Typography 
                    component='' 
                    variant='body2' 
                    align='left'
                  >
                    Lease duration: 
                    <strong> {listing.length_of_lease} months </strong> 
                  </Typography>
                <Typography 
                  component='' 
                  variant='body2' 
                  align='left'
                  style = {{ 
                    display: 'flex',
                    alignItems: 'center',
                    flexWrap: 'wrap'
                  }}
                >
                  Furnished
                  <Checkbox
                    checked = {listing.is_furnished}
                  />
                </Typography>
              </CardContent>
              <CardActions 
                disableSpacing
              >
                <Link
                  color='textPrimary'
                  to= {{
                    pathname:'/listing/' + listing.slug,
                  }}
                >
                  <Button 
                    size='medium'
                    color='secondary'
                    style={{ marginLeft: 'auto' }}
                  >
                    View
                  </Button>
                </Link>
                <IconButton 
                  aria-label='share'
                >
                  <ShareIcon />
                </IconButton>
                </CardActions>
             </div>
           </Card>
         </figure>
        </div>
       ));
    }
  }

  render() {
    const {
      size: { width },
    } = this.props;
    let colWidth = '33.33%';

    if (width <= 768) colWidth = '50%';
    if (width <= 450) colWidth = '80%';

    return(
      <div 
        style={{ width: '80%', margin: 'auto' }}
      >
        <CssBaseline />
        {this.getCityTitle()}
        <StackGrid
          monitorImagesLoaded={true}
          columnWidth={colWidth}
        >
          {this.getLoadingDisplay()}
          {this.getlistings()}
        </StackGrid>
      </div>
    );
  }
}

export default compose(
  SizeMe(),
  withRouter,  
  connect(null, actions)
)(Search);
