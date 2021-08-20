import React from 'react';
import Container from '@material-ui/core/Container';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Link from '@material-ui/core/Link';
import Box from '@material-ui/core/Box';

const useStyles = makeStyles((theme) => ({
	footer: {
    backgroundColor: theme.palette.background.paper,
		borderTop: `1px solid ${theme.palette.divider}`,
    padding: theme.spacing(6),
		marginTop: theme.spacing(8),
		paddingTop: theme.spacing(3),
		paddingBottom: theme.spacing(3),
		[theme.breakpoints.up('sm')]: {
			paddingTop: theme.spacing(6),
			paddingBottom: theme.spacing(6),
		},
	},
}));

function Copyright() {
	return (
		<Typography variant="body2" color="textSecondary" align="center">
			{'Copyright © '}
			<Link color="inherit" href="/">
				YourNextRoommates
			</Link>{' '}
			{new Date().getFullYear()}
			{'.'}
		</Typography>
	);
}

const footers = [
	{
		title: 'Help',
		description: ['Contact Us', 'Privacy', 'Support'],
	},
	{
		title: 'Account',
		description: [
			'Register',
			'Login',
			'Archive Account',
		],
	},
	{
		title: 'Follow Us',
		description: ['Twitter', 'Instagram', 'Facebook'],
	},
];

function Footer() {
	const classes = useStyles();
	return (
		<React.Fragment>
			<Container maxWidth="xl" component="footer" className={classes.footer}>
				<Grid container spacing={5} justifyContent="space-evenly">
					{footers.map((footer) => (
						<Grid item xs={12} sm={4} key={footer.title}>
							<Typography variant="h6" color="textPrimary" gutterBottom >
								{footer.title}
							</Typography>
								{footer.description.map((item) => (
									<Box key={item}>
										<Link href="/" variant="subtitle1" color="textSecondary">
											{item}
										</Link>
									</Box>
								))}
						</Grid>
					))}
				</Grid>
				<Box mt={5}>
					<Copyright />
				</Box>
			</Container>
		</React.Fragment>
	);
}

export default Footer;