import {
  REGISTER,
  LOGIN,
  LOGOUT,
  FETCH_AUTH_USER,
}  from '../actions/types';

const initialState = {};

const userReducer = function (state=initialState, action) {
  switch(action.type) {
    case REGISTER:
      return state;
    case LOGIN:
      return action.payload;
    case LOGOUT:
      return false;
    case FETCH_AUTH_USER:
      return action.payload || false;
    default:
      return state;
  }
}

export default userReducer;
