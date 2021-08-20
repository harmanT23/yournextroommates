import React, { useState, useEffect } from 'react';
import axiosInstance from '../Axios';
import clsx from 'clsx';
// Material UI
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Collapse from '@material-ui/core/Collapse';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import Link from '@material-ui/core/Link';
import IconButton from '@material-ui/core/IconButton';
import FavoriteIcon from '@material-ui/icons/Favorite';
import ShareIcon from '@material-ui/icons/Share';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import Avatar from '@material-ui/core/Avatar';
import Checkbox from '@material-ui/core/Checkbox';
import Button from '@material-ui/core/Button';
import { red } from '@material-ui/core/colors';

const useStyles = makeStyles((theme) => ({
  '@global': {
    ul: {
      margin: 0,
      padding: 0,
      listStyle: 'none',
    },
  },
	cardMedia: {
		paddingTop: '56.25%', // 16:9
	},
	link: {
		margin: theme.spacing(1, 1.5),
	},
	cardHeader: {
		backgroundColor:
			theme.palette.type === 'light'
				? theme.palette.grey[200]
				: theme.palette.grey[700],
	},
  cardGrid: {
    paddingTop: theme.spacing(8),
    paddingBottom: theme.spacing(8),
  },
  card: {
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
  },
  cardContent: {
    flexGrow: 1,
  },
  media: {
    height: 0,
    paddingTop: '56.25%', // 16:9
  },
  expand: {
    transform: 'rotate(0deg)',
    marginLeft: 'auto',
    transition: theme.transitions.create('transform', {
      duration: theme.transitions.duration.shortest,
    }),
  },
  expandOpen: {
    transform: 'rotate(180deg)',
  },
  icon: {
    marginRight: theme.spacing(2),
  },
  avatar: {
    backgroundColor: red[500],
  },
	listingTitle: {
		fontSize: '16px',
		textAlign: 'left',
	},
	listingText: {
		display: 'flex',
		justifyContent: 'left',
		alignItems: 'baseline',
		fontSize: '12px',
		textAlign: 'left',
		marginBottom: theme.spacing(2),
	},
  wrapIcon: {
		display: 'flex',
		alignItems: 'center',
		flexWrap: 'wrap',
	},
}));

const Search = () => {
	const classes = useStyles();
	const search = 'listings';
	const [appState, setAppState] = useState({
		search: '',
		listings: [],
	});

  const [expanded, setExpanded] = React.useState(false);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

	useEffect(() => {
		axiosInstance.get(search + '/' + window.location.search).then((res) => {
			const allListings = res.data;
			setAppState({ listings: allListings });
			console.log(res.data);
		});
	}, [setAppState]);

  if (!appState.listings || appState.listings.length === 0) {
    return (
      <Typography variant="h5" align="center" color="textSecondary" paragraph>
        We cannot find any listings matching your search criteria. Check back later!
      </Typography>
    );
  }

	return (
		<React.Fragment>
      <div className={classes.heroContent}>
        <Container maxWidth="sm">
          <Typography 
            component="h1" 
            variant="h2" 
            align="center" 
            color="textPrimary" 
            gutterBottom
          >
            Listings in {appState.listings[0].city}
          </Typography>
        </Container>
      </div>
			<Container maxWidth="md" component="main">
				<Grid container spacing={5} alignItems="flex-end">
					{appState.listings.map((listing) => {
						return (
							// Enterprise card is full width at sm breakpoint
							<Grid item key={listing.id} xs={12} md={4}>
								<Card className={classes.card}>
                <Link
                    color="textPrimary"
                    href={'listings/' + listing.slug}
                    className={classes.Link}
                >
                <CardHeader
                    avatar={
                      <Avatar 
                        alt={listing.poster.first_name + " " + listing.poster.last_name}
                        className={classes.avatar}
                        src="https://source.unsplash.com/random/100x100/?person" 
                      >
                      </Avatar>
                    }
                    action={
                      <IconButton aria-label="settings">
                        <MoreVertIcon />
                      </IconButton>
                    }
                    title={listing.listing_title}
                    subheader= {"Listed by " + listing.poster.first_name}
                  />
                  </Link>
                  <CardMedia
                    className={classes.cardMedia}
                    image="https://source.unsplash.com/random/320x180/?condo"
                    title="Image title"
                  />
                  <CardContent className={classes.cardContent}>
                    <Typography gutterBottom variant="h5" component="h2">
                      { (listing.address2 ? listing.address2 + " - ":"") + listing.address1}
                    </Typography>
                    <Typography 
                          component="" 
                          variant="body1" 
                          align="left"
                        >
                         <strong>{ "$" + listing.rent_per_month}</strong> per month
                    </Typography>
                    <Typography 
                          component="" 
                          variant="body2" 
                          align="left"
                    >
                      {listing.room_type}
                    </Typography>
                    <Typography 
                        component="" 
                        variant="body2" 
                        align="left"
                    >
                        Earliest move-in date <strong>
                              {listing.earliest_move_in_date}</strong>
                    </Typography>
                    <Typography 
                        component="" 
                        variant="body2" 
                        align="left"
                      >
                        Lease duration <strong>
                              {listing.length_of_lease} months</strong> 
                  </Typography>
                  <Typography 
                        component="" 
                        variant="body2" 
                        align="left"
                        className={classes.wrapIcon}
                      >
                    
                      Furnished
                      <Checkbox
                        checked = {listing.is_furnished}
                      />
                  </Typography> 
                  </CardContent>
                  <CardActions disableSpacing>
                    <Button size="small" color="primary">
                      View
                    </Button>
                    <IconButton aria-label="add to favorites">
                      <FavoriteIcon />
                    </IconButton>
                    <IconButton aria-label="share">
                      <ShareIcon />
                    </IconButton>
                    <IconButton
                      className={clsx(classes.expand, {
                        [classes.expandOpen]: expanded,
                      })}
                      onClick={handleExpandClick}
                      aria-expanded={expanded}
                      aria-label="show more"
                    >
                      <ExpandMoreIcon />
                    </IconButton>
                  </CardActions>
                  <Collapse in={expanded} timeout="auto" unmountOnExit>
                    <CardContent>
                    <ul>
                      <Typography 
                        paragraph 
                        align="left"
                        component="" 
                        variant="body1" 
                      >
                        {listing.room_desc}
                      </Typography>
                      <Typography 
                        component="li" 
                        variant="body2" 
                        align="left"
                      >
                        Number of current tenants: {listing.number_of_residents}
                      </Typography>
                      <Typography 
                        component="li" 
                        variant="body2" 
                        align="left"
                      >
                        Extra expenses: <strong>{"$" + 
                                listing.extra_expenses_per_month}</strong> 
                          /month
                      </Typography>
                    </ul>
                    </CardContent>
                  </Collapse>
                </Card>
							</Grid>
						);
					})}
				</Grid>
			</Container>
		</React.Fragment>
	);
};
export default Search;