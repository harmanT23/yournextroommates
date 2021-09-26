import {
  FETCH_LISTING_LIST,
  FETCH_LISTING
}  from '../actions/types';

const initialState = {};

const listingReducer = function (state=initialState, action) {
  switch(action.type) {
    case FETCH_LISTING_LIST:
      return action.payload;
    case FETCH_LISTING:
      return action.payload || false;
    default:
      return state
  }
}

export default listingReducer;
