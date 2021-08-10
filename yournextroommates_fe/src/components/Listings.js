import React from 'react';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import IconButton from '@material-ui/core/IconButton';
import FavoriteIcon from '@material-ui/icons/Favorite';
import ShareIcon from '@material-ui/icons/Share';
import Avatar from '@material-ui/core/Avatar';
import Checkbox from '@material-ui/core/Checkbox';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import { red } from '@material-ui/core/colors';


const useStyles = makeStyles((theme) => ({
  '@global': {
    ul: {
      margin: 0,
      padding: 0,
      listStyle: 'none',
    },
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
  footer: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(6),
  },
}));


const Listings = (props) => {
  const { listings } = props;
  const classes = useStyles();
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
        {/* Hero unit */}
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
              View the latest or most popular listings in your city. We hope
              you find your next roommates!
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
          {/* End hero unit */}
          <Grid container spacing={4}>
            {listings.map((list) => (
              <Grid item key={list.id} xs={12} sm={6} md={4}>
                <Card className={classes.card}>
                <CardHeader
                    avatar={
                      <Avatar 
                        alt={list.poster.first_name + " " + list.poster.first_name}
                        className={classes.avatar}
                        src="https://source.unsplash.com/random/100x100/?person" 
                      >
                      </Avatar>
                    }
                    title={list.listing_title}
                    subheader= {"Listed by " + list.poster.first_name + 
                                " " + list.poster.last_name}
                  />
                  <CardMedia
                    className={classes.cardMedia}
                    image="https://source.unsplash.com/random/320x180/?condo"
                    title="Image title"
                  />
                  <CardContent className={classes.cardContent}>
                    <Typography gutterBottom variant="h5" component="h2">
                      { (list.address2 ? list.address2 + " - ":"") + list.address1}
                    </Typography>
                    <Typography paragraph align="left">
                      {list.room_desc}
                    </Typography>
                    <ul>
                      <Typography 
                          component="li" 
                          variant="subtitle1" 
                          align="left"
                        >
                          <FormControlLabel
                            control={
                              <Checkbox
                                checked = {list.is_furnished}
                              />
                            }
                            label="Furnished"
                            labelPlacement="start"
                          />
                        </Typography>
                        <Typography 
                          component="li" 
                          variant="subtitle1" 
                          align="left"
                        >
                          Room Type: {list.room_type}
                        </Typography>
                        <Typography 
                          component="li" 
                          variant="subtitle1" 
                          align="left"
                        >
                          Number of current tenants: {list.number_of_residents}
                        </Typography>
                        <Typography 
                          component="li" 
                          variant="subtitle1" 
                          align="left"
                        >
                          Rent: <strong>{ "$" + list.rent_per_month}</strong> 
                            /month
                        </Typography>
                        <Typography 
                          component="li" 
                          variant="subtitle1" 
                          align="left"
                        >
                          Extra expenses: <strong>{"$" + 
                                  list.extra_expenses_per_month}</strong> 
                            /month
                        </Typography>
                        <Typography 
                          component="li" 
                          variant="subtitle1" 
                          align="left"
                        >
                          Earliest move-in date: <strong>
                                {list.earliest_move_in_date}</strong>
                        </Typography>
                    </ul>
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
                  </CardActions>
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
