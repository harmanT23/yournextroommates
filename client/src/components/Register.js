import React, { useState } from 'react';
import axiosInstance from '../Axios';
import { useHistory } from 'react-router-dom';
//MaterialUI
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles((theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center',
	},
	avatar: {
		margin: theme.spacing(1),
		backgroundColor: theme.palette.secondary.main,
	},
	form: {
		width: '100%', // Fix IE 11 issue.
		marginTop: theme.spacing(3),
	},
	submit: {
		margin: theme.spacing(3, 0, 2),
	},
  formControl: {
    margin: theme.spacing(1),
    minWidth: 120,
  },
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
  textField: {
    marginLeft: theme.spacing(1),
    marginRight: theme.spacing(1),
    width: 200,
  },
}));

export default function Register() {

	const history = useHistory();
	const initialFormData = Object.freeze({
		email: '',
		password: '',
    first_name: '',
    last_name: '',
    date_of_birth: '',
    current_city: '',
    current_province: '',
	});

	const [formData, updateFormData] = useState(initialFormData);

	const handleChange = e => {
		updateFormData({
			...formData,
			// Trimming any whitespace
			[e.target.name]: e.target.value.trim(),
		});
	};

	const handleSubmit = (e) => {
		e.preventDefault();
		console.log(formData);

		axiosInstance
			.post(`users/`, {
				email: formData.email,
				user_name: formData.username,
				password: formData.password,
        first_name: formData.first_name,
        last_name: formData.last_name,
        date_of_birth: formData.date_of_birth,
        current_city: formData.current_city,
        current_province: formData.current_province,
			})
			.then((res) => {
				history.push('/login');
				// console.log(res);
				// console.log(res.data);
			});
	};

	const classes = useStyles();

	return (
		<Container component="main" maxWidth="xs">
			<CssBaseline />
			<div className={classes.paper}>
				<Avatar className={classes.avatar}></Avatar>
				<Typography component="h1" variant="h5">
					Sign up
				</Typography>
				<form className={classes.form} noValidate>
        <Grid container spacing={2}>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="email"
								label="email address"
								name="email"
								autoComplete="email"
								onChange={handleChange}
							/>
						</Grid>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								name="password"
								label="password"
								type="password"
								id="password"
								autoComplete="create-password"
								onChange={handleChange}
							/>
						</Grid>
            <Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="first_name"
								label="first name"
								name="first_name"
								autoComplete="your-first-name"
								onChange={handleChange}
							/>
						</Grid>
            <Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="last_name"
								label="last name"
								name="last_name"
								autoComplete="your-last-name"
								onChange={handleChange}
							/>
						</Grid>
            <Grid item xs={12}>
            <TextField
              id="date_of_birth"
              label="Date of Birth"
							name="date_of_birth"
              type="date"
              defaultValue="2021-01-01"
              className={classes.textField}
              InputLabelProps={{
                shrink: true,
              }}
              onChange={handleChange}
            />
						</Grid>
            <Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="current_city"
								label="city"
								name="current_city"
								autoComplete="your-current-city"
								onChange={handleChange}
							/>
						</Grid>
            <Grid item xs={12}>
              <FormControl className={classes.formControl}>
                <InputLabel 
                  id="current_province"
                >
                  Province
                </InputLabel>
                <Select
                  labelId="current_province"
                  id="current_province"
									name="current_province"
                  onChange={handleChange}
									defaultValue="" 
                >
									<MenuItem value=""></MenuItem>
                  <MenuItem value={'Newfoundland and Labrador'}>NL</MenuItem>
                  <MenuItem value={'Prince Edward Island'}>PE</MenuItem>
                  <MenuItem value={'Nova Scotia'}>NS</MenuItem>
                  <MenuItem value={'New Brunswick'}>NB</MenuItem>
                  <MenuItem value={'Quebec'}>QC</MenuItem>
                  <MenuItem value={'Ontario'}>ON</MenuItem>
                  <MenuItem value={'Manitoba'}>MB</MenuItem>
                  <MenuItem value={'Saskatchewan'}>SK</MenuItem>
                  <MenuItem value={'Alberta'}>AB</MenuItem>
                  <MenuItem value={'British Columbia'}>BC</MenuItem>
                  <MenuItem value={'Yukon'}>YT</MenuItem>
                  <MenuItem value={'Northwest Territories'}>NT</MenuItem>
                  <MenuItem value={'Nunavut'}>NU</MenuItem>
                </Select>
              </FormControl>
						</Grid>
						<Grid item xs={12}>
						<Grid item xs={12}>
							<FormControlLabel
								control={<Checkbox value="allowExtraEmails" color="primary" />}
								label="I want to receive inspiration, marketing promotions and updates via email."
							/>
						</Grid>
					</Grid>
					<Button
						type="submit"
						fullWidth
						variant="contained"
						color="primary"
						className={classes.submit}
						onClick={handleSubmit}
					>
						Sign Up
					</Button>
					<Grid container justifyContent="flex-end">
						<Grid item>
							<Link href="/login" variant="body2">
								Already have an account? Sign in
							</Link>
						</Grid>
					</Grid>
        </Grid>
				</form>
			</div>
		</Container>
	);
}