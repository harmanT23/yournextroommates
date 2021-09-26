import {
  UPLOAD_GALLERY,
  FETCH_GALLERY
}  from '../actions/types';

const initialState = {};

const galleryReducer = function (state=initialState, action) {
  switch(action.type) {
    case UPLOAD_GALLERY:
      return action.payload;
    case FETCH_GALLERY:
      return action.payload || false;
    default:
      return state
  }
}

export default galleryReducer;