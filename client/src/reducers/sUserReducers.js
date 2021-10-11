import {
  FETCH_USER,
}  from '../actions/types';

const initialState = {};

const sUserReducer = function (state=initialState, action) {
  switch(action.type) {
    case FETCH_USER:
      return action.payload || false;
    default:
      return state;
  }
}

export default sUserReducer;
