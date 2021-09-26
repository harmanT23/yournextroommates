import { FETCH_IMAGE }  from '../actions/types';

const initialState = {};

const imageReducer = function (state=initialState, action) {
  switch(action.type) {
    case FETCH_IMAGE:
      return action.payload || false;
    default:
      return state
  }
}

export default imageReducer;