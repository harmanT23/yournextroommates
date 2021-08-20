import React from 'react';
import clsx from 'clsx';
// Material UI
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Collapse from '@material-ui/core/Collapse';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import IconButton from '@material-ui/core/IconButton';
import FavoriteIcon from '@material-ui/icons/Favorite';
import ShareIcon from '@material-ui/icons/Share';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import Link from '@material-ui/core/Link';
import Avatar from '@material-ui/core/Avatar';
import Checkbox from '@material-ui/core/Checkbox';
import { red } from '@material-ui/core/colors';


const useStyles = makeStyles((theme) => ({
  '@global': {
    ul: {
      margin: 0,
      padding: 0,
      listStyle: 'none',
    },
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
  heroContent: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(3, 0, 1),
  },
  heroButtons: {
    marginTop: theme.spacing(0),
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
  cardMedia: {
    paddingTop: '56.25%', // 16:9
  },
  cardContent: {
    flexGrow: 1,
  },
  avatar: {
    backgroundColor: red[500],
  },
  link: {
		margin: theme.spacing(1, 1.5),
	},
  footer: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(6),
  },
  wrapIcon: {
		display: 'flex',
		alignItems: 'center',
		flexWrap: 'wrap',
	},
}));


const Listings = (props) => {
  const { listings } = props;
  const classes = useStyles();
  const [expanded, setExpanded] = React.useState(false);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };


  if (!listings || listings.length === 0) {
    return (
      <Typography variant="h5" align="center" color="textSecondary" paragraph>
        We cannot find any listings matching your request. Check back later!
      </Typography>
    );
  }

  return (
    <React.Fragment>
      <CssBaseline />
      <main>
        <div className={classes.heroContent}>
          <Container maxWidth="sm">
            <Typography 
              component="h1" 
              variant="h2" 
              align="center" 
              color="textPrimary" 
              gutterBottom
            >
              Listings
            </Typography>
            <Typography variant="h5" align="center" color="textSecondary" paragraph>
            Browse the latest listings in your city to find YourNextRoommates!
            </Typography>
          </Container>
          </div>
        <div className={classes.heroContent}>
          <Container maxWidth="sm">
            <div className={classes.heroButtons}>
              <Grid container spacing={2} justifyContent="center">
                <Grid item>
                  <Button variant="contained" color="primary">
                    Latest
                  </Button>
                </Grid>
                <Grid item>
                  <Button variant="outlined" color="primary">
                    Popular
                  </Button>
                </Grid>
              </Grid>
            </div>
          </Container>
        </div>
        <Container className={classes.cardGrid} maxWidth="md">
          <Grid container spacing={4}>
            {listings.map((list) => (
              <Grid item key={list.id} xs={12} sm={6} md={4}>
                <Card className={classes.card}>
                <Link
                    color="textPrimary"
                    href={'listings/' + list.slug}
                    className={classes.Link}
                >
                <CardHeader
                    avatar={
                      <Avatar 
                        alt={list.poster.first_name + " " + list.poster.last_name}
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
                    title={list.listing_title}
                    subheader= {"Listed by " + list.poster.first_name}
                  />
                  </Link>
                  <CardMedia
                    className={classes.cardMedia}
                    image="https://source.unsplash.com/random/320x180/?condo"
                    title="Image title"
                  />
                  <CardContent className={classes.cardContent}>
                    <Typography gutterBottom variant="h5" component="h2">
                      { (list.address2 ? list.address2 + " - ":"") + list.address1}
                    </Typography>
                    <Typography 
                          component="" 
                          variant="body1" 
                          align="left"
                        >
                         <strong>{ "$" + list.rent_per_month}</strong> per month
                    </Typography>
                    <Typography 
                          component="" 
                          variant="body2" 
                          align="left"
                    >
                      {list.room_type}
                    </Typography>
                    <Typography 
                        component="" 
                        variant="body2" 
                        align="left"
                    >
                        Earliest move-in date <strong>
                              {list.earliest_move_in_date}</strong>
                    </Typography>
                    <Typography 
                        component="" 
                        variant="body2" 
                        align="left"
                      >
                        Lease duration <strong>
                              {list.length_of_lease} months</strong> 
                  </Typography>
                  <Typography 
                        component="" 
                        variant="body2" 
                        align="left"
                        className={classes.wrapIcon}
                      >
                    
                      Furnished
                      <Checkbox
                        checked = {list.is_furnished}
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
                        {list.room_desc}
                      </Typography>
                      <Typography 
                        component="li" 
                        variant="body2" 
                        align="left"
                      >
                        Number of current tenants: {list.number_of_residents}
                      </Typography>
                      <Typography 
                        component="li" 
                        variant="body2" 
                        align="left"
                      >
                        Extra expenses: <strong>{"$" + 
                                list.extra_expenses_per_month}</strong> 
                          /month
                      </Typography>
                    </ul>
                    </CardContent>
                  </Collapse>
                </Card>
              </Grid>
            ))}
          </Grid>
        </Container>
      </main>
      </React.Fragment>
  );
}

export default Listings;
