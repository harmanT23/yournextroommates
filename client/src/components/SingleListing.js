import React, { useState, useEffect } from 'react';
import axiosInstance from '../Axios';
import { useParams } from 'react-router-dom';
//Material UI
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import Box from '@material-ui/core/Box';
import CssBaseline from '@material-ui/core/CssBaseline';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import SingleBedIcon from '@material-ui/icons/SingleBed';
import EventSeatIcon from '@material-ui/icons/EventSeat';
import LocalLaundryServiceIcon from '@material-ui/icons/LocalLaundryService';
import AcUnitIcon from '@material-ui/icons/AcUnit';
import BathtubIcon from '@material-ui/icons/Bathtub';
import PeopleIcon from '@material-ui/icons/People';
import EventIcon from '@material-ui/icons/Event';
import PaymentIcon from '@material-ui/icons/Payment';
import ReceiptIcon from '@material-ui/icons/Receipt';
import SchoolIcon from '@material-ui/icons/School';
import WorkIcon from '@material-ui/icons/Work';
import { red } from '@material-ui/core/colors';

const useStyles = makeStyles((theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center',
	},
	wrapIcon: {
		display: 'flex',
		alignItems: 'center',
		flexWrap: 'wrap',
	},
	avatar: {
		marginTop: 6,
    backgroundColor: red[500],
  },
	heroButtons: {
    marginTop: theme.spacing(0),
  },
	box: {
		height: 100,
		display: "flex",
		border: "1px solid black",
		padding: 8
	},
}));

function SingleListing() {
	const { slug } = useParams();
	const classes = useStyles();

	const [data, setData] = useState({ listings: [] });

	useEffect(() => {
		const listingSlug = 'listings/' + slug;
		axiosInstance.get(listingSlug).then((res) => {
			setData({ listings: res.data });
			console.log(res.data);
		});
	}, [setData, slug]);

	return (
		<Container component="main" maxWidth="xl">
			<CssBaseline />
			<div className={classes.paper}></div>
			<div className={classes.heroContent}>
				<Container maxWidth="xl">
					<Typography
						variant="h4"
						align="left"
						color="textPrimary"
						gutterBottom
					>
						{data.listings.listing_title}
					</Typography>
				</Container>
				<Container maxWidth="xl">
					<Grid container spacing={1}>
						<Grid item xs={12} sm={6} md={4}>
							<Typography
								variant="h6"
								align="left"
								color="textPrimary"
								gutterBottom
							>
								About this listing
							</Typography>
							<Divider />
							<Typography
								variant="body1"
								align="left"
								color="textSecondary"
								gutterBottom
							>
								{data.listings.room_desc}
							</Typography>
						</Grid>
					</Grid>
					<Grid container spacing={1}>
						<Grid item xs={12} sm={6} md={4}>
							<Typography
								variant="h6"
								align="left"
								color="textPrimary"
								gutterBottom
							>
								Where you'll sleep
							</Typography>
							<Divider />
							<Typography
								variant="body1"
								align="left"
								color="textSecondary"
								className={classes.wrapIcon}
							>
								<SingleBedIcon/> <span> &nbsp; </span>  {data.listings.room_type}
							</Typography>
						</Grid>
					</Grid>
					<Grid container spacing={1}>
						<Grid item xs={12} sm={6} md={4}>
							<Typography
								variant="h6"
								align="left"
								color="textPrimary"
								gutterBottom
							>
								Where you'll be located
							</Typography>
							<Divider />
							<Typography
								variant="body1"
								align="left"
								color="textSecondary"
							>
								{ (data.listings.address2 ? data.listings.address2 + " - ":"") + data.listings.address1 + ", " + data.listings.city + ", " + data.listings.province}
							</Typography>
						</Grid>
					</Grid>
					<Grid container spacing={1}>
						<Grid item xs={12} sm={6} md={4}>
							<Typography
								variant="h6"
								align="left"
								color="textPrimary"
								gutterBottom
							>
								The Space
							</Typography>
							<Divider />
							{data.listings.is_furnished && 
								<Typography
									variant="body1"
									align="left"
									color="textSecondary"
									className={classes.wrapIcon}
								>
									<EventSeatIcon /> <span> &nbsp; </span>  Furnished
								</Typography>
							}
							{data.listings.is_laundry_ensuite &&
								<Typography
									variant="body1"
									align="left"
									color="textSecondary"
									className={classes.wrapIcon}
								>
									<LocalLaundryServiceIcon /> <span> &nbsp; </span>  Ensuite Laundry 								
								</Typography>
							}
							{data.listings.is_air_conditioned &&
								<Typography
									variant="body1"
									align="left"
									color="textSecondary"
									className={classes.wrapIcon}
								>
									<AcUnitIcon /> <span> &nbsp; </span>  Air Conditioning 								
								</Typography>
							}
							{data.listings.number_of_bathrooms > 0 && 
								<Typography
									variant="body1"
									align="left"
									color="textSecondary"
									className={classes.wrapIcon}
								>
									<BathtubIcon /> <span> &nbsp; </span>  {data.listings.number_of_bathrooms} {data.listings.number_of_bathrooms > 1 ? "Bathrooms" : "Bathroom"}							
								</Typography>
							}
							<Typography
								variant="body1"
								align="left"
								color="textSecondary"
								className={classes.wrapIcon}
								justifyContent={'space-evenly'}
							>
								<PeopleIcon /> <span> &nbsp; </span> {data.listings.number_of_residents} {data.listings.number_of_residents > 1 ? "Roommates" : "Roommate"}
							</Typography>
						</Grid>
					</Grid>
					<Grid container spacing={1}>
						<Grid item xs={12} sm={6} md={4}>
							<Typography
								variant="h6"
								align="left"
								color="textPrimary"
								gutterBottom
							>
								Important Details
							</Typography>
							<Divider />
							<Typography
								variant="body1"
								align="left"
								color="textSecondary"
								className={classes.wrapIcon}
							>
								<EventIcon /> <span> &nbsp; </span> Earliest Move-In Date  {data.listings.earliest_move_in_date}
							</Typography>
							<Typography
								variant="body1"
								align="left"
								color="textSecondary"
								className={classes.wrapIcon}
							>
								<PaymentIcon /> <span> &nbsp; </span>  Monthly Rent ${data.listings.rent_per_month}
							</Typography>
							<Typography
								variant="body1"
								align="left"
								color="textSecondary"
								className={classes.wrapIcon}
							>
								<ReceiptIcon /> <span> &nbsp; </span>  Extra Monthly Expenses ${data.listings.extra_expenses_per_month}
							</Typography>
						</Grid>
					</Grid>
					<Grid container spacing={1}>
						<Grid item xs={12} sm={6} md={5}>
								<Typography
										variant="h6"
										align="left"
										color="textPrimary"
										gutterBottom
									>
										Your Roommate
								</Typography>
								<Divider styles={{padding: '10px'}}/>
								<Avatar 
									alt={data.listings.poster ? data.listings.poster.first_name + 
										" " + data.listings.poster.last_name : ""}
									className={classes.avatar}
									variant='square'
									src="https://source.unsplash.com/random/100x100/?person" 
								>
								</Avatar>
									<Typography
									variant="body1"
									align="left"
									color="textPrimary"
									className={classes.wrapIcon}
								>
									{data.listings.poster ? data.listings.poster.first_name + 
                                " " + data.listings.poster.last_name: ""}
								</Typography>
								<Typography
									variant="body1"
									align="left"
									color="textPrimary"
									className={classes.wrapIcon}
								>
									<SchoolIcon /> <span> &nbsp; </span> 
									{data.listings.poster ? data.listings.poster.university_major + 
                                " @ " + data.listings.poster.university: ""}
								</Typography>
								<Typography
									variant="body1"
									align="left"
									color="textPrimary"
									className={classes.wrapIcon}
								>
									<WorkIcon /> <span> &nbsp; </span> 
									{data.listings.poster ? data.listings.poster.profession : ""}
								</Typography>
								<div className={classes.heroButtons}>
									<Box component="span" m={0}>
										<Button size="small" variant="contained" color="primary">
											View Profile
										</Button>
									</Box>
									<Box component="span" m={1}>
										<Button size="small" variant="contained" color="primary">
											Contact
										</Button>
									</Box>
            		</div>
						</Grid>
					</Grid>
				</Container>
			</div>
		</Container>
	);
}

export default SingleListing;