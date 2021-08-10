import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import CircularProgress from '@material-ui/core/CircularProgress';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    '& > * + *': {
      marginLeft: theme.spacing(2),
    },
    justifyContent:'center'
  },
}));

function DataLoading(Component) {
  return function DataLoadingComponent({ isLoading, ...props }) {
    const classes = useStyles();
    if (!isLoading) return <Component {...props} />;
    return (
      <React.Fragment>
        <p style={{ fontSize: '25px' }}>
          Finding listings...
        </p>
        <div className={classes.root}>
          <CircularProgress />
        </div>
      </React.Fragment>

    );
  };
}

export default DataLoading;